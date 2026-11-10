"""
01 - The Quantum Coin
=====================

A normal computer stores information in BITS. Each bit is either 0 or 1,
like a coin lying heads or tails.

A quantum computer uses QUBITS. A qubit can be in a mix of 0 and 1 at the
same time. Think of it as a coin that is still spinning in the air. Only
when you look at it (we call this MEASURING) does it land on 0 or 1.

In this program you will:
  1. Build your first quantum circuit
  2. See the qubit as an arrow
  3. Flip a quantum coin 1000 times

How to run: press the Run button in VS Code (top right).
Pictures open in separate windows. Close each window to continue.
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit_aer import AerSimulator

simulator = AerSimulator()


def run(circuit, shots=1000):
    """Run a circuit on the simulator and count how often each result appears."""
    job = simulator.run(transpile(circuit, simulator), shots=shots)
    return job.result().get_counts()


# ---------------------------------------------------------------------------
# Step 1: Build a quantum coin
# ---------------------------------------------------------------------------
# QuantumCircuit(1, 1) -> 1 qubit, plus 1 normal bit to store the answer
# h(0)                 -> the H gate (Hadamard): puts qubit 0 into a 50/50 mix
# measure(0, 0)        -> look at qubit 0 and write the result into bit 0

coin = QuantumCircuit(1, 1)
coin.h(0)
coin.measure(0, 0)

print("Step 1: Our quantum coin circuit")
print("Read it from left to right: the qubit q passes through H, then gets measured.\n")
print(coin)


# ---------------------------------------------------------------------------
# Step 2: See the qubit as an arrow
# ---------------------------------------------------------------------------
# We can draw a qubit as an arrow inside a ball (the "Bloch sphere"):
#   arrow up       = 0
#   arrow down     = 1
#   arrow sideways = a 50/50 mix (the spinning coin)

print("\nStep 2: The qubit as an arrow")
print("First window: a fresh qubit. It always starts at 0, so the arrow points up.")
start = QuantumCircuit(1)
plot_bloch_multivector(Statevector(start), title="A fresh qubit (0)")
plt.show()

print("Second window: after the H gate. The arrow has turned sideways.")
spinning = QuantumCircuit(1)
spinning.h(0)
plot_bloch_multivector(Statevector(spinning), title="After the H gate")
plt.show()


# ---------------------------------------------------------------------------
# Step 3: Flip the coin 1000 times
# ---------------------------------------------------------------------------
# Each run ("shot") measures the qubit once. Because of the H gate,
# every shot is a fair 50/50 coin toss.

counts = run(coin, shots=1000)
print("\nStep 3: Results of 1000 flips:", counts)
print("You should see roughly 500 zeros and 500 ones. Not exactly 500 each,")
print("because the result is truly random.")
plot_histogram(counts, title="Quantum coin, 1000 flips")
plt.show()


# ---------------------------------------------------------------------------
# TRY IT YOURSELF
# ---------------------------------------------------------------------------
# Change this program and run it again:
#   1. In Step 3, change shots=1000 to shots=10. Run it a few times.
#      Does the coin still look fair?
#   2. Delete the line  coin.h(0)  in Step 1. What happens, and why?
#   3. Replace  coin.h(0)  with  coin.x(0)  (the X gate flips 0 to 1).
#      What do you get now?
#
# WHAT YOU LEARNED
#   - A qubit can be in a mix of 0 and 1, like a spinning coin
#   - The H gate creates a 50/50 mix. The X gate flips 0 and 1.
#   - Measuring forces the qubit to pick 0 or 1
#   - Quantum results are random, so we run a circuit many times (shots)
#     and look at the pattern
#
# Next: 02_linked_coins.py
