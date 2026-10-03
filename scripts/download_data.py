import csv
from pathlib import Path
from urllib.request import urlretrieve

BASE_URL = (
    "https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets"
    "/master/banking_data"
)
RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw" / "banking77"
SPLITS = ("train", "test")


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for split in SPLITS:
        path = RAW_DIR / f"{split}.csv"
        urlretrieve(f"{BASE_URL}/{split}.csv", path)

        with path.open(encoding="utf-8", newline="") as f:
            n_rows = sum(1 for _ in csv.DictReader(f))
        print(f"{split}: {n_rows} rows -> {path}")


if __name__ == "__main__":
    main()
