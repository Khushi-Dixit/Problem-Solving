#1.Basic Triangle Patterns

#*Right-Angled Triangle
leng=int(input())
for i in range(leng+1):
    print("*"*i)
#*Isosceles Triangle:
leng = int(input("Enter the height of the triangle: "))
for i in range(leng):
    x = "*" * (2 * i + 1)  # Creates a string of stars with an increasing odd number
    print(x.center(2 * leng - 1))

#2.Inverted Triangle Patterns

#*Inverted Right-Angled Triangle:
leng = int(input("Enter the height of the triangle: "))
for i in range(leng, 0, -1):
    print("*" * i)



#tree
def tree_is(height):
    width = 2 * height - 1  # Total width of the tree
    for i in range(height):
        stars = 2 * i + 1  # Number of stars on the current level
        line = "*" * stars
        centered_line = line.center(width)  # Center the line within the total width
        print(centered_line)
    
    # Adding a single star at the end of the tree
    x = "*".center(width)
    print(x)

tree_is(5)


