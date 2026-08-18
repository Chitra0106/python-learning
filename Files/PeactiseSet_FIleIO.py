#2
with open(r"ll.txt","r") as  f2:
    content = f2.readlines()
with open(r"notes.txt","w") as f:
    for item in content:
        f.write(item)


#1

#with open(r"notes.txt","w") as f:
    #f.write("Learning Python is fun")