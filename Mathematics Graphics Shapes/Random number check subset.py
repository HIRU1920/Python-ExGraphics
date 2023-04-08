# Prompt the user to input the main set
main_set = set(input("Enter the main set (comma-separated): ").split(","))

# Prompt the user to input the three other sets
set1 = set(input("Enter the first set (comma-separated): ").split(","))
set2 = set(input("Enter the second set (comma-separated): ").split(","))
set3 = set(input("Enter the third set (comma-separated): ").split(","))

# Check if the three other sets are subsets of the main set
if set1.copy().issubset(main_set.copy()):
    print(f"{set1} is a subset of {main_set}")
else:
    print(f"{set1} is not a subset of {main_set}")
if set2.copy().issubset(main_set.copy()):
    print(f"{set2} is a subset of {main_set}")
else:
    print(f"{set2} is not a subset of {main_set}")
if set3.copy().issubset(main_set.copy()):
    print(f"{set3} is a subset of {main_set}")
else:
    print(f"{set3} is not a subset of {main_set}")
