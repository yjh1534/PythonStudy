from bs4 import BeautifulSoup


with open("intermediate\BeautifulSoup\day45\website.html",encoding="UTF-8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
print(soup.title)

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())
    
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)