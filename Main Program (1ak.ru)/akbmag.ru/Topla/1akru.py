from main import Site

akru = Site('https://akbmag.ru/', 'https://akbmag.ru/catalog/akkumulator-topla-energy-75r-700a-278x175x190.html')
find_str = "find('div', class_='card-price').get_text(strip=True)"
akru.parser('span', '', find_str, 'E155')

akru = Site('https://akbmag.ru/', 'https://akbmag.ru/catalog/akkumulator-topla-energy-100r-920a-353x175x190.html')
find_str = "find('div', class_='card-price').get_text(strip=True)"
akru.parser('span', '', find_str, 'E162')

akru = Site('https://akbmag.ru/', 'https://akbmag.ru/catalog/akkumulator-topla-energy-75l-700a-278x175x190.html')
find_str = "find('div', class_='card-price').get_text(strip=True)"
akru.parser('span', '', find_str, 'E179')