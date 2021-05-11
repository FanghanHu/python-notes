# %%
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def navieStep(arr, i):
    "simulate a step in a navie shuffle algorithm, return all possile result"
    results = []
    for j in range(len(arr)):
        copy = arr.copy()
        swap(copy, i, j)
        results.append(copy)
    return results

def navieShuffle(arr):
    "return all possible results of a navie shuffle"
    result = [arr]
    # iterate through each step
    for i in range(len(arr)):
        # use temp to store result of each step
        temp = []
        for tempArr in result:
            temp.extend(navieStep(tempArr, i))
        # replace results from last step with results from this step
        result = temp
    return result

# run the simulation
arr = ["A", "B", "C", "D", "E", "F"]
result = navieShuffle(arr)

# setup a dict to count the number of times each item ends up at each position
count = {}
for item in arr: 
    count[item] = [0] * len(arr)

# counting
for seq in result:
    for i, c in enumerate(seq):
        count[c][i] += 1

# print column names
line = "item"
for i in range(len(arr)):
    line += f"\t{i}"
print(line)

# print number of times for each item ending up in each spot
for key in count:
    line = f"{key} : "
    for n in count[key]:
        line += f"\t{n}"
    print(line)
# %%

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def fyStep(arr, i):
    "simulate a step in Fisher-Yates shuffle, returning all possible results"
    results = []
    for j in range(0, i + 1):
        copy = arr.copy()
        swap(copy, j, i)
        results.append(copy)
    return results

def fyShuffle(arr):
    "return all possible result of a Fisher-Yates shuffle"
    result = [arr]
    # 0 is omitted on purpose as it will always produce the same result as last step
    for i in range(len(arr) - 1, 0, -1):
        temp = []
        for tempArr in result:
            temp.extend(fyStep(tempArr, i))
        result = temp
    return result

# run the simulation
arr = ["A", "B", "C", "D", "E", "F"]
result = fyShuffle(arr)

# setup a dict to count the number of times each item ends up at each position
count = {}
for item in arr: 
    count[item] = [0] * len(arr)

# counting
for seq in result:
    for i, c in enumerate(seq):
        count[c][i] += 1

# print column names
line = "item"
for i in range(len(arr)):
    line += f"\t{i}"
print(line)

# print number of times for each item ending up in each spot
for key in count:
    line = f"{key} : "
    for n in count[key]:
        line += f"\t{n}"
    print(line)
# %%
