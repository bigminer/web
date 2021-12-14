from bs4 import BeautifulSoup
soup = BeautifulSoup
print(soup.get_text())


data = [1, 2, 3, 4]

def data_to_html_table(data):
    html = '<table><tbody>'
    for item in data:
        html += '<tr><td>' + str(item) + '</td></tr>'
        html += '</body></table>'
        return html 

print("data_to_html_table")(data)  