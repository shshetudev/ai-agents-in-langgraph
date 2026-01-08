from transport import Transport


class Truck(Transport):

    def deliver(self) -> str:
        return "Delivering by land in a truck 🚚"


class Ship(Transport):

    def deliver(self) -> str:
        return "Delivering by sea in a ship 🚢"


class Airplane(Transport):

    def deliver(self) -> str:
        return "Delivering by air in an airplane ✈️"

