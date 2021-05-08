# %%
def double(num):
    "return the num * 2" # a string at the begining of the function defination is used in the help message for this function
    return num * 2

for x in range(10):
    print(f"double({x}) -> {double(x)}")

help(double)
# %%
# the yield keyword returns the value and freezes the function's internal state, when the function is called again, 
# it will start at the last yield statement.

def createGenerator():
    # state of n is preserved between each next() call
    n = 1
    yield f"first: {n}"
    n += 1
    yield f"second: {n}"
    n += 1
    yield f"third: {n}"

generator = createGenerator()
#returned object for the function call is a generator object
print(generator)

print(next(generator))
print(next(generator))
print(next(generator))

# using a for loop to iterate through the generator
# however the generator object has been "used up" by previous print call, thus this for loop doesn't run at all
for text in generator:
    print(text)
# %%
# Lambda functions pattern:
# lambda <param1, param2, ...,paramN> : <expression>
# lambda function returns the result of its expression without the return keyword
# Some languages allow lambda functions to be arbitrarily complex; however, Python limits you to a single expression.
triple = lambda num : num * 3
print(f"triple(3) -> {triple(3)}")
# %%
