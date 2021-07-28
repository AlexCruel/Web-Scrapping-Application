from main import Site

lauto884 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389901164&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto884.parser('div', 'catalog-products-table__product-item', find_str, 'F884')

lauto885 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389901165&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto885.parser('div', 'catalog-products-table__product-item', find_str, 'F885')