class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.type = "Employee"

    def calculate_daily_payment(self) -> float:
        # must be greater than zero
        return 200


class Contractor(Employee):
    def __init__(self, id: int, name: str, hourly_rate: float, hours_per_day: int):
        super().__init__(id, name)
        self.hourly_rate = hourly_rate
        self.hours_per_day = hours_per_day
        self.type = "Contractor"

    def calculate_daily_payment(self) -> float:
        # must be greater than zero
        return self.hourly_rate * self.hours_per_day
