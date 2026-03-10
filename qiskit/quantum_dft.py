from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFTGate
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
import numpy as np

def classical_dft(x):
    """Classical DFT implementation"""
    N = len(x)
    X = np.zeros(N, dtype=complex)
    
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    
    return X


def quantum_dft_hardware(x, backend, shots=8192):
    """Quantum DFT on real hardware using measurements"""
    N = len(x)
    n_qubits = int(np.log2(N))
    
    assert N == 2**n_qubits, "Input length must be power of 2"
    
    # Create circuit
    qc = QuantumCircuit(n_qubits)
    
    # Normalize input
    x_norm = x / np.linalg.norm(x)
    
    # Initialize with amplitudes
    qc.initialize(x_norm, range(n_qubits))
    
    # Apply QFT
    qc.append(QFTGate(n_qubits), range(n_qubits))
    
    # Measure all qubits
    qc.measure_all()
    
    # Transpile for hardware
    qc_transpiled = transpile(qc, backend=backend, optimization_level=3)
    
    # Run on hardware
    sampler = SamplerV2(backend)
    job = sampler.run([qc_transpiled], shots=shots)
    print(f"Job ID: {job.job_id()}")
    
    result = job.result()
    counts = result[0].data.meas.get_counts()
    
    # Reconstruct probability distribution
    probs = np.zeros(N)
    for bitstring, count in counts.items():
        idx = int(bitstring, 2)
        probs[idx] = count / shots
    
    return probs


# Example usage
if __name__ == "__main__":
    # Load service and select backend
    service = QiskitRuntimeService()
    backend = service.least_busy(operational=True, simulator=False)
    print(f"Using backend: {backend.name}\n")
    
    # Test signal (must be power of 2)
    N = 4  # Using 4 instead of 8 (fewer qubits for real hardware)
    t = np.arange(N)
    signal = np.sin(2 * np.pi * 1 * t / N)
    
    print("Input signal:", signal)
    
    # Classical DFT (manual)
    X_manual = classical_dft(signal)
    
    # Classical DFT (NumPy)
    X_numpy = np.fft.fft(signal)
    
    # Quantum DFT on hardware
    probs_quantum = quantum_dft_hardware(signal, backend, shots=4096)
    
    print("\nManual DFT magnitudes:", np.abs(X_manual))
    print("NumPy FFT magnitudes: ", np.abs(X_numpy))
    print("Quantum probabilities:", probs_quantum)
    print("\nNote: Quantum hardware measures probability distribution, not complex amplitudes")
