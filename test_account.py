from pytest import *
from account import *


class Test:
    def setup(self):
        self.a1 = Account("johnny")

    def teardown(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == "johnny"
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(1.5) is True
        assert self.a1.get_balance() == approx(1.5, abs=0.01)

    def test_withdraw(self):

        self.a1.deposit(25)
        assert self.a1.withdraw(25) is True
        assert self.a1.get_balance() == 0

        self.a1.deposit(15)
        assert self.a1.withdraw(25) is False
        assert self.a1.get_balance() == 15

        assert self.a1.withdraw(-5) is False
        assert self.a1.get_balance() == 15

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 15

