
def date_today():
    from datetime import datetime
    return datetime.today().strftime("%d.%m.%Y")


def boilerplate_html(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        boilerplate_start = """
        <!DOCTYPE html>
        <html lang='no'>
        <head>
        <meta charset="UTF-8" />   
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        </head>
        <body>
        """
        boilerplate_end = "</body></html>"
        return boilerplate_start + f"{result}" + boilerplate_end
    return wrapper