print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#  Don't change the code above 

# Write your code below this line 

name_string = (name1+name2).lower()
print(name_string)

t = name_string.count("t")
r = name_string.count("r")
u = name_string.count("u")
e = name_string.count("e")
print(t,r,u,e)
l = name_string.count("l")
o = name_string.count("o")
v = name_string.count("v")
e = name_string.count("e")
print(l,o,v,e)
true = t+r+u+e
love = l+o+v+e

true_love = int(str(true)+str(love))
print(true_love)
if true_love < 10 or true_love > 90:
    print("Your score iss "+str(true_love))
elif 40 <= true_love <= 50:
    print("Your score is" +str(true_love)+", you are alright together.")
else:
    print("Your score is "+str(true_love))