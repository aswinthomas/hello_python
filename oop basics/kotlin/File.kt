package com.aswindev.training.oop

import android.provider.ContactsContract.CommonDataKinds.Im

/*
Create a Kotlin program to simulate a basic file processing system. This system should be able to handle different
file formats and perform a series of operations on these files.
Implement a factory pattern to create instances of file types
 */

interface FileProcessor {
    // simulate processing and print that file is being processed
    fun process()
}

const val TEXT = "Text"
const val IMAGE = "Image"
const val AUDIO = "Audio"

class TextFile(private val filename: String) : FileProcessor {
    override fun process() {
        println("Processed file $filename")
    }

}

class ImageFile(private val filename: String) : FileProcessor {
    override fun process() {
        println("Processed file $filename")
    }

}

class AudioFile(private val filename: String) : FileProcessor {
    override fun process() {
        println("Processed file $filename")
    }

}

class FileProcessingApplication {
    fun processFiles(files: List<FileProcessor?>) {
        for (file in files) {
            file?.process()
        }
    }
}

class FileFactory {
    fun createFile(type: String, filename: String): FileProcessor? {
        return when (type) {
            TEXT -> TextFile(filename)
            AUDIO -> AudioFile(filename)
            IMAGE -> ImageFile(filename)
            // or throw exception here
            else -> null
        }
    }
}

fun main() {
    val fileFactory = FileFactory()
    val files = listOf(
        fileFactory.createFile(TEXT, "documents.txt"),
        fileFactory.createFile(IMAGE, "photo.jpeg"),
        fileFactory.createFile(AUDIO, "intro.wav"),
        fileFactory.createFile("UNKNOWN", "example.xyz")
    )

    val app = FileProcessingApplication()
    app.processFiles(files)
}
