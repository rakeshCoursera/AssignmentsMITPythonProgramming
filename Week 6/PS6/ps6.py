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
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
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
        #pass #delete this line and replace with your code here
        self.shift = shift
        Dict ={}
        str_lower = string.ascii_lowercase
        str_upper = string.ascii_uppercase
        for i in range(len(str_upper)):
            if(i+self.shift <26):
                Dict[str_upper[i]] = str_upper[i+self.shift]
            else:
                Dict[str_upper[i]] = str_upper[i+self.shift-26]
                
        for j in range(len(str_lower)):
            if(j+self.shift<26):
                Dict[str_lower[j]] = str_lower[j+self.shift]
            else:
                Dict[str_lower[j]] = str_lower[j+self.shift-26]
        return Dict

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
        #pass #delete this line and replace with your code here
        self.cipher = ''
        self.shift = shift
        str_lower = string.ascii_lowercase
        str_upper = string.ascii_uppercase
        for i in range(len(self.message_text)):
            if(self.message_text[i] in " !@#$%^&*()-_+={}[]|\:;'<>?,./\""):
                self.cipher = self.cipher + self.message_text[i]
            elif(self.message_text[i] in string.digits):
                self.cipher = self.cipher + self.message_text[i]
            elif(self.message_text[i] in str_lower):
                for j in range(len(str_lower)):
                    if(self.message_text[i] == str_lower[j]):
                        if(j+self.shift < 26):
                            self.cipher = self.cipher + str_lower[j+self.shift]
                        else:
                            self.cipher = self.cipher + str_lower[j+self.shift-26]
            else:
                for k in range(len(str_upper)):
                    if(self.message_text[i] == str_upper[k]):
                        if(k+self.shift < 26):
                            self.cipher = self.cipher + str_upper[k+self.shift]
                        else:
                            self.cipher = self.cipher + str_upper[k+self.shift-26]
        return self.cipher   

        
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
        #self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)       
        
        
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
        #pass #delete this line and replace with your code here
        return dict.copy(self.encrypting_dict)

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        #pass #delete this line and replace with your code here
        return self.message_text_encrypted
    
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        pass #delete this line and replace with your code here
        self.shift =shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


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
        #self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

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
        #pass #delete this line and replace with your code here
        best_shift = ()
        self.best_s =()
        decry_msg = []
        world_list = load_words("words.txt")
        for s in range(0,26):
            x = self.apply_shift(26-s)
            #print x
            temp = x.split(' ')
            #print temp
            best = 0
            for i in range(len(temp)):
                signal = False
                signal = is_word(world_list, temp[i])
                if(signal == True):
                    best = best + 1
            #print best
            if(s==0):
                best_shift +=(best,)
                self.best_s += (s,)
                decry_msg += [x]
                #print best_shift,self.best_s, decry_msg
            else:
                if(max(best_shift) <= best):
                    if(max(best_shift) < best):
                        best_shift = ()
                        self.best_s =()
                        decry_msg = []
                        best_shift +=(best,)
                        self.best_s += (26-s,)
                        decry_msg += [x]
                        #print best_shift,self.best_s, decry_msg
                    else:
                        best_shift +=(best,)
                        self.best_s += (26-s,)
                        decry_msg += [x]
                        #print best_shift,self.best_s, decry_msg
        return self.best_s + (decry_msg[0],)

def decrypt_story():
    msg = get_story_string()
    obj = CiphertextMessage(msg)
    story = obj.decrypt_message()
    return story

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print 'Expected Output: jgnnq'
print 'Actual Output:', plaintext.get_message_text_encrypted()
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print 'Expected Output:', (24, 'hello')
print 'Actual Output:', ciphertext.decrypt_message()
