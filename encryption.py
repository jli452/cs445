import base64

class Encrypt:
    def __init__(self):
        pass

    def base64_encrypt(estr):
        encodedBytes = base64.b64encode(estr.s.encode("utf-8"))
        estr.s = str(encodedBytes, "utf-8")
