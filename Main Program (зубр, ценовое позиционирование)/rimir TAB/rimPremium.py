from main import Site

rim53 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/189058.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim53.parser('p', 'item-price__text', find_str, 'AG53')

rim54 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/magic62ah.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim54.parser('p', 'item-price__text', find_str, 'AG54')

rim55 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/magic189072.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim55.parser('p', 'item-price__text', find_str, 'AG55')

rim56 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/magic75ah.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim56.parser('p', 'item-price__text', find_str, 'AG56')

rim57 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/magic100ah.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim57.parser('p', 'item-price__text', find_str, 'AG57')

rim60 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/stopgoagm70ah.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim60.parser('p', 'item-price__text', find_str, 'AG60')

rim61 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/tab213080.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim61.parser('p', 'item-price__text', find_str, 'AG61')

rim62 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/tab-sigagm-92ah.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim62.parser('p', 'item-price__text', find_str, 'AG62')