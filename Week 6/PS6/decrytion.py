import string
#message_text = "ow sjw lscafy 6.00.1p"

def load_words(file_name):
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

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def apply_shift(message_text,shift):
    cipher = ''
    shift = shift
    str_lower = string.ascii_lowercase
    str_upper = string.ascii_uppercase
    for i in range(len(message_text)):
            if(message_text[i] in " !@#$%^&*()-_+={}[]|\:;'<>?,./\""):
                cipher = cipher + message_text[i]
            elif(message_text[i] in string.digits):
                cipher = cipher + message_text[i]
            elif(message_text[i] in str_lower):
                for j in range(len(str_lower)):
                    if(message_text[i] == str_lower[j]):
                        if(j+shift < 26):
                            cipher = cipher + str_lower[j+shift]
                        else:
                            cipher = cipher + str_lower[j+shift-26]
            else:
                for k in range(len(str_upper)):
                    if(message_text[i] == str_upper[k]):
                        if(k+shift < 26):
                            cipher = cipher + str_upper[k+shift]
                        else:
                            cipher = cipher + str_upper[k+shift-26]
    return cipher 

def decrypt_message(message_text):
    best_shift = ()
    best_s =()
    decry_msg = []
    world_list = load_words("words.txt")
    for s in range(0,26):
        x = apply_shift(message_text,26-s)
        print x
        temp = x.split(' ')
        print temp
        best = 0
        for i in range(len(temp)):
            signal = False
            signal = is_word(world_list, temp[i])
            if(signal == True):
                best = best + 1
        print best
        if(s==0):
            best_shift +=(best,)
            best_s += (s,)
            decry_msg += [x]
            print best_shift,best_s, decry_msg
        else:
            if(max(best_shift) <= best):
                if(max(best_shift) < best):
                    best_shift = ()
                    best_s =()
                    decry_msg = []
                    best_shift +=(best,)
                    best_s += (26-s,)
                    decry_msg += [x]
                    print best_shift,best_s, decry_msg
                else:
                    best_shift +=(best,)
                    best_s += (26-s,)
                    decry_msg += [x]
                    print best_shift,best_s, decry_msg
    return best_s + (decry_msg[0],)
    
