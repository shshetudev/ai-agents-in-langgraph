class EmailService:
    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()


    def _connect(self):
        print("Connecting to email server...")


    def _authenticate(self):
        print("Authenticating...")


    def _disconnect(self):
        print("Disconnecting from email server...")

email_service = EmailService()
email_service.send_email()