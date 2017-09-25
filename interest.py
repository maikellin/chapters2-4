#p is principal amount
p = 10000
r = .08
n = 12
t = input("How many years are you investing for?")
t = float(t)
A = p*((1+r/n)**(n*t))
print("Your final amount after",t,"years will be:",A)