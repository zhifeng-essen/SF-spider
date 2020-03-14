# from task import a1

# with open('Log01.txt', 'r') as f:
#     li = [x.split('\t')[0] for x in f]

# a = [x for x in a1 if x not in li]
# print(str(a))
# ['MOL002731', 'MOL006937', 'MOL010933']

import os

l2 = [x for x in os.listdir('D:\\H\\HTML2') if '.html' in x]
l1 = [x for x in os.listdir('D:\\H\\HTML3') if '.html' in x]

a = [x for x in l2 if x not in l1]
print(str(a))
