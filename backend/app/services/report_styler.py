from datetime import datetime
from fpdf import FPDF

class AlphaReport(FPDF):
    """Premium dark-header institutional PDF report."""

    def safe_text(self, text: str) -> str:
        """Strips non-ASCII characters that cause FPDF crashes with standard fonts."""
        if not text: return ""
        try:
            return text.encode("latin-1", "ignore").decode("latin-1")
        except Exception:
            return text.encode("ascii", "ignore").decode("ascii")

    def header(self):
        # Dark header band
        self.set_fill_color(30, 30, 35)
        self.rect(0, 0, 210, 32, "F")
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(255, 255, 255)
        self.set_y(7)
        self.cell(0, 10, "ASSET MANDATE ALPHA", align="L")
        self.set_font("Helvetica", "", 8)
        self.set_text_color(160, 160, 170)
        date_str = f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        self.cell(0, 10, self.safe_text(date_str), align="R")
        self.ln(9)
        self.set_font("Helvetica", "I", 9)
        self.cell(0, 5, "Institutional Portfolio Alpha Core | Intelligence Generated Financial Report", align="L")
        self.ln(14)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(150, 150, 150)
        footer_text = f"MMAM Intelligence Core | Page {self.page_no()} | ALPHA-9 Node"
        self.cell(0, 10, self.safe_text(footer_text), align="C")

    def section_title(self, title: str):
        self.ln(4)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(44, 62, 80)
        safe_title = self.safe_text(title)
        self.cell(0, 8, safe_title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(52, 152, 219)
        self.set_line_width(0.6)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def metric_card(self, label: str, value: str, x: float, y: float, w: float = 60):
        self.set_xy(x, y)
        self.set_fill_color(248, 249, 250)
        self.rect(x, y, w, 18, "F")
        self.set_fill_color(52, 152, 219)
        self.rect(x, y, 2, 18, "F")
        self.set_xy(x + 4, y + 2)
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(127, 140, 141)
        self.cell(w - 6, 5, self.safe_text(label.upper()))
        self.set_xy(x + 4, y + 8)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(26, 26, 26)
        self.cell(w - 6, 8, self.safe_text(value))

    def long_text_box(self, content: str):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(44, 62, 80)
        safe_content = self.safe_text(content)
        self.multi_cell(0, 5, safe_content)
        self.ln(2)
