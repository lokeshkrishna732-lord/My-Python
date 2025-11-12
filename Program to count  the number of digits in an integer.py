# Program to count the number of digits in an integer

num = int(input("Enter a number: "))
count = 0

while num != 0:
    num = num // 10  # remove the last digit
    count += 1

print("Number of digits:", count)
Enter a number: 13
Number of digits: 2
