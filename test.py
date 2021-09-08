# print('eee' in 'aaa-bbb-ccc')

import re
aaa = ['パチンコ','ddd','rrr']

delete_keyword = 'カナダ\nアメリカ\n日本'
keyword = (delete_keyword.split('\n'))

if len([i for i in keyword if i in 'dnjan;rna日カjvnmdddgbtwb']) == 0:
    print(11)
else:
    print(333)




# if (i for i in delete_keyword if re.search(i, 'vdavfbvae')):
#     print(11)
# else:
#     print(333)

# for i in keyword:
        
#     data = re.fullmatch(i, '日')
#     print(data)