# Software Development Prompt Library

This library provides a collection of prompts to assist with various software development tasks. Feel free to adapt and expand upon these examples.

## 1. Code Generation

These prompts focus on generating specific code snippets or entire functions/classes.

* **Prompt 1:** Generate a Python function that checks if a given string is a palindrome. Include docstrings and error handling for non-string inputs.
* **Prompt 2:** Write a React component that displays a simple counter with increment and decrement buttons. Include basic styling.
* **Prompt 3:** Create a SQL query to retrieve all users from a database table named "users" who registered after January 1st, 2023, and order the results by their registration date in ascending order.
* **Prompt 4:** Generate a basic HTML form with fields for name, email, and a submit button. Include appropriate input types and labels.
* **Prompt 5:** Write a JavaScript function that takes an array of numbers as input and returns the average of those numbers.

## 2. Code Explanation

Use these prompts to understand existing code snippets or concepts.

* **Prompt 1:** Explain the following Python code snippet line by line:
    ```python
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    ```
* **Prompt 2:** Describe the purpose and benefits of using the "useEffect" hook in React. Provide a simple use case example.
* **Prompt 3:** What is the difference between a primary key and a foreign key in a relational database? Provide an example table schema to illustrate.
* **Prompt 4:** Explain the concept of "closures" in JavaScript with a clear and concise example.
* **Prompt 5:** Describe the Model-View-Controller (MVC) architectural pattern and its advantages in software development.

## 3. Code Refactoring

These prompts aim to improve the structure, readability, and efficiency of existing code.

* **Prompt 1:** Refactor the following JavaScript code to make it more readable and maintainable:
    ```javascript
    function processData(arr) {
      let res = [];
      for (let i = 0; i < arr.length; i++) {
        if (arr[i] > 5) {
          let doubled = arr[i] * 2;
          res.push(doubled);
        }
      }
      return res;
    }
    ```
* **Prompt 2:** Suggest ways to optimize the performance of the following Python function:
    ```python
    def find_duplicates(data):
        duplicates = []
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] == data[j] and data[i] not in duplicates:
                    duplicates.append(data[i])
        return duplicates
    ```
* **Prompt 3:** Refactor the following HTML and CSS to improve its semantic structure and maintainability (provide the HTML and CSS code here).
* **Prompt 4:** How can I improve the error handling in the following Node.js code block (provide the Node.js code here)?
* **Prompt 5:** Suggest ways to break down the following large Java method into smaller, more manageable units (provide the Java code here).

## 4. Debugging Assistance

Use these prompts to help identify and resolve issues in your code.

* **Prompt 1:** I'm getting a "TypeError: Cannot read property 'name' of undefined" error in my JavaScript code. The relevant code snippet is: `console.log(user.name);`. What could be the possible causes of this error and how can I debug it?
* **Prompt 2:** My Python script is running much slower than expected. How can I profile my code to identify performance bottlenecks?
* **Prompt 3:** My React component is not re-rendering when the state updates. Here's the relevant code: (provide React component code). What could be the issue?
* **Prompt 4:** My SQL query is returning incorrect results. The query is: (provide SQL query). What could be the potential problems?
* **Prompt 5:** I'm encountering a "404 Not Found" error when making an API request from my application. What are the common reasons for this error and how can I troubleshoot it?

## 5. Learning and Conceptual Understanding

These prompts are designed to help you learn new concepts and deepen your understanding of software development principles.

* **Prompt 1:** Explain the SOLID principles of object-oriented design with simple examples for each principle.
* **Prompt 2:** What are the key differences between RESTful and GraphQL APIs? When would you choose one over the other?
* **Prompt 3:** Describe the different types of software testing (e.g., unit, integration, end-to-end) and their importance in the development lifecycle.
* **Prompt 4:** Explain the concept of continuous integration and continuous deployment (CI/CD) and its benefits for software development teams.
* **Prompt 5:** What are the common design patterns used in web development, and can you provide a brief overview of a few popular ones (e.g., observer, factory)?

## 6. Documentation Generation

Use these prompts to create or improve software documentation.

* **Prompt 1:** Generate a docstring for the following Python function, explaining its purpose, arguments, and return value: (provide Python function).
* **Prompt 2:** Write a README file for a simple Node.js library that performs string manipulation. Include installation instructions, usage examples, and contribution guidelines.
* **Prompt 3:** Create API documentation in Markdown format for the following endpoint: `/api/users/{id}` (describe the request method, parameters, request body if any, and possible responses).
* **Prompt 4:** Generate comments for the following C++ code block to explain its functionality: (provide C++ code).
* **Prompt 5:** Write a brief user guide for a command-line tool that converts CSV files to JSON format.

---

**How to Use This Library:**

1.  **Identify your need:** Determine which category best fits your current task.
2.  **Select a prompt:** Choose an existing prompt or adapt one to your specific situation.
3.  **Provide context:** The more details you provide to the AI, the better the results will be. Include relevant code snippets, error messages, or specific requirements.
4.  **Iterate:** If the initial response isn't exactly what you need, refine your prompt and try again.

This template should provide a solid foundation for your software development prompt library. Good luck!
