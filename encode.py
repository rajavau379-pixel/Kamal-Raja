import base64
import zlib

with open("core.py", "rb") as f:
    original_code = f.read()

encoded_code = base64.b64encode(zlib.compress(original_code))

with open("secure_core.txt", "wb") as f:
    f.write(encoded_code)

print("[+] Core file encrypted successfully as 'secure_core.txt'!")
