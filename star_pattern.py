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


