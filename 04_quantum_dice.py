"""
04 - Quantum Dice
=================

Normal computers cannot create truly random numbers. They follow formulas
that only LOOK random. Measuring a qubit, however, is genuinely random,
guaranteed by the laws of physics.

Let's use that to build a quantum dice that rolls 1 to 6.

How to run: press the Run button in VS Code (top right).
Pictures open in separate windows. Close each window to continue.
"""

from collections import Counter

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

simulator = AerSimulator()


# ---------------------------------------------------------------------------
# How it works
# ---------------------------------------------------------------------------
# 1 qubit gives 2 possible answers (0 or 1).
# 3 qubits give 2 x 2 x 2 = 8 possible answers: 000 to 111,
# which are the numbers 0 to 7 in binary.
# We spin all 3 qubits with H gates and measure ONCE to get a random
# number from 0 to 7.

dice = QuantumCircuit(3, 3)
dice.h([0, 1, 2])
dice.measure([0, 1, 2], [0, 1, 2])

print("The dice circuit:")
print(dice)


def roll_dice():
    """Roll the quantum dice once and return a number from 1 to 6."""
    while True:
        result = simulator.run(transpile(dice, simulator), shots=1, memory=True).result()
        bits = result.get_memory()[0]   # for example "101"
        number = int(bits, 2)           # binary to normal number: "101" -> 5
        # A dice has only 6 sides, but we get 8 possible numbers.
        # If we get 6 or 7, we simply roll again.
        if number < 6:
            return number + 1           # turn 0-5 into 1-6


# ---------------------------------------------------------------------------
# Roll it
# ---------------------------------------------------------------------------
print("\nYou rolled:", roll_dice())
print("Run the program again and you will (probably) get a different number.")


# ---------------------------------------------------------------------------
# Is the dice fair?
# ---------------------------------------------------------------------------
rolls = [roll_dice() for _ in range(600)]
tally = Counter(rolls)

print("\n600 rolls:")
for face in range(1, 7):
    print(f"  {face}: {tally[face]} times")
print("Each face should appear about 100 times.")

plot_histogram({str(face): tally[face] for face in range(1, 7)},
               title="600 quantum dice rolls")
plt.show()


# ---------------------------------------------------------------------------
# TRY IT YOURSELF
# ---------------------------------------------------------------------------
#   1. Make a quantum decider: "Should I study or sleep?"
#      (1 qubit, 1 shot). A starter version is below.
#   2. Make a dice with 8 sides. Hint: no re-rolling needed.
#   3. Make a 16-sided dice. How many qubits do you need?

decider = QuantumCircuit(1, 1)
decider.h(0)
decider.measure(0, 0)

answer = simulator.run(transpile(decider, simulator), shots=1, memory=True).result().get_memory()[0]
print("\nThe quantum decider says:", "Study!" if answer == "0" else "Sleep!")


# WHAT YOU LEARNED
#   - Measuring qubits gives truly random results
#   - n qubits can represent 2^n different numbers
#   - You can build real programs with just H gates and measurement
#
# Want to keep going? IBM Quantum Learning has free courses:
#   https://quantum.cloud.ibm.com/learning
