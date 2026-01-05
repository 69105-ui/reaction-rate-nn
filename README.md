# Predicting Reaction Rates with Neural Networks:  
## A Study on When Machine Learning Does *Not* Add Scientific Value

**Author:** Muhammad Sarim Nawaz  
**Institution:** Cadet College Hasanabdal  

---

## Overview

This project explores the use of a neural network to predict chemical reaction rates using synthetic data generated from the Arrhenius equation. Rather than positioning machine learning as a superior alternative, the goal of this study is to **critically evaluate whether machine learning is justified when the governing physical law is already known**.

The project intentionally uses a well-understood kinetic model to test the limits, redundancy, and interpretability trade-offs of neural networks in scientific modeling.

---

## Motivation

Machine learning is increasingly applied to scientific problems where strong theoretical models already exist. While neural networks can approximate complex functions, their use is not always epistemically or practically justified.

This project asks a simple but often ignored question:

> **What does machine learning actually add when the underlying relationship is already known, interpretable, and analytically solvable?**

---

## Methodology

### Data Generation
- Synthetic reaction rate data generated using the Arrhenius equation  
- Parameters sampled across realistic temperature and activation energy ranges  
- No experimental data used (deliberate design choice)

### Models Compared
1. **Classical Arrhenius-based regression**
2. **Feedforward neural network**
   - Trained on the same synthetic dataset
   - Optimized for mean squared error

### Evaluation
- Prediction accuracy on interpolated data
- Extrapolation behavior outside the training range
- Qualitative comparison of interpretability and scientific usefulness

---

## Key Findings

- The neural network successfully learns the Arrhenius relationship **but does not outperform classical regression in accuracy or generalization**.
- The NN acts as a *black-box approximator* of a known equation rather than a source of new insight.
- Extrapolation performance of the neural network is unreliable compared to the physics-based model.
- Interpretability is significantly reduced when replacing an explicit equation with a neural network.

---

## Interpretation

This project demonstrates that **technical capability alone is not sufficient justification for using machine learning in scientific contexts**.

When:
- the governing law is known,
- the model is interpretable,
- and extrapolation is required,

classical approaches remain superior.

The neural network, in this setting, adds computational complexity without adding epistemic value.

---

## Why This Project Matters

Rather than showcasing machine learning as a novelty, this work emphasizes:
- Scientific restraint
- Model selection judgment
- Critical evaluation of ML applicability

These considerations are central to responsible scientific and engineering practice, particularly as machine learning becomes increasingly accessible.

---

## Limitations

- Synthetic data only; no experimental noise modeled
- Single-reaction system
- Neural network architecture kept intentionally simple

These limitations are **acknowledged rather than obscured**, as the objective is methodological evaluation, not performance maximization.

---

## Future Directions

- Introducing experimental noise to test robustness
- Evaluating transfer learning across multiple reaction systems
- Studying cases where Arrhenius assumptions break down

---

## Conclusion

This project serves as a controlled case study illustrating that **machine learning should be applied selectively, not reflexively**. Its value lies not in outperforming established models, but in clarifying *when* such models should remain the default.

---

## Repository Contents

- `data/` — Synthetic datasets generated from Arrhenius equation  
- `models/` — Neural network implementation  
- `notebooks/` — Training, evaluation, and comparison analyses  
- `README.md` — Project overview and interpretation  



