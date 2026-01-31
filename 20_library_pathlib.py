"""
Portfolio: pathlib and file system
Topic: Path, listdir, exists, read_text, write_text
"""

from pathlib import Path


def main():
    print("=== pathlib Demo ===\n")

    # Current directory
    cwd = Path.cwd()
    print("  Path.cwd():", cwd)

    # Join paths
    p = cwd / "some_folder" / "file.txt"
    print("  cwd / 'some_folder' / 'file.txt':", p)

    # Check existence
    print("  p.exists():", p.exists())
    print("  cwd.exists():", cwd.exists())

    # List Python files in current dir
    print("\n--- Python files in current dir ---")
    for f in sorted(Path.cwd().glob("*.py"))[:5]:
        print("  ", f.name)
    print("  ...")

    # Read/write text (if we create a temp file)
    demo = Path("pathlib_demo_temp.txt")
    demo.write_text("Hello from pathlib\n", encoding="utf-8")
    print("\n  Written pathlib_demo_temp.txt")
    content = demo.read_text(encoding="utf-8")
    print("  Read back:", repr(content.strip()))
    demo.unlink()
    print("  Deleted temp file.")


if __name__ == "__main__":
    main()
