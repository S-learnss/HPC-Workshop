from qiskit import transpile
from qiskit.circuit.library import quantum_volume
from qiskit_aer import *
import time
import numpy as np
import matplotlib.pyplot as plt

def quant_vol(qubits=15, depth=10, shots=1):
    sim = AerSimulator(method='statevector', device='CPU')
    circuit = quantum_volume(qubits, depth, seed=0)
    circuit.measure_all()
    circuit = transpile(circuit, sim)
    start = time.time()
    result = sim.run(circuit, shots=shots, seed_simulator=12345).result()
    time_val = time.time() - start
    return time_val

num_qubits = np.arange(2, 10)
qv_depth = 5
num_shots = 10

results_array = []

for i in num_qubits:
    result = quant_vol(qubits=i, depth=qv_depth, shots=num_shots)
    results_array.append(result)
    print(f"Qubits: {i}, Time: {result}")

plt.xlabel('Number of qubits')
plt.ylabel('Time (sec)')
plt.plot(num_qubits, results_array)
plt.title('Quantum Volume Experiment with depth=' + str(qv_depth))
plt.savefig('qv_experiment.png')

