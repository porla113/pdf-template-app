from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf_doc = FPDF(orientation="P", unit="mm", format="A4")
pdf_doc.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():

    # Add a topic page
    pdf_doc.add_page()

    # Header
    pdf_doc.set_font(family="Times", style="B", size=24)
    pdf_doc.set_text_color(100,100,100)
    pdf_doc.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf_doc.line(10,24,200,24)

    # Draw lines
    pdf_doc.set_draw_color(200, 200, 220)
    line_height_start = 34
    for i in range(0, 24):
        line_height = line_height_start + 10 * i
        pdf_doc.line(10, line_height, 200, line_height)

    pdf_doc.ln(251)

    # Footer
    pdf_doc.set_draw_color(0, 0, 0)
    pdf_doc.line(10,275,200,275)
    pdf_doc.set_font(family="Times", style="I", size=12)
    pdf_doc.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1, border=0)

    for i in range(row["Pages"] - 1):
        pdf_doc.add_page()

        # Draw lines
        pdf_doc.set_draw_color(200, 200, 220)
        line_height_start = 24
        for i in range(0, 25):
            line_height = line_height_start + 10 * i
            pdf_doc.line(10, line_height, 200, line_height)

        pdf_doc.ln(263) 

        # Footer
        pdf_doc.set_draw_color(0, 0, 0)
        pdf_doc.line(10,275,200,275)
        pdf_doc.set_font(family="Times", style="I", size=12)
        pdf_doc.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1, border=0)


pdf_doc.output("output.pdf")