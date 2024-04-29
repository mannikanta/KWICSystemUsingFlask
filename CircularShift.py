def generate_shifted_sentence(words, current_index, count, result):
    if count == len(words):
        return result.strip()
    else:
        result += words[current_index] + " "
        current_index = (current_index + 1) % len(words)
        return generate_shifted_sentence(words, current_index, count + 1, result)


def circular_shift_words_for_all_sentences(sentences_list):
    shifted_sentences = []
    # print(sentences_list);
    words = sentences_list.split();
    # print(len(words));
    for j in range(len(words)):
        shifted_sentence = generate_shifted_sentence(words, j, 0, "")
        shifted_sentences.append(shifted_sentence)

    return shifted_sentences