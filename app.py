from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1 , "title": "Go to supermarket", "completed": False},
    {"id": 2, "title" : "study for finals", "comleted": False},
    
]

@app.route('/api/v1/tasks', methods = ['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route ('/api/v1/tasks', methods=['Post'])
def create_task():
    data = request.get_json()

    #400 if 
    if not data or 'title' not in data or data["title"].strip() == "":
        return jsonify({"error": "Title is required"}), 400


    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route('/api/v1/tasks/<int:task_id>', methods=['PUT'])

def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['completed'] = data.get('completed', task['completed'])
            return jsonify(task), 200
        return jsonify({"error": "Task not found"}), 404

@app.route('/api/v1/tasks/<int:task_id>', methods=['DELETE'])

def delete_task(task_id):
    global tasks
    update_task = [t for t in tasks if t["id"] != task_id]

    if len(update_task) == len(tasks):
        return jsonify({"error": "Task not found"}), 404
    
    tasks = update_task
    return jsonify({"message": "Task deleted successfully"}), 204

if __name__ == '__main__':
    app.run(debug=True)


