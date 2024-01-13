package com.aswindev.training.oop
import android.os.Build
import androidx.annotation.RequiresApi
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import java.time.LocalDateTime
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.ConcurrentMap
import kotlin.math.max

// Logger interface for delegation
interface Logger {
    fun log(message: String)
}

// Concrete logger implementation
class ConsoleLogger: Logger {
    override fun log(message: String) {
        println("ConsoleLogger[${LocalDateTime.now()}]: $message")
    }
}

// generic Cache class with logger delegate
open class Cache<T>(private val logger: Logger) {
    // You can use ConcurrentHashMap for simplicity
    protected val dataMap = mutableMapOf<String, T>()
    protected val lock = Any()

    open fun put(key: String, value: T) {
        synchronized(lock) {
            dataMap[key] = value
            logger.log("Cache: Data $key added")
        }
    }

    open fun get(key: String): T? {
        return synchronized(lock) {
            val value: T? = dataMap[key]
            logger.log("Cache: Data $key retrieved")
            value
        }
    }
}

// Extension function to clear Cache
fun <T> TimedCache<T>.clearExpired() {
    this.clearExpiredItems()
}

// Implementation of the Cache generic class with coroutines
open class CoroutineCache<T>(private val logger: Logger) {
    val dataMap = mutableMapOf<String, T>()
    private val mutex = Mutex()

    open suspend fun put(key: String, value: T) {
        mutex.withLock {
            dataMap[key] = value
            logger.log("CoroutineCache: Data $key added")
        }
    }

    open suspend fun get(key: String) {
        mutex.withLock {
            dataMap[key]?.also {
                logger.log("CoroutineCache: Data $key retrieved")
            }
        }
    }
}

// Cache with time-based eviction of items
class TimedCache<T>(private val maxTime: Long, logger: Logger): Cache<T>(logger) {
    private val timeMap = mutableMapOf<String, LocalDateTime>()
    private val timeLock = Any()

    override fun put(key: String, value: T) {
        super.put(key, value)
        synchronized(timeLock) {
            timeMap[key] = LocalDateTime.now()
        }
    }

    fun clearExpiredItems() {
        val now = LocalDateTime.now()
        synchronized(timeLock) {
            for ((key, time) in timeMap) {
                val duration = java.time.Duration.between(now, time).toMinutes()
                if (duration > maxTime) {
                    synchronized(lock) {
                        dataMap.remove(key)
                    }
                }
            }
        }

    }

}

// Cache with size-based eviction of items
class SizeLimitedCache<T>(private val maxSize: Long, logger: Logger): Cache<T>(logger) {
    private val keyQueue = ArrayDeque<String>()
    private val queueLock = Any()

    override fun put(key: String, value: T) {
        super.put(key, value)
        synchronized(queueLock) {
            keyQueue.addLast(key)
            synchronized(lock) {
                while (keyQueue.size > maxSize) {
                    val oldestKey = keyQueue.first()
                    dataMap.remove(oldestKey)
                }
            }
        }
    }
}



fun main() {
    val logger = ConsoleLogger()
    val listCache = Cache<MutableList<String>>(logger)
    listCache.put("students", mutableListOf<String>("Mark", "Lisa", "Pradeep"))
    listCache.put("artists", mutableListOf<String>("Janice", "Monica", "Joey"))
    println(listCache.get("artists"))

    runBlocking {
        val logger = ConsoleLogger()
        val cache = CoroutineCache<String>(logger)

        launch {
            cache.put("key1", "Hello")
        }

        launch {
            val value = cache.get("key1")
            println(value)
        }
    }
}