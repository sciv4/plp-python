# create empy list
my_list = []
print(my_list)

#append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#insert elements
my_list.insert(1, 15)
print(my_list)

#extend list
list2 = [50, 60, 70]
my_list.extend(list2)
print(my_list)

#remove elements
del my_list[-1]
print(my_list)

#sort list
my_list.sort()
print(my_list)

#find and print index of an element
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)





