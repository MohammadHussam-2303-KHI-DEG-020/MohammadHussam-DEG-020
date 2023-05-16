import json
import logging
import os

from flask import Flask, render_template, request
from logging import StreamHandler

# Problem -  App should be able to be executed both during development, with debugging enabled, and in production, with debugging disabled.
# Solution - 
app = Flask(__name__)
app.debug = os.environ.get("DEBUG") == "1"  # Enable debugging if DEBUG environment variable is set to "1"

# Problem 1 - The logs shouldn’t written to a file, but to the container output.

# Solution.
# Logging the logs to container output using streamHandler instead of a log file

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
stream_handler = StreamHandler()
root_logger.addHandler(stream_handler)


TODO_FILE_NAME = "/app/todo_data/todo.json"  #You can change the Path anytime when you want to switch from test to production

if os.path.exists(TODO_FILE_NAME):
    with open(TODO_FILE_NAME) as f:
        TODO_ITEMS = json.load(f)
else:
    TODO_ITEMS = []


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        TODO_ITEMS.append(content)
        # Data is being saved on each hit
        save_todo_items()

    return render_template("index.html", todo_items=TODO_ITEMS)

# This function saves the list on each call making it stateless instead of periodic saving.
def save_todo_items():
    with open(TODO_FILE_NAME, "w") as f:
        json.dump(TODO_ITEMS, f)

# Checks wheather the app is in debug mode or not.
if app.debug:
    app.logger.setLevel(logging.DEBUG)
    app.logger.debug("Debug mode is enabled.")
else:
    app.logger.debug("Debug mode is disabled.")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
