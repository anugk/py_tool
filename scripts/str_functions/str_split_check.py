def getMySplit(user_input):
    try:
        val =str(user_input)
        print("Valid str input.")
        return val.split()
    except ValueError:
        print("Input is not an int")



inputVariable = "hello test"
my_result = getMySplit(inputVariable)
print("Result for {} is {}".format(inputVariable,my_result))

