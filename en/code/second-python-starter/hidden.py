def pirate(phrase, dictionary):    
    for word in dictionary:
        print(f"Replacing {word} with {dictionary[word]}...")
        phrase = phrase.replace(word, dictionary[word])
    print(phrase)
