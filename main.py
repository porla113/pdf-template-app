from fpdf import FPDF

pdf_doc = FPDF(orientation="P", unit="mm", format="A4")

pdf_doc.add_page()

pdf_doc.set_font(family="Times", style="B", size=12)
pdf_doc.cell(w=20, h=12, txt="Hi There!", align="L", ln=1, border=1)
pdf_doc.cell(w=0, h=12, txt="Nice to create PDF", align="L", ln=1, border=1)

pdf_doc.add_page()

pdf_doc.set_font(family="Times", style="B", size=12)
pdf_doc.cell(w=20, h=12, txt="Hi page 2!", align="L", ln=1, border=1)
pdf_doc.cell(w=0, h=12, txt="Nice to create page 2", align="L", ln=1, border=1)

pdf_doc.output("output.pdf")