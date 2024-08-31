def Difficulty(str):
    if not str:
        return 0

    vowels = {'a', 'e', 'i', 'o', 'u'}
    hard_count = 0
    easy_count = 0

    words = str.split()

    for word in words:
        consonants = 0
        vowels_count = 0
        consecutive_consonants = 0
        is_hard_word = False

        for ch in word:
            if ch in vowels:
                vowels_count += 1
                consecutive_consonants = 0
            else:
                consonants += 1
                consecutive_consonants += 1
                if consecutive_consonants == 3:
                    is_hard_word = True
                    break
        
        # Determine if the word is hard or easy
        if is_hard_word or consonants > vowels_count:
            hard_count += 1
        else:
            easy_count += 1

    # Calculate the difficulty quotient
    difficulty_quotient = (5 * hard_count) - (2 * easy_count)
    return difficulty_quotient

# Taking input from the user
str_input = input()

# Calculate and print the difficulty quotient
result = Difficulty(str_input)
print(result)
