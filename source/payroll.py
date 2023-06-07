from typing import List

from source.bank_account import BankAccount
from source.employee import Contractor, Employee
from source.exceptions import PayrollError, NoEntriesError
from source.payroll_entry import PayrollEntry
from source.report import Report, JSONReport


class Payroll:
    def __init__(self, bank_account: BankAccount):
        self.bank_account = bank_account
        self._daily_payments_entries: List[PayrollEntry] = []

    def add_daily_pay(self, date: str, employee: Contractor) -> PayrollEntry:
        daily_payment = employee.calculate_daily_payment()
        payroll_entry = PayrollEntry(
            employee_id=employee.id,
            employee_name=employee.name,
            employee_type=employee.type,
            date=date,
            payment=daily_payment,
            deductions=daily_payment * 24.0 / 100,
            taxes=daily_payment * 6.0 / 100,
        )
        self._daily_payments_entries.append(payroll_entry)
        return payroll_entry

    def create_report(self) -> Report:
        if not self._daily_payments_entries:
            raise PayrollError("No entries to generate report")
        return Report(self._daily_payments_entries)

    def pay(self):
        total = sum(entry.payment for entry in self._daily_payments_entries)
        if total > self.bank_account.balance:
            raise ValueError("Not enough funds")

        self.bank_account.withdraw(total)

        # post-conditions
        self._daily_payments_entries = []
        if self.bank_account.balance < 1_000:
            print("Send an email notifying this")
            print("Do other stuff")


class EmployeePayroll(Payroll):
    def add_daily_pay(self, date: str, employee: Employee) -> PayrollEntry:
        deductions_percentage = 16.0 if employee.type == "Employee" else 24.0
        tax_percentage = 8.0 if employee.type == "Employee" else 6.0
        daily_payment = employee.calculate_daily_payment()
        payroll_entry = PayrollEntry(
            employee_id=employee.id,
            employee_name=employee.name,
            employee_type=employee.type,
            date=date,
            payment=daily_payment,
            deductions=daily_payment * deductions_percentage / 100,
            taxes=daily_payment * tax_percentage / 100,
        )
        self._daily_payments_entries.append(payroll_entry)
        return payroll_entry

    def create_report(self) -> JSONReport:
        if not self._daily_payments_entries:
            raise NoEntriesError("No entries to generate report")
        return JSONReport(self._daily_payments_entries)

    def pay(self):
        total = sum(entry.payment for entry in self._daily_payments_entries)
        if total > self.bank_account.balance:
            raise ValueError("Not enough funds")

        self.bank_account.withdraw(total)
        # Removing the validations at the end of the method violates the LSP because we are
        # weakening the post-conditions
