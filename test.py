# print('eee' in 'aaa-bbb-ccc')

import re

# delete_keyword = 'カナダ\nアメリカ\n日本'
# keyword = (delete_keyword.split('\n'))

# if len([i for i in keyword if i in 'dnjan;rna日カjvnmdddgbtwb']) == 0:
#     print(11)
# else:
#     print(333)


item_price = '￥ 237'



if '-' in item_price:
    p = r'￥ (.*) -'
    q = r'- (.*)'
    min_price = int(re.search(p, item_price).group(1))
    max_price = re.search(q, item_price).group(1)
    print(min_price)
    print(max_price)
else:
    r = r'￥ (.*)'
    item_price = int(re.search(r, item_price).group(1))
    print(item_price)




