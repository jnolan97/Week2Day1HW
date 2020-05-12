#1
total = 0
cube = 1
while(total<1000):
    total = cube**3
    cube += 1
    print(total)

#2 Doesn't work right
total_prime = 0
for i in range(1,20):
    for k in range(2,i):
        if i % k != 0:
            print(i)
            total_prime += 1
            continue     
        else:
            break
print("Total: " , total_prime)

#3
age = input("Enter Age: ")
age = int(age)
if age < 18:
    print("You are a kid")
if age >= 18 and age < 65:
    print("You are an adult")
else:
    print("Senior")