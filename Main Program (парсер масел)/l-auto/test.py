from main import Site

lauto102 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=253141916&search_brandname=G-ENERGY&search_searchtype=1')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto102.parser('div', 'catalog-products-table__product-item', find_str, 'F102')