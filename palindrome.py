def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def is_primo(number: int) -> bool:
        return all([False if number%num == 0 else True for num in range(2, number)])

def run():
    print(is_primo(2))
    #print(is_palindrome(1000))


if __name__ == '__main__':
    run()
