from serviceable.serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
# Path: car_maintenace_system/car/car.py
# Compare this snippet from car_maintenace_system/car/car.py:
# from serviceable.serviceable import Serviceable
# from engine.engine import Engine
# from battery.battery import Battery
#