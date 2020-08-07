from main import Site

lauto857 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389901158&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto857.parser('div', 'catalog-products-table__product-item', find_str, 'F857')

lauto862 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906450&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto862.parser('div', 'catalog-products-table__product-item', find_str, 'F862')

lauto863 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=253711608&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto863.parser('div', 'catalog-products-table__product-item', find_str, 'F863')

lauto864 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906418&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto864.parser('div', 'catalog-products-table__product-item', find_str, 'F864')