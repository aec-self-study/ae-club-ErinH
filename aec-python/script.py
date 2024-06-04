x = 2

print (x)

print (x*2)

y= 'hello'

print(y)

z = x**2 + 5*x
print(z)

my_first_list = ['apple', 1, 'banana', 2]
my_fruit_list = ['apple', 'banana']
my_int_list = [1,2,3]

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

for f in my_fruit_list:
    print(f)

def sq_int(x):
    y = x**2
    return y


y = 5
x = 4

def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False
    
def is_odd(x):
    if x%2 != 0:
        return True
    else:
        return False    
   

def describe_evenness(x):
  if is_even(x):
    print("It’s even!")
  elif is_odd(x):
    print("It’s odd!")
  else:
    print("It’s neither even nor odd!")    