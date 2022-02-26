"""
Bug & Code by Yunhao Cao
"""

import typing


INCREASE_CREDIT = 100

class BankAccount:
    def __init__(self, name : str, initialDeposit : int):
        self.name = name
        self.money = initialDeposit
        self.amountLoaned = 0
        self.credit = 100
        self.totalCredit = 100
    
    # transfer money into another account
    def transferMoney(self, toAccount, amount : int) -> None:
        # TODO: Q1 What check is missing here?
        # TODO: Q2 Another error is presented here, please try to figure it out yourself.
        toAccount.money -= amount
        self.money += amount
    
    def borrowMoney(self,amount : int) -> None:
        # TODO: Q3 What check is missing here?
        self.credit -= amount
        self.amountLoaned += amount
        self.money += amount
    
    def payBackLoan(self,amount : int) -> None:
        if self.money <= amount:
            raise Exception('not enough money to pay back the loan')

        # TODO: Q4 What check is missing here?
        # TODO: Q5 Another erorr is made here, please try to figure it out yourself.

        self.credit += amount
        self.amountLoaned -= amount
        self.money -= amount

        # increment credit each time when a pay back is made
        increaseInCreditAmount = round(amount / self.totalCredit * INCREASE_CREDIT)
        self.totalCredit += increaseInCreditAmount
    
    """
    This function takes in parameters:
    accounts - a python list of BankAccount instances
    eachAmount - a python list of int, eachAmount[i] corresponds to the amount of money that needs to be sent to accounts[i]
    
    Note: The function must fail and no money should be transferred if ANY of the transfers would fail.
    """
    def groupTransfer(self, accounts : typing.List, eachAmount : typing.List[int]) -> None:
        assert len(accounts) == len(eachAmount)

        # TODO: Bug in this function.

        sumAmount = 0
        for i in range(len(eachAmount)):
            ithAmount = eachAmount[i]
            if ithAmount < 0:
                raise Exception("cannot perform negative amount transfer")
            sumAmount += ithAmount
        
        if(self.money < sumAmount):
            raise Exception("not enough money")
        

        for i in range(len(accounts)):
            ithAccount = accounts[i]
            ithAmount = eachAmount[i]
            ithAccount.money -= ithAmount
            self.money += ithAmount
        