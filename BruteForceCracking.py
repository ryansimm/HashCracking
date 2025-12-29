import hashlib
hashes = [
'f14aae6a0e050b74e4b7b9a5b2ef1a60ceccbbca39b132ae3e8bf88d3a946c6d8687f3266fd2b626419d8b67dcf1d8d7c0fe72d4919d9bd05efbd37070cfb41a',
'e85e639da67767984cebd6347092df661ed79e1ad21e402f8e7de01fdedb5b0f165cbb30a20948f1ba3f94fe33de5d5377e7f6c7bb47d017e6dab6a217d6cc24',
'4e2589ee5a155a86ac912a5d34755f0e3a7d1f595914373da638c20fecd7256ea1647069a2bb48ac421111a875d7f4294c7236292590302497f84f19e7227d80',
'afd66cdf7114eae7bd91da3ae49b73b866299ae545a44677d72e09692cdee3b79a022d8dcec99948359e5f8b01b161cd6cfc7bd966c5becf1dff6abd21634f4b'
]
charset = 'abcdefghijklmnopqrstuvwxyz0123456789' # possible characters in the password
cracked = {} # dictionary that stores the cracked hashes

# depth first search recursively
def crack_pass(current, max_len):
    if len(current) > max_len:
        return
    
    hash = hashlib.sha512(current.encode()).hexdigest()
    if hash in hashes:
        cracked[hash] = current
        
    # done recursively because itertools.product makes it too easy :( 
    for c in charset:
        crack_pass(current + c, max_len)

# increase max length until all passwords are found
max_len = 1
while len(cracked) <len(hashes):
    crack_pass('', max_len)
    max_len += 1

print('Passwords =' , list(cracked.values()))



