import random
import string

characters = string.ascii_letters + string.digits + "@._"

print("\nRANDOM PASSWORD GENERATOR => ",end="")
password = "".join([random.choice(characters) for i in range(8)])
print(password)