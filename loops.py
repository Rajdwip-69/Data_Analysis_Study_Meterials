# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Up48wqHbf5jWvO_H1WjiQiIKSWn1U_pt
"""

num = [1,2,3,4,5]
for i in num:
  print(i)

for i in range(5):
  print(i)

for i in range(1,5):
  print(i)

for i in range(1,10,1):
  print(i)

for i in range(12):
  if i%2==0:
    print("This is even",i)

num = int(input("Enter the Number :"))
print("Multiplication Table of :",num)
for i in num(1,11):
  print(f"{num}x{i} = {num*i}")

num_items = int(input("Enter the no of items :"))
total_price = 0
for i in range(num_items):
  price = float(input("Enter the Price of the product:"))
  total_price = total_price+price
  i=i+1
if total_price>100:
  discount = 0.1*total_price
elif 50<=total_price<100:
  discount = 0.5*total_price
else:
  discount = 0
total_bill = total_price-discount
print("Total Bill is :",total_bill)

for i in range(5):
  if i > 3:
    break
print(i)

for i in range(9):
  if i > 3:
    break
  print(i)

for i in range(10):
  if i == 7:
    continue
  print(i)

def my_fun():
  print("Hello from my function")
my_fun()



def display(name):
  print("My name is :",name)
display("Rajdwip")

def addition(a,b):
  return a+b

a = int(input("Enter the First Number :"))
b = int(input("Enter the Second Number :"))
print("The Result of Addition is :")
addition(a,b)

def details_bill():
  print("The last date of bill Payment is 10th March")
  print("After Deadline Fine is Added")
  print("Pay your Bill soon")

for i in range(3):
  a = input("Enter Your Name :")
  print("Customer name is :",a)
  b = int(input("Enter your Electrict Consmption Unit :"))
  bill = b*10
  print("Total Bill:",bill)
  details_bill()

def check_odd_even(number):
  if number%2==0:
    print("The number is even:",number)
  else:
    print("The Number is Odd:",number)
number = int(input("Enter the Number :"))
check_odd_even(number)