"""
03 - Spot the Bug
=================

Quantum programs can go wrong in surprising ways, and they are tricky to
check because the answers are random. Each program below has a bug, or
LOOKS like it does.

For each one:
  1. Read the goal
  2. Run the program and look at the result
  3. Try to find and fix the problem
  4. Check the answers at the bottom of this file only when you are ready

Do 01_quantum_coin.py and 02_linked_coins.py first.

How to run: press the Run button in VS Code (top right).
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

simulator = AerSimulator()


def run(circuit, shots=1000):
    """Run a circuit on the simulator and count how often each result appears."""
    job = simulator.run(transpile(circuit, simulator), shots=shots)
    return job.result().get_counts()


# ===========================================================================
# BUG 1: Where did the answer go?
# Goal: flip a quantum coin 100 times and count the results.
# ===========================================================================
print("BUG 1: Where did the answer go?")

coin1 = QuantumCircuit(1, 1)
coin1.h(0)

try:
    print("Result:", run(coin1, shots=100))
except Exception as error:
    print("ERROR:", error)
    print("Hint: compare this circuit with the one in 01_quantum_coin.py.")
    print("      Which step is missing?")


# ===========================================================================
# BUG 2: The coins don't match
# Goal: two linked coins that always land the same (only 00 and 11),
#       just like in 02_linked_coins.py.
# ===========================================================================
print("\nBUG 2: The coins don't match")

linked = QuantumCircuit(2, 2)
linked.h(1)
linked.cx(0, 1)
linked.measure([0, 1], [0, 1])

print("Result:", run(linked))
print("We wanted only 00 and 11. Here is the circuit:")
print(linked)
print("Hint: the CNOT says 'if qubit 0 is 1, flip qubit 1'.")
print("      Which qubit is spinning before the CNOT?")


# ===========================================================================
# BUG 3: Backwards?
# Goal: flip ONLY qubit 0 to 1.
# A student expected to see 10 (qubit 0 written first).
# ===========================================================================
print("\nBUG 3: Backwards?")

flip = QuantumCircuit(2, 2)
flip.x(0)
flip.measure([0, 1], [0, 1])

print("Result:", run(flip))
print("We got 01, not 10. Is the code wrong?")


# ===========================================================================
# BUG 4: Is my coin broken?
# Goal: check that the quantum coin is fair (about 50/50).
# ===========================================================================
print("\nBUG 4: Is my coin broken?")

coin4 = QuantumCircuit(1, 1)
coin4.h(0)
coin4.measure(0, 0)

print("Result:", run(coin4, shots=6))
print("Run this program a few times. Sometimes the coin looks fair,")
print("sometimes very unfair. Is something wrong with it?")


# WHAT YOU LEARNED
#   - Forgetting to measure means there is no answer to read
#   - A gate on the wrong qubit can give a wrong result with NO error message
#   - Qiskit results are read from right to left
#   - Random programs need many shots before you can judge them
#
# Testing quantum programs is still an open research problem.
# Maybe you will help solve it.
#
# Next (bonus): 04_quantum_dice.py
#
#
#
#
#
#
#
#
#
#
# ===========================================================================
# ANSWERS (scroll down only when you are ready)
# ===========================================================================
#
#
#
#
#
#
#
#
#
#
# BUG 1: We never MEASURED the qubit, so there is nothing to count.
#        Add  coin1.measure(0, 0)  after  coin1.h(0).
#
# BUG 2: The H gate is on the wrong qubit. It should be  linked.h(0).
#        Qubit 0 never spins, so the CNOT never fires, and qubit 1 just
#        flips randomly on its own. The program runs without errors but
#        does the wrong thing. These are the sneakiest bugs.
#
# BUG 3: The code is correct. Qiskit writes results RIGHT TO LEFT:
#        the rightmost digit is qubit 0. So 01 means qubit 1 = 0 and
#        qubit 0 = 1, which is exactly what we wanted.
#        This trips up almost every beginner.
#
# BUG 4: The coin is fine. 6 shots is far too few to judge randomness.
#        Change shots=6 to shots=1000 and the 50/50 pattern becomes clear.
#        For quantum programs, we test the pattern over many runs,
#        never a single run.
