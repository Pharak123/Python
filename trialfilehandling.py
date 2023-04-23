
#program for read and write content when file is already exist
try: 
    file = open('file_text.txt', 'r+')
    var = file.readlines()
    file.seek(0)
    for i in range(0,len(var)):
        print(var[i])
        str = "HPCSA "+var[i]
        file.write(str)
    file.close()
except FileNotFoundError:
    file1 = open('file_text.txt','w+')
    file1.write("I was created with default text\nHow are you?\nHello")
    file1.seek(0)
    var = file1.readlines()
    file1.seek(0)
    for i in range(0,len(var)):
        print(var[i])
        str = "HPCSA "+var[i]
        file1.write(str)
    file1.close()
    
    
    
    