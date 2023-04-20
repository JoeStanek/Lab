class Account:

    def __init__(self, name) -> None:
        """
        Function to initialize name and balance,
        :param name: sets the name of the account
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount) -> bool:
        """
        Allows users to deposit an amount into their account
        :param amount: the amount they want to deposit
        :return: true or false depending on if the process was successful or not
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool:
        """
        Allows users to withdraw an amount from their account
        :param amount: Amount they want to withdraw
        :return: True or False depending on if the process was successful or not
        """
        if amount > 0 or amount < self.__account_balance:
            self.__account_balance -= amount
        else:
            return False

    def get_balance(self) -> int:
        """
        Lets users see their balance
        :return: The users balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Lets users see the account name
        :return: The account name
        """
        return self.__account_name