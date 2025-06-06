def convert_html(
        html_filepath: str, 
        docx_filepath: str|None, 
        pdf_filepath: str|None
    ):
    """
    Converts an HTML file into a Word (.docx) and/or PDF (.pdf) document using PowerShell.

    This function opens the HTML file at `html_filepath` in Microsoft Word (in the background), 
    converts it to DOCX and/or PDF format, and saves the output files. It leverages 
    PowerShell's COM objects for Word automation, making it work only on **Windows** 
    with Microsoft Word installed.

    Args:
        html_path (str): 
            Full path to the HTML file to be converted.
        word_path (str | None, optional): 
            Desired output path for the Word document (.docx). 
        pdf_path (str | None, optional): 
            Desired output path for the PDF document (.pdf). 

    Raises:
        FileNotFoundError: If the specified `html_path` does not exist.
        RuntimeError: If PowerShell execution fails due to missing Word installation or 
                      incorrect file handling.

    Example usage:
        >>> convert_html(html_path="C:\\Users\\...\\Documents\\report.html", docx_filepath="C:\\Users\\...\\Documents\\somewhere\\report.docx", pdf_filepath="C:\\Users\\...\\Documents\\somewhere\\report.pdf")
        # Converts 'report.html' into 'report.docx' and saves it as DOCX and PDF at the given filepaths.

        >>> convert_html(html_path="C:\\Users\\Bruker\\Documents\\report.html", pdf_path=None)
        # Converts 'report.html' into 'report.docx' only (skipping PDF generation), and saves it as DOCX at the given filepath.

    Notes:
        - This function **requires Windows and Microsoft Word installed**.
        - The PowerShell script runs **in the background**, so no GUI pop-ups occur.
        - If both `word_path` and `pdf_path` are `None`, the function **does nothing**.
        
    Thanks to:
        - "Helpfolder" for creating a helpful video on how to create Word documents with Windows Powershell (https://www.youtube.com/watch?v=2eFC1b-GpSI).
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
