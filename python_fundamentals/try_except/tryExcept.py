# 1) What is try-except?
try:
    pass
except Exception as e:
    pass

# 2) What is finally?
try:
    pass
except Exception as e:
    pass
finally:
    pass

# 3) What are custom exceptions?
class tempException(Exception):
    pass

class bank:
    def __init__(self,bal):
        self.bal=bal
    
    def withdraw(self,amount):
        if amount>self.bal:
            raise tempException('Insufficient amount!!')
        else:
            print(amount, "Rs Withdraw")

try:
    b=bank(100)
    b.withdraw(10)
except tempException as e:
    print(e)