# Challenge Week: Task API

This project is a simple Task API built using Flask and SQLAlchemy. The API allows you to perform basic CRUD operations (Create, Read, Update, Delete) on tasks, as well as mark a task as completed.

## Project Structure

- **app.py**: Main Flask application that sets up the API endpoints and database models.
- **instance/**: Folder where the SQLite database (`tasks.db`) is stored. This folder is created automatically if it does not exist.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

Install the required packages using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

## How to Run the Application

1. Ensure you are in the project directory.
2. Run the application:

   ```bash
   python app.py
   ```

3. The API will be accessible at: `http://127.0.0.1:5000`

## API Endpoints

### Create a Task
- **Endpoint:** `/tasks`
- **Method:** POST
- **Body:** JSON with `title` and `description`

Example using PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks" -Method Post -Body '{"title": "Learn Flask", "description": "Build an API"}' -ContentType "application/json"
```

### Retrieve All Tasks
- **Endpoint:** `/tasks`
- **Method:** GET

Example:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks" -Method Get
```

### Update a Task
- **Endpoint:** `/tasks/<task_id>`
- **Method:** PUT
- **Body:** JSON with updated `title` and `description`

Example:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks/1" -Method Put -Body '{"title": "Updated Task", "description": "Updated details"}' -ContentType "application/json"
```

### Mark a Task as Completed
- **Endpoint:** `/tasks/<task_id>/complete`
- **Method:** PATCH

Example:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks/1/complete" -Method Patch
```

### Delete a Task
- **Endpoint:** `/tasks/<task_id>`
- **Method:** DELETE

Example:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks/1" -Method Delete
```

## Testing Sequence Example

Below is an example of a complete testing sequence using PowerShell's **Invoke-RestMethod**:

1. **Create a Task**

   ```powershell
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks" -Method Post -Body '{"title": "Learn Flask", "description": "Build an API"}' -ContentType "application/json"
   ```

   Expected output:
   ```
   completed   : False
   created_at  : 2025-03-08T08:31:47.136940
   description : Build an API
   id          : 1
   title       : Learn Flask
   ```

2. **Retrieve All Tasks**

   ```powershell
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks" -Method Get
   ```

3. **Update the Task**

   ```powershell
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks/1" -Method Put -Body '{"title": "Updated Task", "description": "Updated details"}' -ContentType "application/json"
   ```

   Expected output:
   ```
   completed   : False
   created_at  : 2025-03-08T08:31:47.136940
   description : Updated details
   id          : 1
   title       : Updated Task
   ```

4. **Mark the Task as Completed**

   ```powershell
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks/1/complete" -Method Patch
   ```

   Expected output:
   ```
   completed   : True
   created_at  : 2025-03-08T08:31:47.136940
   description : Updated details
   id          : 1
   title       : Updated Task
   ```

5. **Delete the Task**

   ```powershell
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks/1" -Method Delete
   ```

   Expected output:
   ```
   message
   -------
   Task deleted successfully
   ```

**Note:** The sequence matters. If you delete a task before marking it as completed, the PATCH request for marking it completed will fail because the task no longer exists.
