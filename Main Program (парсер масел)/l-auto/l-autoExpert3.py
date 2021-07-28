from main import Site

lauto309 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=253990071&search_brandname=G-ENERGY&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto309.parser('div', 'catalog-products-table__product-item', find_str, 'F309')

lauto310 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=253990072&search_brandname=G-ENERGY&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto310.parser('div', 'catalog-products-table__product-item', find_str, 'F310')