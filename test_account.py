import pytest
from account import account

class Test:

    def test_init(self):
        self.acc = account("Kareem")
        assert self.acc.get_name() == "Kareem"
        assert self.acc.get_balance() == 0

    def test_deposit(self):
        self.acc = account("Kareem")
        assert self.acc.deposit(50)
        assert self.acc.get_balance() == 50
        assert self.acc.deposit(-50) == False
        assert self.acc.get_balance() == 50


    def test_withdraw(self):
        self.acc = account("Kareem")
        assert self.acc.deposit(50)
        assert self.acc.withdraw(50)
        assert self.acc.get_balance() == 0
        assert self.acc.withdraw(50) == False
        assert self.acc.get_balance() == 0



