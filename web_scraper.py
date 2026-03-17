import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/" 
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')
    books = soup.find_all('article',class_= 'product_pod')
    
    with open('my_books_results.csv','w', newline = '',encoding = 'utf-8') as f:
        
        writer = csv.writer(f)
        writer.writerow(['book title', 'price'])
        
        for book in books:
            title = book.h3.a['title']
            price = book.find('p',class_ = 'price_color').text
            writer.writerow([title,price])
            
            print(f"saved: {title}")
            
            print("\n  done! file 'my_books_results.csv' successfully created  ")
            
            print("could not connect to the website.")