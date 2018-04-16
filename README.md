# useracc
> a python module
> Manage User accounts (so only certain people can use your code!)
# Example
```python
import useracc
from useracc import user

def user_choice():
    return input("\n>>> ").lower().strip()

user.namereg(text="")
user.passreg(text="")
choice = user_choice()
import data
if choice == user.username:
    else("YAY")
except:
    input("Wrong Password!")
