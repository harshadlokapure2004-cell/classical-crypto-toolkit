# Classical Cryptography Toolkit

**Course:** Network Security  
**Project Title:** Design and Development of a Classical Cryptography Toolkit  
**Technology:** Python 3 (Pure Standard Library - No External Crypto Dependencies)  

---

## 📌 Project Overview & Objective

The **Classical Cryptography Toolkit** is a comprehensive, interactive software application developed for the Network Security course. It implements **8 classical cryptography algorithms** (6 Substitution Ciphers and 2 Transposition Ciphers) alongside utility modules for side-by-side performance comparison, text file encryption/decryption, and an educational help module.

The objective of this project is to provide a fully functional, user-friendly, menu-driven command-line interface (CLI) and graphical user interface (GUI) to help students and instructors understand the fundamental mechanics of historical encryption methods.

---

## 🚀 Problem Statement

Develop a menu-driven Cryptography Toolkit that allows users to encrypt and decrypt text using classical ciphers. The application must provide interactive interfaces (CLI & GUI), validate invalid keys gracefully without crashing, display key matrices (Playfair & Hill), handle file I/O operations, compare execution speeds, and pass rigorous unit testing.

---

## ✨ Features

- **8 Classical Ciphers Implemented Manually:**
  1. **Caesar Cipher** (Monoalphabetic shift)
  2. **Monoalphabetic Cipher** (26-letter substitution with random key generation)
  3. **Playfair Cipher** (5x5 matrix digram substitution)
  4. **Hill Cipher** (2x2 matrix modulo linear algebra)
  5. **Vigenère Cipher** (Polyalphabetic keyword shift)
  6. **One-Time Pad (OTP)** (Information-theoretically secure additive cipher with secure key generator)
  7. **Rail Fence Cipher** (Zigzag transposition)
  8. **Columnar Transposition Cipher** (Matrix column shuffling)
- **Dual User Interface:**
  - Interactive **CLI Menu** (Options 1–14)
  - Desktop **Tkinter GUI Dashboard** (Tabbed UI with clipboard & visualizers)
- **File Encryption & Decryption:** Read and write `.txt` files with selected ciphers.
- **Algorithm Comparison Module:** Benchmarks execution time (in ms) across all ciphers.
- **Educational Help Module:** In-depth documentation of algorithm rules, key requirements, and mathematical formulas.
- **Robust Error Handling:** Validates key inputs, non-invertible matrices, and file paths with clean user guidance.

---

## 📁 Project Structure

```text
classical_crypto_toolkit/
│
├── main.py                     # Main CLI launcher and entry point
├── gui.py                      # Tkinter Graphical User Interface module
├── requirements.txt            # Package requirements (Standard Library)
├── README.md                   # Project documentation
├── user_manual.md              # Step-by-step user guide
├── DEMO_GUIDE.md               # 5-minute presentation demonstration sequence
├── PRESENTATION_CONTENT.md     # Presentation slides content (6 slides)
├── PROJECT_REPORT_CONTENT.md   # Complete college project report
│
├── algorithms/                 # Classical Cipher implementations
│   ├── __init__.py
│   ├── caesar.py
│   ├── monoalphabetic.py
│   ├── playfair.py
│   ├── hill.py
│   ├── vigenere.py
│   ├── otp.py
│   ├── rail_fence.py
│   └── columnar.py
│
├── utils/                      # Helper modules
│   ├── __init__.py
│   ├── file_handler.py         # Cross-platform file I/O
│   ├── validator.py            # Input validation & error messaging
│   └── benchmark.py            # Execution time benchmarking
│
├── data/                       # Sample files
│   └── sample_plaintext.txt
│
└── tests/                      # Automated unit test suite
    └── test_algorithms.py
```

---

## 🛠️ Installation & Prerequisites

1. **Prerequisites:** Python 3.8+ installed on your system.
2. **Clone / Download** this project directory.
3. No third-party packages are required. Standard library modules (`tkinter`, `secrets`, `pathlib`, `unittest`) are used.

---

## 💻 How to Run the Application

### 1. Run Interactive CLI Menu
```bash
py main.py
# or
python main.py
```

### 2. Launch GUI Dashboard Directly
```bash
py main.py --gui
# or select Option 14 from the CLI main menu
```

### 3. Run Automated Unit Tests
```bash
py -m unittest discover -s tests -p "test_*.py"
```

---

## 🔐 Description of Implemented Ciphers

| Cipher Name | Category | Key Requirement | Description / Rule |
|---|---|---|---|
| **Caesar Cipher** | Substitution | Integer (e.g. `5`) | Shifts characters by a fixed integer value mod 26. |
| **Monoalphabetic** | Substitution | 26-char string | Maps A-Z to a fixed 26-letter permutation key. |
| **Playfair Cipher** | Substitution | Keyword | Encrypts digrams using a 5x5 matrix (combining I/J). |
| **Hill Cipher** | Substitution | 2x2 Matrix / 4 letters | Encrypts letter pairs via matrix multiplication mod 26. |
| **Vigenère Cipher** | Polyalphabetic | Keyword | Shifts letters using a repeating keyword sequence. |
| **One-Time Pad** | Polyalphabetic | Random String | Mod 26 additive cipher with key length $\ge$ plaintext length. |
| **Rail Fence** | Transposition | Rails integer $\ge 2$ | Writes characters in a zigzag pattern across rails. |
| **Columnar Transposition**| Transposition | Keyword | Writes text in rows, reads columns in key order. |

---

## 🧪 Verified Example (Requirement Check)

- **Plaintext:** `NETWORK SECURITY`
- **Cipher:** Caesar Cipher
- **Key:** `5`
- **Encrypted Output:** `SJYBTWP XJHZWNYD`
- **Decrypted Output:** `NETWORK SECURITY`

---

## ⚠️ Academic & Security Notice

> [!IMPORTANT]  
> This software is an **educational project** for demonstrating historical **classical cryptography**. Classical ciphers are vulnerable to frequency analysis, Kasiski examination, and modern brute-force techniques. They are **NOT** secure for protecting modern digital communication. Modern systems require standardized algorithms such as AES, RSA, or ECC.

---

## 🔮 Future Scope

1. Integration of cryptanalysis tools (Kasiski examination, letter frequency distribution visualizer).
2. Support for 3x3 Hill Cipher matrices.
3. Web interface built with Flask/FastAPI or Streamlit.
