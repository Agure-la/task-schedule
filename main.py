from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/task'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
    scheduled_at = db.Column(db.DateTime)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    message = db.Column(db.String(255))
    sent_at = db.Column(db.DateTime)

# API routes
@app.route('/api/schedule/task', methods=['GET', 'POST'])
def schedule_task():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        tasks = Task.query.filter_by(user_id=user_id).all()
        return jsonify([{'description': task.description, 'scheduled_at': task.scheduled_at} for task in tasks])

    elif request.method == 'POST':
        data = request.json
        new_task = Task(user_id=data['user_id'], description=data['description'], scheduled_at=data['scheduled_at'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task scheduled successfully'}), 201

@app.route('/api/notifications', methods=['GET', 'POST'])
def manage_notifications():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        notifications = Notification.query.filter_by(user_id=user_id).all()
        return jsonify([{'message': notification.message, 'sent_at': notification.sent_at} for notification in notifications])

    elif request.method == 'POST':
        data = request.json
        new_notification = Notification(user_id=data['user_id'], message=data['message'], sent_at=data['sent_at'])
        db.session.add(new_notification)
        db.session.commit()
        return jsonify({'message': 'Notification sent successfully'}), 201
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
