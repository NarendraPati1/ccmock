print("Hello world")

x = int(input("first no :" ))
y = int(input("second no :"))

print(x+y)


n = int(input("Input size"))

def patt(n):
  for i in range(1,n+1):
    for j in range (i):
      print("*",end ="")
    print()

patt(n)
