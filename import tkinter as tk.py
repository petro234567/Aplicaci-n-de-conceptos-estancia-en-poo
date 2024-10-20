import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

class WebScrapingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraping App")
        self.url_label = tk.Label(root, text="Ingrese la URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()
        self.scrape_button = tk.Button(root, text="Iniciar Scraping", command=self.scrape)
        self.scrape_button.pack()
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def scrape(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Ingrese una URL válida")
            return
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            productos = soup.find_all("div", class_="ui-search-result__wrapper")
            resultados = []
            for producto in productos:
                titulo = producto.find("h2", class_="poly-box poly-component__title").text.strip()
                precio = producto.find("span", class_="andes-money-amount").text.strip()
                resultados.append(f"Título: {titulo} - Precio: {precio}")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "\n".join(resultados))
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScrapingApp(root)
    root.mainloop()

   
 #https://listado.mercadolibre.com.co/computadores#D[A:computadores]
   
    

