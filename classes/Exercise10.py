# https://regexr.com/

# """
# --------------------------------
# Exercises -- Regular Expressions
# -------------------------------
# Given the list of strings as input :
emails = [
"gaurav1234@gmail.com",
"pratik190900234@gmail.com",
"2009_rocking_person@yahoo.com",
"GodFather2022@yahoo.com",
"Brocklesner_89_WWE@yahoo.com",
"TheRock_WWE@yahoo.com",
"JohnCena_WWE@yahoo.com",
"Undertaker_Roman_reigns@outlook.com",
"6789764666@rediffmail.com",
"Kane#6789@gmail.com",
"34443Abs@gmail.com",
"343433abc@gmail.com"
]


# 1) provide me the list of emails that do have special characters of #~`! = \W
# 2) provide me the list of emails that start with numbers = \s[0-9].*
# 3) provide me the list of emails that start with numbers followed by an underscore =/^[0-9]+[_]+.*/gm (globally multiline)
# 4) provide me the list of emails that start with numbers followed by an underscore or small case characters = /^[0-9]+[_a-z]+.*/gm
# 5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters = /^[0-9]+[_a-zA-Z].*/gm
# 6) Provide me list of emails with only numbers before the @ = /.*[0-9]+[\W].*/gm
# 7) Provide me list of emails with numbers anywhere before the @ = /.*[0-9].*[\W].*/gm

import re
list1 = []
list2 =[]
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []

for list_item in emails:
    
    if re.search('.*[#~!].*',list_item):
         list1.append(list_item)
         
    if  re.search('^[0-9]+.*',list_item):
        list2.append(list_item)
        #print(list_item)
        
    if  re.search('^[0-9]+_.*',list_item)!=None:
         list3.append(list_item)
    
    if  re.search('^[0-9]+[_a-z]+.*',list_item)!=None:
         list4.append(list_item)
         
         
    if  re.search('^[0-9]+[_a-zA-Z]+.*',list_item)!=None:
         list5.append(list_item)
         
    if  re.search('.*[0-9]+@.*',list_item)!=None:
         list6.append(list_item)
         
         
    if  re.search('.*[0-9].*@.*',list_item)!=None:
         list7.append(list_item)
    
    
    
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
    