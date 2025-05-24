from auto_report.utils import element_to_html

class Element():
    element_type: str = "Element"
    tag: str = None
    end_tag: str = None
    def __init__(self, 
            text: str = None,
            font_color: str = None, 
            font_size: int = None
            ):
        self.text = text
        self.font_color = font_color
        self.font_size = font_size
        self.element_type = Element.element_type
        self.tag = Element.tag
        self.end_tag = Element.end_tag

    def to_html(self):
        # List to collect html substrings
        html_str_list = []
        # Append opening tag
        html_str_list.append(f"<{self.tag}")
        # Add style attribute to opening tag
        if self.font_color or self.font_size:
            style_segments = []
            style_segments.append(' style="')
            if self.font_color:
                style_segments.append(f"color: {self.font_color};")
            if self.font_size: 
                style_segments.append(f" font-size: {self.font_size}px;")
            style_segments.append('"')
            if style_segments:
                style_attribute = "".join(style_segments)
                html_str_list.append(style_attribute)
        # Close the opening tag
        html_str_list.append(">")

        # Add the element text and a closing tag
        html_str_list.append(self.text)
        html_str_list.append(f"</{self.end_tag}>")

        html_string = "".join(html_str_list)
        # style = f'"color: {self.font_color}; font-size: {font_size}px;"'
        return html_string
    
    def all_info_string(self):
        all_info = (
            f"text: {self.text}"
            + f"\nelement type: {self.element_type}"
            + f"\nfont_size: {self.font_size}"
            + f"\nfont_color: {self.font_color}"
        )
        return all_info
    
    def __repr__(self):
        repr_str = f"{self.element_type}: {self.text}"
        if not repr_str:
            return "No representation string for this object."
        return repr_str

class Title(Element):
    element_type: str = "Title"
    tag = "p class=MsoTitle"
    end_tag = "p"
    # <p class=MsoTitle><span style='mso-fareast-font-family:"Times New Roman"'>Title</span></p>
    def __init__(self, 
            text: str, 
            font_color: str = None, #"black", 
            font_size: int = 55
            ):
        super().__init__(text, font_color, font_size)
        self.element_type = Title.element_type
        self.tag = Title.tag
        self.end_tag = Title.end_tag
    def to_html(self):
        html_str = f"""
            <p class=MsoTitle>
            <span style='font-family:"Aptos display"; 
            font-size:"{self.font_size}px"; 
            color:"{self.font_color}"'>
            {self.text}
            </span>
            </p>
        """
        return html_str

class Header(Element):
    element_type: str = "Header"
    tag = "h"
    end_tag = "h"
    def __init__(self,
            text: str, 
            header_size: int = 1,
            font_color: str = None,
            font_size: int = None
            ):
        
        super().__init__(text, font_color, font_size)
        self.element_type = Header.element_type + f"{header_size}"
        self.tag = Header.tag + f"{header_size}"
        self.end_tag = Header.end_tag + f"{header_size}"

class Paragraph(Element):
    element_type = "Paragraph"
    tag = "p"
    end_tag = "p"
    def __init__(self, 
            text, 
            font_color = None, #"black", 
            font_size: int = None, #18
            ):
        super().__init__(text, font_color, font_size)
        self.element_type = Paragraph.element_type
        self.tag = Paragraph.tag
        self.end_tag = Paragraph.end_tag


# class Svg(Element):
#     element_type = "SVG"
#     tag = ""
#     def __init__(self, 
#             text = None, 
#             font_color = None, 
#             font_size = None
#             ):
#         super().__init__(text, font_color, font_size)
#         self.element_type = Svg.element_type
#         self.tag = Svg.tag
#     # def to_html(self):
#     #     html_str = "<svg>"

class Png(Element):
    img_number = 1 # Increases for each Png created.
    element_type = "png"
    tag = "img"
    def __init__(self, 
            text = None, 
            font_color = None, 
            font_size = None,
            src: str = None
            ):
        super().__init__(text, font_color, font_size)
        self.element_type = Png.element_type
        self.tag = Png.tag
        self.src = src
        self.img_number = Png.img_number
        Png.img_number += 1

    def to_html(self):
        # html_str = f"<img src='{self.src}'/>"
        html_str = f"""
            <p class=MsoNormal style='page-break-after:avoid'><span style='mso-fareast-font-family:
            "Times New Roman";mso-no-proof:yes'><img width=50% height=50% id='fig_{self.img_number}'
            src='{self.src}'></span></p>

            <p class=MsoCaption>Figur <!--[if supportFields]><span style='mso-element:field-begin'></span><span
            style='mso-spacerun:yes'> </span>SEQ Figur \* ARABIC <span style='mso-element:
            field-separator'></span><![endif]--><span style='mso-no-proof:yes'>{self.img_number}</span><!--[if supportFields]><span
            style='mso-element:field-end'></span><![endif]-->. {self.text}</p>
            """
        return html_str


    
