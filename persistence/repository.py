from .models import db, Todo
from datetime import datetime

class TodoRepository:
    @staticmethod
    def get_all_todos():
        return Todo.query.filter_by(completed='f').order_by(Todo.created_at.desc()).all()
        # return Todo.query.order_by(Todo.created_at.desc()).all()
    
    @staticmethod
    def get_by_id(todo_id):
        return Todo.query.get(todo_id)
    
    @staticmethod
    def create(title):
        todo = Todo(title=title)
        db.session.add(todo)
        db.session.commit()
        return todo
    
    @staticmethod
    def update(todo_id, **kwargs):
        todo = Todo.query.get(todo_id)
        if not todo:
            return None
        
        for key, value in kwargs.items():
            if hasattr(todo, key):
                setattr(todo, key, value)
        
        db.session.commit()
        return todo
    
    @staticmethod
    def delete(todo_id):
        todo = Todo.query.get(todo_id)
        if not todo:
            return False
        
        db.session.delete(todo)
        db.session.commit()
        return True