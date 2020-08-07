from main import Site

lauto891 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389901161&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto891.parser('div', 'catalog-products-table__product-item', find_str, 'F891')