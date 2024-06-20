def count_char_in_word(word: str) -> dict:
    count_chars = {}
    for letter in word:
        count_chars[letter] = count_chars.get(letter, 0) + 1
    return count_chars


# Unit test
if __name__ == '__main__':
    print(count_char_in_word(word="Happiness"))
    print(count_char_in_word(word="smiles"))