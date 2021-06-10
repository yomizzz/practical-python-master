# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

'''
# 已知贷款年限，贷款金额，贷款利率，每个月还款额，求总还款额？需要还几个月？
i = 0
while principal > 0:
    principal = principal * (1 + rate / 12 ) - payment
    total_paid = total_paid + payment
    i = i + 1

print('Total paid', total_paid)
print('Dave has to pay for ' + str(i) + ' months.')
'''

'''
# 前12个月里，Dave每个月多还$1000，那一共需要还多少钱？需要还几个月？
for j in range(1,13):
    principal = principal * (1 + rate / 12) - payment - 1000
    total_paid = total_paid + payment + 1000
 
i = 13 
while principal > 0:
    principal = principal * (1 + rate / 12 ) - payment
    total_paid = total_paid + payment
    i = i + 1
    
print('Total paid', total_paid)
print('Dave has to pay for ' + str(i-1) + ' months.')
'''

# 从第6年开始到第10年结束的4年时间里，Dave每个月多还$1000，那一共需要还多少钱？需要还几个月？
extra_payment_start_month = 61
extra_payment_end_month = 108
# i=0或者1对于总还款额和还款月份没什么影响，但是对计算每个月剩余应还的本金额有影响
#当i=0时，在第61个月开始多还1000之前，因为是从0开始计数的，所以计算的时候前面已经还了61个月了（相当于提前还了1期），但实际情况应该是只还了60个月。
i = 1 

while principal > 0:
    if i in range(extra_payment_start_month, extra_payment_end_month + 1):
        extra_payment = 1000
    else:
        extra_payment = 0
    principal = principal * (1 + rate / 12 ) - payment - extra_payment
    total_paid = total_paid + payment + extra_payment
    i = i + 1
    if principal >= 0:
        # print(str(i) + " " + str(round(total_paid, 2)) + " " + str(round(principal, 2)))
        # 下述表达式{principal: 0.2f}中冒号后面的空格也会显示在最终的打印结果中，故如果结果中不需要这个空格，冒号后也不能加空格。
        print(f'{i} {total_paid: 0.2f} {principal: 0.2f}')
    else:
        # print(str(i) + " " + str(round(total_paid, 2)) + " 0")
        print(f'{i} {total_paid: 0.2f}  0')
# print('Total paid', round(total_paid, 2))
# print('Months', i-1)
print(f'Total paid {total_paid: 0.2f}')
print(f'Months {i-1}')


'''
# 已知贷款年限，贷款总额，贷款利率，求等额本息每个月还款额和全部要还的总利息额。
month = 360
month_rate = rate / 12
month_paid = principal * month_rate * (1 + month_rate) ** month / ((1 + month_rate) ** month - 1)
total_interest = month_paid * month - principal
print('Every month Dave has to pay $' + str(round(month_paid, 2)) + '.')
print('Dave has to pay $' + str(round(total_interest, 2)) + ' interest.')
'''