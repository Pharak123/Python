my_string = "ICC T20 2022 WC"
my_list=['I', 'C', 'C', ' ', 'T', '2', '0', ' ', '2', '0', '2', '2', ' ', 'W', 'C']
my_tuple=('I', 'C', 'C', ' ', 'T', '2', '0', ' ', '2', '0', '2', '2', ' ', 'W', 'C')
my_range = range(1,5,1)

# print("The operations in the following table are defined on Mutable/Immutable sequence types")
# print("--------------------------------------------------------------------------")

# print("x in s -- True if an item of s is equal to x, else False")
# x= "C"
# print("C" in my_string)
# print("x not in s -- True if an item of s is equal to x, else False")
#print ("c" not in my_string)
#print("W" not in my_list)
#print("v" not in my_tuple)
# print(6 not in my_range)

# print("Concanetation")
# list1 = ['A','B','O',' ','L','I']
# list2 = ['A','B','C',' ']
# print(list1+list2)
# print(my_tuple+my_tuple)
# print(my_string+my_string)

# print("s * n or n * s -- 	equivalent to adding s to itself n times")
# n=3
# print("A",list1*n)
# print("B",list2*n)

# print("s[i] -- ith item of s, origin 0")
# print(list1[2])
# print(list2[2])
# print(list1[0])
list1 = ['A','B','O',' ','L','I']
list2 = [1,49,-1]
# print("s[i:j] -- slice of s from i to j(Exclusive) and step 1")

# #print(list1[0:6:2])
# #print(list2[0:5:1])
# print(list1[:])
# print("len(s) -- length of s")
# print(len(my_list))
# print(len(my_string))
# print(len(my_tuple))
# print(len(list1))
# print(len(list2))

# print("min(s) -- smallest item of s")
# # print(min(list2))
# print(min(my_tuple).isspace())
# # print(min(my_range))
# print(min(my_string).isspace())

# print(max(my_tuple))
# print(max(my_string))
# print(max(list1))
# print(max(list2))

print(list1.index("A"))