import pandas as pd

def preprocess_dataset(input_file="data/zinc_raw.csv", output_file="data/zinc_processed.csv"):
    try:
        df = pd.read_csv(input_file)
        df = df.dropna()
        df = df.sample(frac=1).reset_index(drop=True)
        df.to_csv(output_file, index=False)
        print("Dataset preprocessing completed.")
    except FileNotFoundError:
        print("Dataset file not found. Please place dataset in data folder.")

if __name__ == "__main__":
    preprocess_dataset()
