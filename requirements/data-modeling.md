# Java Backend Development Prompt Library

This library offers a collection of prompts to guide you in various aspects of Java backend software development. Feel free to adapt and expand these examples to fit your specific projects and learning goals.

## Core Java & Fundamentals

These prompts explore essential Java concepts crucial for backend development.

1.  **Prompt:** Demonstrate how to implement a custom comparator in Java to sort a list of `Product` objects based on their price in descending order. Provide the `Product` class definition and the comparator implementation.
2.  **Prompt:** Write a Java code snippet that reads data from a CSV file named `data.csv`, where each line contains comma-separated values for user ID (integer), name (string), and email (string). Store this data in a `List` of `User` objects. Include the `User` class definition and necessary exception handling.
3.  **Prompt:** Explain the concept of multithreading in Java and illustrate how to create and start two threads that concurrently print numbers from 1 to 10. Use the `Runnable` interface for implementation.
4.  **Prompt:** Create a Java function that takes a string as input and returns a new string with all duplicate characters removed while preserving the original order of the remaining characters. For example, input "programming" should return "progamin".
5.  **Prompt:** Design a simple Java class representing a `ShoppingCart` with methods to add items (with quantity), remove items, and calculate the total price. Assume each item has a name and a price.

## Spring Framework

These prompts focus on practical applications of the Spring Framework in backend development.

1.  **Prompt:** Generate a Spring Boot REST controller with an endpoint `/api/greet` that accepts a query parameter `name` and returns a JSON response like `{"message": "Hello, [name]!"}`. Include necessary annotations.
2.  **Prompt:** Demonstrate how to implement basic authentication using Spring Security for an API endpoint `/admin/dashboard`. Configure an in-memory user with username "admin" and password "secret".
3.  **Prompt:** Write a Spring AOP aspect that logs the execution time of all methods annotated with `@LogExecutionTime`. Include the annotation definition and the aspect implementation.
4.  **Prompt:** Create a Spring Data JPA entity `Book` with fields `id` (Long, primary key, auto-generated), `title` (String), and `author` (String). Define a corresponding Spring Data JPA repository interface with a method to find books by title.
5.  **Prompt:** Implement asynchronous processing in a Spring Boot service method using `@Async`. The method should simulate a long-running task (e.g., using `Thread.sleep()`) and log a message before and after execution. Configure the `@EnableAsync` annotation in your main application class.

## Databases & Persistence

These prompts involve working with databases and persistence layers in Java backend applications.

1.  **Prompt:** Write a Spring Data JPA query (using `@Query`) in a `UserRepository` interface to find all users whose names start with a given prefix (case-insensitive).
2.  **Prompt:** Demonstrate how to use `@Transactional` annotation in a Spring service method to ensure that a series of database operations (e.g., transferring funds between two accounts) are treated as a single atomic unit. Include a simplified example with dummy repository methods.
3.  **Prompt:** Outline the steps to configure Flyway or Liquibase in a Spring Boot project to manage database migrations. Provide a basic example of a SQL migration script.
4.  **Prompt:** Show how to configure and use Redis as a caching provider in a Spring Boot application. Demonstrate caching the result of a frequently accessed service method.
5.  **Prompt:** Provide a Java code example using the MongoDB Java driver to connect to a MongoDB database and insert a new document into a collection named "products" with fields "name" and "price".

## API Design & Development

These prompts focus on designing and building effective APIs with Java.

1.  **Prompt:** Design the request and response JSON schemas for an API endpoint that allows clients to submit a new order. Include fields for customer ID, a list of product IDs with quantities, and shipping address.
2.  **Prompt:** Implement a simple Spring REST controller endpoint that returns a resource with HATEOAS links. For example, a `User` resource should include links to retrieve the user's orders and update the user's profile. Use Spring HATEOAS.
3.  **Prompt:** Demonstrate how to implement URI-based API versioning for a GET endpoint that retrieves user details. Create two versions of the endpoint, `/api/v1/users/{id}` and `/api/v2/users/{id}`, with potentially different response structures.
4.  **Prompt:** Show how to implement input validation for a Spring REST controller using `@Valid` and `@RequestBody` along with Bean Validation annotations (e.g., `@NotBlank`, `@Email`, `@Min`). Provide an example of a request DTO and error handling for validation failures.
5.  **Prompt:** Design a rate limiter using a simple in-memory counter and a sliding window approach for a specific API endpoint. Provide a Java implementation that checks if the number of requests from a given IP address exceeds a defined limit within a specific time frame.

## Testing & Quality Assurance

These prompts cover practical testing scenarios in Java backend development.

1.  **Prompt:** Write a JUnit test case for a Spring service method that calculates the discount based on a user's loyalty level. Use Mockito to mock any dependencies of the service.
2.  **Prompt:** Demonstrate how to write an integration test for a Spring Data JPA repository method that saves a new entity to the database and retrieves it. Use `@DataJpaTest` annotation.
3.  **Prompt:** Configure and use the Spring TestRestTemplate to write an end-to-end test for a REST API endpoint that creates a new resource and returns a 201 Created status code.
4.  **Prompt:** Integrate SonarQube analysis into a Maven build process for a Java backend project. Outline the necessary Maven plugin configuration and explain how to interpret the SonarQube report.
5.  **Prompt:** Write a basic performance test using JMeter for a GET API endpoint to measure its response time under concurrent user load. Describe the steps involved in setting up the test plan.

---

Remember to adapt these prompts to your specific learning objectives and the technologies you are working with. Good luck!
