# if

x=10
if x>8:
    print("x is greater than 8")


#if-else
    x=3
    if x>8:
        print("x is greater than 8")
    else:      
            print("x is not greater than 8")



#if-elif-else
x=10
if x<8:
    print("x is less than 8")
elif x==10:
    print("x is equal to 10")
else:   
     print("x is greater than 8 and not equal to 10")


#nested if
x = 10
if x > 5:
    print("x is greater than 5")
if x % 2 == 0:
    print("x is even")


x = 10
y = 5
if x > 5 and y < 10:
     print("Both conditions are True")
if x > 15 or y < 10:
     print("At least one condition is True")
if not x == 5:
     print("x is not equal to 5") 



#if as ternary operator
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)   


#for loop
for i in range(5): #Iterates 0 to 4
    print(i)    


for i in range(5): # Iterates from 0 to 4
    print(i+1)

for i in range(2,5): # Iterates from 0 to 4
    print(i)

for char in "Pandey":
    print(char)



#break in for loop
for i in range(10):
   if i == 5:
       break # Stops when i is 5
print(i)



#continue in for loop
for i in range(5):
    if i==2:
        continue # Skips 2
    print(i)

for i in range(5):
      print(i)
else:
      print("Loop finished successfully!")


#nested for loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")



#while loop
i=1
while i<5 :
    print(i)
    i=i+1



x = 0
while x < 5:
      print(x)
      x += 1


x = 0
while x < 10:
      if x == 5:
           break # Stops loop when x is 5
print(x)
x += 1

x = 0
while x < 5:
   x += 1
   if x == 3:
    continue # Skips the rest of the loop for x = 3
print(x)


x = 0
while x < 3:
   print(x)
   x += 1
else:
    print("Loop completed!")



#Patterns
i=1
while i<5 :
  print(i* "*")
i=i+1


i=5
while i>=0 :
    print(i* "*")
i=i-1

for i in range(5, 0, -1): # Loop controlling the number of elements in each row
   for j in range(5, 5 - i, -1): # Loop to print numbers
        print(j, end=" ")
print() # New line after each row