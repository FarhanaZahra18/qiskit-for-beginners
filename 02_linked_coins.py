"""
02 - Linked Coins (Entanglement)
================================

What if two coins were linked, so that whenever you looked at them they
ALWAYS landed the same way: both 0 or both 1, but never different?

With qubits this is real. It is called ENTANGLEMENT, and it is one of the
things that makes quantum computers special.

In this program you will:
  1. Build two entangled qubits
  2. See that they always agree
  3. See what happens on a noisy (realistic) quantum computer

How to run: press the Run button in VS Code (top right).
Pictures open in separate windows. Close each window to continue.
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

simulator = AerSimulator()


def run(circuit, shots=1000, sim=simulator):
    """Run a circuit on a simulator and count how often each result appears."""
    job = sim.run(transpile(circuit, sim), shots=shots)
    return job.result().get_counts()


# ---------------------------------------------------------------------------
# Step 1: Build the linked coins
# ---------------------------------------------------------------------------
# h(0)      -> spin qubit 0 (50/50)
# cx(0, 1)  -> the CNOT gate: "if qubit 0 is 1, flip qubit 1".
#              This links the two qubits together.
# Then we measure both qubits.

linked = QuantumCircuit(2, 2)
linked.h(0)
linked.cx(0, 1)
linked.measure([0, 1], [0, 1])

print("Step 1: The linked coins circuit")
print("The dot on q_0 joined to the circle on q_1 is the CNOT gate.\n")
print(linked)


# ---------------------------------------------------------------------------
# Step 2: Look at the results
# ---------------------------------------------------------------------------

counts = run(linked)
print("\nStep 2: Results:", counts)
print("Only 00 and 11 appear. The two coins always match, even though each")
print("one on its own is completely random. That is entanglement.")
plot_histogram(counts, title="Linked coins, 1000 runs")
plt.show()


# ---------------------------------------------------------------------------
# Step 3: What about a real quantum computer?
# ---------------------------------------------------------------------------
# Real quantum computers are NOISY: tiny errors creep in from heat,
# vibrations and imperfect hardware. Qiskit has "fake devices" that copy
# the noise of real IBM machines, so we can see this without access to one.

noisy_simulator = AerSimulator.from_backend(FakeManilaV2())
noisy_counts = run(linked, sim=noisy_simulator)

print("\nStep 3: Perfect simulator:", counts)
print("        Noisy device:     ", noisy_counts)
print("On the noisy device, a few 01 and 10 results sneak in, even though")
print("our circuit is correct. Making quantum computers reliable is hard.")
plot_histogram([counts, noisy_counts],
               legend=["Perfect simulator", "Noisy device"],
               title="Perfect vs noisy")
plt.show()


# ---------------------------------------------------------------------------
# TRY IT YOURSELF: three linked coins
# ---------------------------------------------------------------------------
# The circuit below is half done. Add ONE line where marked so that the
# results are only 000 and 111.
# Hint: you need one more CNOT, from qubit 1 to qubit 2.
# (The answer is at the very bottom of this file.)

three = QuantumCircuit(3, 3)
three.h(0)
three.cx(0, 1)
# add one line here

three.measure([0, 1, 2], [0, 1, 2])

print("\nTry it yourself - three coins:", run(three))
print("Goal: only 000 and 111.")


# WHAT YOU LEARNED
#   - Entanglement links qubits so their results are connected
#   - The CNOT gate (cx) is the tool that links them
#   - Real quantum hardware is noisy, so even correct programs show
#     some wrong results
#
# Next: 03_spot_the_bug.py
#
#
#
#
#
# ANSWER (try it yourself first!):
#   three.cx(1, 2)
