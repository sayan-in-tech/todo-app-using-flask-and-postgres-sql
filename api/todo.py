from flask import Blueprint, request, jsonify
from flask import render_template
from services.todo_service import TodoService
from persistence.models import Todo

todo_bp = Blueprint('todo', __name__, url_prefix='/api/todos')

@todo_bp.route('/show_all', methods=['GET'])
def get_todos():
    todos = TodoService.get_all_todos()
    return jsonify([todo.to_dict() for todo in todos])

@todo_bp.route('/create', methods=['POST'])
def create_todo():
    data = request.get_json()
    try:
        todo = TodoService.create_todo(data['title'])
        return jsonify(todo.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
@todo_bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = TodoService.get_todo(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    if request.headers.get('HX-Request') == 'true':
        return render_template('todo/todo_edit_form.html', todo=todo)
    
    return render_template('todo/todo_item.html', todo=todo)


@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.form
    todo = TodoService.update_todo(todo_id, title=data.get('title'), )
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    return render_template('todo/todo_item.html', todo=todo)
 
    # data = request.get_json()
    # todo = TodoService.update_todo(todo_id, **data)
    # if not todo:
    #     return jsonify({'error': 'Todo not found'}), 404
    # return jsonify(todo.to_dict())

@todo_bp.route('/<int:todo_id>/toggle', methods=['PUT'])
def toggle_todo(todo_id):
    todo = TodoService.toggle_todo(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    return render_template('todo/todo_item.html', todo=todo)

@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if not TodoService.delete_todo(todo_id):
        return jsonify({'error': 'Todo not found'}), 404
    return '', 204