from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Zarif"}

@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            "Review LeetCode",
            "Learn FastAPI",
            "Build backend project"
        ]
    }
@app.get("/about")
def about():
    return {
        "name": "Zarif",
        "goal": "Remote Python Backend Developer",
        "current_focus": "FastAPI and LeetCode"
    }