# exception handling

# f = open("abc.txt","r")
# i = 0/0


try:
    f = open("abc.txt")
    450/0
    for line in f:
        print(line)


# except (FileNotFoundError, ZeroDivisionError):
#     print("file toh bna le pehle")
#     print("Zero se kaise divide krte hain??")

except Exception as e:
    print(e.filename)
    print(e)
    print(dir(e))
    print(type(e))