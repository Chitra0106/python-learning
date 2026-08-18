with open(r"tasks.txt","a") as f:
    f.write("Task completed")
    f.write("Task 2\n")
    f.write("Task 3\n")

with open(r"tasks.txt","r") as f:
    content = f.readlines()
    print(list(content))