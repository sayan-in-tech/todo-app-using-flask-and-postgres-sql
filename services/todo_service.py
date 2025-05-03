from persistence.repository import TodoRepository
from datetime import datetime

class TodoService:
    @staticmethod
    def get_all_todos():
        return TodoRepository.get_all_todos()
    
    @staticmethod
    def get_todo(todo_id):
        return TodoRepository.get_by_id(todo_id)
    
    @staticmethod
    def create_todo(title):
        if not title or len(title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        return TodoRepository.create(title)
    
    @staticmethod
    def update_todo(todo_id, **kwargs):
        kwargs['updated_at'] = datetime.now()
        return TodoRepository.update(todo_id, **kwargs)
    
    @staticmethod
    def delete_todo(todo_id):
        return TodoRepository.delete(todo_id)
    
    @staticmethod
    def toggle_todo(todo_id):
        todo = TodoRepository.get_by_id(todo_id)
        if not todo:
            return None
        return TodoRepository.update(todo_id, completed=not todo.completed)