<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>

<h1 align="center">⚛️ Computational Physics Laboratory</h1>
<h3 align="center">
Numerical Methods, Linear Algebra & Scientific Computing — UNIMIB 2025/2026
</h3>

<p align="center">
  <b>A hands-on journey through fundamental numerical algorithms, built from scratch and applied to real physics problems.</b><br>
  <i>3rd Year BSc Physics — University of Milano-Bicocca (UNIMIB)</i>
</p>

---

## 📋 Table of Contents

* [🎯 Overview](#-overview)
* [📂 Repository Structure](#-repository-structure)
* [🧪 The Lessons](#-the-lessons)
* [🧰 The LINALG Library](#-the-linalg-library)
* [🛠 Installation & Requirements](#-installation--requirements)
* [▶️ How to Use](#️-how-to-use)
* [🖼 Gallery](#-gallery)
* [👤 About](#-about)

---

## 🎯 Overview

This repository is a comprehensive collection of computational physics exercises developed during the **Computational Laboratory course** at UNIMIB.

Rather than treating libraries as black boxes, every algorithm is **built from first principles** to understand:

* underlying mathematics
* numerical stability
* convergence properties

From summing infinite series with controlled floating-point error to computing quantum eigenstates in a potential well, each lesson bridges **theoretical physics** with **practical numerical implementation**.

> **Core philosophy:** *Master the algorithm, then optimize it.*

---

## 📂 Repository Structure

```bash
Computational-Lab/
├── 📁 lezione_1/          # Floating-point arithmetic & harmonic series
├── 📁 lezione_2/          # LU decomposition & Poisson equation
├── 📁 lezione_3/          # QR decomposition
├── 📁 lezione_4/          # Eigenvalue QR algorithm & Laplacian operator
├── 📁 lezione_5/          # Interpolation, Runge effect & Splines
├── 📁 lezione_6/          # Least-squares data fitting
├── 📁 lezione_7/          # Root finding & orbital mechanics
├── 📁 lezione_8/          # Newton method, Mandelbrot & quantum wells
├── 📁 lezione_9/          # Hermite polynomials & companion matrix
├── 📁 linalg/             # Custom linear algebra library
└── README.md
```

---

## 🧪 The Lessons

### Lezione 1 — Floating-Point Arithmetic & Series Convergence

* Basel problem in single vs double precision
* Forward vs reverse summation
* Error analysis and convergence plots

👉 **Takeaway:** Order of operations strongly affects numerical error.

---

### Lezione 2 — LU Decomposition & Poisson Equation

* LU with partial pivoting
* Linear system solvers
* Discretized 2D Poisson equation

👉 **Takeaway:** Matrix factorization is the backbone of numerical PDE solving.

---

### Lezione 3 — QR Decomposition

* Classical vs Modified Gram-Schmidt
* Orthogonal factorization
* Least-squares applications

👉 **Takeaway:** Orthogonality = numerical stability.

---

### Lezione 4 — Eigenvalues via QR & Laplacian

* QR algorithm with shifts
* Discrete Laplacian operator
* Eigenvalue spectrum analysis

👉 **Takeaway:** Iterative methods reveal spectral structure.

---

### Lezione 5 — Interpolation & Runge Phenomenon

* Polynomial interpolation
* Runge instability
* Cubic splines (natural & clamped)

👉 **Takeaway:** Splines outperform high-degree polynomials.

---

### Lezione 6 — Algorithmic Data Fitting

* Linear least squares
* Covariance matrices
* χ² and reduced χ²

👉 **Takeaway:** Fitting = statistical inference, not just curve drawing.

---

### Lezione 7 — Root Finding & Orbits

* Bisection & regula falsi
* Kepler equation solution
* Orbital mechanics applications

👉 **Takeaway:** Robustness vs speed trade-off.

---

### Lezione 8 — Newton Method & Fractals

* Newton-Raphson method
* Mandelbrot & Newton fractals
* Quantum potential wells

👉 **Takeaway:** Fast convergence but highly sensitive.

---

### Lezione 9 — Hermite Polynomials & Companion Matrix

* Recursive construction
* Companion matrix eigenvalues
* Root-finding via linear algebra

👉 **Takeaway:** Polynomial roots = eigenvalues.

---

## 🧰 The LINALG Library

Custom-built educational linear algebra toolkit:

| Component          | Description                       |
| ------------------ | --------------------------------- |
| Matrix Class       | Object-oriented matrix operations |
| LU Decomposition   | With pivoting                     |
| QR Decomposition   | Gram-Schmidt variants             |
| Eigenvalue Solvers | QR, power & inverse iteration     |
| Linear Solvers     | Triangular & direct systems       |
| Utilities          | Norms, condition numbers          |

> Built to understand complexity ($O(n^3)$), stability, and structure.

---

## 🛠 Installation & Requirements

```bash
git clone https://github.com/Livio2004/Computational-Lab.git
cd Computational-Lab

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install numpy scipy matplotlib jupyter
```

### Dependencies

* numpy
* scipy
* matplotlib
* jupyter

---

## ▶️ How to Use

Each lesson folder contains:

* 📓 Jupyter notebooks
* 🐍 Python scripts
* 📊 Plots & outputs

Run:

```bash
cd lezione_8
jupyter notebook
```

Notebook structure:

1. Theory
2. Implementation
3. Validation
4. Physics application
5. Visualization


---

## 👤 About

**Author:** Livio
**Institution:** University of Milano-Bicocca
**Course:** Computational Physics Laboratory
**Year:** 2025/2026

This repository reflects a clear philosophy:

> Understand the mathematics → implement the algorithm → validate with physics → visualize the result.

---

<p align="center">
<i>Interested in numerical physics or scientific computing? Feel free to reach out!</i>
</p>

