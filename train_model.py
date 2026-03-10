import torch
from models.ghdo_model import GHDOModel

def train():
    model = GHDOModel()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

    for epoch in range(50):
        loss = model.train_step()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch}: Loss = {loss.item()}")

    torch.save(model.state_dict(), "models/ghdo_model.pt")
    print("Training complete. Model saved.")

if __name__ == "__main__":
    train()
