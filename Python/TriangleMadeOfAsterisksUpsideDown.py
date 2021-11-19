# -------------------------------------------------------------------------------------------------
# Triangle made of asterisks ('*') upside down
# -------------------------------------------------------------------------------------------------
# Let’s print a triangle made of asterisks (‘*’) separated by spaces and consisting
# of n rows again, but this time upside down, and make it symmetrical.
# For example, for n = 4 the triangle should appear as follows:
"""    
    * * * * 
    * * * 
    * * 
    *
"""

n = 4
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("* ", end="")
    print()


