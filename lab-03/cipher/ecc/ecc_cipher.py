import ecdsa
import os

# Tạo thư mục chứa key nếu chưa có
if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Tạo private key và public key
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()
        # Lưu private key
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())
        # Lưu public key
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # Load public key
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
        # Load private key
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
        return vk, sk   # <-- TRẢ VỀ (VerifyingKey, SigningKey)

    def sign(self, message, key=None):
        # Ký dữ liệu bằng private key
        if key is None:
            _, sk = self.load_keys()
            key = sk
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, verifying_key=None):
        # Xác thực chữ ký bằng public key
        if verifying_key is None:
            verifying_key, _ = self.load_keys()
        try:
            return verifying_key.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False
