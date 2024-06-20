def count_words_in_paragraph(filepath: str) -> dict:
    with open(filepath, mode="r", encoding="utf-8") as file:
        all_words = file.read().split()

    count_words = {}
    for word in all_words:
        count_words[word] = count_words.get(word, 0) + 1

    return count_words


# Unit test
if __name__ == '__main__':
    print(count_words_in_paragraph("P1_data.txt"))