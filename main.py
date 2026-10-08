"""
Classical Cryptography Toolkit - Main Launcher
Provides an interactive menu-driven Command Line Interface (CLI) and GUI launcher.

Course: Network Security
Project Title: Design and Development of a Classical Cryptography Toolkit
"""

import sys
import os
from typing import Optional

# Import ciphers
from algorithms.caesar import caesar_encrypt, caesar_decrypt
from algorithms.monoalphabetic import (
    monoalphabetic_encrypt,
    monoalphabetic_decrypt,
    generate_monoalphabetic_key,
)
from algorithms.playfair import playfair_encrypt, playfair_decrypt, generate_playfair_matrix
from algorithms.hill import hill_encrypt, hill_decrypt, parse_hill_key
from algorithms.vigenere import vigenere_encrypt, vigenere_decrypt
from algorithms.otp import otp_encrypt, otp_decrypt, generate_otp_key
from algorithms.rail_fence import rail_fence_encrypt, rail_fence_decrypt
from algorithms.columnar import columnar_encrypt, columnar_decrypt, get_column_order

# Import utilities
from utils.file_handler import read_text_file, write_text_file
from utils.validator import validate_cipher_input
from utils.benchmark import benchmark_algorithms, BENCHMARK_EDUCATIONAL_NOTE
from gui import launch_gui, ALGORITHM_HELP

def print_header(title: str = "CLASSICAL CRYPTOGRAPHY TOOLKIT"):
    print("=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

def display_main_menu():
    print_header("CLASSICAL CRYPTOGRAPHY TOOLKIT")
    print("\nSUBSTITUTION CIPHERS\n")
    print("1. Caesar Cipher")
    print("2. Monoalphabetic Cipher")
    print("3. Playfair Cipher")
    print("4. Hill Cipher")
    print("5. Vigenère (Polyalphabetic) Cipher")
    print("6. One-Time Pad")
    print("\nTRANSPOSITION CIPHERS\n")
    print("7. Rail Fence Cipher")
    print("8. Columnar Transposition Cipher")
    print("\nUTILITY MODULES\n")
    print("9. Compare Algorithms")
    print("10. Encrypt Text File")
    print("11. Decrypt Text File")
    print("12. Help")
    print("13. Exit")
    print("14. Launch Graphical User Interface (GUI)")
    print("=" * 60)

# ------------------------------------------------------------------------------
# CIPHER HANDLERS
# ------------------------------------------------------------------------------
def handle_caesar():
    print_header("1. CAESAR CIPHER")
    text = input("Enter Plaintext: ").strip()
    shift_str = input("Enter Shift Key (integer, e.g. 5): ").strip()
    
    try:
        shift = int(shift_str)
        validate_cipher_input("Caesar Cipher", text, shift)
        enc = caesar_encrypt(text, shift)
        dec = caesar_decrypt(enc, shift)
        
        print("\n--- RESULTS ---")
        print(f"Plaintext:      {text}")
        print(f"Shift Key:      {shift}")
        print(f"Ciphertext:     {enc}")
        print(f"Decrypted Text: {dec}")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

def handle_monoalphabetic():
    print_header("2. MONOALPHABETIC CIPHER")
    text = input("Enter Plaintext: ").strip()
    
    gen_choice = input("Generate a random substitution key? (y/n): ").strip().lower()
    if gen_choice == 'y':
        key = generate_monoalphabetic_key()
        print(f"Generated Random Key: {key}")
    else:
        key = input("Enter 26-character Substitution Key (A-Z permutation): ").strip()
        
    try:
        validate_cipher_input("Monoalphabetic Cipher", text, key)
        enc = monoalphabetic_encrypt(text, key)
        dec = monoalphabetic_decrypt(enc, key)
        
        print("\n--- RESULTS ---")
        print(f"Plaintext:      {text}")
        print(f"Key:            {key.upper()}")
        print(f"Ciphertext:     {enc}")
        print(f"Decrypted Text: {dec}")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

def handle_playfair():
    print_header("3. PLAYFAIR CIPHER")
    text = input("Enter Plaintext: ").strip()
    keyword = input("Enter Keyword (e.g. MONARCHY): ").strip()
    
    try:
        validate_cipher_input("Playfair Cipher", text, keyword)
        enc = playfair_encrypt(text, keyword)
        dec = playfair_decrypt(enc, keyword)
        
        matrix = generate_playfair_matrix(keyword)
        print("\n--- GENERATED 5x5 PLAYFAIR MATRIX ---")
        for row in matrix:
            print("  ".join(row))
            
        print("\n--- RESULTS ---")
        print(f"Plaintext:      {text}")
        print(f"Keyword:        {keyword.upper()}")
        print(f"Ciphertext:     {enc}")
        print(f"Decrypted Text: {dec}")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

def handle_hill():
    print_header("4. HILL CIPHER (2x2 Matrix)")
    text = input("Enter Plaintext: ").strip()
    key_input = input("Enter 4-letter keyword (e.g. HILL) or 4 numbers (e.g. '3 3 2 5'): ").strip()
    
    try:
        validate_cipher_input("Hill Cipher", text, key_input)
        enc = hill_encrypt(text, key_input)
        dec = hill_decrypt(enc, key_input)
        
        matrix = parse_hill_key(key_input)
        print("\n--- 2x2 KEY MATRIX ---")
        print(f"| {matrix[0][0]:2d}  {matrix[0][1]:2d} |")
        print(f"| {matrix[1][0]:2d}  {matrix[1][1]:2d} |")
        
        print("\n--- RESULTS ---")
        print(f"Plaintext:      {text}")
        print(f"Ciphertext:     {enc}")
        print(f"Decrypted Text: {dec}")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

def handle_vigenere():
    print_header("5. VIGENÈRE CIPHER")
    text = input("Enter Plaintext: ").strip()
    keyword = input("Enter Keyword (e.g. SECRETKEY): ").strip()
    
    try:
        validate_cipher_input("Vigenère Cipher", text, keyword)
        enc = vigenere_encrypt(text, keyword)
        dec = vigenere_decrypt(enc, keyword)
        
        print("\n--- RESULTS ---")
        print(f"Plaintext:      {text}")
        print(f"Keyword:        {keyword.upper()}")
        print(f"Ciphertext:     {enc}")
        print(f"Decrypted Text: {dec}")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

def handle_otp():
    print_header("6. ONE-TIME PAD (OTP)")
    text = input("Enter Plaintext: ").strip()
    
    alpha_len = sum(1 for c in text if c.isalpha())
    print(f"Required Key Length (alphabetic chars): {alpha_len}")
    
    gen_choice = input("Generate a secure random OTP key of matching length? (y/n): ").strip().lower()
    if gen_choice == 'y':
        key = generate_otp_key(max(1, alpha_len))
        print(f"Generated Secure OTP Key: {key}")
    else:
        key = input("Enter OTP Key: ").strip()
        
    try:
        validate_cipher_input("One-Time Pad", text, key)
        enc = otp_encrypt(text, key)
        dec = otp_decrypt(enc, key)
        
        print("\n--- RESULTS ---")
        print(f"Plaintext:      {text}")
        print(f"OTP Key:        {key}")
        print(f"Ciphertext:     {enc}")
        print(f"Decrypted Text: {dec}")
        print("\n[NOTE] Unbreakable security requires single-use, truly random key of equal length.")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

def handle_rail_fence():
    print_header("7. RAIL FENCE CIPHER")
    text = input("Enter Plaintext: ").strip()
    rails_str = input("Enter Number of Rails (integer >= 2): ").strip()
    
    try:
        rails = int(rails_str)
        validate_cipher_input("Rail Fence Cipher", text, rails)
        enc = rail_fence_encrypt(text, rails)
        dec = rail_fence_decrypt(enc, rails)
        
        print("\n--- RESULTS ---")
        print(f"Plaintext:      {text}")
        print(f"Number of Rails:{rails}")
        print(f"Ciphertext:     {enc}")
        print(f"Decrypted Text: {dec}")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

def handle_columnar():
    print_header("8. COLUMNAR TRANSPOSITION CIPHER")
    text = input("Enter Plaintext: ").strip()
    keyword = input("Enter Keyword (e.g. GERMAN): ").strip()
    
    try:
        validate_cipher_input("Columnar Transposition Cipher", text, keyword)
        enc = columnar_encrypt(text, keyword)
        dec = columnar_decrypt(enc, keyword)
        
        order = get_column_order(keyword)
        print(f"\nKeyword Column Read Sequence: {order}")
        
        print("\n--- RESULTS ---")
        print(f"Plaintext:      {text}")
        print(f"Keyword:        {keyword.upper()}")
        print(f"Ciphertext:     {enc}")
        print(f"Decrypted Text: {dec}")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

# ------------------------------------------------------------------------------
# UTILITIES & FILE HANDLERS
# ------------------------------------------------------------------------------
def handle_compare():
    print_header("9. COMPARE ALGORITHMS")
    text = input("Enter Plaintext to Benchmark (or press Enter for default sample): ").strip()
    if not text:
        text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG 12345"
        
    print(f"\nBenchmarking algorithms on text length: {len(text)} characters...\n")
    results = benchmark_algorithms(text)
    
    # Print Table Header
    print(f"{'Algorithm Name':<30} | {'Type':<13} | {'Enc Time (ms)':<14} | {'Dec Time (ms)':<14} | Status")
    print("-" * 82)
    for r in results:
        print(f"{r.name:<30} | {r.cipher_type:<13} | {r.encrypt_time_ms:<14.4f} | {r.decrypt_time_ms:<14.4f} | {r.status}")
        
    print(BENCHMARK_EDUCATIONAL_NOTE)

def handle_file_encrypt():
    print_header("10. ENCRYPT TEXT FILE")
    in_path = input("Enter input text file path (e.g. data/sample_plaintext.txt): ").strip()
    
    try:
        content = read_text_file(in_path)
        print(f"Successfully loaded {len(content)} characters from '{in_path}'.")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")
        return
        
    print("\nSelect Cipher:")
    ciphers = [
        "Caesar Cipher", "Monoalphabetic Cipher", "Playfair Cipher",
        "Hill Cipher", "Vigenère Cipher", "One-Time Pad",
        "Rail Fence Cipher", "Columnar Transposition Cipher"
    ]
    for idx, c in enumerate(ciphers, 1):
        print(f"{idx}. {c}")
        
    try:
        c_choice = int(input("\nEnter choice (1-8): ").strip())
        cipher_name = ciphers[c_choice - 1]
    except (ValueError, IndexError):
        print("[ERROR] Invalid cipher selection.")
        return
        
    key = input(f"Enter Key for {cipher_name}: ").strip()
    out_path = input("Enter output file path (e.g. encrypted_output.txt): ").strip()
    
    try:
        validate_cipher_input(cipher_name, content, key)
        
        if cipher_name == "Caesar Cipher":
            res = caesar_encrypt(content, int(key))
        elif cipher_name == "Monoalphabetic Cipher":
            res = monoalphabetic_encrypt(content, key)
        elif cipher_name == "Playfair Cipher":
            res = playfair_encrypt(content, key)
        elif cipher_name == "Hill Cipher":
            res = hill_encrypt(content, key)
        elif cipher_name == "Vigenère Cipher":
            res = vigenere_encrypt(content, key)
        elif cipher_name == "One-Time Pad":
            res = otp_encrypt(content, key)
        elif cipher_name == "Rail Fence Cipher":
            res = rail_fence_encrypt(content, int(key))
        elif cipher_name == "Columnar Transposition Cipher":
            res = columnar_encrypt(content, key)
            
        saved_path = write_text_file(out_path, res)
        print(f"\n[SUCCESS] File encrypted and saved to: '{saved_path}'")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

def handle_file_decrypt():
    print_header("11. DECRYPT TEXT FILE")
    in_path = input("Enter encrypted file path: ").strip()
    
    try:
        content = read_text_file(in_path)
        print(f"Successfully loaded {len(content)} characters from '{in_path}'.")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")
        return
        
    print("\nSelect Cipher:")
    ciphers = [
        "Caesar Cipher", "Monoalphabetic Cipher", "Playfair Cipher",
        "Hill Cipher", "Vigenère Cipher", "One-Time Pad",
        "Rail Fence Cipher", "Columnar Transposition Cipher"
    ]
    for idx, c in enumerate(ciphers, 1):
        print(f"{idx}. {c}")
        
    try:
        c_choice = int(input("\nEnter choice (1-8): ").strip())
        cipher_name = ciphers[c_choice - 1]
    except (ValueError, IndexError):
        print("[ERROR] Invalid cipher selection.")
        return
        
    key = input(f"Enter Key for {cipher_name}: ").strip()
    out_path = input("Enter output decrypted file path: ").strip()
    
    try:
        validate_cipher_input(cipher_name, content, key)
        
        if cipher_name == "Caesar Cipher":
            res = caesar_decrypt(content, int(key))
        elif cipher_name == "Monoalphabetic Cipher":
            res = monoalphabetic_decrypt(content, key)
        elif cipher_name == "Playfair Cipher":
            res = playfair_decrypt(content, key)
        elif cipher_name == "Hill Cipher":
            res = hill_decrypt(content, key)
        elif cipher_name == "Vigenère Cipher":
            res = vigenere_decrypt(content, key)
        elif cipher_name == "One-Time Pad":
            res = otp_decrypt(content, key)
        elif cipher_name == "Rail Fence Cipher":
            res = rail_fence_decrypt(content, int(key))
        elif cipher_name == "Columnar Transposition Cipher":
            res = columnar_decrypt(content, key)
            
        saved_path = write_text_file(out_path, res)
        print(f"\n[SUCCESS] File decrypted and saved to: '{saved_path}'")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")

def handle_help():
    print_header("12. HELP & DOCUMENTATION")
    print("\nAvailable Algorithm Topics:\n")
    topics = list(ALGORITHM_HELP.keys())
    for idx, t in enumerate(topics, 1):
        print(f"{idx}. {t}")
    print("9. Toolkit User Manual & Instructions")
    
    choice_str = input("\nEnter choice (1-9) to view documentation: ").strip()
    try:
        c = int(choice_str)
        if 1 <= c <= 8:
            t_name = topics[c - 1]
            print(f"\n=== {t_name.upper()} ===")
            print(ALGORITHM_HELP[t_name])
        elif c == 9:
            print("\n=== TOOLKIT INSTRUCTIONS ===")
            print("1. Select an algorithm (1-8) from the main menu.")
            print("2. Enter plaintext and key when prompted.")
            print("3. View ciphertext and decrypted text results.")
            print("4. Use Option 9 to compare execution speeds side-by-side.")
            print("5. Use Options 10-11 to process text files.")
            print("6. Use Option 14 or --gui flag to launch Graphical User Interface.")
        else:
            print("[ERROR] Invalid topic selection.")
    except ValueError:
        print("[ERROR] Please enter a valid number.")

# ------------------------------------------------------------------------------
# MAIN LOOP
# ------------------------------------------------------------------------------
def main():
    # Check command line flags
    if len(sys.argv) > 1 and sys.argv[1].lower() in ["--gui", "-g"]:
        print("Launching Graphical User Interface (GUI)...")
        launch_gui()
        return

    while True:
        display_main_menu()
        choice = input("Enter your Choice (1-14): ").strip()
        print()
        
        if choice == '1':
            handle_caesar()
        elif choice == '2':
            handle_monoalphabetic()
        elif choice == '3':
            handle_playfair()
        elif choice == '4':
            handle_hill()
        elif choice == '5':
            handle_vigenere()
        elif choice == '6':
            handle_otp()
        elif choice == '7':
            handle_rail_fence()
        elif choice == '8':
            handle_columnar()
        elif choice == '9':
            handle_compare()
        elif choice == '10':
            handle_file_encrypt()
        elif choice == '11':
            handle_file_decrypt()
        elif choice == '12':
            handle_help()
        elif choice == '13':
            print("Exiting Classical Cryptography Toolkit. Goodbye!")
            sys.exit(0)
        elif choice == '14':
            print("Launching Tkinter Graphical User Interface (GUI)...")
            launch_gui()
        else:
            print("[ERROR] Invalid choice. Please enter a number between 1 and 14.")
            
        input("\nPress Enter to return to the Main Menu...")

if __name__ == "__main__":
    main()
