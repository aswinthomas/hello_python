# Design patterns

Design patterns are well known solutions to recurring problems.

- This way there is no need to reinvent the wheel.
- Use best practices, lower cost and increase quality

## Characteristics

- Language neutral: use in any OOP language
- Dynamic: revise existing ones if needed
- Intentionally incomplete to allow customization

## Types

### Creational Patterns

- To build objects systematically
- Benefit of flexibility. Different object types from same class can be created at runtime
- This uses polymorphism often

### Structural Patters

- To establish relationships between software components
- Meet functional (what it does) and non-functional (how well does it do) requirements
- Different requirements lead to different structures
- This uses inheritance often

### Behavioral Patterns

- How the objects interact with each other
- Meet functional and non-functional requirements
- Focus is to define protocols between objects when working together to meet a requirement
- This heavily uses methods and their signatures

## Pattern Context

- Participants: The classes involved to form a design pattern
- Quality attributes: Non-functional requirements such as reliability and performance. This has an effect on the
  software and architectural solutions address them.
- Forces: Factors or trade-offs to consider. This is manifested in quality attributes and if not dealt with, could
  result in unintended consequences
- Consequences: E.g. Worse performance

## Patterns

### Factory Pattern

Instead of client code directly creating objects, it delegates responsibility to a Factory Method

#### When to use?

- When there are uncertainties in objects used
- Decisions must be be made at runtime on what classes to use

#### Benefits

- Decoupling client code from concrete classes, reducing dependency
- Flexibility of creation ofg object without specifying exact class
- Extensibility by adding mew product classes

#### Components

- Product Interface: Defines an abstract class or interface for the product
- Concrete Product: Implements concrete Products
- Creator Interface:  Defines an abstract creator class or interface, which is essentially a method to create object of the Products.
- Concrete Creator: Implements the creator, creating an instance of Product

### Singleton Pattern

When you only want one object. Global methods and attributes using objects.

#### Benefits

- Single Instance
- Global Access
- Resource Management: Helps manage rfesources that should be shred e.g. db connections


### Builder Pattern

A telescoping constructor occurs when a developer builds a complex object using an excessive number of constructors

#### Components

- Director: in charge of building a product
- Abstract Builder: Interfaces needed to build an object
- Concrete Builder: Inherits from abstract builder and implements the details for the specific product
- product: An object being built


