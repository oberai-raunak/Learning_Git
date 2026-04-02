from src import run_pipeline

def test_pipeline_runs():
    result = run_pipeline()
    assert result == True