# Qiskit for Beginners

Four short Python programs to take your first steps in quantum computing with
[Qiskit](https://www.ibm.com/quantum/qiskit), IBM's open-source quantum SDK.

No physics background needed. If you can read a little Python, you are ready.

## The programs

Do them in order. Each one builds on the previous.

| File | What you will learn |
|------|---------------------|
| `01_quantum_coin.py` | Qubits, the H gate, measurement, randomness |
| `02_linked_coins.py` | Entanglement, the CNOT gate, noise on real hardware |
| `03_spot_the_bug.py` | Four common beginner bugs and how to catch them |
| `04_quantum_dice.py` | True randomness, binary numbers, a small fun project |

Every program is fully commented, ends with a "Try it yourself" section, and
explains what you learned.

## Setup in VS Code (one time only)

1. Install [Python](https://www.python.org/downloads/) 3.10 or newer.
   On Windows, tick **"Add python.exe to PATH"** during installation.
2. In VS Code, install the **Python** extension (by Microsoft).
3. Download this repository: click the green **Code** button above, then
   **Download ZIP**, and unzip it. (Or use `git clone` if you know Git.)
4. In VS Code: **File > Open Folder**, and choose the unzipped folder.
5. Open the terminal (**Terminal > New Terminal**) and run:

   ```
   pip install -r requirements.txt
   ```

   This takes a few minutes the first time.

## Running a program

Open a file, for example `01_quantum_coin.py`, and press the **Run** button
(the triangle at the top right of VS Code).

- Text results appear in the terminal at the bottom.
- Charts and pictures open in separate windows. **Close each window to continue
  the program.**

## Common problems

- **`pip` is not recognized:** try `python -m pip install -r requirements.txt`
- **`No module named qiskit`:** VS Code may be using a different Python.
  Press `Ctrl+Shift+P`, choose **Python: Select Interpreter**, and pick the one
  you installed packages into. Then run `pip install -r requirements.txt` again.

## Keep learning

- [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning): free courses, from basics to advanced
- [Qiskit documentation](https://docs.quantum.ibm.com/)

---
Made by Farhana Zahra for the FAST IBM Qiskit workshop.
