from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self) -> None:
        pass


class EmailService(NotificationService):
    def send_notification(self) -> None:
        print(f"Sending email notification")


class MobileService(NotificationService):
    def send_notification(self) -> None:
        print(f"Sending sms")

class Order:
    def __init__(self, notification_service: NotificationService) -> None:
        self.notification_service = notification_service

    def create(self):
        self.notification_service.send_notification()

emailOrder = Order(EmailService())
emailOrder.create()
mobileOrder = Order(MobileService())
mobileOrder.create()