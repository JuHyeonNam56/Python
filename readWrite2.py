file = open('test.txt')


print(file.readline())



#print lune 별로 출력
# line = file.readline()
#
# while line != "":
#     print(line)
#     line = file.readline()

#values = [abc, bcdaf, "cat", dog. elephant]
for line in file.readlines():
    print(line)


file.close()