from main import Site

lauto852 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=253511605&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto852.parser('div', 'catalog-products-table__product-item', find_str, 'F852')

lauto854 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=0000001875&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto854.parser('div', 'catalog-products-table__product-item', find_str, 'F854')
