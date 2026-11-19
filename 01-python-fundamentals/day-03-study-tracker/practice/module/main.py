# Usage of the module
from mymodule import students
import platform

for x in students:
    print(f"I am {x['name']}, {x['age']} years old and i am {x['status']}")