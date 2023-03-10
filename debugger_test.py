def say_hello(name):
    return f"hello {name}"


# Intended output:
#
# > say_hello("kay")
# => "hello kay"

# took about 5 secs

def encode(text, key):
    cipher = make_cipher(key) #makes a alphabet siezed list of leters with no duplicates, using the key at the very start

    ciphertext_chars = [] 



    for i in text:          
        ciphered_char = chr(65 + cipher.index(i)) #returns the unicode symbol of number 65 + whereveer the letter is found in the cipher(10 for h for example)
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)

    

def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65] # ord(i) is the unicode number of the encrypted letter - "K" = 75. minus 65 = 10. cipher[10] = h
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 26)] #makes ther alphabet as a list

    cipher_with_duplicates = list(key) + alphabet #adds the given key to the list of the alphabet

    cipher = [] #makes a blank list to append to later


    for i in range(0, len(cipher_with_duplicates)):                         #This block - appens the blank list with one of every letter, with the key starting it
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])


    return cipher  #the cypher that is returnned is the lnegth of the alphabet, but with the key at the start and no duplicates







def get_most_common_letter(text):

    new_string = ""

    for i in text:
        if i != " ":
            new_string += i

    counter = {} #emoty dict

    for char in new_string: #each letter in text - ''e
        counter[char] = counter.get(char, 0) + 1

    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]

    return letter

class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        pass

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        pass

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass