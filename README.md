# Expected Modularity Calculation in Probabilistic Networks

This repository provides the official implementation of the methods presented in the paper **"Fast and Accurate Algorithms to Calculate Expected Modularity in Probabilistic Networks"**.

We introduce two methods for computing the expected modularity of a given community partition in probabilistic networks, where each edge is associated with an existence probability.

- **PWP-EMOD:** An exact method based on the Poisson-binomial distribution.
- **APWP-EMOD:** A computationally efficient approximation using the Discrete Fourier Transform (DFT).

The repository includes algorithm implementations, synthetic network generators, benchmark datasets, and scripts for reproducing the experiments presented in the paper.

## Methods

In a probabilistic network, each edge exists independently with a specified probability. The expected modularity of a community partition is defined as the probability-weighted average of modularity across all possible graph realizations.

Rather than explicitly enumerating all possible worlds, our methods group realizations according to edge counts within, between, and outside communities.

Both methods follow three main steps:

1. Partition possible graph realizations according to their community-related edge counts.
2. Calculate the probabilities of these edge-count configurations using the Poisson-binomial distribution (PWP) or DFT (APWP).
3. Aggregate the corresponding modularity values to obtain the expected modularity.

## Repository Structure

```text
.
├── algorithms/       # PWP, APWP, and baseline implementations
├── generators/       # Synthetic network generation
├── utils/            # Community and graph I/O utilities
├── experiments/      # Experimental scripts corresponding to the paper
├── datasets/         # Benchmark datasets
├── requirements.txt  # Python dependencies
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/XINS3/Expected-modularity-calculation-over-uncertain-graph.git
cd Expected-modularity-calculation-over-uncertain-graph
```

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

The original experiments used Python 3.8.10 and 3.9.13.

### Additional Dependency: DFT_cpp

The APWP implementation uses [DFT_cpp](https://github.com/XINS3/DFT_cpp), a separate C++ extension for computing edge-count probabilities using DFT.

Install it using:

```bash
git clone --recursive https://github.com/XINS3/DFT_cpp.git
python -m pip install ./DFT_cpp
```

See the [DFT_cpp repository](https://github.com/XINS3/DFT_cpp) for build prerequisites and detailed installation instructions.

PWP does not require `DFT_cpp`.

## Quick Start

The following example demonstrates how to calculate the expected modularity of a small uncertain network using PWP and APWP.

Consider an undirected probabilistic graph with four nodes, four possible edges, and two communities.

```python
from algorithms.Algorithms import PWP, APWP

# Edges in the uncertain graph
edges = [(0, 1), (1, 2), (2, 3), (0, 3)]

# Existence probabilities corresponding to each edge
probabilities = [0.8, 0.3, 0.9, 0.2]

# Community partition
communities = [[0, 1], [2, 3]]

# Exact expected modularity
emod_pwp = PWP(edges, probabilities, communities)

# DFT-based approximate expected modularity
emod_apwp = APWP(edges, probabilities, communities)

print(f"PWP-EMOD:  {emod_pwp}")
print(f"APWP-EMOD: {emod_apwp}")
```

**Input parameters:**

| Parameter | Description |
|---|---|
| `edges` | List of possible edges, represented as node pairs |
| `probabilities` | Existence probabilities corresponding to the edges |
| `communities` | Community partition represented as a list of node sets or lists |

Both functions return an expected modularity value for the specified community partition.

For this example, the exact PWP result and approximate APWP result can be compared directly. APWP requires `DFT_cpp` to be installed.

**Note:** The example assumes that the imports in `algorithms/Algorithms.py` have been updated to support the reorganized package structure.

## Reproducing the Experiments

Experimental scripts are provided in `experiments/`, organized according to the sections of the paper.

| Paper Section | Experiment | Script |
|---|---|---|
| 4.1 | Accuracy and execution time | `Accuracy_and_execution_time_4.1.py` |
| 4.1 | Additional accuracy and timing experiments | `Accuracy_and_execution_time_ex2_4.1.py` |
| 4.2.1 | Comparison with weighted graphs | `Comparison_with_weighting_4.2.1.py` |
| 4.2.2 | Comparison with thresholding | `Comparison_with_thresholding_4.2.2.py` |
| 4.2.3 | Comparison with sampling (CCS) | `Comparison_with_sampling_CCS_4.2.3.py` |
| 4.2.3 | Comparison with sampling (LCCS) | `Comparison_with_sampling_LCCS_4.2.3.py` |
| 4.3 | Factors influencing execution time | `Factors_influencing_execution_time_ex1_4.3.py` |
| 4.3 | Additional execution-time experiments | `Factors_influencing_execution_time_ex2_4.3.py` |
| 4.4 | Sampling comparison on real-world datasets | `Comparison_with_sampling_realdatasets_4.4.py` |

For example, to run the comparison with thresholding from the repository root:

```bash
python -m experiments.Comparison_with_thresholding_4.2.2
```

Some scripts require benchmark data stored in `datasets/`. Run them from the repository root and ensure that imports and dataset paths are configured correctly.

## Datasets

The `datasets/` directory contains network data used in the experiments.

Synthetic graph generation utilities are available in `generators/`. The experiments investigate different network configurations and compare expected modularity calculation methods in terms of accuracy and computational performance.

## Citation

If you use this implementation or the experimental results in your research, please cite:

**Fast and Accurate Algorithms to Calculate Expected Modularity in Probabilistic Networks.**

*Full bibliographic details and a BibTeX entry can be added here.*