import os
print(os.getcwd())
a = os.listdir(r"C:\Users\mailc\PyCharmMiscProject\FilesFolders")
print(a)
print(os.path.exists(r"C:\Users\mailc\PyCharmMiscProject\FilesFolders"))
os.remove(r"C:\Users\mailc\PyCharmMiscProject\FilesFolders\Sample.txt")
os.rmdir(r"C:\Users\mailc\PyCharmMiscProject\FilesFolders") #to remove empty directories