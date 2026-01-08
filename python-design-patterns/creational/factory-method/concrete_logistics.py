from logistics import Logistics
from transport import Transport
from concrete_transports import Truck, Ship, Airplane


class RoadLogistics(Logistics):

    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):

    def create_transport(self) -> Transport:
        return Ship()


class AirLogistics(Logistics):

    def create_transport(self) -> Transport:
        return Airplane()

