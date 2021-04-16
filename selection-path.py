#if, elif and else: 
pages = 20
if pages < 9:
    print("It's too short")
elif pages > 99:
    print("It's too long")
else:
    print("prefect")

#conditional expression selector:
vehicle = "car"
wheels = 4 if vehicle == "car" else 2
#which equals to:
if vehicle == "car":
    wheel = 4
else:
    wheel = 2

#chain comparsion:
if 15 < pages < 30:
    print("pages is between 15 and 30.")

