#We have a file before reding or writing
# f = open("file_name"          , "mode")
#    smple.txt           r : read mode
#   demo.docx            w : write mode

# data = f.read()

#     f.close()

# carchter :meaning
# 'r': Open a file for reading.
# 'w': Open a file for writing.
# 'x': Open a file for exclusive creation
# 'a': Open a file for appending
# 'b': Binary mode. 
# 't': Text mode
# '+': Adding '+' to a mode means the
# file is opened for both reading and writing.

f = open("E:\python\Files in python\w.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# # f.close()


2#Reading a file

file = open("E:\python\Files in python\w.txt", 'r')
#data = f.read() #reads entire file
line1 = file.readline()  # reads one line at a time
print(line1) #Output: adnan
line2 = file.readline()
print(line2) #Output:ahmed


2#Writing to a file