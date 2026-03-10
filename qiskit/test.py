from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

'''qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
 
sampler = StatevectorSampler()
result = sampler.run([qc], shots=1024).result()
print(result[0].data.meas.get_counts())'''

# Save credentials (run once)
QiskitRuntimeService.save_account(
    channel="ibm_cloud",
    token="zPVa7RiFVwgj7k7CjR-GzCo2qEXHTS4SekUSyt1tSMIV",
    overwrite=True
)

# Load service and select backend
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)
print(f"Using backend: {backend.name}")

# Your circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Run on real quantum hardware
sampler = SamplerV2(backend)
job = sampler.run([qc], shots=1024)
print(f"Job ID: {job.job_id()}")

result = job.result()
print(result[0].data.meas.get_counts())
