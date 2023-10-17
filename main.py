import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime



assets_base = [
    {"name": "AZUL4"},
    {"name": "ELET3"},
    {"name": "ITSA4"},
    {"name": "GGBR4"},
    {"name": "GOAU4"},

    {"name": "CASH3"},
    {"name": "TAEE11"},
    {"name": "CSNA3"},
    {"name": "LREN3"},
    {"name": "AMAR3"},

]

start = datetime.now().strftime("%X")
for asset in assets_base:

    url = f"https://www.google.com/finance/quote/{asset['name']}:BVMF?hl=pt"


    response = requests.get(url)

    class_to_value = 'YMlKec fxKbKc'
    class_to_name = 'zzDege'
    class_to_simbol = 'PdOqHc'


    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        value = soup.find('div', class_=class_to_value).text
        name = soup.find('div', class_=class_to_name).text
        simbol = soup.find('div', class_=class_to_simbol).text

        simbol_trated = simbol[14:20].strip()
        value_trated = re.sub(r'[^0-9,.]', '', value)
        
        
        
        print({
            "name":name,
            "value": f'R$ {value_trated}',
            "simbol": simbol_trated
        })
    

end = datetime.now().strftime("%X")

print({
    "start_execution":start,
    "end_execution":end,
})
