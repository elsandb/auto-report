
def convert_html(
        html_filepath: str, 
        docx_filepath: str|None, 
        pdf_filepath: str|None
    ):
    """
    Converts an HTML file into a Word (.docx) and/or PDF (.pdf) document using PowerShell.

    This function automates the process of opening an HTML file in Microsoft Word, 
    converting it to DOCX and/or PDF format, and saving the output files. It leverages 
    PowerShell's COM objects for Word automation, making it work only on **Windows** 
    with Microsoft Word installed.

    Args:
        html_path (str): 
            Full path to the HTML file to be converted.
        word_path (str | None, optional): 
            Desired output path for the Word document (.docx). 
            If set to `"inherit"`, the DOCX file is saved in the same directory as `html_path` 
            with the same filename but with `.docx` extension. Default is `"inherit"`. If not passed, or if set to `None`, a Word 
            document will not be created.
        pdf_path (str | None, optional): 
            Desired output path for the PDF document (.pdf). 
            If set to `"inherit"`, the PDF file is saved in the same directory as `html_path` 
            with the same filename but with `.pdf` extension. Default is `"inherit"`. If not passed, or if set to `None`, a PDF 
            document will not be created.

    Raises:
        FileNotFoundError: If the specified `html_path` does not exist.
        RuntimeError: If PowerShell execution fails due to missing Word installation or 
                      incorrect file handling.

    Example usage:
        >>> convert_html(html_path="C:\\Users\\Bruker\\Documents\\report.html")
        # Converts 'report.html' into 'report.docx' and 
        # 'report.pdf' in the same directory.

        >>> convert_html(html_path="C:\\Users\\Bruker\\Documents\\report.html", word_path="C:\\Users\\Bruker\\SomewhereElse\\my_report.docx")
        # Converts 'report.html' into 'my_report.docx' in the `SomewhereElse` folder, 
        # while the PDF remains named 'report.pdf' and is saved in the same folder.

        >>> convert_html(html_path="C:\\Users\\Bruker\\Documents\\report.html", pdf_path=None)
        # Converts 'report.html' into 'report.docx' only, 
        # skipping PDF generation.

    Notes:
        - This function **requires Windows and Microsoft Word installed**.
        - The PowerShell script runs **in the background**, so no GUI pop-ups occur.
        - If both `word_path` and `pdf_path` are `None`, the function **does nothing**.

    *This function is made with help from Microsoft copilot
    """
    import subprocess
    # Fix variable substitution in PowerShell script
    ps1_script = f"""
        $Word = New-Object -ComObject Word.Application
        $Word.Visible = $False

        # Open the HTML file
        $Document = $Word.Documents.Open('{html_filepath}')

        # Save as DOCX if the path is provided
        if (![string]::IsNullOrEmpty('{docx_filepath}')) {{
            $Document.SaveAs('{docx_filepath}', 16)  # 16 = DOCX format
        }}

        # Save as PDF if the path is provided
        if (![string]::IsNullOrEmpty('{pdf_filepath}')) {{
            $Document.SaveAs('{pdf_filepath}', 17)  # 17 = PDF format
        }}

        # Close document and Word
        $Document.Close()
        $Word.Quit()
    """

    # Run PowerShell script with explicit encoding
    subprocess.run(["powershell.exe", "-Command", ps1_script], shell=False, text=True, encoding='utf-8')

    # print(f"{html_filepath = }")
    # print(f"{docx_filepath = }")
    # print(f"{pdf_filepath = }")






