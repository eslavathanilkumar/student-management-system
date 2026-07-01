from flask import Flask
from database import db
from routes.student_routes import student_bp

app = Flask(__name__)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize db
db.init_app(app)

# register routes
app.register_blueprint(student_bp)

@app.route("/")
def home():
    return "Student Management System Running with DB"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()   # creates tables automatically

    app.run(debug=True)