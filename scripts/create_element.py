from auto_report.elements import Title, Header, Paragraph, Png

if __name__ == "__main__":
    title = Title("Annual report 2025")
    print(title)

    h1 = Header(
        text="Man-Years in health centers 2015-2024",
        header_size=1,
        font_color="navy"
    )
    print(h1)

    h2 = Header(
        text="Rogaland",
        header_size=2,
        font_color="navy"
    )
    print(h2)