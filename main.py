# task 1
num = input("enter five-digit number: ")
if len(num) != 5:
    num = input("do not forget to enter five-digit number: ")

if len(num)==5:
    for i in num:
        print(i )
else:
    print("You have entered wrong number ")

#task 2
str = "Vazgen"
print( len(str))

# task 3
p=14
prime = False
if p == 2:
    prime = True
elif p % 2 != 0:
    for num in range(3, p , 2):
        if p % num != 0:
            prime = True
        else:
            prime = False
            break
if prime:
    print("The number is prime")
else:
    print("the number is not prime")

#task 4

for x in range(1,6):
    print(x, 0)

#task 5
num1 = 4
num2 = 5
num3 = 6
if num1 + num2 == num3:
   print ("yes")
else:
    print ("no")

#task 6
sum = 0
for x in range (0, 15):
    sum += x
print (sum)



