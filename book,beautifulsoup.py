import requests
from bs4 import BeautifulSoup
import csv
BASE = "https://books.toscrape.com"

csv_file = open('books_data2.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Price', 'Stock', 'Rating', 'Image', 'Link'])


user_input_1 = input("Enter what do you want books info or every book info: ")
all_links = []
user_input = input(
    "Enter a book title from it: books_1, travel_2, mystery_3, "
    "historical-fiction_4, sequential-art_5, classics_6, philosophy_7, romance_8, "
    "womens-fiction_9, fiction_10, childrens_11, religion_12, nonfiction_13, music_14, "
    "default_15, science-fiction_16, sports-and-games_17, add-a-comment_18, fantasy_19, "
    "new-adult_20, young-adult_21, science_22, poetry_23, paranormal_24, art_25, "
    "psychology_26, autobiography_27, parenting_28, adult-fiction_29, humor_30, horror_31, "
    "history_32, food-and-drink_33, christian-fiction_34, business_35, biography_36, "
    "thriller_37, contemporary_38, spirituality_39, academic_40, self-help_41, historical_42, "
    "christian_43, suspense_44, short-stories_45, novels_46, health_47, politics_48, "
    "cultural_49, erotica_50, crime_51: "
)
def books_data(soup):
    for book in soup.find_all('article', class_='product_pod'):
        link = book.find('a')['href']
        link = link[6:]
        full_link = f"https://books.toscrape.com/catalogue/{link}"
        title = book.h3.a['title']
        img = book.find('img')['src']
        product_price = book.find('p', class_='price_color').get_text(strip=True)
        stock = book.find('p', class_='instock availability').get_text(strip=True)
        rating = book.find('p', class_='star-rating')['class'][1]
        csv_writer.writerow([title, product_price, stock, rating, img, full_link])
if user_input_1 == 'books info':
    if user_input == 'books_1':
        page = 1
        while True:
            if page == 1:
                url = f"https://books.toscrape.com/catalogue/category/{user_input}/index.html"
            else:
                url = f"https://books.toscrape.com/catalogue/category/{user_input}/page-{page}.html"

            response = requests.get(url)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.content, "lxml")

            for h1 in soup.find_all('h1'):
                print(h1.get_text(strip=True))
            print(f'page number is {page}')
            books_data(soup)
            page = page + 1
    else:
        page = 1
        while True:
            if page == 1:
                url = f"https://books.toscrape.com/catalogue/category/books/{user_input}/index.html"
            else:
                url = f"https://books.toscrape.com/catalogue/category/books/{user_input}/page-{page}.html"

            response = requests.get(url)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.content, "lxml")

            for h1 in soup.find_all('h1'):
                print(h1.get_text(strip=True))
            print(f'page number is {page}')
            for h1 in soup.find_all('h1'):
                print(h1.get_text(strip=True))
            print(f'page number is {page}')
            books_data(soup)
            page = page + 1

### every book info
def links_books(soup):
    for book in soup.find_all('article', class_='product_pod'):
        link = book.find('a')['href']
        link = link[6:]
        full_link = f"https://books.toscrape.com/catalogue/{link}"
        all_links.append(full_link)

def books_info(link):
    response = requests.get(link)
    if response.status_code != 200:
        return
    soup = BeautifulSoup(response.content, "lxml")

    title = soup.find('h1').get_text(strip=True)
    product_price = soup.find('p', class_='price_color').get_text(strip=True)
    stock = soup.find('p', class_='instock availability').get_text(strip=True)
    rating = soup.find('p', class_='star-rating')['class'][1]
    img = soup.find('img')['src']
    print(f"Title: {title}")
    print(f"Price: {product_price}")
    print(f"Stock: {stock}")
    print(f"Rating: {rating}")
    print(f"Image: {img}")
    print("------------------------")
    csv_writer.writerow([title, product_price, stock, rating, img, link])
if user_input_1 == 'every book info':
    if user_input == 'books_1':
        page = 1

        while True:
            if page == 1:
                url = f"https://books.toscrape.com/catalogue/category/{user_input}/index.html"
            else:
                url = f"https://books.toscrape.com/catalogue/category/{user_input}/page-{page}.html"

            response = requests.get(url)
            if response.status_code != 200:
                break
            soup = BeautifulSoup(response.content, "lxml")
            links_books(soup)
            print(f'page number is {page}')
            page = page + 1
        for link in all_links:
            books_info(link)
csv_file.close()
