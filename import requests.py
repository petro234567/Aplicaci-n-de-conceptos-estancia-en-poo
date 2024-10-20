import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.co/smartphone#D[A:smartphone]"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

productos = soup.find_all("div", class_="ui-search-result__wrapper")

print(type(productos))

for producto in productos:
    titulo = producto.find("h2", class_ ="poly-box poly-component__title").text.strip()

    precio = producto.find("span", class_ ="andes-money-amount").text.strip()

    print(f"Título: {titulo}")
    print(f"Precio: {precio}")