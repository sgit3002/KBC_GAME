p = ["National bird ?" , "fruite ?" , "song"]
# q = ["peacock" , "mango" , "janagana"]
#peacock = 1
#mango = 2
#janagana =3
q= [1, 2, 3]
count =0
print (p[0])
print (" 1. peacock\n" , "2. crow\n", "3. salik\n" , "4. cow\n")
ans = int(input("Enter your ans '1 or 2 or 3 or 4': ")) 
if ans==q[0]:
    print("Your ans is correct")
    count = count +1
else :
    print("Your ans is wrong")   
print (p[1])
print (" 1. naspati\n" , "2. mango\n", "3. jack\n" , "4. lebu\n")
ans = int(input("Enter your ans '1 or 2 or 3 or 4': ")) 
if ans==q[1]:
    print("Your ans is correct")
    count = count +1
else :
    print("Your ans is wrong")   
print (p[2])
print (" 1. saki\n" , "2. dilbar\n", "3. janagana\n" , "4. hamma\n")
ans = int(input("Enter your ans '1 or 2 or 3 or 4': ")) 
if ans==q[2]:
    print("Your ans is correct")
    count = count +1
else :
    print("Your ans is wrong")   
print ("you correcly answered " , count, "questions")
print("You earned", count*100, "money")