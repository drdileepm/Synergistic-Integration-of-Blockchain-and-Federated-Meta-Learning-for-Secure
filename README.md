# GHDO Framework – Geometric Deep Reinforcement Learning for Drug Design

This repository provides a reproducible implementation of the **Geo-Hierarchical Drug Optimiser (GHDO)** framework proposed in the manuscript:

*Geometric Deep Reinforcement Learning with Hierarchical Variational Autoencoders for De Novo Drug Design and Activity Optimization*

## Project Overview

The GHDO framework integrates:

- Multi-Stage Variational Autoencoders (MS-VAE)
- Geometric Soft Actor-Critic reinforcement learning
- Molecular graph generation
- Binding affinity evaluation

This repository contains all required scripts to reproduce the experiments.

## Installation

Install dependencies:

pip install -r requirements.txt

## Running Experiments

1. Dataset preprocessing  
python preprocess_dataset.py

2. Train model  
python train_model.py

3. Generate molecules  
python generate_molecules.py

4. Evaluate results  
python evaluate_results.py

## Datasets

Experiments use public datasets such as **ZINC250k** and **PDBbind**.
