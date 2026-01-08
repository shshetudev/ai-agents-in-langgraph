from abc import ABC, abstractmethod
from transport import Transport


class Logistics(ABC):

    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()

        result = f"Logistics: Planning delivery...\n"
        result += f"Logistics: {transport.deliver()}"

        return result

