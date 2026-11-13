import os

JOKE = (
    "I asked my AI coding agent to fix a one-character typo. "
    "It refactored 14 files, renamed two functions, and now the typo "
    "is the only line that still compiles."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
