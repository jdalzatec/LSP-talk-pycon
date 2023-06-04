from source.bank_account import BankAccount
from source.employee import Contractor, Employee
from source.payroll import Payroll, EmployeePayroll


def main():
    c1 = Contractor(123, 'John Doe', 40.0, 4)
    c2 = Contractor(567, 'Olivia Guy', 25.4, 5)
    e1 = Employee(999, 'Maria Smith')

    bank_account = BankAccount()
    bank_account.deposit(1_000)

    payroll = Payroll(bank_account)  # EmployeePayroll(bank_account)
    payroll.add_daily_pay('2021-01-01', c1)
    payroll.add_daily_pay('2021-01-02', c1)
    payroll.add_daily_pay('2021-01-02', c2)
    payroll.add_daily_pay('2021-01-02', e1)

    report = payroll.create_report()
    print(report.generate())
    payroll.pay()
    print(bank_account.balance)


if __name__ == '__main__':
    main()
