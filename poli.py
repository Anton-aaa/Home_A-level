def is_palindrome(poli):
    number = str(poli)

    rebmun = number[::-1]

    if rebmun == number:
        return True
    else:
        return False

assert is_palindrome("aba") is True
assert is_palindrome("abc") is False
assert is_palindrome(12345) is False
assert is_palindrome(12321) is True


def get_longest_palindrome(star):
    revers = star[::-1]

    biggest = ""

    for s_index, s_symbol in enumerate(star):
        for r_index, r_symbol in enumerate(revers):
            if r_symbol == s_symbol and s_index == 0:
                if revers[r_index:-s_index - 1] + star[s_index] == star[s_index:-r_index]:
                    if len(biggest) < len(star[s_index:-r_index]):
                        biggest = star[s_index:-r_index]
            elif r_symbol == s_symbol and r_index == 0:
                if revers[r_index:-s_index] == star[s_index:-r_index - 1] + revers[r_index]:
                    if len(biggest) < len(star[s_index:-r_index - 1] + revers[r_index]):
                        biggest = star[s_index:-r_index - 1] + revers[r_index]
            elif r_symbol == s_symbol:
                if revers[r_index:-s_index] == star[s_index:-r_index]:
                    if len(biggest) < len(star[s_index:-r_index]):
                        biggest = star[s_index:-r_index]

    return biggest

assert get_longest_palindrome("f21aaaa1b1aaavgfa1b2") == "aaa1b1aaa"
assert get_longest_palindrome("0123219") == "12321"
assert get_longest_palindrome("1012210") == "012210"


def get_longest_uniq_length(string):
    dict_with_indices = {}
    start = 0
    max_length = 1
    for index, symbol in enumerate(string):
        symbol_index = dict_with_indices.get(symbol)
        if symbol_index and symbol_index >= start:
            start = symbol_index + 1
        dict_with_indices[symbol] = index
        length = index - start + 1
        if length > max_length:
            max_length = length
    return max_length


assert get_longest_uniq_length("abcdefg") == 7
assert get_longest_uniq_length("racecar") == 4