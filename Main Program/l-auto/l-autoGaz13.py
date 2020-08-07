from main import Site

lauto887 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906427&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto887.parser('div', 'catalog-products-table__product-item', find_str, 'F887')

lauto888 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906572&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto888.parser('div', 'catalog-products-table__product-item', find_str, 'F888')