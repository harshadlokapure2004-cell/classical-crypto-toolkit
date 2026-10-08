# User Manual - Classical Cryptography Toolkit

Welcome to the **Classical Cryptography Toolkit** user manual. This guide provides step-by-step instructions for operating both the Command Line Interface (CLI) and Graphical User Interface (GUI).

---

## 1. Starting the Application

### Option A: Command Line Interface (CLI)
1. Open a terminal / command prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/classical_crypto_toolkit
   ```
3. Run:
   ```bash
   py main.py
   ```
4. The main menu will be displayed with options 1 to 14.

### Option B: Graphical User Interface (GUI)
1. Run:
   ```bash
   py main.py --gui
   ```
   Or select **Option 14** from the CLI main menu.

---

## 2. Operating the Cipher Dashboard (GUI)

1. **Select Cipher:** Click the dropdown menu at the top of the **Cipher Dashboard** tab and choose your desired cipher (e.g., *Caesar Cipher*, *Playfair Cipher*, *Hill Cipher*).
2. **Key Input:** 
   - Observe the updated hint next to the key entry field.
   - Enter your key (e.g., `5` for Caesar, `MONARCHY` for Playfair, `HILL` for Hill Cipher).
   - For **Monoalphabetic** or **One-Time Pad**, click **Generate Key** to create a valid random key automatically.
3. **Enter Plaintext:** Type your message in the **Plaintext Input** box.
4. **Encrypt:** Click **Encrypt**. The encrypted text will appear in the output box.
5. **Decrypt:** Click **Decrypt** to convert the ciphertext back to plaintext.
6. **Matrix Visualization:** For Playfair and Hill ciphers, view the generated 5x5 matrix or 2x2 key matrix directly below the output box.
7. **Copy Output:** Click **Copy Output** to copy the ciphertext to your system clipboard.

---

## 3. Encrypting and Decrypting Text Files

1. Switch to the **File Operations** tab in the GUI or choose **Option 10 / 11** in the CLI.
2. Click **Browse...** to pick a target `.txt` file (e.g., `data/sample_plaintext.txt`).
3. Select the desired cipher and enter the key.
4. Click **Encrypt & Save File** or **Decrypt & Save File**.
5. Choose where to save the output file when prompted.
6. Check the status log at the bottom for confirmation.

---

## 4. Comparing Algorithm Execution Speeds

1. Open the **Compare Algorithms** tab in the GUI or choose **Option 9** in the CLI.
2. Enter a sample plaintext or use the default string.
3. Click **Run Comparison Across All Ciphers**.
4. Review the generated table showing:
   - Algorithm Name
   - Cipher Type (Substitution vs Transposition)
   - Encryption Time (in ms)
   - Decryption Time (in ms)
   - Status & Sample Output
5. Read the educational notice detailing why execution time does not equal cryptographic security.

---

## 5. Accessing Help & Documentation

- **In GUI:** Open the **Help & Documentation** tab, select an algorithm topic on the left listbox, and read the explanation on the right.
- **In CLI:** Choose **Option 12 (Help)** and select a topic number (1–9).

---

## 6. Exiting the Application

- **GUI:** Click the **Exit Application** button at the bottom right or close the window.
- **CLI:** Enter **13** in the main menu.
