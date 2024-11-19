import string

def remove_punctuation(sentence):
    # Use string.punctuation to get a list of all punctuation characters
    return ''.join(char for char in sentence if char not in string.punctuation)

# Example usage
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = print(sentence[::-1])
    print("Sentence rebersed :", result)
    print("Karan singh Ghugtyal , 2202301530023")