package com.aswindev.training.oop

/*
Create a Kotlin program to simulate a notification system. This system should be capable of sending different
types of notifications (e.g., email, SMS, push notification) and should be easily extendable to accommodate new
notification types in the future.
Use Strategy Pattern to allow dynamic changes of notification sending behavior at runtime
 */
interface NotificationSender {
    // simulate sending a notification. Print type of notification and content
    fun sendNotification(message: String)
}

class EmailNotificationSender: NotificationSender {
    override fun sendNotification(message: String) {
        println("Sending Email Notification: $message")
    }
}

class SMSNotificationSender: NotificationSender {
    override fun sendNotification(message: String) {
        println("Sending SMS Notification: $message")
    }
}

class PushNotificationSender: NotificationSender {
    override fun sendNotification(message: String) {
        println("Sending Push Notification: $message")
    }
}

class NotificationManager(private var notificationSender: NotificationSender) {
    fun setNotificationSender(sender: NotificationSender) {
        notificationSender = sender
    }
    fun sendNotification(message: String) {
        notificationSender.sendNotification(message)
    }
}

fun main() {
    val emailSender = EmailNotificationSender()
    val smsSender = SMSNotificationSender()
    val pushSender = PushNotificationSender()

    val message = "Your package is out for delivery"
    val notifyManager = NotificationManager(emailSender)
    notifyManager.sendNotification(message)
    notifyManager.setNotificationSender(smsSender)
    notifyManager.sendNotification(message)
    notifyManager.setNotificationSender(pushSender)
    notifyManager.sendNotification(message)
}