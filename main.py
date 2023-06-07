from source.bank_account import BankAccount
from source.employee import Contractor
from source.payroll import Payroll, EmployeePayroll


def main():
    c1 = Contractor(123, "John Doe", 40.0, 8)

    bank_account = BankAccount()
    bank_account.deposit(1_000)

    payroll = EmployeePayroll(bank_account)
    payroll.add_daily_pay("2021-01-01", c1)
    payroll.pay()

    print(bank_account.balance)

    payroll.add_daily_pay("2021-01-02", c1)
    payroll.pay()

    print(bank_account.balance)


if __name__ == "__main__":
    main()
