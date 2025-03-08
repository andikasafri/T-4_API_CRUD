from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Ensure the instance folder exists
if not os.path.exists("instance"):
    os.makedirs("instance")

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'instance', 'tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

# Create database tables
with app.app_context():
    db.create_all()

class TaskAPI(MethodView):
    """Handles CRUD operations for tasks"""
    
    def get(self, task_id=None):
        """Retrieve all tasks or a specific task by ID"""
        try:
            if task_id:
                task = Task.query.get_or_404(task_id)
                return jsonify(task.to_dict()), 200
            tasks = Task.query.all()
            return jsonify([task.to_dict() for task in tasks]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 404

    def post(self):
        """Create a new task"""
        try:
            data = request.get_json()
            if not data or 'title' not in data or 'description' not in data:
                return jsonify({"error": "Missing required fields"}), 400

            task = Task(
                title=data['title'],
                description=data['description']
            )
            db.session.add(task)
            db.session.commit()
            return jsonify(task.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    def put(self, task_id):
        """Update an existing task"""
        try:
            task = Task.query.get_or_404(task_id)
            data = request.get_json()
            
            if 'title' in data:
                task.title = data['title']
            if 'description' in data:
                task.description = data['description']
            
            db.session.commit()
            return jsonify(task.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    def delete(self, task_id):
        """Delete a task"""
        try:
            task = Task.query.get_or_404(task_id)
            db.session.delete(task)
            db.session.commit()
            return jsonify({"message": "Task deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

class CompleteTaskAPI(MethodView):
    """Handles task completion status"""
    
    def patch(self, task_id):
        """Mark a task as completed"""
        try:
            task = Task.query.get_or_404(task_id)
            task.completed = True  # Mark task as completed
            db.session.commit()  # Ensure changes are saved
            return jsonify(task.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

# Register routes
task_view = TaskAPI.as_view('task_api')
complete_task_view = CompleteTaskAPI.as_view('complete_task_api')

app.add_url_rule('/tasks', view_func=task_view, methods=['GET', 'POST'])
app.add_url_rule('/tasks/<int:task_id>', view_func=task_view, methods=['GET', 'PUT', 'DELETE'])
app.add_url_rule('/tasks/<int:task_id>/complete', view_func=complete_task_view, methods=['PATCH'])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
