from dataclasses import dataclass, asdict


@dataclass
class PayrollEntry:
    employee_id: int
    employee_name: str
    employee_type: str
    date: str
    payment: float
    deductions: float
    taxes: float
    total: float = 0.0

    def __post_init__(self):
        self.total = self.payment + self.deductions + self.taxes

    def to_dict(self):
        return asdict(self)
