import os
print(os.getcwd()) # currnet working directory
print(os.listdir()) # list of all dorectories
os.rmdir("tasks")
os.mkdir("tasks") # create a floder
os.remove(os.path.join("tasks","README.md"))

import shutil
#shutil.copy("tasks.txt", r"C:\Users\mailc\PyCharmMiscProject\.venv\Files\ShUtil module")
#shutil.move("notes.txt", r"C:\Users\mailc\PyCharmMiscProject\.venv\Files\ShUtil module")