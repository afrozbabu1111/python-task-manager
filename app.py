//Python Task Manager
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Python Task Manager</title>
        </head>
        <body>
            <h1>Welcome to Python Task Manager!</h1>
            <p>My first Python application is running.</p>
            <p>I am learning DevOps step by step.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
