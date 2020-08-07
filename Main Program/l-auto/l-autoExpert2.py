from main import Site

lauto303 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=253651811&search_brandname=G-ENERGY&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto303.parser('div', 'catalog-products-table__product-item', find_str, 'F303')

lauto304 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=253651812&search_brandname=G-ENERGY&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto304.parser('div', 'catalog-products-table__product-item', find_str, 'F304')

lauto305 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=253651813&search_brandname=G-ENERGY&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto305.parser('div', 'catalog-products-table__product-item', find_str, 'F305')

lauto307 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=253651814&search_brandname=G-ENERGY&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto307.parser('div', 'catalog-products-table__product-item', find_str, 'F307')