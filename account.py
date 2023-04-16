class account:
     
    def __init__ (self, name):
        
        self.__account_name=name   #private data variables initialising using double underscore __
        self.__account_balance=0

    
    def deposit(self, amount):
                
        if amount>0:  #amount checking
            
            self.__account_balance=self.__account_balance+amount 
            
            return True
        
        else:
            
            return False
            
    def withdraw(self, amount):

        if amount>0: #amount checking
            
            if amount<=self.__account_balance:  #limit checking
                
                self.__account_balance=self.__account_balance-amount  #updating bank balance- amount reduction
                
                return True
            
            else:
                
                return False
        else:
            
            return False
        
    def getbalance(self):
    
        return self.__account_balance  #returning balance
        
    def getname(self):
        
        return self.__account_name   #returning name
