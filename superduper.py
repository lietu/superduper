import hashlib
import sys
from pathlib import Path

# https://docs.python.org/3/library/hashlib.html#hash-algorithms
HASH_ALGO = "sha256"

Hashes = dict[str, list[str]]


def _scan_recursive(hashes: Hashes, path: Path):
    print(f"Scanning {path.absolute()}")

    # Loop through contents
    try:
        for child in path.iterdir():
            if child.is_file():
                try:
                    with child.open(mode="rb") as f:
                        # Get file hash
                        hash_ = hashlib.file_digest(f, HASH_ALGO).hexdigest()
                        if hash_ not in hashes:
                            hashes[hash_] = []
                        hashes[hash_].append(str(child.absolute()))
                except IOError as e:
                    print(e)
            elif child.is_dir():
                _scan_recursive(hashes, child)
    except IOError as e:
        print(e)


def scan(start_path: Path):
    hashes: Hashes = {}
    _scan_recursive(hashes, start_path)
    print("")
    print("")
    print("Results:")
    print("")
    dupes = []
    for hash_ in hashes:
        count = len(hashes[hash_])
        if count > 1:
            dupes.append(f"{count} dupes for {hash_}: {' '.join(hashes[hash_])}")
    print(f"Found {len(hashes)} unique files")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Incorrect arguments.")
        sys.exit(1)

    start_path = sys.argv[1] if len(sys.argv) == 2 else "."
    scan(Path(start_path))
