# Matrix Inversion

## Orthogonal Matrices
For orthogonal matrices, the inverse equals the transpose:
```
A⁻¹ = Aᵀ
```

### Proof
An orthogonal matrix satisfies: A·Aᵀ = I

Multiply both sides by A⁻¹ on the left:
A⁻¹·A·Aᵀ = A⁻¹·I
I·Aᵀ = A⁻¹
Aᵀ = A⁻¹

### Example
```
A = [cos(θ)  -sin(θ)]  (rotation matrix)
    [sin(θ)   cos(θ)]

Aᵀ = [cos(θ)   sin(θ)]
     [-sin(θ)  cos(θ)]

Verify A·Aᵀ = I:
A·Aᵀ = [cos(θ)  -sin(θ)] · [cos(θ)   sin(θ)]
       [sin(θ)   cos(θ)]   [-sin(θ)  cos(θ)]

     = [cos²(θ)+sin²(θ)    cos(θ)sin(θ)-sin(θ)cos(θ)]
       [sin(θ)cos(θ)-cos(θ)sin(θ)    sin²(θ)+cos²(θ)]

     = [1  0] = I  ✓
       [0  1]

Note: The identity matrix I has 1s on the main diagonal and 0s elsewhere.
      It's the "do nothing" matrix: A·I = I·A = A

Therefore: A⁻¹ = Aᵀ
```

## Non-Orthogonal Matrices

### Determinant
The determinant is a scalar value that indicates if a matrix is invertible (det(A) ≠ 0).

#### The Pattern: Cofactor Expansion
1. Pick any row or column
2. For each element:
   - Multiply it by the determinant of the smaller matrix (remove that element's row & column)
   - Alternate signs: +, -, +, -, ...
3. Sum all terms

For 2×2 matrix:
```
det([a b]) = ad - bc
    [c d]
```

For 3×3 matrix:
```
det([a b c]) = a(ei-fh) - b(di-fg) + c(dh-eg)
    [d e f]
    [g h i]
```

For n×n matrices: Use cofactor expansion along any row or column.

For 4×4 matrix, expand along first row:
```
det([a b c d]) = a·det([f g h]) - b·det([e g h]) + c·det([e f h]) - d·det([e f g])
    [e f g h]        [j k l]        [i k l]        [i j l]        [i j k]
    [i j k l]        [n o p]        [m o p]        [m n p]        [m n o]
    [m n o p]
```

#### Example: 4×4 Determinant
```
A = [2  1  0  3]  ← We'll expand along row 1
    [1  0  2  1]
    [0  1  1  2]
    [1  2  0  1]

Step 1: For each element in row 1, cross out its row and column:

Element 2 (position 1,1):     Element 1 (position 1,2):     Element 0 (position 1,3):     Element 3 (position 1,4):
[X  X  X  X]                  [X  X  X  X]                  [X  X  X  X]                  [X  X  X  X]
[X  0  2  1]                  [1  X  2  1]                  [1  0  X  1]                  [1  0  2  X]
[X  1  1  2]                  [0  X  1  2]                  [0  1  X  2]                  [0  1  1  X]
[X  2  0  1]                  [1  X  0  1]                  [1  2  X  1]                  [1  2  0  X]

Remaining 3×3:               Remaining 3×3:               Skip (element is 0)          Remaining 3×3:
[0  2  1]                     [1  2  1]                                                   [1  0  2]
[1  1  2]                     [0  1  2]                                                   [0  1  1]
[2  0  1]                     [1  0  1]                                                   [1  2  0]

Step 2: Apply alternating signs (+, -, +, -):
det(A) = (+2)·det([0 2 1]) + (-1)·det([1 2 1]) + (+0)·det([...]) + (-3)·det([1 0 2])
              [1 1 2]             [0 1 2]                                [0 1 1]
              [2 0 1]             [1 0 1]                                [1 2 0]

Step 3: Calculate each 3×3 determinant (using same pattern):

For det([0 2 1])  ← expand along row 1 with signs: +, -, +
       [1 1 2]
       [2 0 1]
= (+0)·det([1 2]) + (-2)·det([1 2]) + (+1)·det([1 1])
         [0 1]           [2 1]           [2 0]
= 0(1-0) - 2(1-4) + 1(0-2)
= 0 + 6 - 2 = 4

For det([1 2 1])  ← expand along row 1 with signs: +, -, +
       [0 1 2]
       [1 0 1]
= (+1)·det([1 2]) + (-2)·det([0 2]) + (+1)·det([0 1])
         [0 1]           [1 1]           [1 0]
= 1(1-0) - 2(0-2) + 1(0-1)
= 1 + 4 - 1 = 4

For det([1 0 2])  ← expand along row 1 with signs: +, -, +
       [0 1 1]
       [1 2 0]
= (+1)·det([1 1]) + (-0)·det([0 1]) + (+2)·det([0 1])
         [2 0]           [1 0]           [1 2]
= 1(0-2) - 0 + 2(0-1)
= -2 + 0 - 2 = -4

Substitute back:
det(A) = 2(4) - 1(4) + 0 - 3(-4)
       = 8 - 4 + 0 + 12
       = 16
```

### Inverse Calculation Methods

#### 1. Gaussian Elimination
Augment A with identity matrix [A|I], then row reduce to [I|A⁻¹]

#### 2. Adjugate Method
```
A⁻¹ = (1/det(A)) × adj(A)
```
where adj(A) is the adjugate (transpose of cofactor matrix)


