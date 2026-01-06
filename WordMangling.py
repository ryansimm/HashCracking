import hashlib 
import random 
import time # import for measuring the time taken to run the mangling functions

cracked = {} # dictionary that stores the cracked hashes

with open('PasswordDictionary.txt', 'r') as file:
    pass_list = [line.strip() for line in file if line.strip()]

# error handling in case file is empty or not found
if file is None or len(pass_list == 0):
    print("Password dictionary file is empty or not found.")
    exit()

# convert letters to leetspeak - common substitutions taken from https://www.gamehouse.com/blog/leet-speak-cheat-sheet/
def leetspeak(word):
    leet_dict = {'a': '4', 'A': '4',
                 'e': '3', 'E': '3',
                 'i': '1', 'I': '1',
                 'o': '0', 'O': '0',
                 's': '5', 'S': '5',
                 't': '7', 'T': '7',
                 'b': '8', 'B': '8',
                 'q': '9', 'Q': '9',
                 'g': '6', 'G': '6',
                 'z': '2', 'Z': '2'
                 }
    return ''.join(leet_dict.get(c, c) for c in word)

# word mangling function 
def mangle_word(word):
    variants = set()
    variants.add(word)
    variants.add(word.capitalize())
    variants.add(leetspeak(word))
    variants.add(word + '1')
    variants.add(word + '123')
    variants.add(word + '!')
    variants.add(word + '#')
    variants.add(word * 2)
    return variants


# mangle all of the passwords in the password dictionary 
mangled = set()
for word in pass_list:
    mangled.update(mangle_word(word))

# select 3 random password from the list and hash them
rndpass = random.sample(list(mangled), 5)

random_pass = {}
for pword in rndpass:
    random_pass[pword] = mangle_word(pword)
hashes = [hashlib.sha512(pword.encode()).hexdigest() for pword in rndpass]
#hashes = [hashlib.sha256(pword.encode()).hexdigest() for pword in rndpass]

# start timer
start = time.time()
# crack the hashes using the mangled password list
for hash in hashes:
    for pword in mangled:
        if hashlib.sha512(pword.encode()).hexdigest() == hash:
        #if hashlib.sha512(pword.encode()).hexdigest() == hash:
            cracked[hash] = pword
            break

# end timer
end = time.time()

total_time = end - start

print("Cracked Passwords =", list(cracked.values()))
print("Time taken to run mangling functions: ",total_time, "seconds")
print("Amount of passwords mangled:", len(mangled))

# wanted to make it possible to see the mangled passwords too (if wanted)
show_variants = input("Would you like to see the mangled passwords? (y/n): ")
if show_variants == 'y':
    for pword, variants in random_pass.items():
        print("Mangled Passwords for ",  pword ," : ")
        for variant in variants:
            print(variant)
