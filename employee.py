"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

"""
Going to dive into full OO mode 
"""

class ContractCommission: 
    def __init__(self, number_of_contracts: int, pay_per_contract: int):
        self.number_of_contracts = number_of_contracts
        self.pay_per_contract = pay_per_contract
class Employee:
    def __init__(self, name: str, commission: ContractCommission=None, bonus_commission: int=None):
        self.name = name
        self.commission = commission
        self.bonus_commission = bonus_commission

    def get_pay(self):
        pay = self.bonus_commission if self.bonus_commission is not None else 0
        pay += self.commission.number_of_contracts * self.commission.pay_per_contract if self.commission is not None else 0
        return pay

    def __str__(self):
        if self.commission is not None:
            return f" and receives a commission for {self.commission.number_of_contracts} contract(s) at {self.commission.pay_per_contract}/contract"
        elif self.bonus_commission is not None: 
            return f" and receives a bonus commission of {self.bonus_commission}"
        else:
            return ""
        
class MonthlyEmployee(Employee):

    def __init__(self, name: str, salary: int, commission: ContractCommission=None, bonus_commission: int=None):
        super().__init__(name, commission, bonus_commission)
        self.salary = salary
        

    def get_pay(self):
        pay = self.salary
        pay += super().get_pay()
        return pay

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}{super().__str__()}.  Their total pay is {self.get_pay()}."

class ContractEmployee(Employee):

    def __init__(self, name: str, pay_per_hour: int, number_of_hours: int, commission: ContractCommission=None, bonus_commission: int=None):
        super().__init__(name, commission, bonus_commission)
        self.pay_per_hour = pay_per_hour
        self.number_of_hours = number_of_hours
        

    def get_pay(self):
        pay = self.pay_per_hour * self.number_of_hours
        pay += super().get_pay()
        return pay
        

    def __str__(self):
        return f"{self.name} works on a contract of {self.number_of_hours} hours at {self.pay_per_hour}/hour{super().__str__()}.  Their total pay is {self.get_pay()}."



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, commission=ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 25, 150, commission=ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 30, 120, bonus_commission=600)
