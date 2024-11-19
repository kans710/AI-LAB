def sort_letters_in_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Sort the letters in each word
    sorted_words = [''.join(sorted(word)) for word in words]
    
    # Join the sorted words back into a sentence
    return ' '.join(sorted_words)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = sort_letters_in_words(sentence)
    print("Modified sentence:", result)

print("Karan Singh Ghugtyal , 2202301530023")