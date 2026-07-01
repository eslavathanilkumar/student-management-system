from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Student Management System Running"

def create_app():
    return app

if __name__ == "__main__":
    app.run(debug=True)