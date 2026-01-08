# SRP: Single Responsibility Principle
# A class should have only one reason to change.
# Here, the UserService class is responsible for user registration,
# while the EmailSender class is responsible for sending emails.

class EmailSender:
    def send_email(self, subject, recipient):
        print(f"Sending email to {recipient}: {subject}")

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserService:
    def register(self, user):
        print(f"Registering user: {user.username}")

        # Send email notification
        email_sender = EmailSender()
        email_sender.send_email("Welcome to our platform!", user.email)

if __name__ == "__main__":
    user = User("john_doe", "john.doe@gmail.com")
    user_service = UserService()
    user_service.register(user)