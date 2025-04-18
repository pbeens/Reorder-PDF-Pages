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

### 1. Install `pipx` (if not already installed)

**macOS (via Homebrew):**
```bash
brew install pipx
pipx ensurepath

Windows (via Python):

python -m pip install --user pipx
python -m pipx ensurepath

Restart your terminal afterward.

2. Install uv using pipx

pipx install uv

3. Set up the environment and install dependencies

uv venv
uv pip install PyPDF2

⚡ Usage

Option A: Interactive Mode

uv venv run python reorder_pdf.py

You will be prompted:

Enter the full path of the scanned PDF file:

Drag the PDF into the terminal window (macOS or Windows), then press Enter.

Output:

A new file will be saved in the same folder with _reordered added to its name:

Original:  /Users/peter/Downloads/Report.pdf
Reordered: /Users/peter/Downloads/Report_reordered.pdf
```

🤔 How It Works

If a PDF is scanned odd-pages first (1, 3, 5…) followed by even-pages (2, 4, 6…), the pages appear out of order.

This script:
	1.	Splits the document into odd and even halves
	2.	Reverses the even half (if needed)
	3.	Interleaves odd and even pages: 1,2,3,4,5,6…

It also handles files with an odd total number of pages.

⸻

✉ License

MIT License. No warranties. Use at your own risk.

