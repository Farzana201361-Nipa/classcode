
from collections import OrderedDict

list1= [9,9,8,5,5,10,2,2,3]
def rm_duplicates_odict():
    return list(OrderedDict.fromkeys(list1))

print(rm_duplicates_odict())