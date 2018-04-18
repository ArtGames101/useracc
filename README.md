# useracc
> a python module

> Manage User accounts (so only certain people can use your code!)
# Multi-User Example
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
```

# One User Example
```
# Imports
import useracc
from useracc import user

# Register Username
user.ousername()
# Register Password
user.ouserpass()

def user_choice():
    return input("\n>>> ").lower().strip()

choice = user_choice()
from data import ouser
if choice == ouser.username:
    print("YAY")
else:
    print("Nope.")
```
