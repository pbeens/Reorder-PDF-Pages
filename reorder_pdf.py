import os
from PyPDF2 import PdfReader, PdfWriter

def reorder_scanned_pdf(input_path):
    # Validate path
    if not os.path.isfile(input_path):
        print("❌ File does not exist.")
        return

    # Extract base name and folder
    folder = os.path.dirname(input_path)
    base = os.path.basename(input_path)
    name, ext = os.path.splitext(base)

    # Construct output path
    output_path = os.path.join(folder, f"{name}_reordered{ext}")

    # Read the PDF
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    # Divide pages into odd and even
    half = total_pages // 2
    odd_pages = reader.pages[:half]
    even_pages = reader.pages[half:]
    even_pages = list(even_pages)[::-1]  # reverse if scanned in reverse order

    writer = PdfWriter()

    # Interleave
    for i in range(half):
        writer.add_page(odd_pages[i])
        if i < len(even_pages):
            writer.add_page(even_pages[i])

    # Handle last page for odd total
    if total_pages % 2 != 0:
        writer.add_page(reader.pages[-1])

    # Save file
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"✅ Reordered PDF saved to:\n{output_path}")

if __name__ == "__main__":
    input_path = input("Enter the full path of the scanned PDF file: ").strip().strip('"').strip("'")
    reorder_scanned_pdf(input_path)