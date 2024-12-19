from os import access
from src.utils import get_html
from src.soup import Soup
from src.__init__ import BASE_URL
from src.utils import get_html, save_to_xlsx

def main():
    soup = get_html(BASE_URL)
    output = soup.scrape()
    save_to_xlsx(output, "schools.xlsx")

if __name__ == '__main__':
    main()