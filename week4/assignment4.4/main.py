import os
import logging
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('FLASK_ENV') == 'development'
app.config['TODO_DB'] = os.environ.get('TODO_DB', 'todo.db')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

def init_db():
    with sqlite3.connect(app.config['TODO_DB']) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS todo
                     (content text)''')
        conn.commit()

def add_todo_item(item):
    with sqlite3.connect(app.config['TODO_DB']) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO todo VALUES (?)', (item,))
        conn.commit()

def get_todo_items():
    with sqlite3.connect(app.config['TODO_DB']) as conn:
        c = conn.cursor()
        c.execute('SELECT content FROM todo')
        todo_items = [item[0] for item in c.fetchall()]
    return todo_items

init_db()

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        add_todo_item(content)

    todo_items = get_todo_items()

    return render_template("index.html", todo_items=todo_items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

