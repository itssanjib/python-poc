i = 10
name = "Sanjib Pal"
map_test = {'key1' : 'Value1', 11 : 'test'}
array_test = ("a", "b", "c");
list_test = [1,2,3,4,5]
ver_touple = tuple()


# Defining a function
def log_string(str:'String' = "Ok") -> 'String':
    print("The string is " + str)
    
# Defining a function with arbitrary argument list
def log_multiple_string(*str):
    for s in str:
        print("The string is " + s)
        
print()            