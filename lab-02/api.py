from cipher.vigenere import VigenereCipher
from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json or {}
    plain_text = data.get('plain_text')
    key = data.get('key')
    if plain_text is None or key is None:
        return jsonify({'error': "Missing 'plain_text' or 'key'"}), 400
    encrypted_text = caesar_cipher.encrypt_text(plain_text, int(key))
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json or {}
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if cipher_text is None or key is None:
        return jsonify({'error': "Missing 'cipher_text' or 'key'"}), 400
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, int(key))
    return jsonify({'decrypted_message': decrypted_text})

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json or {}
    plain_text = data.get('plain_text')
    key = data.get('key')
    if plain_text is None or key is None:
        return jsonify({'error': "Missing 'plain_text' or 'key'"}), 400
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json or {}
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if cipher_text is None or key is None:
        return jsonify({'error': "Missing 'cipher_text' or 'key'"}), 400
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# RAIL FENCE CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json or {}
    plain_text = data.get('plain_text')
    key = data.get('key')
    if plain_text is None or key is None:
        return jsonify({'error': "Missing 'plain_text' or 'key'"}), 400
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, int(key))
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json or {}
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if cipher_text is None or key is None:
        return jsonify({'error': "Missing 'cipher_text' or 'key'"}), 400
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, int(key))
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
