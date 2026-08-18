try:
    with open("ll.txt", "r") as f:
        for line in f:
            print(line)

except FileNotFoundError:
    print("File not found.")
    #f.close() no need to write close method because with statement it automatically closes