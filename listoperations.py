a = {'abba', 'bbaa', 'abbaba', 'bbaabb'}
for word in a:
    left = 0
    right = len(word) - 1
    is_palindrome = True

    while left < right:
        if word[left] != word[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1

    if is_palindrome:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

