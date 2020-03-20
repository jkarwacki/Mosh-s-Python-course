from pathlib import Path

# Absolute path
# Relative path

path = Path("ecommerce")
print(path.exists())

path1 = Path("emails")
# create directory
# path1.mkdir()
# remove directory
# path1.rmdir()


path2 = Path()
# ex. glob("*.py") for all .py files
for file in path2.glob("*"):
    print(file)


