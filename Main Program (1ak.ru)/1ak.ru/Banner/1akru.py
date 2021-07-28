from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/110-ah-banner-power-bull-110-40-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C48')