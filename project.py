from flask import Flask, render_template, request, redirect, url_for
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

app = Flask(__name__)

prywatny_klucz = None
publiczny_klucz = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_keys', methods=['POST'])
def generate_keys():
    global private_key, public_key
    private_key, public_key = generate_key_pair()
    save_key_to_file(prywatny_klucz, 'private_key.pem')
    save_key_to_file(publiczny_klucz, 'public_key.pem')
    return redirect(url_for('index'))

@app.route('/import_public_key', methods=['POST'])
def import_public_key():
    global public_key
    public_key = load_public_key_from_file('public_key.pem')
    return redirect(url_for('index'))

@app.route('/sign_file', methods=['POST'])
def sign_file_route():
    if private_key is None:
        return "Generate or import private key first."
    file_path = request.form['file_path']
    signature = sign_file(private_key, file_path)
    return f"Signature: {signature.hex()}"

@app.route('/verify_signature', methods=['POST'])
def verify_signature_route():
    if public_key is None:
        return "Import public key first."
    file_path = request.form['file_path']
    signature_hex = request.form['signature']
    signature = bytes.fromhex(signature_hex)
    try:
        verify_signature(public_key, file_path, signature)
        return "Signature is valid."
    except Exception as e:
        return f"Signature is invalid. Error: {str(e)}"

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    return private_key, public_key

def save_key_to_file(key, filename):
    with open(filename, 'wb') as key_file:
        key_bytes = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        key_file.write(key_bytes)

def load_public_key_from_file(filename):
    with open(filename, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

def sign_file(private_key, file_path):
    with open(file_path, 'rb') as file_to_sign:
        data = file_to_sign.read()
        signature = private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

def verify_signature(public_key, file_path, signature):
    with open(file_path, 'rb') as file_to_verify:
        data = file_to_verify.read()
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

if __name__ == '__main__':
    app.run(debug=True)