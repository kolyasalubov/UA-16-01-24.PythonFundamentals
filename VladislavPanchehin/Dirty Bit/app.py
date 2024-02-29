# import the Flask class, render_template, request, redirect and url_for functions
from flask import Flask, \
    render_template, \
    request, \
    redirect, \
    url_for

# import the SQLAlchemy module to work with the database inside the Flask application.
from flask_sqlalchemy import SQLAlchemy
# line creates an instance of the Flask application.
# The __name__ parameter tells Flask the path to the current module
app = Flask(__name__)
# Set the SQLite database URI for the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# Disable change tracking for SQLAlchemy.
# This improves application performance by preventing unnecessary change tracking.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# secret key for defender app
app.config['SECRET_KEY'] = 'burn_baby_burn'
# Creates a SQLAlchemy object and associates it with the Flask application
db = SQLAlchemy(app)

# The block defines the data model for tasks (Todo) in the application.
# Each task has an ID, a name, and a flag indicating whether it has completed or failed.


class Todo(db.Model):
    # Create a Todo model to represent the table in the database
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))  # Task ID (primary key)
    done = db.Column(db.Boolean)  # Task name

# Route for home page


@app.route('/')
def home():
    todo_list = Todo.query.all()  # Get a list of all tasks from the database
    total_tasks = len(todo_list)  # Calculate the total number of tasks
    # Calculate the number of completed tasks
    completed_tasks = sum(todo.done for todo in todo_list)

# Calculate the success of completing tasks as a percentage
    if total_tasks == 0:
        success_rate = 0
    else:
        success_rate = round((completed_tasks / total_tasks) * 100)

# Determine the color and image of the message depending on the success of execution
    if success_rate <= 20:
        message_color = "red"
        message = "Погано попрацював"
        message_image = "static/bad.png"
    elif success_rate <= 40:
        message_color = "grey"
        message = "Слабо, можна краще"
        message_image = "static/poor.png"
    elif success_rate <= 60:
        message_color = "blue"
        message = "Нормально"
        message_image = "static/normal.png"
    elif success_rate <= 80:
        message_color = "lightgreen"
        message = "Добре попрацював"
        message_image = "static/good.png"
    else:
        message_color = "green"
        message = "Дуже добре"
        message_image = "static/excellent.png"

# Display an HTML template with the passed variables
    return render_template('base.html',
                           todo_list=todo_list,
                           total_tasks=total_tasks,
                           completed_tasks=completed_tasks,
                           success_rate=success_rate,
                           message=message,
                           message_color=message_color,
                           message_image=message_image)

# Route for adding a new task


@app.route('/add', methods=['POST'])
def add():
    name = request.form.get("name")  # Get the task name from the form data
    new_task = Todo(name=name, done=False)  # Create a new task
    db.session.add(new_task)  # Add a task in the database session
    db.session.commit()  # Save changes to the database
    return redirect(url_for("home"))  # Redirect to home page

# Route to update task state


@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.get(todo_id)  # Get the task by identifier
    todo.done = not todo.done  # Invert the task execution state
    db.session.commit()  # Save changes to the database
    return redirect(url_for("home"))  # Redirect to home page

# Route for deleting a task


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get(todo_id)  # Get the task by identifier
    db.session.delete(todo)  # Remove the task from the database session
    db.session.commit()  # Save changes to the database
    return redirect(url_for("home"))  # Redirect to home page


# Start the Flask web server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
