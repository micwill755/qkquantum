# Quantum Gates

## What are Quantum Gates?

Quantum gates are operations that manipulate qubits (quantum bits). They are the building blocks of quantum circuits.

**Key differences from classical gates:**
- Classical: operate on bits (0 or 1)
- Quantum: operate on qubits (superposition of |0⟩ and |1⟩)
- All quantum gates are **unitary matrices** (reversible)

## Qubit Representation

A qubit state is a vector:
```
|ψ⟩ = α|0⟩ + β|1⟩

In vector form:
|0⟩ = [1]    |1⟩ = [0]
      [0]          [1]

General state:
|ψ⟩ = [α]
      [β]

where |α|² + |β|² = 1 (probability constraint)
```

## How Gates Work

Apply gate U to state |ψ⟩:
```
|ψ'⟩ = U|ψ⟩  (matrix-vector multiplication)
```

## Single-Qubit Gates

### 1. Pauli-X Gate (Quantum NOT)

```
X = [0  1]
    [1  0]
```

**Effect:** Flips |0⟩ ↔ |1⟩

**Examples:**
```
X|0⟩ = [0  1] · [1] = [0] = |1⟩
       [1  0]   [0]   [1]

X|1⟩ = [0  1] · [0] = [1] = |0⟩
       [1  0]   [1]   [0]

X on superposition:
|ψ⟩ = (|0⟩ + |1⟩)/√2 = [1/√2]
                        [1/√2]

X|ψ⟩ = [0  1] · [1/√2] = [1/√2] = (|1⟩ + |0⟩)/√2
       [1  0]   [1/√2]   [1/√2]
```

### 2. Pauli-Y Gate

```
Y = [0  -i]
    [i   0]
```

**Effect:** Flips and adds phase

**Examples:**
```
Y|0⟩ = [0  -i] · [1] = [ 0] = i|1⟩
       [i   0]   [0]   [ i]

Y|1⟩ = [0  -i] · [0] = [-i] = -i|0⟩
       [i   0]   [1]   [ 0]
```

### 3. Pauli-Z Gate (Phase Flip)

```
Z = [1   0]
    [0  -1]
```

**Effect:** Leaves |0⟩ unchanged, flips sign of |1⟩

**Examples:**
```
Z|0⟩ = [1   0] · [1] = [1] = |0⟩
       [0  -1]   [0]   [0]

Z|1⟩ = [1   0] · [0] = [ 0] = -|1⟩
       [0  -1]   [1]   [-1]

Z on superposition:
|ψ⟩ = (|0⟩ + |1⟩)/√2 = [1/√2]
                        [1/√2]

Z|ψ⟩ = [1   0] · [1/√2] = [ 1/√2] = (|0⟩ - |1⟩)/√2
       [0  -1]   [1/√2]   [-1/√2]
```

### 4. Hadamard Gate (H)

```
H = [1/√2    1/√2 ]
    [1/√2   -1/√2 ]
```

**Effect:** Creates superposition from basis states

**Examples:**
```
H|0⟩ = [1/√2    1/√2 ] · [1] = [1/√2] = (|0⟩ + |1⟩)/√2
       [1/√2   -1/√2 ]   [0]   [1/√2]

H|1⟩ = [1/√2    1/√2 ] · [0] = [ 1/√2] = (|0⟩ - |1⟩)/√2
       [1/√2   -1/√2 ]   [1]   [-1/√2]

H on superposition (H is self-inverse):
|ψ⟩ = (|0⟩ + |1⟩)/√2

H|ψ⟩ = H·H|0⟩ = |0⟩  (applying H twice returns to original)
```

### 5. Phase Gate (S)

```
S = [1   0]
    [0   i]
```

**Effect:** Adds 90° phase to |1⟩

**Examples:**
```
S|0⟩ = [1   0] · [1] = [1] = |0⟩
       [0   i]   [0]   [0]

S|1⟩ = [1   0] · [0] = [0] = i|1⟩
       [0   i]   [1]   [i]
```

### 6. T Gate (π/8 Gate)

```
T = [1   0        ]
    [0   e^(iπ/4) ]
```

**Effect:** Adds 45° phase to |1⟩

**Example:**
```
T|1⟩ = [1   0        ] · [0] = [    0     ] = e^(iπ/4)|1⟩
       [0   e^(iπ/4) ]   [1]   [e^(iπ/4) ]
```

## Gate Properties

### Reversibility
All quantum gates are reversible:
```
U·U† = I
U⁻¹ = U†
```

### Self-Inverse Gates
Some gates are their own inverse:
```
X·X = I  (X² = I)
Y·Y = I  (Y² = I)
Z·Z = I  (Z² = I)
H·H = I  (H² = I)
```

### Gate Composition
Gates can be combined by matrix multiplication:
```
Apply X then H:
H·X|0⟩ = H|1⟩ = (|0⟩ - |1⟩)/√2
```

## Visualization Summary

```
|0⟩ ─X─ → |1⟩
|1⟩ ─X─ → |0⟩

|0⟩ ─H─ → (|0⟩ + |1⟩)/√2
|1⟩ ─H─ → (|0⟩ - |1⟩)/√2

|0⟩ ─Z─ → |0⟩
|1⟩ ─Z─ → -|1⟩
```

## Why These Gates Matter

- **X, Y, Z**: Fundamental rotations (Pauli matrices)
- **H**: Creates superposition (essential for quantum algorithms)
- **S, T**: Phase gates (used in quantum error correction)
- **Combinations**: Build complex quantum algorithms
