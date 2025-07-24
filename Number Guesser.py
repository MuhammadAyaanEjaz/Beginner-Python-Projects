def binary_search_guess(low, high):
    print(f"Think of a number between {low} and {high}.")
    input("Press Enter when ready.")
    while low <= high:
        mid = (low + high) // 2
        print(f"Is your number {mid}?")
        reply = input("Enter '<' if smaller, '>' if greater, '=' if correct: ")
        if reply == '=':
            print("Guessed it!")
            break
        elif reply == '<':
            high = mid - 1
        elif reply == '>':
            low = mid + 1
        else:
            print("Invalid input.")

binary_search_guess(1, 100)
