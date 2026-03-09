# Unitary Matrices

## What is a Conjugate?

### Complex Conjugate
For a complex number z = a + bi, the complex conjugate is:
```
z* = a - bi
```
Simply flip the sign of the imaginary part.

**Examples:**
```
(3 + 4i)* = 3 - 4i
(2 - 5i)* = 2 + 5i
(7 + 0i)* = 7 - 0i = 7  (real numbers are their own conjugate)
```

## Conjugate Transpose (Hermitian Transpose)

For a matrix, the conjugate transpose (denoted U† or U*):
1. **Transpose** the matrix (swap rows and columns)
2. Take the **complex conjugate** of each element

**Example:**
```
U = [1+2i    3-i ]
    [4i      5   ]

Step 1 - Transpose:
Uᵀ = [1+2i   4i ]
     [3-i    5  ]

Step 2 - Complex conjugate each element:
U† = [1-2i   -4i]
     [3+i    5  ]
```

## Unitary Matrices

A unitary matrix is the complex version of an orthogonal matrix.

**Definition:** U is unitary if U·U† = I

**Key property:** U⁻¹ = U† (inverse equals conjugate transpose)

### Full Example: Hadamard Gate

```
H = [1/√2    1/√2 ]
    [1/√2   -1/√2 ]

Step 1 - Find conjugate transpose H†:
Since H has only real numbers, H† = Hᵀ

Hᵀ = [1/√2    1/√2 ]
     [1/√2   -1/√2 ]

So H† = H (Hadamard is self-adjoint)

Step 2 - Verify H·H† = I:
H·H† = [1/√2    1/√2 ] · [1/√2    1/√2 ]
       [1/√2   -1/√2 ]   [1/√2   -1/√2 ]

Row 1, Col 1: (1/√2)(1/√2) + (1/√2)(1/√2) = 1/2 + 1/2 = 1
Row 1, Col 2: (1/√2)(1/√2) + (1/√2)(-1/√2) = 1/2 - 1/2 = 0
Row 2, Col 1: (1/√2)(1/√2) + (-1/√2)(1/√2) = 1/2 - 1/2 = 0
Row 2, Col 2: (1/√2)(1/√2) + (-1/√2)(-1/√2) = 1/2 + 1/2 = 1

H·H† = [1  0] = I  ✓
       [0  1]

Therefore: H⁻¹ = H†
```

### Example with Complex Numbers: Phase Gate

```
S = [1   0 ]
    [0   i ]

Step 1 - Find conjugate transpose S†:
Transpose:
Sᵀ = [1   0]
     [0   i]

Complex conjugate:
S† = [1   0 ]
     [0  -i ]

Step 2 - Verify S·S† = I:
S·S† = [1   0] · [1   0 ]
       [0   i]   [0  -i ]

     = [1·1 + 0·0      1·0 + 0·(-i)]
       [0·1 + i·0      0·0 + i·(-i)]

     = [1    0  ]
       [0   -i² ]

     = [1   0] = I  ✓  (since i² = -1, so -i² = 1)
       [0   1]

Therefore: S⁻¹ = S†
```

## Why Unitary Matrices in Quantum Computing?

- **Preserve probability**: Total probability always equals 1
- **Reversible**: Every quantum operation can be undone
- **Physical requirement**: All valid quantum gates must be unitary
