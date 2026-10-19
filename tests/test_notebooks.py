import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"
NOTEBOOKS = ("restaurant_feature_engineering.ipynb", "restaurant_review_analysis.ipynb")


def test_notebooks_are_valid_and_outputs_are_cleared() -> None:
    for name in NOTEBOOKS:
        notebook = json.loads((NOTEBOOK_DIR / name).read_text(encoding="utf-8"))
        assert notebook["cells"]
        assert any(cell["cell_type"] == "code" for cell in notebook["cells"])
        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                assert cell.get("outputs", []) == []
                assert cell.get("execution_count") is None


def test_notebooks_use_a_consistent_dataset_path() -> None:
    for name in NOTEBOOKS:
        source = (NOTEBOOK_DIR / name).read_text(encoding="utf-8")
        assert "data/restaurants.csv" in source
        assert "resturent.csv" not in source
        assert "%pip install" not in source
