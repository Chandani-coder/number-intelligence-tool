print("----Number Intelligence Tool----")
def menu():
    print("\n1.Check Even/Odd")
    print("2.Sum of first n number")
    print("3.Factorial of number")
    print("4.Check Prime or not")
    print("5.Exit")
#check even or odd
def is_even_odd(n):
    if n%2==0:
        return "Even"
    return "Odd"
#find the sum of first n number
def first_sum(n):
    sum=(n*(n+1))//2
    return sum
#find the factorial
def factorial(n):
    #check n is 1 or 0
    if n==1 or n==0:
        return 1
    #check n is positive
    if n<0:
        return "Invalid"
    return n*factorial(n-1)
#Check prime by square root method
def is_prime(n):
    #check n is 1 or 0
    if n==1 or n==0:
        return False
    #check n is 2 or 3
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return "Not Prime"
        return "Prime"
while True:
    try:
        n=int(input("\nEnter a number:"))
        if n<0:
            print("Negative Number not allowed")
        menu()
        choice=int(input("Choose btwn 1/2/3/4/5:"))
        if choice==1:
            print("Number is:", is_even_odd(n))
        elif choice==2:
            print("Sum:", first_sum(n))
        elif choice==3:
            print("Factorial",factorial(n))
        elif choice==4:
            print("Number is",is_prime(n))
        elif choice==5:
            break
        else:
            print("Invalid Number:")
    except ValueError:
        print("Pls enter valid number:")
        
        
        
    
   

