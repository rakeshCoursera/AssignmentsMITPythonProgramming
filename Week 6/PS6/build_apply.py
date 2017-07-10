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
        
