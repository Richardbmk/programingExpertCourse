"""TIM SOLUTION""" 
class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0.0

    def get_balance(self):
        return round(self._balance)

    def set_balance(self, balance):
        if type(balance) not in [int, float]:
            return

        if balance < 0 or balance >= 100000:
            return

        self._balance = balance
