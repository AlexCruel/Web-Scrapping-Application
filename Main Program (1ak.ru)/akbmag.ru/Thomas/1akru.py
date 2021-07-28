from main import Site

akru = Site('https://akbmag.ru/', 'https://akbmag.ru/catalog/akkumulator-thomas-60l-540a-242x175x190.html')
find_str = "find('div', class_='card-price').get_text(strip=True)"
akru.parser('span', '', find_str, 'E435')

akru = Site('https://akbmag.ru/', 'https://akbmag.ru/catalog/akkumulator-thomas-60r-540a-242x175x190.html')
find_str = "find('div', class_='card-price').get_text(strip=True)"
akru.parser('span', '', find_str, 'E436')

akru = Site('https://akbmag.ru/', 'https://akbmag.ru/catalog/akkumulator-thomas-60r-510a-232x173x225.html')
find_str = "find('div', class_='card-price').get_text(strip=True)"
akru.parser('span', '', find_str, 'E438')

akru = Site('https://akbmag.ru/', 'https://akbmag.ru/catalog/akkumulator-thomas-60l-510a-232x173x225.html')
find_str = "find('div', class_='card-price').get_text(strip=True)"
akru.parser('span', '', find_str, 'E439')

akru = Site('https://akbmag.ru/', 'https://akbmag.ru/catalog/akkumulator-thomas-74r-680a-278x175x190.html')
find_str = "find('div', class_='card-price').get_text(strip=True)"
akru.parser('span', '', find_str, 'E443')

akru = Site('https://akbmag.ru/', 'https://akbmag.ru/catalog/akkumulator-thomas-100r-830a-353x175x190.html')
find_str = "find('div', class_='card-price').get_text(strip=True)"
akru.parser('span', '', find_str, 'E449')