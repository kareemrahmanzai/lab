import pytest
from account import account

def test_init():
  acc = account("Kareem")
  assert acc.getname() == "Kareem"
  assert acc.getbalance() == 0
  
def test_deposit():
  acc = account("Kareem")
  assert acc.deposit() == 100
  assert acc.getbalance() == 100
  
def test_withdraw():
  
