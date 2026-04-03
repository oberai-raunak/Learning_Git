from src import build_features

def test_features_runs():
    result = build_features()
    assert result == True
