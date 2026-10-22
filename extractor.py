import zlib
import marshal
import re

def extract_and_decode(disassembly_file):
    try:
        with open(disassembly_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        print("File loaded successfully. Searching for byte objects in layers...")
        
        # Find all byte strings inside the disassembly text
        byte_patterns = re.findall(r"bytes len=\d+ preview=b'(.*?)'", content)
        
        for i, b_str in enumerate(byte_patterns):
            print(f"Processing layer item {i}...")
            try:
                # Convert string representation back to actual bytes
                raw_bytes = eval(f"b'{b_str}'")
                
                # Attempt zlib decompression
                decompressed = zlib.decompress(raw_bytes)
                
                # Attempt marshal loads to check if it's a code object
                code_obj = marshal.loads(decompressed)
                
                # Save the decoded layer
                output_filename = f"decoded_layer_{i}.bin"
                with open(output_filename, 'wb') as out_f:
                    out_f.write(decompressed)
                print(f"Successfully decoded and saved: {output_filename}")
                
            except Exception as e:
                # If zlib or marshal fails, it might be raw bytecode or encoded differently
                continue
                
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    extract_and_decode('RML_static_disassembly.txt')
