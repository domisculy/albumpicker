pipinstall: requests-html
pipinstall: parsedatetime

from datetime import datetime 
import requests_html
import parsedatetime
sess = requests_html.HTMLSession()

def try_cast(value, cast):
    try:
        return cast(value)
    except ValueError:
        return 0

class Album:
    def __init__(self, in_html):
        self.title = in_html.find('.page_charts_section_charts_item_title', first=True). text