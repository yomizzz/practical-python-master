
price_width = 10
item_width = 42 - price_width

# 如果需要在字符串中保留{}，则需要输入两个{}，即{{}}
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('=' * 42)
print(header_fmt.format('Item', 'Price'))
print('-' * 42)

print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots(16 oz)', 8))
print(fmt.format('Prunes(4 lbs)', 12))

print('=' * 42)