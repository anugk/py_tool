# comment first 2 statements on same indent.
'''
print (5-2)

print (5%2)
'''
# print (2**3) # power with two astrix

# print (400%300)

a = 100
s="TestString-->>"
## print String and int together.
#print ('{},{}'.format(s, a))

#print (type (a))

#print (type (s))

my_address = "FREMONT CA"
#print(len(my_address))

# print('{}{}={}'.format(my_address,"<--length is-->",len(my_address)))

my_string = "Hello World"

#print(my_string[-1])

#print(my_string[4])

print("SLICE TEST")

# to get from start to 2nd, 3rd is excluded index
#print(my_string[:3])

# to get from 1st index till end
#print(my_string[1:])

# step size between start to end
#print(my_string[::2])

# Reverse a string trick.
#print(my_string[::-1])


print(my_string+' Januray 4th')

# print(my_string.upper())

# print(my_string.split())

# print(my_string.split('l'))

print('The {2} {1} {0}'.format('fox','brown','quick'))

print('The {b} {f} {q}'.format(f='fox',b='brown',q='quick'))

#result = 100/777
#print (result)

#print ("The result was {r:4.3f}".format(r=result))

first_list=['one','two',3,5.0]

print(first_list)

first_list.append("ADDED_ITEM")

print(first_list)

print(first_list.pop())

print("AFTER POP {}".format(first_list))

first_list.append("2ADD_ITEM")

print(first_list.pop(2))
print("AFTER 2nd POP {}".format(first_list))

num_list = [7,4,10,50,2];
num_list.sort();

print("After sort {}".format(num_list))


# to reverse list
num_list.reverse();
print("After Reverse Sort {}".format(num_list))

# Dictonary uses Curly braces

first_dictonary = {'a1':'anurag','a2':'mishra'}

print("First key is {}".format(first_dictonary['a1']))

# dictionary with multiple objects type
second_dictonary = {'a1':'anurag','a2':['a','b','c'],'a3':{'insideKey':200}}

# here we access a2 key-->2nd element(1st index) -->upper.

print(second_dictonary['a2'][1].upper())

print(second_dictonary['a3']['insideKey'])

# noticed when we used upper on number nothing got printed -->print(second_dictonary['a3']['insideKey'].upper())

# keys(),  values() an d items() for both key/value

# keys must be string

print(first_dictonary.keys())
print(first_dictonary.values())
print(first_dictonary.items())


first_tuple = (1,2,4)

print("first_tuple type is: {}".format(type(first_tuple)))

print(first_tuple[0])

# re-assigmnet not allowed for tuples.
#first_tuple[0] =10

my_test_list = [1,1,1,3,4,4,5]
print ("set keeps only unique values {}".format(set(my_test_list)))

#Boolean

print("Boolean type check {},{}".format(type(True),type(False)))


# NoneType
b = None
print("NoneType check {} ".format(type(b)))

# File reading

my_file_path='/Users/tkmaarv/anurag_source/py_tool_scripts/tests/first.tst'

with open(my_file_path) as my_new_file:
    content_of_file = my_new_file.read()
print(content_of_file)


with open(my_file_path,mode='w') as my_w_file:
    my_w_file.write('Hello World')
    my_w_file.close()



with open(my_file_path) as my_new_file:
    content_of_file = my_new_file.read()
print(content_of_file)


# in if elif else colon at the end is MUST
loc='Bank'

if loc=='B2':
    print ("B2 output")
elif loc=='Bank':
    print('Its Bank')
elif loc=='C2':
    print ('C2--')
else:
    print ("Anything else")


my_list = [1,2,3,4,5,6,7,8,9,10]

# for my_number in my_list:
#    print(my_number)

 # for loop to print even number
for my_number in my_list:
    if my_number%2 == 0:
        print("my even number {}".format(my_number))
    else:
        print("odd number {}".format(my_number))


# for loop to sum the number
my_list_sum=0

for my_sum_num in my_list:
    my_list_sum = my_list_sum+my_sum_num


print("-------------------------final sum is {}".format(my_list_sum))

# for loop to sum the number ENDS

for my_character in "HELLO WORLD":
    print("My character is : {}".format(my_character))

# underscore when we don't need variable name


for _ in "HELLO WORLD":
    print("Just print")

# tuple unpacking
my_tuple_list = [(1,2),(3,4),(5,6),(9,10)]

for a,b in my_tuple_list:
    print(b)


# for dictionary key value items()
my_dictionary = {'k1':1,'k2':2,'k3':3}

for my_key,my_value in my_dictionary.items():
    print("my key values   {},{}".format(my_key,my_value))

# enumerate
    print('------------------------enumerate test---------------------')

for index,my_character in enumerate("HELLO WORLD"):
    print(index,my_character)



#flattened /Comprehensive for loop to make list

my_letter_list =[my_letter for my_letter in 'HELLOHELLOJI']


print(my_letter_list)


# define a function

def print_name(my_name):
    return 'Hello  '+my_name

# call function below:
print(print_name('MIKE'))

print("-----------------------------------------------------------------------------------")
def myfunc_add(*args):
    mylist=[]
    for element in args:
        if element%2==0:
            mylist.append(element)

    return mylist



print(myfunc_add(1,2,3,4))

'''
def animal_crackers(text):
    if text[0]==text[text.index('\s')+1,text.index('\s')+2]
        return True
    else
        return False
'''

my_check = 'Hello Billo';
print(my_check[0])
print(my_check.index(' '))
print(my_check[int(my_check.index(' '))])

def getMyReverseSentence(text):
    print(text.split()[::-1])


getMyReverseSentence('I am home')