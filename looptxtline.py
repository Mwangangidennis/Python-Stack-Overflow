for line in file:
    # if i in lines:
    print(line)
    print('Printing Line')
    i += 1
file.close()


# or
# Python program to count the number of lines in a text file

# Opening a file
# import counter as counter

file = open("Quiz1.dat", "r")
Counter = 0

# Reading from file
Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("This is the number of lines in the file")
print(Counter)

file.close()
# Counting End

file = open("Quiz1.dat", "r")
c = Counter
a = 1
reading = file.readlines()

while a < c:
    print(a)
    print(reading[a])
    a = a + 1
