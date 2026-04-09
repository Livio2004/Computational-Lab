# ⚛️ Computational Physics Laboratory (UNIMIB 2025/2026)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Data%20Analysis-green.svg)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Scientific%20Computing-orange.svg)](https://scipy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **A comprehensive collection of computational physics algorithms, statistical data analysis, and numerical methods developed during the 3rd-year Computational Laboratory at the University of Milano-Bicocca (UNIMIB).**

## 🎯 Overview
This repository serves as a portfolio of advanced numerical problem-solving. Rather than simply calling black-box library functions, these exercises focus on **building fundamental algorithms from scratch**, understanding their mathematical foundations, and exploring numerical stability in physical simulations.

All assignments and code documentation are provided in English to ensure accessibility for the broader scientific community.

## 🧠 Key Competencies & Algorithms

### 1. Advanced Statistical Data Analysis
* **Least Squares Fitting:** Implementation of generalized linear and non-linear regression models.
* **Error Propagation:** Rigorous calculation of covariance matrices, Jacobian transformations, and parameter uncertainties.
* **Confidence Bands:** Derivation of $1\sigma$ and $2\sigma$ confidence intervals using both exact analytical propagation and **Monte Carlo** simulations.
* **Non-Linear Models:** Fitting of complex physical distributions (e.g., Breit-Wigner resonances) handling correlated data arrays.

### 2. Numerical Linear Algebra (From Scratch)
* **Cholesky Decomposition:** Custom algorithm built without `scipy` to securely invert ill-conditioned covariance matrices and solve standard Normal Equations.
* **Forward/Backward Substitution:** Efficient solving of triangular systems, avoiding computationally expensive matrix inversions.

### 3. Advanced Theoretical Topics
* **Random Matrix Theory (RMT):** Explorations into the statistical properties of eigenvalues in complex systems.
* **Euclidean Matrices:** Analysis of distance-dependent stochastic matrices bridging geometry and linear algebra.

## 📂 Repository Structure

```text
├── 01_Linear_Fitting_and_Cholesky/    # From-scratch implementations of algebraic fitting
├── 02_NonLinear_Models/               # SciPy optimization, Jacobians, and Breit-Wigner fits
├── 03_MonteCarlo_Simulations/         # Stochastic error propagation and confidence bands
├── 04_Random_Matrix_Theory/           # RMT fundamentals and Euclidean distances
└── README.md
