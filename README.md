# FastAPI Task CRUD API

A beginner FastAPI CRUD API for managing tasks.

## Tech Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Git/GitHub

## Features

* Create a task
* Get all tasks
* Get task by ID
* Update task
* Delete task

## Task Model

Each task has:

* `id`
* `title`
* `completed`

## Endpoints

```text
GET /
GET /tasks
POST /tasks
GET /tasks/{task_id}
PUT /tasks/{task_id}
DELETE /tasks/{task_id}
```

## Example Request Body

```json
{
  "title": "Learn FastAPI",
  "completed": false
}
```

## What I Learned

* FastAPI app setup
* Decorators
* Pydantic BaseModel
* Request body
* Path parameters
* Temporary list storage
* Manual ID counter
* Full CRUD API structure

## Future Improvements

* Query parameter filtering
* Proper error handling with HTTPException
* PostgreSQL database
* Authentication
* Deployment
