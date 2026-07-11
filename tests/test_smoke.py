from pathlib import Path


def test_course_structure_exists() -> None:
    assert Path("README.md").exists()
    assert Path("docs/FASE-01.md").exists()
    assert Path("docs/FASE-05.md").exists()
    assert Path("src/python/ml_pipeline.py").exists()
