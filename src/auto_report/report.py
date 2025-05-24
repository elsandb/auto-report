import os

from auto_report.convert import convert_html
from utils import boilerplate_html, date_today

class Report:
    report_number = 1
    def __init__(self):
        self.elements = []
        self.element_html = []

    def add(self, element):
        self.elements.append(element)

    @boilerplate_html
    def to_html(self):
        html_str = ""
        for e in self.elements:
            html_str += e.to_html()
        return html_str

    def to_docx(self, html_fp, docx_fp):
        html_str = self.to_html()
        self._save_file(html_fp, html_str)
        convert_html(
            html_filepath = html_fp,
            docx_filepath = docx_fp,
            pdf_filepath = None
        )
    
    def to_pdf(self, html_fp, pdf_fp):
        html_str = self._to_html()
        self._save_file(html_fp, html_str)
        convert_html(
            html_filepath = html_fp,
            docx_filepath = None,
            pdf_filepath = pdf_fp
        )
    
    def _save_file(self, file_path, content):
        # TODO: Create folders if they do not exist.
        # TODO: Check if file already exist, and as user if they want to overwrite it or not.
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    
    def __repr__(self):
        repr_str = ""
        for e in self.elements:
            repr_str += e.__repr__()
            repr_str += '\n'
        return repr_str

if __name__ == "__main__":
    from auto_report.elements import Title, Header, Paragraph
    nr = 1
    cwd = os.getcwd()
    html_fp = f"{cwd}/temp/{date_today()}_rep{nr}.html"
    docx_fp = f"{cwd}/word_pdf/{date_today()}_rep{nr}.docx"
    pdf_fp = f"{cwd}/word_pdf/{date_today()}_rep{nr}.pdf"
    print(html_fp)
    # print(docx_fp)
    # print(pdf_fp)


    location = "Møre og romsdal"

    r = Report()
    r.add(Title(f"Rapport om {location}"))
    r.add(Header("Header 1", header_size=1))
    r.add(Paragraph("The first paragraph. Lorem ipsum dolor calor amet."))
    r.to_docx(html_fp, docx_fp)
    r.to_pdf(html_fp, pdf_fp)
