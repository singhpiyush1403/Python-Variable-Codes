
age = 25  
price = 99.99 
name = "John Doe"  
is_student = True  


value = 10
value = "Now I'm a string!"


x, y, z = 1, 2, 3
a = b = c = 42


first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)


integer_value = int("100")
float_value = float("3.14")
string_value = str(42)
print("Casted Values:", integer_value, float_value, string_value)

global_var = "I am global"

def example_function():
    local_var = "I am local"
    global global_var
    global_var += " and modified"
    print(local_var)
    print(global_var)

example_function()
print("Outside function:", global_var)


PI = 3.14159
GRAVITY = 9.8
print("Constants: PI =", PI, ", GRAVITY =", GRAVITY)


print("Type of name:", type(name))
print("Type of is_student:", type(is_student))


temp = "This is temporary"
print(temp)
del temp
 
print("\nSummary of Variables:")
print("Age:", age)
print("Price:", price)
print("Full Name:", full_name)
print("Global Variable:", global_var)
