# COnstructor & Destructor 
# class Bank_Account():
#     def __init__(self, customer_name, customer_balance, account_number):
#         self.customer_name = customer_name
#         self.balance = customer_balance
#         self.account_number = account_number
        
#     def cus_name(self, username):
#         print("Account user name :" , username)
        
# customer1 =  Bank_Account("vipin", 200, 2356855)
# customer1.cus_name("suresh")
# print(customer1.customer_name, customer1.account_number, customer1.balance)
    

# convert the list into dictionary
# a = [1,21,20]
# b = ["v", "i", "p"]

# dictionary = dict(zip(a, b))
# print(dictionary)

# compare a and b is same or not
# a = "vipin"
# b = (a.replace("","").lower())[::-1]
# # print(b)

# if a == b:
#     print("yes content was same")
# else:
#     print("not same")    


#reverse string

# a = "vipin"
# print(a[::-1])

# reverse a int

# a = 221

# def test(a):
#     b = str(a)   #  -> convert int to str
#     reversed_b = b[::-1]    # ->  reserve the str
#     print(type(reversed_b))
#     print(reversed_b)
#     c = int(reversed_b)
#     print(type(c))
#     print(c)

# test(a)    

# a = "vipinraj.k20@gmail.com"
# b = a.split(".")
# print(b[2])

# def duplicate_remove(input_value):
#     a = set()
#     b = []
#     for i in input_value:
#         if i not in a:
#             a.add(i)
#             b.append(i)
#     return ''.join(b)        

# input_value = "malayalam"
# output = duplicate_remove(input_value)
# print(output)


# def test():
#     return 1 
#     return 2
# a = test()
# print(a)

# def test():
#     yield 1 
#     yield 2
# a = test()
# print(list(a))

# for i in range(9):
#     if i > 3:
#         break
#     print(i)

# for i in range(9):
#     if i == 3:
#         continue
#     print(i)    