a=5
table_5 =[]
for i in range(1,11):
    table_5.append(5*i)
print(table_5)
table_6=[6*i for i in range(1,11)]
print(table_6)
#Tuples and operations
a=(1,2,3,4,5,6,7,8,9,10)
print(a)
print(a[2]) # tuple are immutable
b=(1,) # tuple with 1 element required , to consider it as tuple
print(b)
tu=(3,2,12,12,12)
a,b,c,d,e=tu
print(a)
print(b)
print(tu.index(12))
print(tu.count(12))

#Set - collections of objects, no duplicates
fruitsset = {"Apple","banana","Cherry"}
print(fruitsset)

fruitsset.remove("banana") #if only presents will throw error in case of error
print(fruitsset)
fruitsset.discard("Cherry") # if not present also work not throw error
fruitsset.add("banana")
print(fruitsset)
print(len(fruitsset))
fruitsset.pop()
print(fruitsset)
#print(fruitsset[1]) # it is not allowd to do so - will throw error

set_a = {1,2,3,4,5}
ste_b ={5,6,7,8,9}
set_c = set_a.union(ste_b)
set_d =  set_a.difference(ste_b)
set_e = set_a.symmetric_difference(ste_b)
set_f = set_a.intersection(ste_b)
print(set_c)
print(set_d)
print(set_e)
print(set_f)
