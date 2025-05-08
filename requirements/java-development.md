# Java Backend Development Prompt Library

This library contains prompts designed to assist with various aspects of Java backend software development. Feel free to adapt and expand upon these prompts for your specific needs.

## Core Java & Fundamentals

These prompts focus on fundamental Java concepts and their application in backend development.

1.  **Prompt:** Explain the concept of dependency injection in Java and provide a simple code example using Spring Framework annotations.
2.  **Prompt:** Describe the differences between `ArrayList` and `LinkedList` in Java. When would you choose one over the other in a backend application?
3.  **Prompt:** How can you implement exception handling in a Java backend application to gracefully manage errors and provide informative responses to clients? Provide a code snippet demonstrating a `try-catch-finally` block.
4.  **Prompt:** Discuss the importance of immutability in Java objects, especially in concurrent backend environments. Provide an example of creating an immutable class.
5.  **Prompt:** Explain the role of interfaces and abstract classes in Java backend design. Provide a scenario where using an interface would be more beneficial than an abstract class.

## Spring Framework

These prompts target the Spring Framework, a popular choice for building Java backend applications.

1.  **Prompt:** Generate a basic Spring Boot controller that handles a GET request to `/api/users` and returns a list of dummy user objects in JSON format.
2.  **Prompt:** Describe how you would implement RESTful API authentication using Spring Security in a Java backend application. Outline the key components and configuration steps.
3.  **Prompt:** Explain the concept of Aspect-Oriented Programming (AOP) in Spring. Provide an example of how you might use AOP for logging API requests.
4.  **Prompt:** How can you configure database interactions in a Spring Boot application using Spring Data JPA? Provide an example of a simple entity and repository.
5.  **Prompt:** Describe different ways to handle asynchronous operations in a Spring Boot application. Compare and contrast `@Async` and using a message queue like RabbitMQ.

## Databases & Persistence

These prompts relate to database interactions and data persistence in Java backend development.

1.  **Prompt:** Write a JPA query (using either JPQL or the Criteria API) to retrieve all users whose email address contains a specific domain.
2.  **Prompt:** Explain the concept of database transaction management in a Java backend application. How can you ensure atomicity, consistency, isolation, and durability (ACID properties)?
3.  **Prompt:** Describe different database migration strategies in a Java backend environment. What are the pros and cons of each approach?
4.  **Prompt:** How can you implement caching mechanisms (e.g., using Redis or Caffeine) in a Java backend application to improve performance and reduce database load?
5.  **Prompt:** Discuss different types of NoSQL databases and when you might choose one over a traditional relational database in a Java backend project.

## API Design & Development

These prompts focus on designing and developing robust APIs using Java.

1.  **Prompt:** Design a RESTful API endpoint for creating a new product, including the request and response formats (JSON). Consider validation and error handling.
2.  **Prompt:** Explain the principles of HATEOAS (Hypermedia as the Engine of Application State) and how it can improve the evolvability of your Java backend API.
3.  **Prompt:** How can you implement API versioning in a Java backend application? Discuss different strategies like URI versioning and header-based versioning.
4.  **Prompt:** Describe best practices for securing your Java backend APIs, including input validation, authorization, and protection against common web vulnerabilities.
5.  **Prompt:** How would you design and implement rate limiting for your Java backend API to prevent abuse and ensure fair usage?

## Testing & Quality Assurance

These prompts cover testing strategies and quality assurance practices in Java backend development.

1.  **Prompt:** Write a unit test using JUnit and Mockito to verify the functionality of a service method in a Spring Boot application.
2.  **Prompt:** Explain the difference between unit tests, integration tests, and end-to-end tests in the context of a Java backend application.
3.  **Prompt:** How can you implement integration tests for your Spring Data JPA repositories to ensure they interact correctly with the database?
4.  **Prompt:** Describe different code quality tools that can be used in a Java backend project (e.g., SonarQube, Checkstyle, PMD) and their benefits.
5.  **Prompt:** How would you approach performance testing a Java backend API to identify potential bottlenecks and ensure it meets performance requirements?

---

**Note:** This is a starting template. You can add more categories relevant to your specific needs, such as Microservices, Security, Messaging, Cloud Technologies, etc. Remember to tailor the prompts to the specific technologies and libraries you are using.
