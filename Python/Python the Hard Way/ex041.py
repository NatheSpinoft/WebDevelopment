import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "Class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
        "*** = %%%()":
    "Set *** to an instance of class %%%.",
        "***.***(@@@)":
    "From *** get the *** function, and call it with parameters self, @@@.",
        "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

# Do they want to drill phases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "English":
    PHRASE_FIRST = True

# Load up the words to the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_count = snippet.count("%%%")
    other_count = snippet.count("***")
    
    # Limit the sample size to the number of available words
    class_names = [w.capitalize() for w in random.sample(WORDS, min(class_count, len(WORDS)))]
    other_names = random.sample(WORDS, min(other_count, len(WORDS)))

    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

    # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

    # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

    # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL- D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            raw_input("> ")
            print ("ANSWER: %s\n\n") % answer
except EOFError:
    print ("\nBye")        
