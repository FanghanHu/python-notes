# %%
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def navieSwap(arr, i):
    "return an array of possible results by having item at i swap with every other item including itself"
    result = []
    for j in range(len(arr)):
        copy = arr.copy()
        swap(copy, i, j)
        result.append(copy)
    return result

def navieShuffle(arr):
    "return all possible results of a navie shuffle"
    result = [arr]
    # iterate through each step
    for i in range(len(arr)):
        # use temp to store result of each step
        temp = []
        for tempArr in result:
            temp.extend(navieSwap(tempArr, i))
        # replace results from last step with results from this step
        result = temp
    return result

arr = ["A", "B", "C", "D", "E", "F"]
result = navieShuffle(arr)

count = {}
for item in arr: 
    count[item] = [0] * len(arr)

for seq in result:
    for i, c in enumerate(seq):
        count[c][i] += 1

#print column names
line = "item"
for i in range(len(arr)):
    line += f"\t{i}"
print(line)

#print number of times for each item ending up in each spot
for key in count:
    line = f"{key} : "
    for n in count[key]:
        line += f"\t{n}"
    print(line)
# %%
