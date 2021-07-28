from main import Site

rim26 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/polarblue60ahk.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim26.parser('p', 'item-price__text', find_str, 'AG26')

rim27 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/tab121066.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim27.parser('p', 'item-price__text', find_str, 'AG27')

rim31 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/polarblue75ah.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim31.parser('p', 'item-price__text', find_str, 'AG31')

rim33 = Site('https://www.rimir.by/', 'https://www.rimir.by/products/car/tab/polarblue100ah.html')
find_str = "find('div', class_='total-price__item').get_text(strip=True)"
rim33.parser('p', 'item-price__text', find_str, 'AG33')