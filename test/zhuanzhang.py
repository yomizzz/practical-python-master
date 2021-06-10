"""
在不对临界资源（银行账户）进行保护的前提下，用100个线程向同一个银行账户转入1元钱
目的：看看在不对临界资源进行保护的情况下，会产生什么样的结果
运行结果：远远小于100元，运行3次分别是1，2，1

Version: 0.1
Author: yomi
Date: 2021-06-09
"""

from time import sleep
from threading import Thread


class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟受理存款业务需要0.01秒的时间
        sleep(0.01)
        # 修改账户余额
        self._balance = new_balance

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
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为：￥%d元' % account.balance)


if __name__ == '__main__':
    main()
