#11
dict_1 = {"num1":1,"num2":2}
dict_2 = {"num1":3,"num2":4}
#dict_3 = {**dict_1, **dict_2}
dict_3 = dict_1|dict_2
print(dict_3)
#10
pnp_dist = {"iphone":50000,"laptop":30000,"Tv":40000}
maxprice = 0
for product, price in pnp_dist.items():
    if price > maxprice:
        maxprice = price
print(maxprice)


#9
list_1 = [1,2,3,4,5,6,7,8,9,9,8,7]
set_1 = set(list_1)
print(set_1)
#8
fnp_dict = {"Jon":12345,"Ram":67890,"Rao":90986767}
print(fnp_dict.keys())
print(fnp_dict.values())
items = ((i,j) for i, j in fnp_dict.items())
print(list(items))
for key,value in fnp_dict.items():
    print(key,value)
#7
student_dict = {"name":"john","age":30,"Grade":"A"}
print(student_dict["name"])
student_dict["Grade"]="A+"
student_dict["City"] = "hyd"
print(student_dict.values())
#6
set_a = {1,2,3}
set_b= {4,5,6}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
#5
my_set = {1,2,3,4,5,6,6,7,8}
print(my_set) # duplicate removed
my_set.add(10)
print(4 in my_set)
isthere = False
for i in my_set:
    if i==4:
        isthere=True
        break
print(str(isthere))
#4
tuple_coords ={10,20}
print(tuple_coords)
#tuple_coords[0] = 50 it will throw error so copying to list and changing the value
list_coords = list(tuple_coords)
print(list_coords)
list_coords[0] = 50
tuple_coords=tuple(list_coords)
print(tuple_coords)
#3
num_sort_list =[5,2,3,7,1,8,3]
num_sort_list.sort()
num_sort_list.append(10)
print(num_sort_list)
num_sort_list.reverse()
num_sort_list.remove(2)
print(num_sort_list)

#2
number_list=list(range(1,11))
#same above = below
number1_list = [i for i in range(1,11)]
print(number_list[0:3])
print(number_list[len(number_list)-3:])
#1
fruits_list =["apple","banana","cherry"]
print(fruits_list[0])
fruits_list[1] ="orange"
print(fruits_list)
print(len(fruits_list))
