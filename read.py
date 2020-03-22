file1 = open("MyFile.txt","w")
file1.write("Hello\n")
file1.write("I am Pratham\n")
file1.write("I love cricket\n")
file1.write("I am 19 years old\n")
file1.close()
file1 = open("MyFile.txt","r")  
print(file1.read())



