from letters import LetterState
class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, secret):
        self.secret = secret.upper()
        self.attempts = []

    def attempt(self, word):
        self.attempts.append(word)

    def guess(self, word):
        result = []
        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            result.append(letter)

        return result

    @property
    def is_solved(self):
        if len(self.attempts) > 0 and self.secret == self.attempts[-1]:
            return True
        else:
            return False

    @property
    def remaining_attempts(self):
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved




