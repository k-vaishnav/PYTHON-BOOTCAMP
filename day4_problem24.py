#  gcd and lcm
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
lcm=a*b
while b!=0:
    a,b=b,a%b
lcm=lcm//a
print(f"lcm of 2 numbers is {lcm}")
print(f"gcd of 2 numbers is {a}")
