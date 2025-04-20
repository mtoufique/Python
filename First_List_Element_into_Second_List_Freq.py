list_1=[1,2,2,3,9,100,99,8]
list_2=[1,2,2,8,200]

#output
#1:1,2:2,3:0,9:0,100:0,99:0,8:1

count_list=[]
for i in list_1:
    if i in list_2:
        count_list.append(list_2.count(i))
    else:
        count_list.append(0)
print(dict(zip(list_1,count_list)))