import bs4, requests

# Create a URL without pagination num
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# List of titles with 4 or 5 stars
titles_high_rating = []

# iterate pages
for page in range(1,10):
    url_page = url_base.format(page)
    results = requests.get(url_page)
    soup = bs4.BeautifulSoup(results.text,'lxml')

    # Select data from the book
    books = soup.select('.product_pod')

    # iterate books
    for book in books:

        # Check if it has 4 or 5 stars
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) !=0:

            # Save title
            book_title = book.select('a')[1]['title']

            # Add book to list
            titles_high_rating.append(book_title)

for title in titles_high_rating:
    print(title)