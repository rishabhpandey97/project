# import random
# print(random.randint(5,10))

# print(random.randrange(3,9))

# l = ["apple","banana","cherry"]
# print(random.choice(l))

# l = [10,20,30,40]
# print(random.choice(l))

# r = random.random()
# print(r)

# l = [10,20,30,40]
# random.shuffle(l)
# print(l)

# a = random.uniform(3,9)
# print(a)

# project guess nom
# import random
# target=random.randint(1,100)
# while True:
#      userchoice=(input("guess the number or QUIT : "))
#      if(userchoice=="QUIT"):
#           break
        
#      userchoice=int(userchoice)
#      if(userchoice==target):
#           print("sucess:correct guess!!")
#           break
#      elif(userchoice<target):
#           print("your nom was too small.take bigger nom")
#      else:
#           print("your nom was too big.take a small nom")

# print("-----game over---")

# random password generate
import random
import string
pass_len = 8
charValue = string.ascii_letters+string.digits+string.punctuation

# list comprehension (function for i)
  
res = ''.join([random.choice(charValue) for i in range (pass_len)])
print(res)


# password = ""
# for i in range(pass_len):
#     password +=(random.choice(charValue))
#     print("your random pass is:",password)
    
          
# print(string.ascii_letters) 
# print(string.digits)
# print(string.punctuation)



