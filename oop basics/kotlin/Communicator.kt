package com.aswindev.training.oop

import java.lang.Exception

// interface (Abstraction)
interface Communicator {
    fun send()
}

class EmailCommunication(val packageId: Int = 100): Communicator {
    // private property (Encapsulation)
    private val smtpServerAddress = "smtp.example.com"
    private var additionalBody : String = ""
    companion object {
        private const val DEFAULT_PACKAGE_ID = 100
        fun getDefaultPackageId() : Int = DEFAULT_PACKAGE_ID
    }

    // secondary constructor
    constructor(packageId: Int, additionalInfo: String) : this(packageId) {
        additionalBody = additionalInfo
    }
    // private property (Encapsulation)
    private fun createBody(): String {
        return """
            Hello there,
            Your package $packageId is out for delivery.
            $additionalBody
            Regards,
            Your Delivery Team
        """.trimIndent()
    }
    // private property (Encapsulation)
    private fun connect() {
        if (smtpServerAddress.isBlank()) {
            throw Exception("SMTP server address is Blank!!!")
        }
        println("Connecting to SMTP server: $smtpServerAddress")
    }
    // private property (Encapsulation)
    private fun sendEmail() {
        try {
            val emailBody = createBody()
            connect()
            println("Sending email with body:$emailBody")
        } catch (e: Exception) {
            println("Failed to send email: ${e.message}")
        }

    }

    // Implementing the 'send' method from the Communicator interface (Abstraction)
    override fun send() {
        sendEmail()
    }
}

class SMSCommunication(private val phoneNumber: String): Communicator {
    private fun sendSMS() {
        if (phoneNumber.isBlank()) {
            throw Exception("Phone number is Blank!!!")
        }
        println("Sending SMS to number: $phoneNumber")
    }
    override fun send() {
        sendSMS()
    }
}

fun main() {
    val comms1 = EmailCommunication()
    comms1.send()
    val comms2 = EmailCommunication(250, "This is a high priority email")
    comms2.send()
    val comms3 = SMSCommunication("+65 878902843")
    comms3.send()
    val faultyComms1 = SMSCommunication("")
    faultyComms1.send()
}