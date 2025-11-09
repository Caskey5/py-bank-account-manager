class User:
    def __init__(
            self,
            first_name, 
            last_name, 
            email, 
            phone_number, 
            password
):
            self.user_id: int = 0
            self.first_name = first_name
            self.last_name = last_name 
            self.email = email
            self.phone_number = phone_number 
            self.password = password
            # self.users = []
            # self.balance: float = 0.0
            # self.transactions = []

    def _full_name(self):
        return f'{self.first_name} {self.last_name}' 

    def __str__(self):
        return self._full_name()