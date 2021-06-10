"""
通过"锁"来保护临界资源（银行账户），用100个线程向同一个银行账户转入1元钱，从而获取正确的结果


Version: 0.1
Author: yomi
Date: 2021-06-09
"""

from time import sleep
from threading import Thread, Lock

class Account(object):
    
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance  = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()
    
    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    
    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账号余额为：￥%d元' % account.balance)


if __name__ == '__main__':
    main()