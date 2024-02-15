API Routes
1. /api/schedule/task
GET: Retrieve scheduled tasks for a user.
POST: Schedule a new task.
Example Usage:
GET: Retrieve scheduled tasks for a user


GET /api/schedule/task?user_id=<user_id>
POST: Schedule a new task


POST /api/schedule/task
Content-Type: application/json

{
  "user_id": "<user_id>",
  "description": "<task_description>",
  "scheduled_at": "<scheduled_date_time>"
}
2. /api/notifications
GET: Fetch notifications for a user.
POST: Send a notification.
Example Usage:
GET: Fetch notifications for a user


GET /api/notifications?user_id=<user_id>
POST: Send a notification


POST /api/notifications
Content-Type: application/json

{
  "user_id": "<user_id>",
  "message": "<notification_message>",
  "sent_at": "<sent_date_time>"
}
Running the Application
To run the application, follow these steps:

Install the required dependencies by running:


pip install -r requirements.txt
Start the Flask application by running:

python app.py
Access the API endpoints using a REST client or integrate them into your frontend application
