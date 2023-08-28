class Tire:
    def needs_service(self, tire_wear):
        pass


class CarriganTires(Tire):
    def needs_service(self, tire_wear):
        return any(x >= 0.9 for x in tire_wear)


class OctoprimeTires(Tire):
    def needs_service(self, tire_wear):
        return sum(tire_wear) >= 3
