a = "ram"
b = "Rao"
c= "John"
d= "Ricky"
a1 = "hyd"
template =''' Hi {} ,
How are you 
How was your weekend?
how is the whether in {} now
regards,
{}
'''
template2 = "Dear {}, iam in {} now."
print(template.format(a,a1,a))
print(template2.format(a,a1))
print(f"hi {a}, I am in {a1} now , how is {b} now") #f string 
