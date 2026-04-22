<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>

<h1 align="center">⚛️ Computational Physics Laboratory</h1>
<h3 align="center">Numerical Methods, Linear Algebra & Scientific Computing — UNIMIB 2025/2026</h3>

<p align="center">
  <b>A hands-on journey through fundamental numerical algorithms, built from scratch and applied to real physics problems.</b><br>
  <i>3rd Year BSc Physics — University of Milano-Bicocca (UNIMIB)</i>
</p>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [The Lessons](#-the-lessons)
  - [Lezione 1 — Floating-Point Arithmetic & Series Convergence](#lezione-1--floating-point-arithmetic--series-convergence)
  - [Lezione 2 — LU Decomposition & Poisson Equation](#lezione-2--lu-decomposition--poisson-equation)
  - [Lezione 3 — QR Decomposition](#lezione-3--qr-decomposition)
  - [Lezione 4 — Eigenvalues via QR & The Laplacian](#lezione-4--eigenvalues-via-qr--the-laplacian)
  - [Lezione 5 — Interpolation, Runge Phenomenon & Splines](#lezione-5--interpolation-runge-phenomenon--splines)
  - [Lezione 6 — Algorithmic Data Fitting](#lezione-6--algorithmic-data-fitting)
  - [Lezione 7 — Root Finding & Elliptical Orbits](#lezione-7--root-finding--elliptical-orbits)
  - [Lezione 8 — Newton's Method, Mandelbrot Fractals & Potential Wells](#lezione-8--newtons-method-mandelbrot-fractals--potential-wells)
  - [Lezione 9 — Hermite Polynomials & Companion Matrix](#lezione-9--hermite-polynomials--companion-matrix)
- [The LINALG Library](#-the-linalg-library)
- [Installation & Requirements](#-installation--requirements)
- [How to Use](#-how-to-use)
- [About](#-about)

---

## 🎯 Overview

This repository is a comprehensive collection of computational physics exercises developed during the **Computational Laboratory course** at UNIMIB. Rather than treating libraries as black boxes, every algorithm is **built from first principles** to understand the underlying mathematics, numerical stability, and convergence properties.

From summing infinite series with controlled floating-point error to computing quantum eigenstates in a potential well, each lesson bridges **theoretical physics** with **practical numerical implementation**.

> **Core philosophy:** *Master the algorithm, then optimize it.*

---

## 📂 Repository Structure
Computational-Lab/
├── 📁 lezione_1/          # Floating-point arithmetic & harmonic series
├── 📁 lezione_2/          # LU decomposition & Poisson equation
├── 📁 lezione_3/          # QR decomposition
├── 📁 lezione_4/          # Eigenvalue QR algorithm & Laplacian operator
├── 📁 lezione_5/          # Interpolation, Runge effect & Splines
├── 📁 lezione_6/          # Algorithmic least-squares data fitting
├── 📁 lezione_7/          # Root finding: bisection, regula falsi & orbital mechanics
├── 📁 lezione_8/          # Newton-Raphson, Mandelbrot fractals & quantum wells
├── 📁 lezione_9/          # Hermite polynomials & companion matrix eigenvalues
├── 📁 linalg/             # Custom linear algebra library (functions & classes)
└── README.md
plain

Copy

---

## 🧪 The Lessons

### Lezione 1 — Floating-Point Arithmetic & Series Convergence
**Topic:** Numerical stability in finite-precision arithmetic.  
**What I did:**
- Computed the Basel problem series $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$ in **single** and **double precision**.
- Compared **normal ordering** ($1 \to N$) vs. **reverse ordering** ($N \to 1$) to study catastrophic cancellation and accumulation of round-off error.
- Plotted the absolute error $|S(N) - \pi^2/6|$ as a function of $N$ to visualize convergence rates and precision limits.

**Key takeaway:** The order of operations matters. Summing small terms first minimizes floating-point error.

---

### Lezione 2 — LU Decomposition & Poisson Equation
**Topic:** Direct solvers for linear systems and PDE discretization.  
**What I did:**
- Implemented **LU decomposition with partial pivoting** from scratch to factorize matrices into lower and upper triangular forms.
- Applied forward/backward substitution to solve linear systems efficiently.
- Discretized the **2D Poisson equation** $\nabla^2 \phi = \rho$ on a grid and solved the resulting sparse linear system using the custom LU solver.

**Key takeaway:** Understanding matrix factorization is essential before calling `scipy.linalg.solve`.

---

### Lezione 3 — QR Decomposition
**Topic:** Orthogonal factorization for stable linear algebra.  
**What I did:**
- Implemented **QR decomposition** using classical and modified Gram-Schmidt orthogonalization.
- Used the QR factorization to solve overdetermined systems and as a foundation for eigenvalue algorithms.
- Compared numerical stability of different orthogonalization approaches.

**Key takeaway:** Orthogonal matrices preserve numerical stability; Gram-Schmidt variants differ significantly in rounding error.

---

### Lezione 4 — Eigenvalues via QR & The Laplacian
**Topic:** Spectral methods and iterative eigenvalue solvers.  
**What I did:**
- Built the **QR algorithm with shifts** to compute the full spectrum of a matrix iteratively.
- Constructed the discrete **Laplacian operator** matrix on a 1D/2D domain.
- Computed eigenvalues and eigenfunctions of the Laplacian, connecting numerical linear algebra to quantum mechanical boundary value problems.

**Key takeaway:** The QR algorithm transforms a matrix into Schur form, revealing its spectral properties through iteration.

---

### Lezione 5 — Interpolation, Runge Phenomenon & Splines
**Topic:** Function approximation and polynomial interpolation pitfalls.  
**What I did:**
- Implemented **polynomial interpolation** using the **Vandermonde matrix** and Lagrange basis.
- Demonstrated the **Runge phenomenon** — oscillatory divergence of high-degree polynomial interpolation at equispaced nodes.
- Built **cubic splines** (natural and clamped) to achieve smooth, piecewise interpolation without Runge artifacts.

**Key takeaway:** More points $\neq$ better approximation. Splines provide controlled smoothness where global polynomials fail.

---

### Lezione 6 — Algorithmic Data Fitting
**Topic:** Linear regression and least-squares optimization.  
**What I did:**
- Implemented **linear least-squares fitting** algorithmically using the Normal Equations.
- Computed covariance matrices, parameter uncertainties, and goodness-of-fit metrics ($\chi^2$, reduced $\chi^2$).
- Propagated errors from data to fitted parameters using Jacobian analysis.

**Key takeaway:** Fitting is not just drawing a line — it's a statistical inference problem with quantifiable uncertainty.

---

### Lezione 7 — Root Finding & Elliptical Orbits
**Topic:** Bracketing methods and celestial mechanics.  
**What I did:**
- Implemented **bisection method** and **regula falsi (false position)** for robust root finding in 1D.
- Solved **Kepler's equation** $M = E - e\sin E$ for the eccentric anomaly $E$ of an elliptical planetary orbit.
- Compared convergence rates and reliability of bracketing methods across different eccentricities.

**Key takeaway:** Bracketing methods guarantee convergence but sacrifice speed; they are indispensable for robust physics solvers.

---

### Lezione 8 — Newton's Method, Mandelbrot Fractals & Potential Wells
**Topic:** Newton-Raphson iteration, complex dynamics, and quantum mechanics.  
**What I did:**
- Implemented **Newton-Raphson method** for rapid root convergence (quadratic near simple roots).
- Generated the **Mandelbrot set** and **Newton fractals** by iterating complex maps, visualizing basins of attraction.
- Applied Newton's method to find **bound states (even and odd)** in a finite quantum potential well by matching wavefunction logarithmic derivatives.

**Key takeaway:** Newton's method is powerful but sensitive to initial guesses; its complex dynamics produce stunning fractal structures.

---

### Lezione 9 — Hermite Polynomials & Companion Matrix
**Topic:** Spectral methods for orthogonal polynomials.  
**What I did:**
- Constructed **Hermite polynomials** recursively and evaluated their properties.
- Built the **companion matrix** of a Hermite polynomial and computed its eigenvalues to find the polynomial roots with high precision.
- Connected orthogonal polynomial theory to linear algebra eigenproblems.

**Key takeaway:** The roots of a polynomial are the eigenvalues of its companion matrix — a beautiful bridge between algebra and spectral theory.

---

## 🧰 The LINALG Library

Every lesson relies on a **custom linear algebra library** (`linalg/`) developed alongside the exercises. It is not a wrapper around NumPy/SciPy — it is a pedagogical toolkit containing the core implementations:

| Component | Description |
|-----------|-------------|
| **Matrix Class** | Object-oriented matrix with overloaded operators |
| **LU Decomposition** | With partial pivoting, forward/backward substitution |
| **QR Decomposition** | Gram-Schmidt (classical & modified) |
| **Eigenvalue Solvers** | QR algorithm, power iteration, inverse iteration |
| **Linear Solvers** | Direct and triangular system solvers |
| **Utility Functions** | Norms, condition numbers, matrix generators |

> **Why build our own?** To understand the $O(n^3)$ complexity, numerical stability, and memory layout before trusting external libraries.

---

## 🛠 Installation & Requirements

```bash
# Clone the repository
git clone https://github.com/Livio2004/Computational-Lab.git
cd Computational-Lab

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install numpy scipy matplotlib jupyter
Dependencies

numpy — array manipulation and numerical utilities
scipy — benchmarks and special functions (used for comparison, not as black boxes)
matplotlib — publication-quality plots, fractals, and convergence graphs
jupyter — interactive exploration and visualization
▶️ How to Use

Each lezione_* folder is self-contained and includes:
Jupyter notebooks (.ipynb) with theory, derivation, and live code
Python scripts (.py) for standalone execution
Generated plots and data outputs
Navigate to any lesson and launch Jupyter:
bash

Copy
cd lezione_8
jupyter notebook
Every notebook follows this structure:
Theoretical Background — Mathematical derivation of the method
From-Scratch Implementation — Step-by-step algorithm coding
Validation — Comparison with analytical solutions or library functions
Physics Application — Real-world problem (orbits, quantum wells, PDEs)
Visualization — Plots, fractals, convergence curves, and error analysis
🖼 Gallery

Add your best plots here!
Suggested images to include in an assets/ folder:
<p align="center">
  <img src="./assets/runge_phenomenon.png" width="45%" alt="Runge phenomenon vs cubic splines" />
  <img src="./assets/newton_fractal.png" width="45%" alt="Newton fractal basins of attraction" />
</p>
<p align="center">
  <img src="./assets/poisson_solution.png" width="45%" alt="2D Poisson equation solution" />
  <img src="./assets/potential_well_states.png" width="45%" alt="Even and odd states in a quantum well" />
</p>
(Create an assets/ folder and save your favorite plots from the notebooks!)
👤 About

Author: Livio
Institution: University of Milano-Bicocca (UNIMIB)
Course: Computational Physics Laboratory — 3rd Year BSc Physics
Academic Year: 2025/2026
This repository represents my approach to scientific computing: understand the mathematics, implement the algorithm, validate against physics, and visualize the result. Every line of code was written to learn why numerical methods work, not just how to call them.
<p align="center">
  <i>Interested in numerical physics, scientific computing, or just want to chat about fractals? Feel free to reach out!</i>
</p>
```
