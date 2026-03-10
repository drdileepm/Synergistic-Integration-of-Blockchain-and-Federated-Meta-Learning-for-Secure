from rdkit import Chem
import random

def generate_molecule():
    smiles_examples = [
        "CCO",
        "CCN",
        "CCC",
        "C1=CC=CC=C1"
    ]
    return random.choice(smiles_examples)

if __name__ == "__main__":
    print("Generated molecules:")
    for i in range(10):
        print(generate_molecule())
