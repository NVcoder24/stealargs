import sys, os
import pathlib

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

with open(f"{application_path}/args.txt", "w") as f:
    f.write("\n".join(sys.argv))

print(f"{application_path}/args.txt")
print("=================")
print("\n".join(sys.argv))
print("=================")
input("ENTER TO EXIT")