# Reorder PDF Pages

A command-line tool to fix PDFs scanned one-sided at a time (e.g., all odd pages, then all even pages) so that they are reordered into proper sequential order.

This script is compatible with **macOS** and **Windows** and supports **drag-and-drop input** on both systems.

## ✨ Features

- Interleaves odd and even scanned pages into correct order
- Preserves original PDF folder location
- Supports drag-and-drop file paths
- Cross-platform: macOS ☑ Windows ☑
- Uses fast, isolated Python environments via [`uv`](https://github.com/astral-sh/uv)

## 🚀 Installation

### 1. Install **uv** globally *(one‑time)*

**macOS (via Homebrew):**
```bash
python3 -m pip install --user uv
```
**Windows (via Python):**
```
py -m pip install --user uv
```

Restart your terminal afterward.

### 2. Create a project‑local virtual environment and install dependencies
```
uv venv .venv                 # creates .venv in the repo root
uv pip install PyPDF2         # super‑fast resolver & installer
# (or: uv pip install -r requirements.txt when you add one)
```
### 3. Run the tool
```
uv venv run python reorder_pdf.py
```

`uv venv run …` executes the command inside the virtual environment, so you never have to activate/deactivate manually.
When prompted, drag the scanned PDF into the terminal and press Enter

### 🤔 How It Works

If a PDF is scanned odd-pages first (1, 3, 5…) followed by even-pages (2, 4, 6…), the pages appear out of order.

This script:
	1.	Splits the document into odd and even halves
	2.	Reverses the even half (if needed)
	3.	Interleaves odd and even pages: 1,2,3,4,5,6…

It also handles files with an odd total number of pages.

⸻

✉ License

MIT License. No warranties. Use at your own risk.

