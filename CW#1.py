pd1 = ["Zheng, Edwin", "Zheng, Angela", "Zheng, Reng"]
pd2 = ["adfasdf","adsfsadfa","adsfadsf"]

pd_num = input("What period?")
name_index = input("What index? (0 base)")
pd_num = int(pd_num)
name_index = int(name_index)
if pd_num == 1:
    print (pd1[name_index])
if pd_num == 2:
    print (pd2[name_index])
