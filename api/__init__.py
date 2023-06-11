from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://cqtdgqvm:FbD22gPUCjOaD-i86tm1uJvQGP1L6_W5@ruby.db.elephantsql.com/cqtdgqvm"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def hello():
    return 'Wood Guitars Backend'
