from fpdf import FPDF
from datetime import datetime
import os

class AlphaReport(FPDF):
    """Premium institutional PDF report with advanced styling and distinct variants."""

    def __init__(self, mode="Standard", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = mode # Standard, Intelligence, Risk, Executive
        self.accent_color = (52, 152, 219) # Alpha Blue by default
        
        if mode == "Intelligence":
            self.accent_color = (155, 89, 182) # Purple for Intel
        elif mode == "Risk":
            self.accent_color = (231, 76, 60) # Red for Risk
        elif mode == "Executive":
            self.accent_color = (44, 62, 80) # Dark Navy for Exec

    def safe_text(self, text: str) -> str:
        """Strips non-ASCII characters that cause FPDF crashes."""
        if not text: return ""
        try:
            return text.encode("latin-1", "ignore").decode("latin-1")
        except Exception:
            try:
                return text.encode("ascii", "ignore").decode("ascii")
            except:
                return ""

    def header(self):
        # Premium Header Band
        self.set_fill_color(30, 30, 35)
        self.rect(0, 0, 210, 35, "F")
        
        # Accent side-bar in header
        self.set_fill_color(*self.accent_color)
        self.rect(0, 0, 5, 35, "F")
        
        # Title
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(255, 255, 255)
        self.set_y(8)
        self.set_x(12)
        title_map = {
            "Standard": "ASSET MANDATE ALPHA",
            "Intelligence": "STRATEGIC INTELLIGENCE",
            "Risk": "INSTITUTIONAL RISK AUDIT",
            "Executive": "EXECUTIVE ALPHA BRIEF"
        }
        self.cell(0, 10, title_map.get(self.mode, "ALPHA CORE REPORT"), align="L")
        
        # Meta info
        self.set_font("Helvetica", "", 8)
        self.set_text_color(160, 160, 170)
        date_str = f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        self.set_xy(150, 8)
        self.cell(50, 10, self.safe_text(date_str), align="R")
        
        self.set_xy(12, 18)
        self.set_font("Helvetica", "I", 9)
        subtitle_map = {
            "Standard": "Comprehensive Portfolio Analysis & Quantitative Performance",
            "Intelligence": "Bespoke Neural Insights & Market Sentiment Convergence",
            "Risk": "Deep-Tail Risk Metrics & Algorithmic Hedging Analysis",
            "Executive": "High-Level Strategic Overview for Asset Managers"
        }
        self.cell(0, 5, subtitle_map.get(self.mode, "Institutional Intelligence System"), align="L")
        
        # Page break spacer
        self.set_y(40)

    def footer(self):
        self.set_y(-15)
        # Footer line
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.1)
        self.line(10, self.get_y(), 200, self.get_y())
        
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(140, 140, 140)
        footer_text = f"MMAM Alpha Core | {self.mode.upper()} DEPLOYMENT | Page {self.page_no()}"
        self.cell(0, 10, self.safe_text(footer_text), align="C")
        
        # Confidential tag
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(180, 0, 0)
        self.set_xy(160, self.get_y())
        self.cell(40, 10, "STRICTLY CONFIDENTIAL", align="R")

    def section_title(self, title: str):
        self.ln(6)
        # Section ID dot
        curr_y = self.get_y()
        self.set_fill_color(*self.accent_color)
        self.circle(12, curr_y + 4, 1.5, "F")
        
        self.set_x(16)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(44, 62, 80)
        self.cell(0, 8, self.safe_text(title.upper()), new_x="LMARGIN", new_y="NEXT")
        
        # Clean separator line
        self.set_draw_color(*self.accent_color)
        self.set_line_width(0.8)
        self.line(16, self.get_y(), 200, self.get_y())
        self.ln(4)

    def metric_card(self, label: str, value: str, x: float, y: float, w: float = 62, trend: str = None):
        # Background shadow/glow effect
        self.set_xy(x+0.5, y+0.5)
        self.set_fill_color(230, 230, 235)
        self.rect(x, y, w, 22, "F")
        
        # Main body
        self.set_xy(x, y)
        self.set_fill_color(255, 255, 255)
        self.rect(x, y, w, 22, "F")
        
        # Left Accent Border
        self.set_fill_color(*self.accent_color)
        self.rect(x, y, 2.5, 22, "F")
        
        # Label
        self.set_xy(x + 6, y + 3)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(110, 120, 130)
        self.cell(w - 10, 5, self.safe_text(label.upper()), align="L")
        
        # Value
        self.set_xy(x + 6, y + 10)
        self.set_font("Helvetica", "B", 15)
        self.set_text_color(30, 35, 45)
        self.cell(w - 10, 8, self.safe_text(value), align="L")
        
        # Optional Trend indicator
        if trend:
            self.set_xy(x + w - 15, y + 3)
            is_up = trend.startswith("+")
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(39, 174, 96 if is_up else 192, 57, 43)
            self.cell(10, 5, self.safe_text(trend), align="R")

    def box_note(self, title: str, content: str):
        self.set_fill_color(245, 247, 249)
        self.set_draw_color(*self.accent_color)
        self.set_line_width(0.3)
        
        start_y = self.get_y()
        self.set_font("Helvetica", "B", 10)
        self.set_x(15)
        # We pre-calculate dimensions or use a simple hack
        self.ln(2)
        self.set_text_color(*self.accent_color)
        self.cell(0, 5, f" {self.safe_text(title)}", ln=True)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(60, 70, 80)
        self.multi_cell(0, 5, f" {self.safe_text(content)}")
        
        end_y = self.get_y()
        # Draw the box around
        self.rect(12, start_y, 188, end_y - start_y + 2)
        self.ln(4)

    def summary_table(self, rows: list, headers: list, col_widths: list):
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(44, 62, 80)
        self.set_text_color(255, 255, 255)
        
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 8, h, border=0, fill=True, align="C")
        self.ln()
        
        self.set_font("Helvetica", "", 9)
        self.set_text_color(40, 45, 50)
        for idx, row in enumerate(rows):
            fill = idx % 2 != 0
            if fill: self.set_fill_color(242, 245, 248)
            else: self.set_fill_color(255, 255, 255)
            
            for i, val in enumerate(row):
                self.cell(col_widths[i], 7, self.safe_text(str(val)), border=0, fill=True, align="C")
            self.ln()
