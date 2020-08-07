from main import Site

lauto911 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906424&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto911.parser('div', 'catalog-products-table__product-item', find_str, 'F911')

lauto912 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906850&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto912.parser('div', 'catalog-products-table__product-item', find_str, 'F912')

lauto913 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906419&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto913.parser('div', 'catalog-products-table__product-item', find_str, 'F913')

lauto914 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906420&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto914.parser('div', 'catalog-products-table__product-item', find_str, 'F914')

lauto915 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906786&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto915.parser('div', 'catalog-products-table__product-item', find_str, 'F915')

lauto916 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906787&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto916.parser('div', 'catalog-products-table__product-item', find_str, 'F916')

lauto921 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906859&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto921.parser('div', 'catalog-products-table__product-item', find_str, 'F921')

lauto922 = Site('http://www.l-auto.by/', 'http://www.l-auto.by/offers/?search_searchstring=2389906860&search_brandname=GAZPROMNEFT&search_searchtype=1&tab-search-line=search-by-articles')
find_str = "find('div', class_='offer__product-price').get_text(strip=True)"
lauto922.parser('div', 'catalog-products-table__product-item', find_str, 'F922')