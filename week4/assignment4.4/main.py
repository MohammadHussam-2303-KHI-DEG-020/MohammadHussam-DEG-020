import os
import logging
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('FLASK_ENV') == 'development'
app.config['DB_HOST'] = os.environ.get('DB_HOST', 'db')
app.config['DB_PORT'] = int(os.environ.get('DB_PORT', 5432))
app.config['DB_NAME'] = os.environ.get('DB_NAME', 'your_database_name')
app.config['DB_USER'] = os.environ.get('DB_USER', 'your_username')
app.config['DB_PASSWORD'] = os.environ.get('DB_PASSWORD', 'your_password')

# Configure logging to output to the container output
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
root_logger.addHandler(stream_handler)

def add_todo_item(item):
    conn = psycopg2.connect(
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        dbname=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD']
    )
    c = conn.cursor()
    c.execute('INSERT INTO todo (content) VALUES (%s)', (item,))
    conn.commit()
    conn.close()

def get_todo_items():
    conn = psycopg2.connect(
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        dbname=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD']
    )
    c = conn.cursor()
    c.execute('SELECT content FROM todo')
    todo_items = [item[0] for item in c.fetchall()]
    conn.close()
    return todo_items

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        add_todo_item(content)

    todo_items = get_todo_items()

    return render_template("index.html", todo_items=todo_items)

if __name__ == "__main__":
    if app.config['DEBUG']:
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
    else:
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
