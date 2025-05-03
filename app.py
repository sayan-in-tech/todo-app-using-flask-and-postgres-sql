from flask import Flask, render_template, request, redirect, url_for
from persistence.models import db
from api.todo import todo_bp
from services.todo_service import TodoService
import psycopg2
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(todo_bp)

    with app.app_context():
        db.create_all()

    # Routes
    @app.route('/')
    def index():
        todos = TodoService.get_all_todos()
        return render_template('todo/index.html', todos=todos)
    
    @app.route('/todos', methods=['POST'])
    def create_todo():
        title = request.form.get('title')
        try:
            todo = TodoService.create_todo(title)
            return render_template('todo/todo.html', todo=todo)
        except Exception as e:
            return str(e)
        
    @app.route('/todos/<int:todo_id>', methods=['DELETE'])
    def delete_todo(todo_id):
        if not TodoService.delete_todo(todo_id):
            return "Todo not found", 404
        return redirect(url_for('index'))
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)