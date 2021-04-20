#%%
try:
    print("hello world")
    raise ValueError("error with our values")
except ValueError as e:
    print("except block handles error:")
    print(e)
else:
    print("this block happens when there is no error in the try block.")
finally:
    print("Finally will always execute, even if code is interupted by break or return.")
# %%
import random

try:
    print("you can catch multiple types of error in a sinle except block")
    raise random.choice((ValueError("ValueError"), TypeError("TypeError")))
except (ValueError, TypeError) as e:
    print("just wrap the error types inside a tuple.")
    print(f"We have {e} this time.")
except ValueError:
    print("when multiple except block catches the same error, only the first one runs")
# %%

try:
    print("You can catch all errors with an except block without any error type")
    raise ValueError("error with our values")
except:
    print("but it is a bad idea, because it hides unexpected errors.")