import sys
import os
import click
import subprocess
import fitz

# Try to import pymupdf4llm for standard digital PDFs
try:
    import pymupdf4llm
except ImportError:
    pymupdf4llm = None

@click.command()
@click.argument("pdf_path", type=click.Path(exists=True))
@click.option("--output-dir", "-o", type=click.Path(), default=".", help="Directory to save the markdown and images.")
@click.option("--no-images", is_flag=True, help="Disable image extraction.")
@click.option("--force-ocr", is_flag=True, help="Force Deep Learning OCR (Marker) instead of lightweight digital extraction.")
def main(pdf_path, output_dir, no_images, force_ocr):
    """
    QUANT KNOWLEDGE BASE EXTRACTOR
    
    Extracts text, tables, and mathematically formatted elements from PDFs 
    into clean Markdown for AI Agent consumption.
    """
    click.echo(f"🔄 Processing: {pdf_path}")
    
    # -------------------------------------------------------------
    # 1. Check if the PDF is scanned (No digital text)
    # -------------------------------------------------------------
    is_scanned = False
    try:
        doc = fitz.open(pdf_path)
        text_length = 0
        pages_to_check = min(10, len(doc))
        for i in range(pages_to_check):
            text_length += len(doc[i].get_text("text").strip())
        
        if text_length < 50:  # If the first 10 pages have almost no text
            is_scanned = True
            click.secho(
                f"\n⚠️  WARNING: '{os.path.basename(pdf_path)}' appears to be a SCANNED document (images only).", 
                fg='yellow', bold=True
            )
            click.echo("The tool will automatically switch to Deep Learning OCR (Marker-PDF) to extract the equations and text.\n")
    except Exception as e:
        pass

    # -------------------------------------------------------------
    # 2. Extract Data
    # -------------------------------------------------------------
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    md_file_path = os.path.join(output_dir, f"{base_name}.md")
    images_dir = os.path.join(output_dir, f"{base_name}_assets")

    if force_ocr or is_scanned:
        # Use Marker-PDF for OCR
        click.secho("🧠 Initializing Local Vision OCR (Marker-PDF)... This will use your local CPU/GPU.", fg='cyan')
        try:
            # Resolve marker_single relative to THIS Python executable (always inside the venv/Scripts)
            scripts_dir = os.path.dirname(sys.executable)
            marker_exe = os.path.join(scripts_dir, "marker_single.exe")
            if not os.path.exists(marker_exe):
                marker_exe = os.path.join(scripts_dir, "marker_single")  # non-Windows fallback

            if not os.path.exists(marker_exe):
                click.secho("❌ 'marker_single' not found inside the current venv Scripts folder.", fg='red')
                sys.exit(1)

            cmd = [marker_exe, pdf_path, "--output_dir", output_dir]
            subprocess.run(cmd, check=True)
            click.secho(f"✅ Success [OCR Mode]! Knowledge base markdown saved to: {output_dir}", fg='green')
        except subprocess.CalledProcessError as e:
            click.secho(f"❌ Error during OCR extraction: {e}", fg='red')
            sys.exit(1)

    else:
        # Use PyMuPDF4LLM for fast digital extraction
        if pymupdf4llm is None:
            click.secho("❌ 'pymupdf4llm' not found.", fg='red')
            sys.exit(1)
            
        if not no_images:
            os.makedirs(images_dir, exist_ok=True)
            click.echo(f"📸 Image extraction enabled. Assets will be saved to: {images_dir}")

        try:
            md_text = pymupdf4llm.to_markdown(
                doc=pdf_path,
                write_images=not no_images,
                image_path=images_dir,
                image_format="png"
            )
            with open(md_file_path, "w", encoding="utf-8") as f:
                f.write(md_text)
            click.secho(f"✅ Success [Digital Mode]! Knowledge base markdown saved to: {md_file_path}", fg='green')
        except Exception as e:
            click.secho(f"❌ Error during extraction: {e}", fg='red')
            sys.exit(1)

if __name__ == "__main__":
    main()
