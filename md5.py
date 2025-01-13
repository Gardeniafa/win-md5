import hashlib
import os
import sys
import time
import re

def calculate_md5(input_obj):
    """
    Calculate the MD5 hash of a file or a string.
    
    :param input_obj: Path to file or input string
    :return: Tuple of MD5 hash, input type ('File' or 'String'), elapsed time, and file size (if applicable)
    """
    if os.path.isfile(input_obj):
        # MD5 for file
        start_time = time.time()
        hasher = hashlib.md5()
        file_size = os.path.getsize(input_obj)
        with open(input_obj, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return hasher.hexdigest(), 'File', elapsed_time, file_size
    else:
        # MD5 for string
        md5_hash = hashlib.md5(input_obj.encode('utf-8')).hexdigest()
        return md5_hash, 'String', None, None

def is_valid_md5(md5_str):
    """
    Validate if the given string is a valid MD5 hash.
    
    :param md5_str: String to validate
    :return: True if valid, False otherwise
    """
    return re.fullmatch(r"[a-fA-F0-9]{32}", md5_str) is not None

def format_size(size):
    """
    Format file size into human-readable string.
    
    :param size: Size in bytes
    :return: Formatted size string
    """
    if size < 1024:
        return f"{size:.3f} Bytes"
    elif size < 1024 ** 2:
        return f"{size / 1024:.3f} KB"
    elif size < 1024 ** 3:
        return f"{size / 1024 ** 2:.3f} MB"
    else:
        return f"{size / 1024 ** 3:.3f} GB"

def print_usage():
    print("Usage: md5 <input> [value]")
    print("  input: the object you want to calculate MD5 value for, if it is not existing file, it will be seem as string")
    print("  value: optional, the MD5 value to compare with, it should be real md5 value (32 characters with hexadecimal)")
    print("Example:\n  md5 hello\n  md5 path/to/file\n  md5 hello 5d41402abc4b2a76b9719d911017c592")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    input_obj = sys.argv[1]

    if input_obj in ('-h', '--help'):
        print_usage()
        sys.exit(0)

    md5_to_compare = sys.argv[2] if len(sys.argv) > 2 else None

    if md5_to_compare and not is_valid_md5(md5_to_compare):
        print("\033[91mError: The provided MD5 value is not valid.\033[0m")
        print_usage()
        sys.exit(1)

    md5_hash, input_type, elapsed_time, file_size = calculate_md5(input_obj)

    if md5_to_compare:
        if md5_hash == md5_to_compare:
            md5_output = f"\033[92m{md5_hash}\033[0m"  # Green color
        else:
            md5_output = f"\033[91m{md5_hash}\033[0m"  # Red color
    else:
        md5_output = md5_hash

    if input_type == 'File':
        size_str = format_size(file_size)
        print(f"file {os.path.basename(input_obj)}({size_str}) md5 = {md5_output} (in {elapsed_time:.3f} seconds)")
    else:
        print(f"string \"{input_obj}\" md5 = {md5_output}")

if __name__ == "__main__":
    main()
