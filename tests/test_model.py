
from src import run_model

def test_model_runs():
    result = run_model()
    assert result == True
