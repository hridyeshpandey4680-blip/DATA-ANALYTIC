print("hello, welcome to data analytics")

#variable declaration
name= "pandey"
age= 22

print (name, age)

name= "pandey"
age= 22
name= "Aman"
age= 25
print(name, age)

first_name = "pandey"
last_name = "ji"
age = 22
is_adult = True
print(first_name, last_name, age, is_adult)

#Taking input from user
name = input("Enter your name: ")
print("Hello", name)


#Arithmetic operations
print(6+7)
print(10-3)
print(4*5)
print(20/4)
print(20//4)
print(20%4)
print(2**3)


i=5
i=i+7
print(i)
i +=2
print(i)
i-=2
print(i)
i*=2
print(i)


#operators precedence
result = 10 + 5 * 2
print(result)
result = (10 + 5) * 2
print(result)


#Comparison operators
print(5 > 3)
print(5 < 3)
print(5 == 3)
print(5 <=3)
print(5 != 3)


#Logical operators
print(5 > 3 and 2 < 4)
print(5 > 3 or 2 < 4)
print(not (5 > 3))


# Data Types : int, float, str, bool
age = 22
new_Age= age+4
print(new_Age)

age= input("Enter your age: ") #typecasting
new_age= int(age) + 4
print(new_age)


number = 20
float(number) #typecasting int to float
print(number)


num=number+float(number)
print(num)


#This is First Program in Python
first_num=input("Enter first number: ")
second_num=input("Enter second number: ")
sum=first_num+second_num  
#print(sum)
print("sum is: " + sum)


first_num=input("first number ")
second_num=input("second number ")
sum=int (first_num) + int (second_num)
#print(sum)
#print("sum is : " + sum)
print("sum is : " + str (sum))



#Operation on String
name= "Hridyesh Kumar Pandey"
print(name)

print(name.upper())

print(name.lower())

print(name.find('i')) #return location starting from 0.

print(name.find('Hridyesh'))

print(name.find('e'))

print(name.find('Pandey'))

print(name.replace("Hridyesh Kumar Pandey" , "Pandey ji"))
print(name)


print(name.replace("Hridyesh" , "Mr. Hridyesh"))


print(name.replace("p" , "pa"))

print("t" in name)

print("h" in name)