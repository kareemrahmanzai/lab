import pytest
from account import account

class Test:

    def test_init(self):
        self.acc = account("Kareem")
        assert self.acc.getname() == "Kareem"
        assert self.acc.getbalance() == 0

    def test_deposit(self):
        self.acc = account("Kareem")
        assert self.acc.deposit(50)
        assert self.acc.getbalance() == 50
        assert self.acc.deposit(-50) == False
        assert self.acc.getbalance() == 50


    def test_withdraw(self):
        self.acc = account("Kareem")
        assert self.acc.deposit(50)
        assert self.acc.withdraw(50)
        assert self.acc.getbalance() == 0



