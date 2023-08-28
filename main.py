from datetime import date
from car.car_factory import CarFactory

def main():
    current_date = date.today()
    last_service_date = date(2023, 1, 1)
    current_mileage = 6000
    last_service_mileage = 1000

    car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)

    print("Does the car need service?", car.needs_service())

if __name__ == "__main__":
    main()
# # Path: car_maintenace_system/main.py
