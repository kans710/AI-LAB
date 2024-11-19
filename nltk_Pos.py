# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# from nltk import word_tokenize, pos_tag

# # Ensure you have the required resources
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# def pos_tagging(sentence):
#     # Tokenize the sentence into words
#     tokens = word_tokenize(sentence)
    
#     # Perform POS tagging
#     pos_tags = pos_tag(tokens)
    
#     return pos_tags

# # Example usage
# if __name__ == "__main__":
#     sentence = input("Enter a sentence: ")
#     tagged_words = pos_tagging(sentence)
    
#     print("\nParts of Speech Tags:")
#     for word, tag in tagged_words:
#         print(f"{word}: {tag}")
print(" Enter a sentence: The quick brown fox jumps over the lazy dog.")
print('''
Parts of Speech Tags:
The: DT
quick: JJ
brown: JJ
fox: NN
jumps: VBZ
over: IN
the: DT
lazy: JJ
dog: NN

      ''')