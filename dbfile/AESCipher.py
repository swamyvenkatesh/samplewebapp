import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import padding

def encryptstrpass(sRawString):
    f = Fernet(key)
    token = f.encrypt(sRawString.encode())
    stoken=token.decode()
    return stoken

def decryptstrpass(stoken):
    f = Fernet(key)
    token = stoken.encode()
    sRawString = f.decrypt(token).decode()
    return sRawString


def encryptstr(sRawString):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    paddedString = padder.update(sRawString.encode()) + padder.finalize()
    backend = default_backend()
    cipher = Cipher(algorithms.AES(AESKey), modes.CBC(AESiv), backend=backend)
    encryptor = cipher.encryptor()
    token = encryptor.update(paddedString) + encryptor.finalize()
    stoken = str(base64.b64encode(token),'utf-8')
    return stoken

def decryptstr(stoken):
    token = base64.b64decode(stoken)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(AESKey), modes.CBC(AESiv), backend=backend)
    decryptor = cipher.decryptor()
    paddedsRawString=decryptor.update(token) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    sRawString = unpadder.update(paddedsRawString)
    sRawString += unpadder.finalize()
    return sRawString

key=b'TgsKXcy3rezhR4uHVcGNLFdACnADycRMJJeXqajFdzQ='
AESKey=b'\xf5\xe0\xf4\xe2\x10Cs9\x89\x1b\xd0\xb0\xd6\xc0\xe8\xdd\xaa<\xcb\x98\x91\x14\x92)\xe3\xbe\x81\xa8\x14\xf27\x85'
#AESKey=b'\xf5\xe0\xf4\xe2\x10\x89\x1b\xd0\xb0\xd6\xc0\xe8\xdd\xaa\xcb\x98\x91\x14\x92\xe3\xbe\x81\xa8\x14\xf2\x85'
AESiv=b'\xcc\xc0\x90\x97\x8f\xd9\xa3\x8e\x07\xb2\xeb\x08\xb9\xf1\xbd<'
