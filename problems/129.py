def unigram_probability(corpus: str, word: str) -> float:
    words = corpus.split()
    count = sum(1 for w in words if w == word)
    return round(count / len(words), 4)


if __name__ == "__main__":
    corpus = "The quick brown fox jumps over the lazy dog"
    word = "fox"
    print(unigram_probability(corpus, word))
