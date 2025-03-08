# Week 17 - Flask for Backend

## Objective

The objective of this challenge is to build a simple RESTful API using Flask to manage tasks. This exercise will help students reinforce their understanding of API development, HTTP methods, and JSON responses.

## Challenge Overview

Students will develop a **Task Management API** that supports basic **CRUD** (Create, Read, Update, Delete) operations. The API should be able to:

- **Create a new task**
- **Retrieve all tasks**
- **Retrieve a task by ID**
- **Update a task**
- **Delete a task**
- **(Bonus) Mark a task as completed**
- **(Bonus) Use class-based views** ([Flask Class-Based Views](https://flask.palletsprojects.com/en/stable/views/))

---

## Instructions

### **1. Setup**

#### **Install Flask if not already installed:**

```sh
uv add flask
```

#### **Create a Python script (`app.py`) for the API.**

---

## **2. API Requirements**

### **Create a Task**

- **Endpoint:** `POST /tasks`
- **Request Body:**
  ```json
  {
    "title": "Task Title",
    "description": "Task Description"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Task Title",
    "description": "Task Description",
    "completed": false
  }
  ```

### **Retrieve All Tasks**

- **Endpoint:** `GET /tasks`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Learn Flask",
      "description": "Build an API using Flask.",
      "completed": false
    }
  ]
  ```

### **Retrieve a Specific Task**

- **Endpoint:** `GET /tasks/<task_id>`
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Learn Flask",
    "description": "Build an API using Flask.",
    "completed": false
  }
  ```

### **Update a Task**

- **Endpoint:** `PUT /tasks/<task_id>`
- **Request Body:**
  ```json
  {
    "title": "Updated Task Title",
    "description": "Updated Task Description"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Task updated successfully."
  }
  ```

### **Delete a Task**

- **Endpoint:** `DELETE /tasks/<task_id>`
- **Response:**
  ```json
  {
    "message": "Task deleted successfully."
  }
  ```

### **(Bonus) Mark a Task as Completed**

- **Endpoint:** `PATCH /tasks/<task_id>/complete`
- **Response:**
  ```json
  {
    "message": "Task marked as completed."
  }
  ```

---

## **Evaluation Criteria**

- **Correct implementation of API endpoints**
- **Proper use of HTTP methods and status codes**
- **Clear and structured code with proper documentation**
- **Effective teamwork and problem-solving approach**

This challenge encourages students to apply their Flask knowledge while working collaboratively to design a functional API. 🚀
