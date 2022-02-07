from cryptography.fernet import Fernet
from flask import *
import base64
app = Flask(__name__)
app.config['SECRET_KEY'] = 'woohoo'

class EncryptionStr:
    def __init__(self, encrypt, s):
        self.encrypt = encrypt
        self.s = s

def base64_encrypt(estr):
    encodedBytes = base64.b64encode(estr.s.encode("utf-8"))
    estr.s = str(encodedBytes, "utf-8")

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/update', methods=('GET', 'POST'))
def update():
    if request.method == 'POST':
        str = request.form['str']
        estr = EncryptionStr(base64_encrypt, str)
        estr.encrypt(estr)
        return estr.s

if __name__ == '__main__':
    app.debug = True
    app.run()


#build using "docker build -t getting-started ."
#then run the image with "docker run --publish 5000:5000 getting-started" or any port
#then go on browser and type "localhost:5000" in search bar or any port
