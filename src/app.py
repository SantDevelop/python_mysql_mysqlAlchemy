from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), unique=True)

    description = db.Column(db.String(200))
    def _init_(self, title, description):
        self.title = title
        self.description = description

db.create_all()
class TaskSchema(ma.Schema):
    class Meta:
        fields=('id', 'title', 'description')
        
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/task', method=['POST'])

def create_task():
    print(request.json)
    return 'Recived'

if __name__ == "__main__":
    app.run(debug=True) 