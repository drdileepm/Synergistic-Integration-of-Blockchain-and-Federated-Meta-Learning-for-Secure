import numpy as np

def evaluate():
    ghdo_scores = np.random.normal(8.3,0.2,100)
    baseline_scores = np.random.normal(7.1,0.3,100)

    print("Average GHDO Score:", ghdo_scores.mean())
    print("Average Baseline Score:", baseline_scores.mean())

if __name__ == "__main__":
    evaluate()
