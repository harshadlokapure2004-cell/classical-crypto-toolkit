# ⏱️ 5-MINUTE PROJECT DEMONSTRATION GUIDE

Follow this step-by-step sequence for a smooth 5-minute presentation / viva demonstration to your evaluator or class:

---

## 🕒 Timeline & Sequence

### 1. Start the Application (0:00 - 0:30)
- Open terminal in the project directory.
- Run the main program:
  ```bash
  py main.py
  ```
- Point out the **Classical Cryptography Toolkit** main menu displaying all 8 ciphers (Substitution & Transposition) and 5 utility options.

---

### 2. Launch GUI Dashboard (0:30 - 1:00)
- Select Option **14** from CLI (or run `py main.py --gui`).
- Show the clean Tkinter dashboard with tabbed navigation:
  - *Cipher Dashboard*
  - *File Operations*
  - *Compare Algorithms*
  - *Help & Documentation*

---

### 3. Demonstrate Verification Example (Caesar Cipher) (1:00 - 1:45)
- In the **Cipher Dashboard** tab, keep **Caesar Cipher** selected.
- Enter Plaintext: `NETWORK SECURITY`
- Enter Shift Key: `5`
- Click **Encrypt**. Show the output: `SJYBTWP XJHZWNYD`.
- Click **Decrypt**. Show that it restores `NETWORK SECURITY`.

---

### 4. Demonstrate Polygraphic Substitution (Playfair Cipher) (1:45 - 2:30)
- Change selected cipher to **Playfair Cipher**.
- Enter Plaintext: `INSTRUMENT`
- Enter Keyword: `MONARCHY`
- Click **Encrypt**. Point out:
  1. The digram ciphertext result.
  2. The generated **5x5 Playfair Matrix** displayed on screen.

---

### 5. Demonstrate Transposition Cipher (Rail Fence Cipher) (2:30 - 3:15)
- Change selected cipher to **Rail Fence Cipher**.
- Enter Plaintext: `DEFEND THE EAST WALL`
- Enter Rails: `3`
- Click **Encrypt** and **Decrypt** to show how characters are rearranged in a zigzag pattern without changing letter identities.

---

### 6. Demonstrate File Encryption & Decryption (3:15 - 4:00)
- Switch to the **File Operations** tab.
- Click **Browse...** and select `data/sample_plaintext.txt`.
- Select **Vigenère Cipher** with key `SECRETKEY`.
- Click **Encrypt & Save File** and save to `data/sample_encrypted.txt`.
- Now browse `data/sample_encrypted.txt` and click **Decrypt & Save File** to demonstrate file restoration.

---

### 7. Demonstrate Algorithm Comparison (4:00 - 4:30)
- Switch to the **Compare Algorithms** tab.
- Click **Run Comparison Across All Ciphers**.
- Highlight the side-by-side execution time table (in milliseconds).
- Explain the **Educational Disclaimer**: *Fast execution speed does NOT mean higher cryptographic security.*

---

### 8. Show Educational Help & Exit (4:30 - 5:00)
- Switch to **Help & Documentation** tab.
- Select **One-Time Pad** or **Hill Cipher** to show the embedded academic reference guide.
- Click **Exit Application**. Conclude your demo.
