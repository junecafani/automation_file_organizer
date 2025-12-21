# Automation File Organizer

A Python-based CLI tool for scanning folders and safely renaming files using a controlled **dry-run → confirm** workflow.

This project focuses on **automation fundamentals**, clear execution flow, and safety-first file operations.

---

## Version
**v1.0**

---

## Purpose

This tool was built to:
- Practice real-world Python automation
- Learn safe file operations
- Build a CLI-driven workflow
- Avoid accidental destructive actions using preview-first logic

---

## Features

- Scan folder contents (files & subfolders)
- Detect file vs folder
- Display file sizes with automatic unit conversion (KB, MB, GB)
- Count files and subfolders recursively
- Command-line interface (CLI)
- Bulk file rename with **dry-run** and **confirm** modes
- Clear execution flow and validation

---

## Requirements

- Python 3.9+
- Standard library only (no external dependencies)

---

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd automation_file_organizer
```

## Project Structure
automation_file_organizer/
│
├── main.py # Entry point (CLI)
├── README.md
│
├── organizer/
│ ├── init.py
│ └── core.py # Core logic (scan, rename, utils)
│
└── tests/
├── sample_files/
└── secretary kim/

## CLI Arguments

| Argument | Required | Description |
|--------|---------|------------|
| `--path` | ✅ | Target folder path |
| `--mode` | ❌ | Operation mode (`scan` / `rename`) |
| `--dry-run` | ❌ | Preview rename without changing files |
| `--confirm` | ❌ | Apply rename (REAL change) |

---

## Usage

### 1️⃣ Scan folder (default mode)

Showing folders and size

```bash
python main.py --path tests/sample_files
```

## Example Output

```bash
[FILE] example.txt || 12.4 KB
[FOLDER] downloads || 2 folders || 5 files
```
## Usage

This tool is executed via command line using Python.

Basic format:

```bash
python main.py --path <target_folder> [--mode scan|rename] [--dry-run | --confirm]
```

## Scan Mode (Default)

Scan mode lists files and folders inside the target directory and displays basic information.

```bash
python main.py --path tests/sample_files
```

## Example output:

```bash
[FILE] example.txt || 12.4 KB
[FOLDER] downloads || 2 folders || 5 files
```
Notes:
- This is the default mode.
- No files are modified.
- Safe to run anytime.

## Rename Mode

Rename mode is used for bulk renaming files.
It requires explicit flags to prevent accidental changes.

### Dry Run (Preview Only – Safe)

Shows what would be renamed without changing anything.

```bash
python main.py --path "tests/secretary kim" --mode rename --dry-run
```

Example output:
```bash
[INFO] Dry-run mode enabled
[DRY-RUN] video1.mp4 -> secretary-kim_1.mp4
[DRY-RUN] video2.mp4 -> secretary-kim_2.mp4
```
Nothing is modified in this mode.

## Confirm (Apply Rename – Real Execution)
This will actually rename files.
```bash
python main.py --path "tests/secretary kim" --mode rename --confirm
```

Example output: 
```bash
[INFO] Confirm mode enabled
[OK] Rename applied
```
Only files are renamed. Folders are skipped.

## CLI Arguments
| Argument | Required | Description |
|--------|----------|-------------|
| `--path` | Yes | Target folder path |
| `--mode` | No | Operation mode: `scan` (default) or `rename` |
| `--dry-run` | No | Preview rename without modifying files |
| `--confirm` | No | Apply rename changes |

## Rename Rules
Only files are renamed (folders are ignored)

Rename format:
```bash
secretary-kim_1.ext
secretary-kim_2.ext
secretary-kim_3.ext
```
File order follows os.listdir()

## Notes
- Rename mode will not run without --dry-run or --confirm
- Invalid paths cause immediate exit
- Empty folders are handled safely
- Dry-run is always recommended before confirm