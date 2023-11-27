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

| Pattern                                                                                                                                                     | When                                                                                                                                                                                        | Components                                                                                                                                                                                                                                                                                                                                                                       | 
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Factory**: Instead of client code directly creating objects, it delegates responsibility to a Factory Method                                              | <ul><li>Decoupling client code from concrete classes</li><li>Flexibility of creation of object without specifying exact class</li><li>Extensibility by adding mew product classes</li></ul> | <ul><li>Product Interface: Defines an abstract class or interface for the product</li><li>Concrete Product: Implements concrete Products</li><li>Creator Interface:  Defines an abstract creator class or interface, which is essentially a method to create object of the Products.</li><li>Concrete Creator: Implements the creator, creating an instance of Product</li></ul> |
| **Singleton**: When you only want one object. Global methods and attributes using objects.                                                                  | <ul><li>Single Instance</li><li>Global Access</li><li>Resource Management: Helps manage resources that should be shred e.g. db connections</li></ul>                                        |                                                                                                                                                                                                                                                                                                                                                                                  |
| **Builder**: Solves situation of a telescoping constructor, which occurs when a developer builds a complex object using an excessive number of constructors |                                                                                                                                                                                             | <ul><li>Director: in charge of building a product</li><li>Abstract Builder: Interfaces needed to build an object</li><li>Concrete Builder: Inherits from abstract builder and implements the details for the specific product</li><li>Product: An object being built</li></ul>                                                                                                   |
| **Prototype**: Useful when instantiating many identical objects could be expensive, instead clone them.                                                     |                                                                                                                                                                                             | <ul><li>Prototypical instance</li><li>Clone</li><ul>                                                                                                                                                                                                                                                                                                                             |
| **Decorator**: Add features to existing objects dynamically without changing structures                                                                     |                                                                                                                                                                                             | <ul><li>Functions are objects in Py</li><li>Built in decorator feature</li></ul>                                                                                                                                                                                                                                                                                                 |
| **Proxy**: To create a highly resource intensive object                                                                                                     | <ul><li>Postpone object creation unless absolutely necessary</li><li>Find a placeholder</li></ul>                                                                                           | <ul><li>Clients: wait to interact with a proxy</li><li>Proxy: Responsible for creating resource intensive Producer objects</li><li>Producer: resource intensive object</li></ul>                                                                                                                                                                                                 |