from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

BUFFER_SIZE = 65536

def encrypt(masterPass, file):
    key = masterPass

    inputFile = open(file, 'rb')
    outputFile = open(file + ".encrypted", 'wb')

    cipher_encrypt = AES.new(key, AES.MODE_CFB)

    outputFile.write(cipher_encrypt.iv)

    buffer = inputFile.read(BUFFER_SIZE)

    while len(buffer) > 0:
        ciphered_bytes = cipher_encrypt.encrypt(buffer)
        outputFile.write(ciphered_bytes)
        buffer = inputFile.read(BUFFER_SIZE)

    inputFile.close()
    outputFile.close()

def decrypt(masterpass, file):

    key = masterpass

    inputFile = open(file, 'rb')
    outputFile = open(file.replace('.encrypted', ''), 'wb')

    iv = inputFile.read(16)

    cipher_encrypt = AES.new(key, AES.MODE_CFB, iv=iv)

    buffer = inputFile.read(BUFFER_SIZE)

    while len(buffer) > 0:
        decrypted_bytes = cipher_encrypt.decrypt(buffer)
        outputFile.write(decrypted_bytes)
        buffer = inputFile.read(BUFFER_SIZE)

    inputFile.close()
    outputFile.close()
