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

<table>
  <tr>
    <th>Pattern</th>
    <th>Use cases</th>
    <th>Components</th>
  </tr>
  <tr>
    <td><strong>Factory</strong>: This is a creational pattern used to provide abstraction. Instead of client code 
directly creating objects, it delegates responsibility to a Factory Method e.g. ordering a combo meal at a restaurant.
      <ul>
        <li>Decoupling client code from concrete classes. Placing redundant code e.g. create burger into a class and 
calling it from multiple places would be 'Simple Factory', but then we would have to modify the class when new items 
need to be added, and also would need to know the class type e.g. CheeseBurger meal when calling.</li>
        <li>Flexibility of creation of object without specifying exact class</li>
        <li>Extensibility by adding new product classes</li>
      </ul>
    </td>
    <td>
    <ul>
      <li>Library Frameworks: It’s commonly used in library frameworks, allowing developers to extend and customize the behavior of a library.</li>
      <li>Plug-in Architectures: When building applications with extensible plug-in architectures, the Factory Method pattern simplifies the addition of new plug-ins without modifying existing code.</li>
      <li>Testing: Factories can be used to create mock objects for unit testing.</li>
    </ul>
    </td>
    <td>
      <ul>
        <li>Product Interface: Defines an abstract class or interface for the product. For example, Burger.</li>
        <li>Concrete Product: Implements concrete Products e.g. VeganBurger, CheeseBurger etc.</li>
        <li>Creator Interface: Defines an abstract creator class or interface that has a FactoryMethod e.g. getBurger() 
but without the implementation</li>
        <li>Concrete Creator: Implements the creator and FactoryMethod e.g. CheeseBurgerCreator</li>
      </ul>
      Now when a new Burger type is added, the FactoryMethod in Creator Interface doesn't change.
    </td>
  </tr>
  <tr>
    <td><strong>Singleton</strong>: When you only want one object. Global methods and attributes using objects. This is 
a <strong>creational pattern</strong>.</td>
    <td>
    <ul>
      <li>Database Connection Pools: Enhancing database interaction efficiency via a unified connection pool.</li>
      <li>Logger Services: Centralizing application logging through a single logger instance.</li>
      <li>Configuration Management: Ensuring a solitary configuration manager instance oversees application settings.</li>
      <li>Hardware Access: Controlling access to hardware resources, such as a printer or sensor, through a single instance.</li>
    </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Builder</strong>: Solves situation of a telescoping constructor, which occurs when a developer builds a complex object using an excessive number of constructors. This is a <strong>creational pattern</strong>.</td>
    <td></td>
    <td><ul><li>Director: in charge of building a product</li><li>Abstract Builder: Interfaces needed to build an object</li><li>Concrete Builder: Inherits from abstract builder and implements the details for the specific product</li><li>Product: An object being built</li></ul></td>
  </tr>
  <tr>
    <td><strong>Decorator</strong>: Add features to existing objects dynamically without changing structures. This is a <strong>structural pattern</strong>.</td>
    <td></td>
    <td><ul><li>Functions are objects in Py</li><li>Built in decorator feature</li></ul></td>
  </tr>
  <tr>
    <td><strong>Adapter</strong>: Converts interface of a class to one that client is expecting. This is a <strong>structural pattern</strong>.</td>
    <td>
    <ul>
      <li>Legacy System Integration: When you need to integrate a legacy system or library with modern code, the Adapter pattern can make the transition smoother. It allows you to wrap the legacy code with an adapter, ensuring it conforms to the expected interface of the new system.</li>
      <li>Third-Party Libraries: When working with third-party libraries or APIs that do not align with your system’s requirements, adapters can serve as intermediaries. They translate the third-party interface into one that your codebase understands.</li>
      <li>Interface Evolution: As your software evolves, you may encounter situations where the interfaces of existing classes need to change. Adapters can help maintain backward compatibility by presenting the old interface while internally implementing the new one.</li>
    </ul>
    </td>
    <td>
    Object Adapter takes on interface of one object while wrapping the behavior of other. Class Adapter relies on inheritance, inheriting interfaces form both objects, overriding methods, but only available in C++.
    <ul>
      <li>Target Interface: The target interface defines the contract that the client code expects. It is the interface the adapter will conform to, allowing the client to interact with the adaptee seamlessly.</li>
      <li>Adaptee: The adaptee is the class or component with an incompatible interface. It’s the object you want to make use of but cannot interact with directly from the client. Usually a 3rd party or legacy service.</li>
      <li>Adapter: The intermediary that bridges the gap between the target interface and the adaptee. It translates calls from the client in a way that the adaptee can understand and respond to.</li>
    </ul>
    </td>
  </tr>
  <tr>
    <td><strong>Strategy</strong>: Offers family of interchangeable algorithms for clients. This is a <strong>behavioral pattern</strong>.</td>
    <td></td>
    <td>
      <ul>
      <li>Abstract strategy with default set of behaviors</li>
      <li>Concrete strategy with behaviors</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><strong>Observer</strong>: Establishes 1:many relationship between a subject and multiple observers. A subject needs to be monitored, and the observers need to be notified when there is a change in the subject. <strong>Singleton pattern</strong> is related to this pattern. This is a <strong>behavioral pattern</strong>.</td>
    <td></td>
    <td>
    <ul>
      <li>Subject: abstract class that has interface that allows operations like attach, detach, notify</li>
      <li>Observer</li>
    </ul>
    </td>
  </tr>
  <tr>
    <td><strong>Prototype</strong>: Useful when instantiating many identical objects could be expensive, instead clone them.</td>
    <td></td>
    <td><ul><li>Prototypical instance</li><li>Clone</li></ul></td>
  </tr>

  <tr>
    <td><strong>Proxy</strong>: To create a highly resource intensive object</td>
    <td><ul><li>Postpone object creation unless absolutely necessary</li><li>Find a placeholder</li></ul></td>
    <td><ul><li>Clients: wait to interact with a proxy</li><li>Proxy: Responsible for creating resource intensive Producer objects</li><li>Producer: resource intensive object</li></ul></td>
  </tr>

  <tr>
    <td><strong>Composite</strong>: Maintains a tree data structure to represent part whole relationships</td>
    <td></td>
    <td>Recursive data structure with elements having sub elements Menu &rarr; submenu &rarr; subsubmenu <ul><li>Component: Abstract class</li><li>Child: Concrete component class</li><li>Composite: Concrete component class with child objects</li></td>
  </tr>
  <tr>
    <td><strong>Bridge</strong>: Helps untangle unnecessarily complicated class hierarchy, especially when implementation classes are mixed with implementation independent classes</td>
    <td></td>
    <td>Implementation independent and dependant circle abstraction</td>
  </tr>

  <tr>
    <td><strong>Visitor</strong>: Allows adding new features to existing clas hierarchy without changing it.</td>
    <td></td>
    <td>
    <ul>
      <li>Visitor</li>
      <li>Location being visited</li>
    </ul>
    </td>
  </tr>
  <tr>
    <td><strong>Iterator</strong>: Allows a client to have sequential access to aggregate object without exposing underlying structure.</td>
    <td></td>
    <td>
    </td>
  </tr>

  <tr>
    <td><strong>Chain of responsibility</strong>: Opens possibilities of processing for a request. It decouples request and its processing. <strong>Composite pattern</strong> is related to this pattern. </td>
    <td></td>
    <td>
      <ul>
      <li>Abstract handler: stores a successor that handles the request if the current handler does not handle it</li>
      <li>Concrete handler: implements checking if it can handle the request</li>
      </ul>
    </td>
  </tr>
</table>

### How each patterns differ

<table>
  <tr>
    <th>Adapter Pattern</th>
    <th>Other Pattern</th>
  </tr>
  <tr>
    <td>Ensures interface compatibility between classes with incompatible interfaces.</td>
    <td><strong>Bridge:</strong> Separates abstraction from implementation to enable independent variations.</td>
  </tr>
  <tr>
    <td>Ensures interface compatibility through adaptation and translation.</td>
    <td><strong>Decorator:</strong> Dynamically adds responsibilities to objects without interface changes, often extending functionality at runtime.</td>
  </tr>
  <tr>
    <td>Translates calls to ensure compatibility between interfaces.</td>
    <td><strong>Proxy:</strong> Controls object access, serving as a protective barrier with a focus on access control and lazy loading.</td>
  </tr>
  <tr>
    <td>Ensures compatibility between existing interfaces without altering source code.</td>
    <td><strong>Facade:</strong> Simplifies client interactions by providing a unified, higher-level interface to a group of interfaces, focusing on a streamlined experience rather than individual conversions.</td>
  </tr>
</table>

