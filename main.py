from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf_doc = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    # print(row["Topic"])
    page = 0

    while page < row["Pages"]:
        pdf_doc.add_page()

        pdf_doc.set_font(family="Times", style="B", size=24)
        pdf_doc.set_text_color(100,100,100)
        pdf_doc.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
        pdf_doc.line(10,24,200,24)
        page += 1

pdf_doc.output("output.pdf")