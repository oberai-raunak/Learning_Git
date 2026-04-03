# Just a placeholder for the model that will be trained. In a real application, this would contain the definition of the model architecture and any related functions.
from sklearn.linear_model import LogisticRegression
import os
env = os.getenv("ENV", "dev")

def run_model(sample=True):
    
    print("Model simulation running...")
    return True

if __name__ == "__main__":
    print(f"Running in {env} environment")
    run_model()


