from cryptography.fernet import Fernet
from flask import *
from encryption import Encrypt
from estring import EncryptionStr
app = Flask(__name__)
app.config['SECRET_KEY'] = 'woohoo'

@app.route('/')
def render_site():
    return render_template('index.html')

@app.route('/update', methods=('GET', 'POST'))
def update():
    if request.method == 'POST':
        str = request.form['str']
        estr = EncryptionStr(Encrypt.base64_encrypt, str)
        estr.encrypt(estr)
        return estr.s

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()    
