"""
Test script for the ToDo API
Run this after starting the API server with: uvicorn app.main:app --reload
"""

import requests
import json
from uuid import UUID

BASE_URL = "http://localhost:8000"

def print_response(resp):
    """Pretty print the response"""
    print(f"Status: {resp.status_code}")
    try:
        print(json.dumps(resp.json(), indent=2))
    except:
        print(resp.text)
    print("-" * 50)

def main():
    print("\n=== Testing ToDo API ===\n")
    
    # Get root
    print("GET /")
    resp = requests.get(f"{BASE_URL}/")
    print_response(resp)
    
    # Get all todos (empty at first)
    print("GET /todos (should be empty)")
    resp = requests.get(f"{BASE_URL}/todos")
    print_response(resp)
    
    # Create a todo
    print("POST /todos (create low priority todo)")
    todo1 = {
        "title": "Learn Python",
        "description": "Master Python basics",
        "priority": "low",
        "completed": False
    }
    resp = requests.post(f"{BASE_URL}/todos", json=todo1)
    print_response(resp)
    todo1_id = resp.json()["id"]
    
    # Create another todo
    print("POST /todos (create high priority todo)")
    todo2 = {
        "title": "Learn FastAPI",
        "description": "Build a REST API",
        "priority": "high",
        "completed": False
    }
    resp = requests.post(f"{BASE_URL}/todos", json=todo2)
    print_response(resp)
    todo2_id = resp.json()["id"]
    
    # Get all todos
    print("GET /todos (should have 2 items)")
    resp = requests.get(f"{BASE_URL}/todos")
    print_response(resp)
    
    # Get a specific todo
    print(f"GET /todos/{todo1_id}")
    resp = requests.get(f"{BASE_URL}/todos/{todo1_id}")
    print_response(resp)
    
    # Update a todo
    print(f"PUT /todos/{todo1_id} (mark as completed)")
    update_data = {
        "title": "Learn Python",
        "description": "Master Python basics",
        "priority": "low",
        "completed": True
    }
    resp = requests.put(f"{BASE_URL}/todos/{todo1_id}", json=update_data)
    print_response(resp)
    
    # Get all todos again
    print("GET /todos (first todo should be completed)")
    resp = requests.get(f"{BASE_URL}/todos")
    print_response(resp)
    
    # Delete a todo
    print(f"DELETE /todos/{todo2_id}")
    resp = requests.delete(f"{BASE_URL}/todos/{todo2_id}")
    print_response(resp)
    
    # Get all todos after deletion
    print("GET /todos (should have 1 item)")
    resp = requests.get(f"{BASE_URL}/todos")
    print_response(resp)
    
    print("\n=== Test complete ===\n")

if __name__ == "__main__":
    main()