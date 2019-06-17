import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        shift_lowercase_string = string.ascii_lowercase[shift:]+string.ascii_lowercase[:shift]
        shift_uppercase_string = string.ascii_uppercase[shift:]+string.ascii_uppercase[:shift]

        shift_dict = {}
        for letter in string.ascii_lowercase:
            shift_dict[letter] = shift_lowercase_string[string.ascii_lowercase.index(letter)]
        for letter in string.ascii_uppercase:
            shift_dict[letter] = shift_uppercase_string[string.ascii_uppercase.index(letter)]
        return shift_dict.copy()


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        '''# shift_dict = Message.build_shift_dict(self, shift)   This is wrong'''
        shift_dict = self.build_shift_dict(shift)
        shift_string = ''
        # text_list = []
        # for letter in self.message_text:
        #     text_list.append(letter)
        # for letter in text_list:
        #     if letter in shift_dict.keys():
        #         text_list[text_list.index(letter)] = shift_dict[letter]
        # for letter in text_list:
        #     shift_string += letter
        for letter in self.message_text:
            if letter in shift_dict.keys():
                shift_string += shift_dict[letter]
            else:
                shift_string += letter
        return shift_string



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        Message.__init__(self,text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted[:]

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        text = self.message_text
        PlaintextMessage.__init__(self,text,shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        encrypt_massage = self.message_text.split(' ')

        #get the original encrypt_massage, and store here for later to decrypt the whole message
        # because when we try different shift,
        #the Message.__init__ will be rewrote
        text = self.get_message_text()
        max_ = 0
        # maxs_ =[]
        # tuple_max = ()
        shift_dict = {}
        best_shift = 0
        #try different shift to decrypt the message
        for shift in range(26):
            num = 0
            for word in encrypt_massage:
                #reinitiate the Message.__init__ method using word, so to get the decrypted word
                Message.__init__(self,word)
                #get the decrypted word
                decrypt_text_word = self.apply_shift(shift)   ###  26 - shifl   do not know what is going on here
                #check if the word is a valid_word
                if is_word(self.get_valid_words(),decrypt_text_word) == True:
                    num += 1
            #use the num of valid_word as keys, and the shift as values, to create a shift_dict{num:shift}
            shift_dict[num] = shift
            # maybe this two line of code is not necessary
            #----
            if num > max_:
                max_ = num
            #----
        #get the key of the best_shift
        max_ = max(shift_dict.keys())
        #get the best_shift
        best_shift = shift_dict[max_]
        #reinitiate Message.__init__ use text
        Message.__init__(self,text)
        #decrypt the message
        decrypt_text_text = self.apply_shift(best_shift)  ###  26 - best_shift  do not know what is going on here
        ## This is right, but I do not know how, in the question, is said a tuple, this is not a tuple
        return best_shift , decrypt_text_text
                        # use  ',' to separate different things to return
        '''
        if you know the shift used to encode the message, decoding it is trivial.
        If message is the encrypted message, and s is the shift used to encrypt the message,
        then apply_shift(message, 26-s) gives you the original plaintext message.
        But in here, we do not know the shift used to encrypt the message,
        we try to use different shift to decrypt the message, and find the best_shift
        the best_shift is the shift best decrypt the message,
        so we do not need to use 26 - s in this part.
        '''
def decrypt_story():
    story = get_story_string()
    CiphertextMessage.decrypt_message(story)


#
# story = get_story_string()
# print(story)




# #Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())
#
# #Example test case (CiphertextMessage)
# ciphertext = CiphertextMessage('jgnnq')
# print('Expected Output:', (24, 'hello'))
# print('Actual Output:', ciphertext.decrypt_message())
