# %%

#open temp.txt and write "Hello‐WorldEND"
with open("temp.txt", "w") as tmp:
    print("hello", "world", end="END", sep="-", file=tmp)


# %%
# A guess the number game
target = 20

while True:
    value = input("Guess a number: ")
    try:
        value = int(value)
        break
    except ValueError:
        print("please enter a valid number.")

if value > target:
    print("too high")
elif value < target:
    print("too low")
else:
    print("Correct!")
# %%
# files are iterable by each line.
with open("lines.txt", "r") as file:
    for line in file:
        print(line)
# %%
