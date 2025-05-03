# To-Do List Application

A modern, responsive web application for managing your daily tasks with real-time updates using HTMX.

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

## Features

- **Real-time updates** with HTMX for a seamless user experience
- **Create, Read, Update, Delete** operations for todo items
- **Mark tasks as completed** with visual feedback
- **Responsive design** works on desktop and mobile devices
- **Popup editing** for quick task modifications
- **PostgreSQL database** for reliable data storage
- **Flask backend** providing a robust API

## Technologies Used

### Backend
- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [PostgreSQL](https://www.postgresql.org/) - Relational database
- [Psycopg2](https://www.psycopg.org/) - PostgreSQL adapter for Python

### Frontend
- [HTMX](https://htmx.org/) - Allows for AJAX, CSS Transitions, WebSockets without writing JavaScript
- HTML5 & CSS3 - Structure and styling
- JavaScript - Enhanced interactivity

## Project Structure

```
To-Do List/
├── api/                # API endpoints
│   └── todo.py         # Todo CRUD operations
├── persistence/        # Database related code
│   ├── models.py       # Database models
│   └── repository.py   # Database access layer
├── services/           # Business logic
│   └── todo_service.py # Todo business logic
├── static/             # Static assets
│   ├── css/            # Stylesheets
│   │   └── styles.css  # Main stylesheet
│   └── js/             # JavaScript files
│       └── script.js   # Main script file
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   └── todo/           # Todo templates
│       ├── index.html  # Main todo page
│       └── todo_item.html # Todo item template
├── app.py              # Application initialization
└── requirements.txt    # Project dependencies
```

## Installation

### Prerequisites
- Docker and Docker Compose installed on your system

### Running with Docker

1. **Clone the repository**

```bash
git clone https://github.com/sayan-in-tech/todo-app-using-flask-and-postgres-sql.git
cd todo-app-using-flask-and-postgres-sql
```

2. **Build and run the Docker containers**

```bash
docker-compose up -d
```

This command builds the Docker images and starts the containers in detached mode.

### Docker Configuration

#### Environment Variables

Create a `.env` file in the project root to store your environment variables:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=todo_db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
SECRET_KEY=your_secret_key_here
```

#### Customizing PostgreSQL

You can customize your PostgreSQL configuration by editing the `docker-compose.yml` file:

```yaml
services:
  postgres:
    image: postgres:13
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5

  web:
    build: .
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
      - SECRET_KEY=${SECRET_KEY}
    ports:
      - "5000:5000"

volumes:
  postgres_data:
```

#### Database Persistence

The PostgreSQL data is persisted using a named volume (`postgres_data`). This ensures your data remains intact even if the containers are stopped or removed.

#### Production Deployment Considerations

For production environments:

1. **Use secrets management**: 
   - Replace plain text environment variables with Docker secrets or a secure vault solution

2. **Configure SSL**:
   - Add SSL certificates for secure HTTPS connections

3. **Set up regular backups**:
   - Configure automated PostgreSQL database backups

3. **Access the application**

The application will be available at `http://localhost:5000`

4. **Stop the containers**

```bash
docker-compose down
```

## API Documentation

### Todo Endpoints

#### Get All Todos
```
GET /api/todos/show_all
```
Returns all active todos ordered by creation date.

#### Create Todo
```
POST /api/todos/create
```
Creates a new todo item.

**Body**:
```json
{
  "title": "Task description"
}
```

#### Get Todo
```
GET /api/todos/:id
```
Returns a specific todo by ID.

#### Update Todo
```
PUT /api/todos/:id
```
Updates a specific todo.

**Form Data**:
```
title: Updated task description
```

#### Toggle Todo Completion
```
PUT /api/todos/:id/toggle
```
Toggles the completion status of a todo.

#### Delete Todo
```
DELETE /api/todos/:id
```
Deletes a specific todo.

## Data Model

### Todo

| Field      | Type      | Description                           |
|------------|-----------|---------------------------------------|
| id         | Integer   | Primary key                           |
| title      | String    | The title/description of the task     |
| completed  | Boolean   | Whether the todo is completed         |
| created_at | DateTime  | When the todo was created             |
| updated_at | DateTime  | When the todo was last updated        |

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [HTMX](https://htmx.org/) for making interactive web applications with minimal JavaScript
- [Flask](https://flask.palletsprojects.com/) for the excellent Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) for the powerful ORM capabilities
````
