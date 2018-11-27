def print_fruit():
  fruits = ['apple', 'banana', 'mango']
  for fruit in fruits:
    print(fruit.capitalize())

def fint_odd(m):
  for n in range(2, m):
    for i in range(2, n):
      if n % i == 0:
        print("{0} equals {1} * {2}".format(n, i, n / i))
        break
    else:
      print("{} is a prime number".format(n))

def difine():
  list = [1,2,3,4]
  for i in list:
    if i >2:
      print(i)
      break
  else:
    print("end")

if __name__ == '__main__':
  difine()
