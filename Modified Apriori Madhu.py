#!/usr/bin/env python
# coding: utf-8

# In[1]:


#METHOD: PARTITIONING

import pandas as pd
import itertools
data = pd.read_csv('padata1.csv')

#FIRST PARTITION OF DATA

print("FIRST PARTITION")
print(data.head(10))
print("--------------------------------------------------------------------------------------")
minimum_support_count_1 = 1
records = []
for i in range(0, 10):
    records.append([str(data.values[i,j]) for j in range(0, 4)])

items = sorted([item for sublist in records for item in sublist if item != 'nan'])
def stage_1(items, minimum_support_count):
    c1 = {i:items.count(i) for i in items}
    l11 = {}
    for key, value in c1.items():
        if value >= minimum_support_count:
           l11[key] = value 
    
    return c1, l11
c1, l11 = stage_1(items, minimum_support_count_1)
print("L11 => ", l11)


#SECOND PARTITION OF DATA
print("SECOND PARTITION")
print(data.tail(10))
print("--------------------------------------------------------------------------------------")
minimum_support_count_2 = 1
records = []
for i in range(10, 20):
    records.append([str(data.values[i,j]) for j in range(0, 4)])

items = sorted([item for sublist in records for item in sublist if item != 'nan'])
def stage_1(items, minimum_support_count):
    c1 = {i:items.count(i) for i in items}
    l12 = {}
    for key, value in c1.items():
        if value >= minimum_support_count:
           l12[key] = value 
    
    return c1, l12
c1, l12 = stage_1(items, minimum_support_count_2)
print("L12 => ", l12)

# UNION OF DATA 
l123 = dict(l11)

l123.update(l12) 

for i, j in l11.items():

    for x, y in l12.items():

        if i == x:

            l123[i]=(j+y)


print("--------------------------------------------------------------------------------------")
print("COMBINED DICT L123 =>",l123)

# MADHU's MINIMUM SUPPORT COUNT 
minimum_support_count =2
l1 = dict((k, v) for k, v in l123.items() if v >= minimum_support_count)

print("--------------------------------------------------------------------------------------")
print("FINAL L1 = >", l1)


#print(l1.keys())


records = []
for i in range(0, 20):
    records.append([str(data.values[i,j]) for j in range(0, 4)])

items = sorted([item for sublist in records for item in sublist if item != 'nan'])
def stage_2(l1, records, minimum_support_count):
    l1 = sorted(list(l1.keys()))
    L1 = list(itertools.combinations(l1, 2))
    c2 = {}
    l2 = {}
    for iter1 in L1:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c2[iter1] = count
    for key, value in c2.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l1, 1):
                l2[key] = value 
    
    return c2, l2
    
def stage_3(l2, records, minimum_support_count):
    l2 = list(l2.keys())
    L2 = sorted(list(set([item for t in l2 for item in t])))
    L2 = list(itertools.combinations(L2, 3))
    c3 = {}
    l3 = {}
    for iter1 in L2:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c3[iter1] = count
    for key, value in c3.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l2, 2):
                l3[key] = value 
        
    return c3, l3
def stage_4(l3, records, minimum_support_count):
    l3 = list(l3.keys())
    L3 = sorted(list(set([item for t in l3 for item in t])))
    L3 = list(itertools.combinations(L3, 4))
    c4 = {}
    l4 = {}
    for iter1 in L3:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c4[iter1] = count
    for key, value in c4.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l3, 3):
                l4[key] = value 
        
    return c4, l4

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)
    
def check_subset_frequency(itemset, l, n):
    if n>1:    
        subsets = list(itertools.combinations(itemset, n))
    else:
        subsets = itemset
    for iter1 in subsets:
        if not iter1 in l:
            return False
    return True

#c1, l1 = stage_1(items, minimum_support_count)
c2, l2 = stage_2(l1, records, minimum_support_count)
c3, l3 = stage_3(l2, records, minimum_support_count)
c4, l4 = stage_4(l3, records, minimum_support_count)
#print("L1 => ", l1)
print("--------------------------------------------------------------------------------------")
print("L2 => ", l2)
print("--------------------------------------------------------------------------------------")
print("L3 => ", l3)
print("--------------------------------------------------------------------------------------")
print("L4 => ", l4)
print("--------------------------------------------------------------------------------------")

itemlist = {**l1, **l2,**l3,**l4}

sets = []
for iter1 in list(l3.keys()):
    subsets = list(itertools.combinations(iter1, 2))
    sets.append(subsets)

def support_count(itemset, itemlist):
    return itemlist[itemset]
list_l3 = list(l3.keys())
for i in range(0, len(list_l3)):
    for iter1 in sets[i]:
        a = iter1
        b = set(list_l3[i]) - set(iter1)
        confidence = (support_count(list_l3[i], itemlist)/support_count(iter1, itemlist))*100
        print("Confidence{}->{} = ".format(a,b), confidence)


# In[ ]:





# In[ ]:




