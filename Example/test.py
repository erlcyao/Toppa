"""
                   _oo0oo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  0\  =  /0
                ___/`---'\___
              .' \\|     |// '.
             / \\|||  :  |||// \
            / _||||| -:- |||||- \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |_/ |
           \  .-\__  '-'  ___/-. /
         ___'. .'  /--.--\  `. .'___
      ."" '<  `.___\_<|>_/___.' >' "".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `_.   \_ __\ /__ _/   .-` /  /
 =====`-.____`.___ \_____/___.-`___.-'=====
                   `=---='
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           菩提本无树   明镜亦非台
           本来无BUG    何必常修改
"""
# Tests & Test Code By Yunhao Cao

from random import random
import typing
from models import BankAccount
import traceback

def performTest(listOfFn : typing.List):
    for fn in listOfFn:
        result = False
        try:
            result = fn()
        except AssertionError as e:
            print()
            print("Assertion Failed, reason below")
            print(str(e))
            print()
            print(traceback.format_exc())
        except BaseException as e:
            print()
            print("Failed, Encountered erorr during test")
            print(str(e))
            print()
            print(traceback.format_exc())
        
        print()
        if result == False:
            print("Test Failed")
            return
    print()
    print("TEST DONE! ALL SUCCESSFUL!")    

def checkEq(expected, actual, errMessage = None):
    msg = errMessage if not(errMessage is None) else ("Expected [" + str(expected) + "], but got [" + str(actual) + "]")
    if expected != actual:
        raise AssertionError(msg)

def testQ1() -> bool:
    print("======Q1======")
    print("=> BankAccount.transferMoney")
    yunhaoAccount = BankAccount("Yunhao Cao",0)
    howardAccount = BankAccount("Howard Meng",0)
    try:
        yunhaoAccount.transferMoney(howardAccount,1000)
    except BaseException as e:
        pass
    else:
        print("Failed, can you transfer money when you don't have enough money?")
        return False

    print("Passed Q1 Test!")
    print("==============")
    print()
    return True

def testQ2() -> bool:
    print("======Q2======")
    print("=> BankAccount.transferMoney")
    yunhaoAccount = BankAccount("Yunhao Cao",100)
    howardAccount = BankAccount("Howard Meng",0)
    try:
        yunhaoAccount.transferMoney(howardAccount,100)
    except BaseException as e:
        print("Failed, an exception is triggered")
        print(str(e))
        return False
    
    checkEq(0,yunhaoAccount.money,"After transfer, the account of whom is transferring should have less money.")
    checkEq(100,howardAccount.money,"After transfer, the account of whom is receiving the transfer should have more money.")
    print("Passed Q2 Test!")
    print("==============")
    print()
    return True


def testQ3() -> bool:
    print("======Q3======")
    print("=> BankAccount.borrowMoney")
    yunhaoAccount = BankAccount("Yunhao Cao",100)
    try:
        yunhaoAccount.borrowMoney(120)
    except BaseException as e:
        pass
    else:
        print("Failed, if we try to borrow too much money that exceeds our credit, we should not be allowed to do so")
        return False
    
    print("Passed Q3 Test!")
    print("==============")
    print()
    return True

def testQ4() -> bool:
    print("======Q4======")
    print("=> BankAccount.payBackLoan")
    yunhaoAccount = BankAccount("Yunhao Cao",100)
    howardAccount = BankAccount("Howard Meng",0)

    yunhaoAccount.borrowMoney(100)
    yunhaoAccount.transferMoney(howardAccount,200)
    try:
        yunhaoAccount.payBackLoan(100)
    except BaseException as e:
        pass
    else:
        print("Failed, if we try to pay back loan when we don't have money, are we allowed to have negative balance?")
        return False

    try:
        howardAccount.payBackLoan(50)
    except BaseException as e:
        pass
    else:
        print("Failed, if we don't have money loaned but want to \"pay back\" loan, are we allowed to?")
        return False

    print("Passed Q4 Test!")
    print("==============")
    print()
    return True


def testQ5() -> bool:
    print("======Q5======")
    print("=> BankAccount.payBackLoan")
    yunhaoAccount = BankAccount("Yunhao Cao",100)
    yunhaoAccount.borrowMoney(100)
    yunhaoAccount.payBackLoan(100)
    try:
        yunhaoAccount.borrowMoney(200)
    except BaseException as e:
        print("Failed, our credit should grow as we pay back our previous loan")
        return False

    checkEq(0,yunhaoAccount.credit,"Failed, our credit should grow as we pay back our previous loan")

    print("Passed Q5 Test!")
    print("==============")
    print()
    return True

def testQ6() -> bool:
    print("======Q6======")
    print("=> BankAccount.groupTransfer")
    
    initialRecipientAmounts = [round(random() * 1000) for i in range(4)]
    transferAmounts = [round(random()*20) for i in range(4)]
    recipientNames = ['Howard Meng','Bowen Wang','Random Guy 1', 'Random Guy 2']

    yunhaoAccount = BankAccount("Yunhao Cao",1000000000000) #Yunhao Really Rich here, huh?
    recipientAccounts = [BankAccount(recipientNames[i],initialRecipientAmounts[i]) for i in range(4)]
    
    yunhaoAccount.groupTransfer(recipientAccounts,transferAmounts)
    

    checkEq(1000000000000 - sum(transferAmounts),yunhaoAccount.money)
    for i in range(4):
        checkEq(initialRecipientAmounts[i] + transferAmounts[i],recipientAccounts[i].money)

    print("Passed Q6 Test!")
    print("==============")
    print()
    return True


if __name__ == '__main__':
    performTest([
        testQ1,
        testQ2,
        testQ3,
        testQ4,
        testQ5,
        testQ6
    ])