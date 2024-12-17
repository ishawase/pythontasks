class uniqueWords:
    def findUniqueWords(self):
        user_input = input("enter input: ")
        splited_words = user_input.split(" ")
        unique_words = set(splited_words)
        print(f" Unique Words: {unique_words}; Number of Unique Words: {len(unique_words)}")

words = uniqueWords()
words.findUniqueWords()