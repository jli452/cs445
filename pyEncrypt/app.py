from cryptography.fernet import Fernet
from flask import Flask
import base64
app = Flask(__name__)

class EncryptionStr:
    def __init__(self, encrypt, s):
        self.encrypt = encrypt
        self.s = s

def base64_encrypt(estr):
    encodedBytes = base64.b64encode(estr.s.encode("utf-8"))
    estr.s = str(encodedBytes, "utf-8")

def main():
    estr = EncryptionStr(base64_encrypt, "hello world")
    print(estr.s)
    estr.encrypt(estr)
    print(estr.s)

if __name__ == "__main__":
    main()

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

#build using "docker build -t getting-started ."
#then run the image with "docker run --publish 5000:5000 getting-started" or any port
#then go on browser and type "localhost:5000" in search bar or any port