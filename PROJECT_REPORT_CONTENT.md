# COLLEGE MINI-PROJECT REPORT CONTENT

---

## 1. Title Page

**PROJECT TITLE:** Design and Development of a Classical Cryptography Toolkit  
**COURSE:** Network Security  
**ACADEMIC YEAR:** 2025–2026  
**DEPARTMENT:** Computer Science & Engineering / Information Technology  
**TECHNOLOGY:** Python 3 (Standard Library)  

---

## 2. Objectives

1. To design and develop an interactive, menu-driven software application implementing classical cryptography algorithms.
2. To manual implement 8 historical ciphers (6 Substitution Ciphers and 2 Transposition Ciphers) without relying on external cryptography libraries.
3. To provide both a Command Line Interface (CLI) and a Graphical User Interface (GUI) for ease of demonstration.
4. To implement file encryption/decryption modules capable of reading and writing text files.
5. To provide side-by-side performance benchmarking and educational help modules for student comprehension.

---

## 3. Problem Statement

Develop a Cryptography Toolkit allowing users to encrypt and decrypt text using classical ciphers. The system must validate user inputs (shifts, matrix invertibility, key lengths), handle edge cases without crashing, display intermediate cryptographic matrices (Playfair 5x5 and Hill 2x2), and provide automated test verification.

---

## 4. Software Requirements

- **Programming Language:** Python 3.8 or higher
- **User Interface Libraries:** Tkinter / TTK (Standard Library)
- **Utilities:** `secrets`, `pathlib`, `math`, `unittest`
- **Operating System:** Cross-platform (Windows / Linux / macOS)
- **External Dependencies:** None (100% Pure Python Standard Library)

---

## 5. System Design

### 5.1 System Architecture Diagram

```text
+-------------------------------------------------------------------+
|                     USER INTERFACE LAYER                          |
|    +-----------------------------+   +-----------------------+    |
|    |  CLI Main Menu (main.py)    |   |  GUI Dashboard (gui)  |    |
|    +-----------------------------+   +-----------------------+    |
+----------------------------------+--------------------------------+
                                   |
                                   v
+-------------------------------------------------------------------+
|                    VALIDATION & UTILITIES LAYER                   |
|   +-------------------+  +------------------+  +---------------+  |
|   | validator.py      |  | file_handler.py  |  | benchmark.py  |  |
|   +-------------------+  +------------------+  +---------------+  |
+----------------------------------+--------------------------------+
                                   |
                                   v
+-------------------------------------------------------------------+
|                    ALGORITHMS ENGINE LAYER                        |
|  Substitution: Caesar | Monoalphabetic | Playfair | Hill |        |
|                Vigenère | One-Time Pad                            |
|  Transposition: Rail Fence | Columnar Transposition               |
+-------------------------------------------------------------------+
```

### 5.2 Textual Flowchart

```text
[START] --> Launch main.py (or gui.py)
   |
   +--> Display Main Menu (Options 1 - 14)
   |
   +--> User Selects Option:
   |      |
   |      +-- [Options 1 - 8]: Select Cipher (Caesar, Playfair, etc.)
   |      |     |--> Input Plaintext & Key
   |      |     |--> Validate Key via validator.py
   |      |     |--> Execute Encryption / Decryption Algorithm
   |      |     |--> Display Results & Matrices (if applicable)
   |      |
   |      +-- [Option 9]: Compare Algorithms
   |      |     |--> Input Plaintext
   |      |     |--> Run benchmark across all 8 ciphers
   |      |     |--> Display Timing Table & Educational Disclaimer
   |      |
   |      +-- [Options 10 - 11]: File Encrypt / Decrypt
   |      |     |--> Read File via file_handler.py
   |      |     |--> Process Content & Prompt for Save Path
   |      |     |--> Write Output File & Log Confirmation
   |      |
   |      +-- [Option 12]: Help & Documentation
   |      |     |--> Display Algorithm Explanations
   |      |
   |      +-- [Option 13/14]: Exit or Launch GUI
   |
[END] <-- User exits application
```

---

## 6. Algorithms

### 6.1 Substitution Ciphers

1. **Caesar Cipher:**
   Shifts each letter by a fixed integer $k \pmod{26}$.
   - Encryption: $C_i = (P_i + k) \pmod{26}$
   - Decryption: $P_i = (C_i - k) \pmod{26}$

2. **Monoalphabetic Cipher:**
   Replaces each letter of the alphabet with a corresponding letter from a 26-character permutation key.
   
3. **Playfair Cipher:**
   Uses a 5x5 matrix generated from a keyword ('J' merged with 'I'). Plaintext is split into digrams. Identical letters in a pair receive filler character 'X'.
   - Rules: Same row $\rightarrow$ shift right/left; Same column $\rightarrow$ shift down/up; Rectangle $\rightarrow$ swap columns.

4. **Hill Cipher:**
   Polygraphic 2x2 matrix substitution using modulo linear algebra:
   - Encryption: $\vec{C} = K \cdot \vec{P} \pmod{26}$
   - Decryption: $\vec{P} = K^{-1} \cdot \vec{C} \pmod{26}$, where $K^{-1} = \det(K)^{-1} \text{adj}(K) \pmod{26}$. Key matrix must satisfy $\gcd(\det(K), 26) = 1$.

5. **Vigenère Cipher:**
   Polyalphabetic substitution where key letters dictate Caesar shifts for corresponding message characters.

6. **One-Time Pad (OTP):**
   Mod 26 additive cipher matching key length to message alphabetic length. Offers perfect secrecy when the key is truly random, equal in length, and used only once.

### 6.2 Transposition Ciphers

7. **Rail Fence Cipher:**
   Writes plaintext in a zigzag path across $N$ rails ($N \ge 2$) and reads off row by row.

8. **Columnar Transposition Cipher:**
   Writes plaintext in rows under a keyword matrix, then reads out columns in sorted alphabetical order of the key letters.

---

## 7. Program Modules

- `main.py`: Entry point and interactive CLI menu handler.
- `gui.py`: Desktop graphical interface constructed with Tkinter & TTK.
- `algorithms/`: Modular directory containing individual python implementations for each cipher.
- `utils/file_handler.py`: Safe reading/writing of text files with exception handling.
- `utils/validator.py`: Comprehensive key validation and error message formatting.
- `utils/benchmark.py`: Comparative execution speed timer using `time.perf_counter()`.

---

## 8. Sample Inputs and Outputs

### Verification Test Case (Requirement 9 Check)
- **Cipher:** Caesar Cipher
- **Plaintext:** `NETWORK SECURITY`
- **Key:** `5`
- **Ciphertext Output:** `SJYBTWP XJHZWNYD`
- **Decrypted Output:** `NETWORK SECURITY`

---

## 9. Testing

| Test Case ID | Test Description | Input Plaintext & Key | Expected Output | Actual Output | Status |
|---|---|---|---|---|---|
| TC-01 | Caesar Cipher Sample | Plaintext: `NETWORK SECURITY`<br>Key: `5` | `SJYBTWP XJHZWNYD` | `SJYBTWP XJHZWNYD` | PASS |
| TC-02 | Caesar Decryption | Ciphertext: `SJYBTWP XJHZWNYD`<br>Key: `5` | `NETWORK SECURITY` | `NETWORK SECURITY` | PASS |
| TC-03 | Caesar Invalid Shift | Plaintext: `TEST`<br>Key: `abc` | Error: Shift key must be an integer | Error: Shift key must be an integer | PASS |
| TC-04 | Monoalphabetic Valid | Plaintext: `ATTACK AT DAWN`<br>Key: `QWERTYUIOPASDFGHJKLZXCVBNM` | `QZZQAP QZ RQPZ` | `QZZQAP QZ RQPZ` | PASS |
| TC-05 | Monoalphabetic Invalid Key | Plaintext: `TEST`<br>Key: `SHORTKEY` | Error: Key must be 26 characters long | Error: Key must be 26 characters long | PASS |
| TC-06 | Playfair Encryption | Plaintext: `INSTRUMENT`<br>Key: `MONARCHY` | Digram matrix encrypted output | `GATLMZRQTX` | PASS |
| TC-07 | Hill Cipher Valid | Plaintext: `HELP`<br>Key: `HILL` | Matrix multiplication output | `HIAT` | PASS |
| TC-08 | Hill Invalid Determinant | Plaintext: `TEST`<br>Key: `2 4 2 4` | Error: Determinant has no inverse mod 26 | Error: Determinant has no inverse mod 26 | PASS |
| TC-09 | Vigenère Encryption | Plaintext: `Network Security`<br>Key: `KEY` | `Xetgypi Ccombsww` | `Xetgypi Ccombsww` | PASS |
| TC-10 | OTP Short Key | Plaintext: `PLAINTEXT`<br>Key: `SHORT` | Error: Key length shorter than plaintext | Error: Key length shorter than plaintext | PASS |
| TC-11 | Rail Fence 3 Rails | Plaintext: `DEFEND THE EAST WALL`<br>Key: `3` | `D N E T E T E L F D H S A L E W` | `D N E T E T E L F D H S A L E W` | PASS |
| TC-12 | Columnar Transposition | Plaintext: `SECRET MESSAGE`<br>Key: `GERMAN` | Matrix column shuffling output | Encrypted string matching column order | PASS |

---

## 10. Results

All 17 automated unit tests passed in 0.001 seconds (`py -m unittest discover -s tests`). All 8 classical ciphers successfully encrypt plaintext and decrypt ciphertext back to the exact original text.

---

## 11. Applications

- Educational tool for Network Security, Cryptography, and Computer Science curricula.
- Interactive demonstration of substitution vs transposition cipher mechanics.
- Benchmark platform for comparing algorithm execution complexity.

---

## 12. Future Scope

- Cryptanalysis utilities (Letter frequency analysis charts, Kasiski examination).
- Extension to 3x3 Hill matrices and 3DES/AES modern ciphers.
- Web application deployment using Python Web Frameworks (Flask / FastAPI).

---

## 13. Links & References

- Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice*. Pearson.
- Python 3 Standard Library Documentation: `https://docs.python.org/3/`
