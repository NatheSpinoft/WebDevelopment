def find_and_print_snippet(text, word):
    # Find the position of the word in the text
    position = text.find(word)
    
    # Check if the word was found
    if position != -1:
        # Get a snippet of 12 characters from the found position
        snippet = text[position:position + 12]
        print(f"Snippet found: {snippet}")
    else:
        print("Word not found in text.")

# Example usage
text = "Python programming is both fun and powerful. It's widely used in many fields."
word = "fun"

find_and_print_snippet(text, word)
