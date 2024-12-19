from bs4 import BeautifulSoup
from .models import School
from .__init__ import BASE_URL
import re

class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, "html.parser")
        
    def scrape(self):
        output = []
        table_center = self.find_all("table", class_="center")
        for table in table_center:
            table = table.find("table")
            td = table.find_all("td")
            
            # school name
            name = td[0].find("h3").get_text().strip() if td[0].find("h3") else ""

            # address
            br1 = td[0].find_all("br")

            address1 = br1[0].next_sibling.strip() if len(br1) > 0 and br1[0].next_sibling else ""
            address2 = br1[1].next_sibling.strip() if len(br1) > 1 and br1[1].next_sibling else ""
            address3 = br1[2].next_sibling.strip() if len(br1) > 2 and br1[2].next_sibling else ""
            address = f"{address1}, {address2}, {address3}".strip(", ")

            # program director
            br2 = td[1].find_all("br")
            program_director = br2[0].next_sibling.strip() if len(br2) > 0 and br2[0].next_sibling else ""
            program_director = program_director.replace("Chief Nurse Administrator: ", "")

            # phone number
            phone_tag = td[1].find(string=re.compile("Phone:"))
            phone_number = phone_tag.strip().replace("Phone: ", "") if phone_tag else ""

            # email
            email = td[1].find("span").get_text().replace("E-Mail: ", "") if td[1].find("span") else ""

            # website
            website = td[0].find("a")["href"] if td[0].find("a") else ""

            school = School(
                name=name,
                address=address,
                phone_number=phone_number,
                program_director=program_director,
                email=email,
                website=website
            )
            
            output.append(school)
        
        return output
