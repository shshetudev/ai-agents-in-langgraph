from logistics import Logistics
from concrete_logistics import RoadLogistics, SeaLogistics, AirLogistics


def client_code(logistics: Logistics) -> None:
    print(f"\nClient: I'm not aware of the creator's class, but it still works.")
    print(logistics.plan_delivery())


def main():
    print("=" * 60)
    print("Factory Method Pattern - Logistics Transportation System")
    print("=" * 60)

    print("\n--- Scenario 1: Road Transportation ---")
    print("App: Launched with RoadLogistics.")
    road_logistics = RoadLogistics()
    client_code(road_logistics)

    print("\n" + "-" * 60)
    print("\n--- Scenario 2: Sea Transportation ---")
    print("App: Launched with SeaLogistics.")
    sea_logistics = SeaLogistics()
    client_code(sea_logistics)

    print("\n" + "-" * 60)
    print("\n--- Scenario 3: Air Transportation ---")
    print("App: Launched with AirLogistics.")
    air_logistics = AirLogistics()
    client_code(air_logistics)

    print("\n" + "=" * 60)
    print("\nKey Benefits of Factory Method Pattern:")
    print("1. Avoids tight coupling between creator and concrete products")
    print("2. Single Responsibility Principle - product creation code in one place")
    print("3. Open/Closed Principle - can add new transport types without changing existing code")
    print("4. Makes the code more flexible and easier to extend")
    print("=" * 60)


if __name__ == "__main__":
    main()

