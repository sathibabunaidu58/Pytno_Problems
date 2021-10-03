
f = open("readme.txt", "r")

f.seek(20)

print(f.tell())

print(f.readline())
f.close()
