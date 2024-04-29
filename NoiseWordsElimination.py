def eliminate_sentences_starting_with_noise_words(shifted_sentences, noise_words_list):
    shifted_sentences = [sentence for sentence in shifted_sentences if not any(sentence.lower().startswith(noise_word.lower()) for noise_word in noise_words_list)]
    return shifted_sentences