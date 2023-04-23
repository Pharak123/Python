#read the contents if the it is present
#if the file is not present then create the blank file
#and write "I was created with default text" to the file.

# try:
#     file = open("file_text.txt")
#     if file:
        
#         print(file.read())
#         file.close()
#         print("File is closed ",file.closed)
#     else:
#         raise FileNotFoundError()
    
# except FileNotFoundError:
#     print("File is not exists")

# try:
#     file = open("file_text.txt","r")
#     if file:
#         print(file.read())
    

# except FileNotFoundError:
#     file = open("file_text.txt","w")
#     file.write("I was created with default text")
#     file.seek(0)
#     print(file.read())
    
# file.close()
   
####################################################################################################

try:
    file = open("file_text.txt","r+")
    
    content = file.readlines()
    file.seek(0)
    file = open("file_text.txt","w")
    for i in range(len(content)):
        str = "HPCSA " + content[i]
        file.write(str)
        
    file.close()        
except FileNotFoundError:
   
   file1 = open("file_text.txt","w+")
   file1.write("I was created with default text\nHow are you?\nHello")
   file1.seek(0)
   content = file1.readlines()
   print(content)
   file1.seek(0)
   for i in range(len(content)):
            str = "HPCSA " + content[i]
            file1.write(str)
    
            
   file1.close()        


    