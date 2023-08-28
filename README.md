# Car Service Manager

## Overview

Car Service Manager is a Python project which is was part of the Back-End Engineering Job Simulation program by "Lyft Inc" from Forage, aimed at managing the servicing needs of a fleet of cars. It employs design patterns such as Factory Method, Strategy, and Composition to maintain an easily extensible, modular codebase.

## Features

- Easily determine if any component (Engine, Battery, etc.) of a car needs service.
- Add new types of car components with minimal code changes.
- Update the service criteria for different components centrally.
- Different car models composed of various parts for flexible configuration.

## Design Patterns Used

- **Factory Method**: For creating instances of different types of cars.
- **Strategy Pattern**: For managing service criteria centrally.
- **Composition Over Inheritance**: To compose cars from various parts.

## Directory Structure

```plaintext

├── battery/
│   ├── __init__.py
│   └── battery.py
├── car/
│   ├── __init__.py
│   └── car.py
├── engine/
│   ├── __init__.py
│   └── engine.py
├── serviceable/
│   └── serviceable.py
├── tires/  # New directory
│   ├── __init__.py
│   └── tires.py
├── tests/  
│   ├── __init__.py
│   ├── test_battery.py
│   ├── test_engine.py
│   └── test_tires.py  # New test file
├── README.md
└── main.py

```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chinesefirewall/forage-lyft-starter-repo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CarServiceManager
   ```

3. Run the program:

   ```bash
   python main.py  # or however you choose to run it
   ```

## Usage

To create a new car:

```python
from car.car import Car
from CarFactory import CarFactory
from datetime import date

# Create a Calliope model car
car = CarFactory.create_calliope(date.today(), date(2023, 1, 1), 6000, 1000)

# Check if the car needs service
if car.needs_service():
    print("This car needs service.")
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
