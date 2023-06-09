class account:
    """ This is an account class to compute several bank tasks
    """


    def __init__(self, name: str) -> None:
        """ Sets object of the class
        """
        self.__account_name = name
        self.__account_balance = 0


    def deposit(self, amount):
        """ Adds amount to account balance or returns False
        """
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False


    def withdraw(self, amount):
        """ Subtracts amount from account balance or returns False
        """
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance = self.__account_balance - amount
                return True
            else:
                return False
        else:
            return False


    def get_balance(self) -> str:
        """ use methods to return account balance via account_balance private variable
        """
        return self.__account_balance


    def get_name(self) -> str:
        """ returns account name via account_name private variable
        """
        return self.__account_name
