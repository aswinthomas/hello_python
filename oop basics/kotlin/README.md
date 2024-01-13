# Object-Oriented Programming in Kotlin
OOP is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).

## Classes
In OOP, classes are blueprints for creating objects. They encapsulate data for the object and methods to manipulate that data.

- Attributes: Represent the properties or state of an entity (e.g., age of a person).
- Methods: Represent the behavior of an entity (e.g., a method cancelEvent() in an Event class).

```kotlin
class Person(val name: String, var age: Int) {
    fun celebrateBirthday() {
        age++
    }
}
```

## Principles of OOP
1. Encapsulation
Encapsulation involves bundling the data and the methods that operate on the data within one unit. This restricts direct access to some of the object's components, which is a means of preventing accidental interference and misuse of the methods and data. In Kotlin, this is achieved using visibility modifiers like private, protected, etc.

```kotlin
class Account(private var balance: Double) {
    fun deposit(amount: Double) {
        if (amount > 0) {
            balance += amount
        }
    }

    fun getBalance(): Double {
        return balance
    }
}
```

2. Abstraction
Abstraction means hiding the complex reality while exposing only the necessary parts. It helps in reducing programming complexity and effort. In Kotlin, this is achieved using abstract classes and interfaces.

```kotlin
interface Communicator {
    fun send(message: String)
}

class EmailCommunicator : Communicator {
    override fun send(message: String) {
        // Send an email
    }
}
```

3. Inheritance
Inheritance is a mechanism where a new class is derived from an existing class. The new class is called a subclass, and the existing class is known as the superclass. It facilitates code reuse and can lead to an improvement in the logical structure of the code. Kotlin supports single inheritance from classes but can implement multiple interfaces.

```kotlin
open class Vehicle(val make: String, val model: String)

class Car(make: String, model: String, val doors: Int) : Vehicle(make, model)
```

4. Polymorphism
Polymorphism allows objects to be treated as instances of their parent class rather than their actual class. This means a single entity (method or object) can take on various forms. In Kotlin, polymorphism is achieved through method overriding (runtime polymorphism) and method overloading (compile-time polymorphism).

```kotlin
open class Shape {
    open fun draw() {
        println("Drawing a shape")
    }
}

class Circle : Shape() {
    override fun draw() {
        println("Drawing a circle")
    }
}
```
