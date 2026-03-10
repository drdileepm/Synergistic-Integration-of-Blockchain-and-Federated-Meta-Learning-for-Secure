#!/bin/bash

echo "Step 1: Preprocess dataset"
python preprocess_dataset.py

echo "Step 2: Train model"
python train_model.py

echo "Step 3: Generate molecules"
python generate_molecules.py

echo "Step 4: Evaluate results"
python evaluate_results.py
