"""
Graphical User Interface (GUI) Module
Built using Python standard tkinter and ttk libraries for a clean, professional dashboard.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import time
from typing import Dict, Any

# Import algorithm functions and utilities
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
from algorithms.columnar import columnar_encrypt, columnar_decrypt

from utils.file_handler import read_text_file, write_text_file
from utils.benchmark import benchmark_algorithms, BENCHMARK_EDUCATIONAL_NOTE
from utils.validator import validate_cipher_input

# Help explanations dictionary
ALGORITHM_HELP = {
    "Caesar Cipher": (
        "CIPHER TYPE: Substitution (Monoalphabetic Shift)\n\n"
        "DESCRIPTION:\n"
        "One of the earliest and simplest ciphers. Each letter in the plaintext is shifted by a fixed number of positions down the alphabet.\n\n"
        "KEY REQUIREMENTS:\n"
        "An integer shift value (e.g., 3 or 5).\n\n"
        "ENCRYPTION FORMULA: C = (P + k) mod 26\n"
        "DECRYPTION FORMULA: P = (C - k) mod 26"
    ),
    "Monoalphabetic Cipher": (
        "CIPHER TYPE: Substitution (Monoalphabetic Permutation)\n\n"
        "DESCRIPTION:\n"
        "Replaces each letter of the alphabet with a unique corresponding letter according to a fixed 26-letter substitution alphabet key.\n\n"
        "KEY REQUIREMENTS:\n"
        "A string of exactly 26 unique alphabetic characters (e.g., QWERTYUIOPASDFGHJKLZXCVBNM).\n\n"
        "FEATURES:\n"
        "Supports 'Generate Random Key' for quick key creation."
    ),
    "Playfair Cipher": (
        "CIPHER TYPE: Substitution (Polygraphic 5x5 Matrix)\n\n"
        "DESCRIPTION:\n"
        "Encrypts pairs of letters (digrams) using a 5x5 matrix constructed from a keyword. 'J' is merged with 'I'.\n\n"
        "KEY REQUIREMENTS:\n"
        "An alphabetic keyword (e.g., MONARCHY).\n\n"
        "RULES:\n"
        "- Same Row: Shift right (encrypt) / left (decrypt).\n"
        "- Same Column: Shift down (encrypt) / up (decrypt).\n"
        "- Rectangle: Swap column indices."
    ),
    "Hill Cipher": (
        "CIPHER TYPE: Substitution (Polygraphic 2x2 Matrix)\n\n"
        "DESCRIPTION:\n"
        "Uses linear algebra mod 26 with a 2x2 key matrix to transform letter pairs.\n\n"
        "KEY REQUIREMENTS:\n"
        "A 4-letter word (e.g., HILL) or 4 integers (e.g., '3 3 2 5'). Matrix determinant must be coprime to 26.\n\n"
        "FORMULA: [C1, C2]^T = [K] * [P1, P2]^T mod 26"
    ),
    "Vigenère Cipher": (
        "CIPHER TYPE: Polyalphabetic Substitution\n\n"
        "DESCRIPTION:\n"
        "Uses a repeating keyword where each letter of the key determines the Caesar shift for the corresponding plaintext letter.\n\n"
        "KEY REQUIREMENTS:\n"
        "An alphabetic keyword (e.g., SECRETKEY).\n\n"
        "FORMULA: C_i = (P_i + K_i) mod 26"
    ),
    "One-Time Pad": (
        "CIPHER TYPE: Polyalphabetic Substitution (Mod 26 Additive / Unbreakable)\n\n"
        "DESCRIPTION:\n"
        "Mathematically unbreakable if key is truly random, equal in length to plaintext, and used only once.\n\n"
        "KEY REQUIREMENTS:\n"
        "Random key with length >= alphabetic length of plaintext."
    ),
    "Rail Fence Cipher": (
        "CIPHER TYPE: Transposition (Zigzag Pattern)\n\n"
        "DESCRIPTION:\n"
        "Writes plaintext in a downward/upward zigzag path across a specified number of parallel rails and reads off row by row.\n\n"
        "KEY REQUIREMENTS:\n"
        "An integer number of rails (key >= 2)."
    ),
    "Columnar Transposition Cipher": (
        "CIPHER TYPE: Transposition (Matrix Column Shuffling)\n\n"
        "DESCRIPTION:\n"
        "Writes plaintext in rows under a keyword, then reads out characters column by column in alphabetical order of the key.\n\n"
        "KEY REQUIREMENTS:\n"
        "An alphabetic keyword (e.g., GERMAN)."
    ),
}

CIPHER_KEY_HINTS = {
    "Caesar Cipher": "Enter integer shift (e.g., 5):",
    "Monoalphabetic Cipher": "Enter 26 unique letters (A-Z permutation):",
    "Playfair Cipher": "Enter keyword (e.g., MONARCHY):",
    "Hill Cipher": "Enter 4 letters (e.g. HILL) or 4 numbers (e.g. '3 3 2 5'):",
    "Vigenère Cipher": "Enter keyword (e.g., SECRETKEY):",
    "One-Time Pad": "Enter key (length >= plaintext letters):",
    "Rail Fence Cipher": "Enter number of rails (integer >= 2):",
    "Columnar Transposition Cipher": "Enter keyword (e.g., GERMAN):",
}

class CryptoToolkitGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Classical Cryptography Toolkit - Network Security Project")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Configure Styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Color palette
        self.primary_color = "#1E293B"     # Slate 800
        self.accent_color = "#2563EB"      # Blue 600
        self.bg_color = "#F8FAFC"          # Slate 50
        
        self.root.configure(bg=self.bg_color)
        
        # Custom Widget Styles
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("Header.TFrame", background=self.primary_color)
        self.style.configure("Header.TLabel", background=self.primary_color, foreground="white", font=("Helvetica", 16, "bold"))
        self.style.configure("SubHeader.TLabel", background=self.primary_color, foreground="#94A3B8", font=("Helvetica", 10))
        self.style.configure("Action.TButton", font=("Helvetica", 10, "bold"), padding=6)
        
        # Header Banner
        header_frame = ttk.Frame(self.root, style="Header.TFrame", padding=15)
        header_frame.pack(fill="x", side="top")
        
        lbl_title = ttk.Label(header_frame, text="CLASSICAL CRYPTOGRAPHY TOOLKIT", style="Header.TLabel")
        lbl_title.pack(anchor="w")
        
        lbl_sub = ttk.Label(header_frame, text="Network Security Mini-Project | Substitution & Transposition Ciphers", style="SubHeader.TLabel")
        lbl_sub.pack(anchor="w")
        
        # Notebook (Tabbed Interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Tabs
        self.tab_dashboard = ttk.Frame(self.notebook, padding=10)
        self.tab_file_op = ttk.Frame(self.notebook, padding=10)
        self.tab_benchmark = ttk.Frame(self.notebook, padding=10)
        self.tab_help = ttk.Frame(self.notebook, padding=10)
        
        self.notebook.add(self.tab_dashboard, text=" Cipher Dashboard ")
        self.notebook.add(self.tab_file_op, text=" File Operations ")
        self.notebook.add(self.tab_benchmark, text=" Compare Algorithms ")
        self.notebook.add(self.tab_help, text=" Help & Documentation ")
        
        # Initialize UI for all tabs
        self._build_dashboard_tab()
        self._build_file_tab()
        self._build_benchmark_tab()
        self._build_help_tab()
        
    # --------------------------------------------------------------------------
    # TAB 1: DASHBOARD
    # --------------------------------------------------------------------------
    def _build_dashboard_tab(self):
        # Top Frame: Cipher Selection & Key
        ctrl_frame = ttk.LabelFrame(self.tab_dashboard, text=" Cipher Configuration ", padding=10)
        ctrl_frame.pack(fill="x", side="top", pady=5)
        
        # Cipher Select Dropdown
        ttk.Label(ctrl_frame, text="Select Cipher:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.combo_cipher = ttk.Combobox(
            ctrl_frame,
            values=list(CIPHER_KEY_HINTS.keys()),
            state="readonly",
            width=30,
            font=("Helvetica", 10)
        )
        self.combo_cipher.set("Caesar Cipher")
        self.combo_cipher.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        self.combo_cipher.bind("<<ComboboxSelected>>", self._on_cipher_change)
        
        # Key Label & Entry
        self.lbl_key = ttk.Label(ctrl_frame, text=CIPHER_KEY_HINTS["Caesar Cipher"], font=("Helvetica", 10))
        self.lbl_key.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        key_input_frame = ttk.Frame(ctrl_frame)
        key_input_frame.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
        
        self.entry_key = ttk.Entry(key_input_frame, width=35, font=("Courier", 10))
        self.entry_key.insert(0, "5")
        self.entry_key.pack(side="left", fill="x", expand=True)
        
        self.btn_gen_key = ttk.Button(key_input_frame, text="Generate Key", command=self._generate_key, state="disabled")
        self.btn_gen_key.pack(side="left", padx=5)
        
        # Middle Split: Plaintext & Ciphertext
        split_frame = ttk.Frame(self.tab_dashboard)
        split_frame.pack(fill="both", expand=True, pady=10)
        
        # Left Panel: Plaintext Input
        left_box = ttk.LabelFrame(split_frame, text=" Plaintext Input ", padding=8)
        left_box.pack(side="left", fill="both", expand=True, padx=(0, 5))
        
        self.txt_input = tk.Text(left_box, wrap="word", font=("Courier", 10), height=8)
        self.txt_input.pack(fill="both", expand=True)
        self.txt_input.insert("1.0", "NETWORK SECURITY")
        
        # Right Panel: Ciphertext Result
        right_box = ttk.LabelFrame(split_frame, text=" Output / Decrypted Result ", padding=8)
        right_box.pack(side="right", fill="both", expand=True, padx=(5, 0))
        
        self.txt_output = tk.Text(right_box, wrap="word", font=("Courier", 10), height=8)
        self.txt_output.pack(fill="both", expand=True)
        
        # Matrix/Info Display (for Playfair & Hill Matrix visualizer)
        self.lbl_matrix_info = ttk.Label(self.tab_dashboard, text="", font=("Courier", 9, "bold"), foreground="#0F172A")
        self.lbl_matrix_info.pack(fill="x", pady=2)
        
        # Action Buttons Frame
        btn_bar = ttk.Frame(self.tab_dashboard, padding=5)
        btn_bar.pack(fill="x", side="bottom")
        
        btn_encrypt = ttk.Button(btn_bar, text="Encrypt", style="Action.TButton", command=self._do_encrypt)
        btn_encrypt.pack(side="left", padx=5)
        
        btn_decrypt = ttk.Button(btn_bar, text="Decrypt", style="Action.TButton", command=self._do_decrypt)
        btn_decrypt.pack(side="left", padx=5)
        
        btn_clear = ttk.Button(btn_bar, text="Clear", command=self._clear_dashboard)
        btn_clear.pack(side="left", padx=5)
        
        btn_copy = ttk.Button(btn_bar, text="Copy Output", command=self._copy_output)
        btn_copy.pack(side="left", padx=5)
        
        btn_exit = ttk.Button(btn_bar, text="Exit Application", command=self.root.quit)
        btn_exit.pack(side="right", padx=5)

    def _on_cipher_change(self, event=None):
        cipher = self.combo_cipher.get()
        self.lbl_key.config(text=CIPHER_KEY_HINTS.get(cipher, "Enter Key:"))
        
        # Enable key generation button for Monoalphabetic & OTP
        if cipher in ["Monoalphabetic Cipher", "One-Time Pad"]:
            self.btn_gen_key.config(state="normal")
        else:
            self.btn_gen_key.config(state="disabled")
            
        # Set sample default keys
        defaults = {
            "Caesar Cipher": "5",
            "Monoalphabetic Cipher": "QWERTYUIOPASDFGHJKLZXCVBNM",
            "Playfair Cipher": "KEYWORD",
            "Hill Cipher": "HILL",
            "Vigenère Cipher": "SECRETKEY",
            "One-Time Pad": "SECRETKEYWORDOK",
            "Rail Fence Cipher": "3",
            "Columnar Transposition Cipher": "GERMAN"
        }
        if cipher in defaults:
            self.entry_key.delete(0, tk.END)
            self.entry_key.insert(0, defaults[cipher])
            
        self.lbl_matrix_info.config(text="")

    def _generate_key(self):
        cipher = self.combo_cipher.get()
        if cipher == "Monoalphabetic Cipher":
            new_key = generate_monoalphabetic_key()
            self.entry_key.delete(0, tk.END)
            self.entry_key.insert(0, new_key)
        elif cipher == "One-Time Pad":
            text = self.txt_input.get("1.0", tk.END).strip()
            alpha_len = sum(1 for c in text if c.isalpha())
            if alpha_len == 0:
                alpha_len = 10
            new_key = generate_otp_key(alpha_len)
            self.entry_key.delete(0, tk.END)
            self.entry_key.insert(0, new_key)

    def _do_encrypt(self):
        cipher = self.combo_cipher.get()
        text = self.txt_input.get("1.0", tk.END).rstrip("\n")
        key = self.entry_key.get().strip()
        
        try:
            validate_cipher_input(cipher, text, key)
            res = ""
            
            if cipher == "Caesar Cipher":
                res = caesar_encrypt(text, int(key))
            elif cipher == "Monoalphabetic Cipher":
                res = monoalphabetic_encrypt(text, key)
            elif cipher == "Playfair Cipher":
                res = playfair_encrypt(text, key)
                matrix = generate_playfair_matrix(key)
                matrix_str = "Playfair 5x5 Matrix: " + " | ".join("".join(row) for row in matrix)
                self.lbl_matrix_info.config(text=matrix_str)
            elif cipher == "Hill Cipher":
                res = hill_encrypt(text, key)
                matrix = parse_hill_key(key)
                self.lbl_matrix_info.config(text=f"Hill 2x2 Key Matrix: [{matrix[0]} , {matrix[1]}]")
            elif cipher == "Vigenère Cipher":
                res = vigenere_encrypt(text, key)
            elif cipher == "One-Time Pad":
                res = otp_encrypt(text, key)
            elif cipher == "Rail Fence Cipher":
                res = rail_fence_encrypt(text, int(key))
            elif cipher == "Columnar Transposition Cipher":
                res = columnar_encrypt(text, key)
                
            self.txt_output.delete("1.0", tk.END)
            self.txt_output.insert("1.0", res)
        except Exception as e:
            messagebox.showerror("Cipher Error", str(e))

    def _do_decrypt(self):
        cipher = self.combo_cipher.get()
        text = self.txt_input.get("1.0", tk.END).rstrip("\n")
        key = self.entry_key.get().strip()
        
        try:
            validate_cipher_input(cipher, text, key)
            res = ""
            
            if cipher == "Caesar Cipher":
                res = caesar_decrypt(text, int(key))
            elif cipher == "Monoalphabetic Cipher":
                res = monoalphabetic_decrypt(text, key)
            elif cipher == "Playfair Cipher":
                res = playfair_decrypt(text, key)
            elif cipher == "Hill Cipher":
                res = hill_decrypt(text, key)
            elif cipher == "Vigenère Cipher":
                res = vigenere_decrypt(text, key)
            elif cipher == "One-Time Pad":
                res = otp_decrypt(text, key)
            elif cipher == "Rail Fence Cipher":
                res = rail_fence_decrypt(text, int(key))
            elif cipher == "Columnar Transposition Cipher":
                res = columnar_decrypt(text, key)
                
            self.txt_output.delete("1.0", tk.END)
            self.txt_output.insert("1.0", res)
        except Exception as e:
            messagebox.showerror("Cipher Error", str(e))

    def _clear_dashboard(self):
        self.txt_input.delete("1.0", tk.END)
        self.txt_output.delete("1.0", tk.END)
        self.lbl_matrix_info.config(text="")

    def _copy_output(self):
        out_text = self.txt_output.get("1.0", tk.END).rstrip("\n")
        if out_text:
            self.root.clipboard_clear()
            self.root.clipboard_append(out_text)
            messagebox.showinfo("Copied", "Output copied to clipboard.")

    # --------------------------------------------------------------------------
    # TAB 2: FILE OPERATIONS
    # --------------------------------------------------------------------------
    def _build_file_tab(self):
        box = ttk.LabelFrame(self.tab_file_op, text=" Encrypt / Decrypt Text Files ", padding=15)
        box.pack(fill="both", expand=True)
        
        # File Select
        ttk.Label(box, text="Select Text File:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", pady=10)
        self.entry_file_path = ttk.Entry(box, width=50, font=("Courier", 10))
        self.entry_file_path.grid(row=0, column=1, padx=5, pady=10)
        
        btn_browse = ttk.Button(box, text="Browse...", command=self._browse_file)
        btn_browse.grid(row=0, column=2, padx=5, pady=10)
        
        # Cipher Choice
        ttk.Label(box, text="Select Cipher:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", pady=10)
        self.combo_file_cipher = ttk.Combobox(box, values=list(CIPHER_KEY_HINTS.keys()), state="readonly", width=30)
        self.combo_file_cipher.set("Caesar Cipher")
        self.combo_file_cipher.grid(row=1, column=1, sticky="w", padx=5, pady=10)
        
        # Key Input
        ttk.Label(box, text="Enter Key:", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w", pady=10)
        self.entry_file_key = ttk.Entry(box, width=50, font=("Courier", 10))
        self.entry_file_key.insert(0, "5")
        self.entry_file_key.grid(row=2, column=1, padx=5, pady=10)
        
        # Action Buttons
        btn_box = ttk.Frame(box, padding=10)
        btn_box.grid(row=3, column=0, columnspan=3, pady=20)
        
        btn_file_enc = ttk.Button(btn_box, text="Encrypt & Save File", style="Action.TButton", command=self._encrypt_file_action)
        btn_file_enc.pack(side="left", padx=10)
        
        btn_file_dec = ttk.Button(btn_box, text="Decrypt & Save File", style="Action.TButton", command=self._decrypt_file_action)
        btn_file_dec.pack(side="left", padx=10)
        
        # Status Log Output
        self.txt_file_log = tk.Text(box, height=10, font=("Courier", 9), wrap="word")
        self.txt_file_log.grid(row=4, column=0, columnspan=3, fill="both", expand=True, pady=10)
        self.txt_file_log.insert("1.0", "File Operations Log:\nSelect a file and algorithm to begin.")

    def _browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.entry_file_path.delete(0, tk.END)
            self.entry_file_path.insert(0, file_path)

    def _encrypt_file_action(self):
        in_path = self.entry_file_path.get().strip()
        cipher = self.combo_file_cipher.get()
        key = self.entry_file_key.get().strip()
        
        try:
            content = read_text_file(in_path)
            validate_cipher_input(cipher, content, key)
            
            out_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")],
                title="Save Encrypted File As"
            )
            if not out_path:
                return
                
            if cipher == "Caesar Cipher":
                res = caesar_encrypt(content, int(key))
            elif cipher == "Monoalphabetic Cipher":
                res = monoalphabetic_encrypt(content, key)
            elif cipher == "Playfair Cipher":
                res = playfair_encrypt(content, key)
            elif cipher == "Hill Cipher":
                res = hill_encrypt(content, key)
            elif cipher == "Vigenère Cipher":
                res = vigenere_encrypt(content, key)
            elif cipher == "One-Time Pad":
                res = otp_encrypt(content, key)
            elif cipher == "Rail Fence Cipher":
                res = rail_fence_encrypt(content, int(key))
            elif cipher == "Columnar Transposition Cipher":
                res = columnar_encrypt(content, key)
                
            saved_path = write_text_file(out_path, res)
            
            log_msg = f"[SUCCESS] Encrypted '{in_path}'\nUsing: {cipher}\nOutput File: {saved_path}\n"
            self.txt_file_log.insert(tk.END, f"\n{log_msg}")
            messagebox.showinfo("Success", f"File encrypted successfully!\nSaved to: {saved_path}")
        except Exception as e:
            messagebox.showerror("File Error", str(e))

    def _decrypt_file_action(self):
        in_path = self.entry_file_path.get().strip()
        cipher = self.combo_file_cipher.get()
        key = self.entry_file_key.get().strip()
        
        try:
            content = read_text_file(in_path)
            validate_cipher_input(cipher, content, key)
            
            out_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")],
                title="Save Decrypted File As"
            )
            if not out_path:
                return
                
            if cipher == "Caesar Cipher":
                res = caesar_decrypt(content, int(key))
            elif cipher == "Monoalphabetic Cipher":
                res = monoalphabetic_decrypt(content, key)
            elif cipher == "Playfair Cipher":
                res = playfair_decrypt(content, key)
            elif cipher == "Hill Cipher":
                res = hill_decrypt(content, key)
            elif cipher == "Vigenère Cipher":
                res = vigenere_decrypt(content, key)
            elif cipher == "One-Time Pad":
                res = otp_decrypt(content, key)
            elif cipher == "Rail Fence Cipher":
                res = rail_fence_decrypt(content, int(key))
            elif cipher == "Columnar Transposition Cipher":
                res = columnar_decrypt(content, key)
                
            saved_path = write_text_file(out_path, res)
            
            log_msg = f"[SUCCESS] Decrypted '{in_path}'\nUsing: {cipher}\nOutput File: {saved_path}\n"
            self.txt_file_log.insert(tk.END, f"\n{log_msg}")
            messagebox.showinfo("Success", f"File decrypted successfully!\nSaved to: {saved_path}")
        except Exception as e:
            messagebox.showerror("File Error", str(e))

    # --------------------------------------------------------------------------
    # TAB 3: BENCHMARK / COMPARISON
    # --------------------------------------------------------------------------
    def _build_benchmark_tab(self):
        top = ttk.Frame(self.tab_benchmark, padding=5)
        top.pack(fill="x")
        
        ttk.Label(top, text="Plaintext for Comparison:", font=("Helvetica", 10, "bold")).pack(anchor="w")
        self.txt_bench_input = tk.Text(top, height=3, font=("Courier", 10))
        self.txt_bench_input.pack(fill="x", pady=5)
        self.txt_bench_input.insert("1.0", "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG 12345")
        
        btn_run_bench = ttk.Button(top, text="Run Comparison Across All Ciphers", style="Action.TButton", command=self._run_benchmark)
        btn_run_bench.pack(anchor="w", pady=5)
        
        # Results Treeview Table
        table_frame = ttk.Frame(self.tab_benchmark, padding=5)
        table_frame.pack(fill="both", expand=True)
        
        columns = ("name", "type", "enc_time", "dec_time", "status", "sample_cipher")
        self.tree_bench = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)
        
        self.tree_bench.heading("name", text="Algorithm Name")
        self.tree_bench.heading("type", text="Cipher Type")
        self.tree_bench.heading("enc_time", text="Enc Time (ms)")
        self.tree_bench.heading("dec_time", text="Dec Time (ms)")
        self.tree_bench.heading("status", text="Status")
        self.tree_bench.heading("sample_cipher", text="Sample Ciphertext")
        
        self.tree_bench.column("name", width=180)
        self.tree_bench.column("type", width=110)
        self.tree_bench.column("enc_time", width=100, anchor="e")
        self.tree_bench.column("dec_time", width=100, anchor="e")
        self.tree_bench.column("status", width=80, anchor="center")
        self.tree_bench.column("sample_cipher", width=250)
        
        scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree_bench.yview)
        self.tree_bench.configure(yscrollcommand=scroll.set)
        
        self.tree_bench.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        
        # Educational Note Text Box
        self.txt_bench_note = tk.Text(self.tab_benchmark, height=6, font=("Courier", 8), background="#F1F5F9")
        self.txt_bench_note.pack(fill="x", pady=5)
        self.txt_bench_note.insert("1.0", BENCHMARK_EDUCATIONAL_NOTE)

    def _run_benchmark(self):
        text = self.txt_bench_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter plaintext for benchmarking.")
            return
            
        # Clear existing rows
        for item in self.tree_bench.get_children():
            self.tree_bench.delete(item)
            
        results = benchmark_algorithms(text)
        for r in results:
            self.tree_bench.insert(
                "",
                "end",
                values=(
                    r.name,
                    r.cipher_type,
                    f"{r.encrypt_time_ms:.4f}",
                    f"{r.decrypt_time_ms:.4f}",
                    r.status,
                    r.ciphertext[:30] + ("..." if len(r.ciphertext) > 30 else "")
                )
            )

    # --------------------------------------------------------------------------
    # TAB 4: HELP & DOCUMENTATION
    # --------------------------------------------------------------------------
    def _build_help_tab(self):
        frame = ttk.Frame(self.tab_help, padding=10)
        frame.pack(fill="both", expand=True)
        
        left = ttk.Frame(frame)
        left.pack(side="left", fill="y", padx=(0, 10))
        
        ttk.Label(left, text="Select Topic:", font=("Helvetica", 10, "bold")).pack(anchor="w")
        
        self.list_help_topics = tk.Listbox(left, width=28, font=("Helvetica", 10), height=18)
        self.list_help_topics.pack(fill="y", expand=True)
        
        for name in ALGORITHM_HELP.keys():
            self.list_help_topics.insert(tk.END, name)
            
        self.list_help_topics.bind("<<ListboxSelect>>", self._on_help_select)
        
        right = ttk.Frame(frame)
        right.pack(side="right", fill="both", expand=True)
        
        ttk.Label(right, text="Algorithm Details & Guide:", font=("Helvetica", 10, "bold")).pack(anchor="w")
        
        self.txt_help_detail = tk.Text(right, wrap="word", font=("Helvetica", 10), background="#F8FAFC")
        self.txt_help_detail.pack(fill="both", expand=True)
        
        self.list_help_topics.select_set(0)
        self._on_help_select()

    def _on_help_select(self, event=None):
        sel = self.list_help_topics.curselection()
        if not sel:
            return
        topic = self.list_help_topics.get(sel[0])
        content = ALGORITHM_HELP.get(topic, "No documentation available.")
        
        self.txt_help_detail.delete("1.0", tk.END)
        self.txt_help_detail.insert("1.0", f"=== {topic.upper()} ===\n\n{content}")

def launch_gui():
    """Launches the Tkinter GUI dashboard."""
    root = tk.Tk()
    app = CryptoToolkitGUI(root)
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
