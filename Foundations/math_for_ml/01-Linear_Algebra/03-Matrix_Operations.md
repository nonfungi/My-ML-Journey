Section 3: Matrix Operations Matrices are the workhorses of machine learning. Here are the most fundamental operations you need to know.

Matrix Transposition The transpose of a matrix, denoted as A T , is an operation that flips the matrix over its main diagonal. In other words, the rows of the original matrix become the columns of the transposed matrix.
Example:

If:

A=​

1 3 5​

2 4 6​

​

Then its transpose is:

A T =[ 1 2​

3 4​

5 6​] 2. Matrix Addition and Scalar Multiplication These operations are straightforward and work element by element, just like with vectors.

Matrix Addition: You can only add two matrices if they have the same dimensions. The addition happens element-wise.

[ a c​

b d​]+[ e g​

f h​]=[ a+e c+g​

b+f d+h​] Scalar Multiplication: You multiply every element of the matrix by a single scalar number.

k⋅[ a c​

b d​]=[ ka kc​

kb kd​] 3. Matrix Multiplication (The Most Important Operation) Matrix multiplication is not element-wise. It's a process of combining two matrices to produce a third. It's the core operation in linear transformations and neural networks.

The Rule: To multiply two matrices A and B (to get C=AB), the number of columns in matrix A must be equal to the number of rows in matrix B.

Calculation: Each element in the resulting matrix C is the dot product of a row from matrix A and a column from matrix B.

Example:

Let:

A=[ 1 3​

2 4​],B=[ 5 7​

6 8​] Then C=AB is calculated as:

C=[ (1⋅5+2⋅7) (3⋅5+4⋅7)​

(1⋅6+2⋅8) (3⋅6+4⋅8)​]=[ 19 43​

22 50​] Critical Property: Matrix multiplication is not commutative. This means that in most cases, AB  =BA. The order matters!

Hadamard Product (Element-wise Product) There is also an element-wise product, which is less common in transformations but used in some ML algorithms. It's denoted by the ⊙ symbol.
Formula:

[ a c​

b d​]⊙[ e g​

f h​]=[ ae cg​

bf dh​] It's important not to confuse this with standard matrix multiplication.

Multiplying a Matrix by Its Transpose A very common and powerful operation in machine learning is multiplying a matrix, A, by its transpose, A T . This results in a square and symmetric matrix.
Calculation: The product A T A is often called the Gram matrix. Its elements are the dot products of the columns of A.

Resulting Matrix Properties:

Square: If A is m×n, then A T A will be n×n.

Symmetric: A matrix M is symmetric if M=M T . The matrix A T A always has this property.

Example:

Using the matrix from the transpose example:

A=​

1 3 5​

2 4 6​

​

The product A T A is:

A T A=[ 1 2​

3 4​

5 6​]​

1 3 5​

2 4 6​

​=[ (1⋅1+3⋅3+5⋅5) (2⋅1+4⋅3+6⋅5)​

(1⋅2+3⋅4+5⋅6) (2⋅2+4⋅4+6⋅6)​]=[ 35 44​

44 56​] Notice that the resulting matrix is symmetric (M 12​=M 21​).

Use in ML:

Principal Component Analysis (PCA): The matrix A T A is used to compute the covariance matrix of the data (after centering). The eigenvectors of this covariance matrix are the principal components.

Linear Regression: It's used to solve the "normal equations," which provide a direct analytical solution for finding the optimal model parameters.