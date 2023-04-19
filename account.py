class account:
     """ This is an account class to compute several bank tasks """
     
    def __init__ (self, name):  
        """ Sets object of the class """
        self.__account_name = name  
        self.__account_balance = 0

    
    def deposit(self, amount):
        """ Adds amount to account balance or returns False """       
        if amount > 0:  
            self.__account_balance = self.__account_balance + amount 
            return True
        else:   
            return False
            
    def withdraw(self, amount):
        """ Subtracts amount from account balance or returns False """
        if amount > 0: 
            if amount <= self.__account_balance: 
                self.__account_balance = self.__account_balance-amount  
                return True
            else:    
                return False
        else:   
            return False
        
    def getbalance(self):
        """ use methods to return account balance via account_balance variable """
        return self.__account_balance 
        
    def getname(self): 
        """ returns account name via account_name variable """
        return self.__account_name   
