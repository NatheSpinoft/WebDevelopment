class segment_a():
    def __init__(self, character, dialogue):
        self.character = character
        self.dialogue = dialogue

    def dialoguing(self):
        print("This character, %s has a dialogue of a %s" % (self.character, self.dialogue))
