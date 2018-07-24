from random import randint
import hashlib

def createfile():
    pinint = randint(0,999999)
    pin = str(pinint)
    print(pin)
    hash_object = hashlib.sha256(pin.encode())
    hashed = hash_object.hexdigest()
    print(hashed)
    f= open("hash.txt","w+")
    f.write(hashed)
    f.close()

def bruteforce(startnumber, endnumber):
     for i in range(startnumber, endnumber): 
        f = open("hash.txt","r")
        hashfromfile = f.read()
        print(i)
        brute = str(i)
        hash_object = hashlib.sha256(brute.encode())
        checkhash = hash_object.hexdigest()
        print(checkhash)
        if hashfromfile == checkhash:
            return brute
        
createfile()

print("The pin number was " + bruteforce(0, 1000000))