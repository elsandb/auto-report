from auto_report.elements import Title, Header, Paragraph, Png

def test_title() -> None:
    t = Title(
        text="Annual report 2025",
        font_color="blue",
        font_size=35
    )
    assert t.element_type == "Title"
    assert t.tag == "p class=MsoTitle"
    expected_html_str = f"""
            <p class=MsoTitle>
            <span style='font-family:"Aptos display"; 
            font-size:"35px"; 
            color:"blue"'>
            Annual report 2025
            </span>
            </p>
        """
    assert t.to_html() == expected_html_str

def test_header():
    h1 = Header(
        text="Man-Years in health centers 2015-2024",
        header_size=1,
        font_color="navy"
    )
    h2 = Header(
        text="Rogaland",
        header_size=2,
        font_color="pink"
    )
    assert h1.tag == "h1"
    assert h2.tag == "h2"
    assert h1.element_type == "Header1"
    assert h2.element_type == "Header2"
    assert h1.to_html() == '<h1 style="color: navy;">Man-Years in health centers 2015-2024</h1>'
    assert h2.to_html() == '<h2 style="color: pink;">Rogaland</h2>'
