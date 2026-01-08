# Predicting Reaction Rates with Neural Networks  
## A Study on When Machine Learning Does Not Add Scientific Value

**Author:** Muhammad Sarim Nawaz  
**Institution:** Cadet College Hasanabdal  

---

## Overview

This project investigates the use of a neural network to predict chemical reaction rate constants using synthetic data generated from the Arrhenius equation. Rather than positioning machine learning as a superior alternative, the objective is to critically evaluate whether machine learning adds scientific or epistemic value when the governing physical law is already known, interpretable, and analytically solvable.

The project is designed as a methodological case study examining redundancy, interpretability loss, and extrapolation behavior when a black-box model is applied to a system governed by established theory.

---

## Motivation

Machine learning is increasingly applied to scientific problems where strong theoretical models already exist. While neural networks are powerful function approximators, their application is not always epistemically or practically justified.

This project addresses a fundamental question:

**What does machine learning actually add when the underlying relationship is known, interpretable, and grounded in physical theory?**

Rather than assuming value, this work evaluates machine learning against classical methods under controlled conditions.

---

## Methodology

### Data Generation

- Synthetic reaction rate data generated using the Arrhenius equation:

  \[
  k = A e^{-E_a / RT}
  \]

- Parameters sampled across physically realistic temperature and activation energy ranges  
- No experimental data used (deliberate design choice)

Synthetic data ensures that the true functional relationship is known, allowing direct evaluation of whether the neural network recovers structure rather than noise.

---

### Models Compared

#### Physics-Based Model
- Classical Arrhenius model
- Parameters \(A\) and \(E_a\) estimated via nonlinear least squares
- Trained on the same dataset as the neural network

#### Neural Network
- Feedforward neural network
- Inputs: Temperature (T), Activation Energy (Ea), Pre-exponential factor (A)
- Output: Reaction rate constant (k)
- Architecture:
  - 2 hidden layers
  - 32 units per layer
  - ReLU activations
  - ~2,000 trainable parameters
- Optimized using mean squared error loss

No physical equations or constraints were explicitly encoded in the neural network.

---

## Evaluation Criteria

Models were evaluated on:

- Prediction accuracy on interpolated data  
- Extrapolation behavior outside the training temperature range  
- Qualitative comparison of interpretability and scientific usefulness  

Key plots and comparisons are provided in:
- `notebooks/training_comparison.ipynb`
- `notebooks/extrapolation_analysis.ipynb`

---

## Key Findings

- The neural network successfully approximates the Arrhenius relationship within the training domain.
- Prediction accuracy does not exceed that of the physics-based model.
- Extrapolation performance of the neural network is unstable compared to the Arrhenius model (see extrapolation plots).
- Interpretability is significantly reduced when replacing an explicit equation with a black-box model.

These results indicate that the neural network acts primarily as a function approximator of a known law rather than a source of new scientific insight.

---

## Interpretation

This project demonstrates that technical capability alone does not justify the use of machine learning in scientific modeling.

When:
- the governing law is known,
- the model is interpretable,
- and extrapolation beyond observed data is required,

classical physics-based approaches remain superior.

In this context, the neural network adds computational complexity without adding explanatory or epistemic value.

---

## Why This Project Matters

Rather than showcasing machine learning as a novelty, this work emphasizes:

- Scientific restraint  
- Model selection judgment  
- Critical evaluation of ML applicability  

These considerations are essential for responsible scientific practice, particularly as machine learning tools become increasingly accessible.

---

## Limitations

- Synthetic data only; experimental noise not modeled  
- Single-reaction system  
- Neural network architecture intentionally kept simple  

These limitations are acknowledged explicitly, as the goal is methodological evaluation rather than performance maximization.

---

## Future Directions

- Introduce controlled experimental noise to assess robustness  
- Evaluate transfer learning across multiple reaction systems  
- Study regimes where Arrhenius assumptions break down  

Such extensions would help identify conditions under which machine learning may offer genuine advantages.

---

## Conclusion

This project serves as a controlled case study illustrating that machine learning should be applied selectively rather than reflexively. Its value lies not in outperforming established models, but in clarifying when those models should remain the default. The scientific contribution is therefore methodological: identifying the boundary between useful approximation and unnecessary complexity.

---

## Repository Structure

- `data/` — Synthetic datasets generated from the Arrhenius equation  
- `models/` — Neural network implementation  
- `notebooks/` — Training, evaluation, and extrapolation analyses  
- `README.md` — Project overview and interpretation  



