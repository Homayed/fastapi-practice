# FastAPI CRUD Day

Today I completed basic in-memory CRUD with FastAPI.

What I built:
- GET /tasks to read all tasks
- POST /tasks to create a task
- GET /tasks/{task_id} to read one task
- PUT /tasks/{task_id} to update one task
- DELETE /tasks/{task_id} to delete one task

Concepts learned:
- FastAPI app
- Decorators
- GET, POST, PUT, DELETE
- Pydantic BaseModel
- Request body
- Path parameter
- Temporary in-memory list storage
- Task ID using next_id

Important:
The tasks list is temporary. If the server restarts, data disappears.
Later PostgreSQL will replace this list.