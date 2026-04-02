from src import run_features

def test_features_runs():
    result = run_features()
    assert result == True
