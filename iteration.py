# %%
#while loop:
#else block will execute when exiting the loop, or if the while statement is false from the begining,
# else block won't execute when breaking the loop with a break keyword.
num = 5
while num < 10:
    print(f"num: {num}")
    num+=1
else:
    print("wow, num is big now!")

# %%
#breaking out of while with the break keyword, return also break loops
while True:
    num-=1
    if num < 4:
        break

# %%
nums = [1, 2, 3, 4, 5]
#For loop:
for num in nums:
    if num < 3:
        continue #skip rest of the code and start next iteration
    print(f"num: {num}")
else:
    print("else block in for loop")

# %%
#use the enumerate function to access the sequence number corralated with each element.
nums = [1, 2, 3, 4, 5]
for num in enumerate(nums):
    print(f"num: {num}")

# %%
#enumerate() takes a second optional argument that specifies the sequence starting number, 
#which you could use, for example, to indicate the line number in a file, starting with 1 rather than the 0 default
nums = [1, 2, 3, 4, 5]
for i, num in enumerate(nums, 1):
    print(f"i: {i}, num: {num}")

# %%
#Inline loop structures: 
#List Comprehension:  <result expression> for <loop variable> in <iterable> if <filter expression>    
[n*n for n in range(1, 100) if n % 2 == 0] #All squares of numbers between 1~100 that is an even number