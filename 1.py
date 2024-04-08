import hashlib
import base64


encoded_text = "WmFzdGFuYXdpYW0gc2llIGtvZ28gdyB0eW0gcm9rdSBvYmxhYw=="


decoded_text = base64.b64decode(encoded_text).decode('utf-8')

md5_hash = hashlib.md5(decoded_text.encode()).hexdigest()

print("Odkodowany tekst:", decoded_text)
print("MD5 hash:", md5_hash)
