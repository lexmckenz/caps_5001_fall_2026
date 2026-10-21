import b
import sys

print(f"path: {sys.path}") #same as PYTHONPATH

print(b.x)

if __name__ == '__main__':
    # this runs whenever the script is executed directly
    # adding this to b.py wont have it run when imported
    b.spam('gumby')