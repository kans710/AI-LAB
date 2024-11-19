import string

# Predefined list of common stop words
STOP_WORDS = set([
    "the", "is", "in", "and", "to", "a", "of", "on", "for", "with", "as", 
    "at", "this", "by", "from", "an", "or", "it", "that", "are", "was", "be", 
    "not", "you", "your", "but", "if", "we", "can", "they", "their", "all", "so"
])

def remove_stop_words(file_path):
    try:
        # Read the file content
        with open(file_path, "r") as file:
            text = file.read()
        
        # Tokenize the text into words
        words = text.split()
        
        # Remove stop words and punctuation
        cleaned_words = [
            word.strip(string.punctuation) for word in words 
            if word.lower().strip(string.punctuation) not in STOP_WORDS
        ]
        
        # Join the cleaned words back into a passage
        cleaned_text = ' '.join(cleaned_words)
        
        # Save the cleaned text back to the file (optional)
        with open(file_path, "w") as file:
            file.write(cleaned_text)
        
        return cleaned_text

    except FileNotFoundError:
        print("The specified file does not exist.")
        return None


if __name__ == "__main__":
    file_path = "passage.txt"  # Replace with your file path
    cleaned_text = remove_stop_words(file_path)
    if cleaned_text:
        print("Cleaned Passage:")
        print(cleaned_text)
        
