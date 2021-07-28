from main import Site

b53 = Site('https://bat.by/', 'https://bat.by/catalog/akkumulators/akom/akom-6st-55-reaktor-evro')
find_str = "find('span', class_='PricesalesPrice').get_text(strip=True)"
b53.parser('span', 'PricesalesPrice', find_str, 'E53')

b54 = Site('https://bat.by/', 'https://bat.by/catalog/akkumulators/akom/akom-6st-62-reaktor-evro')
find_str = "find('span', class_='PricesalesPrice').get_text(strip=True)"
b54.parser('span', 'PricesalesPrice', find_str, 'E54')

b55 = Site('https://bat.by/', 'https://bat.by/catalog/akkumulators/akom/akom-6st-75-reaktor-evro')
find_str = "find('span', class_='PricesalesPrice').get_text(strip=True)"
b55.parser('span', 'PricesalesPrice', find_str, 'E55')

b57 = Site('https://bat.by/', 'https://bat.by/catalog/akkumulators/akom/akom-6st-100-reaktor-evro')
find_str = "find('span', class_='PricesalesPrice').get_text(strip=True)"
b57.parser('span', 'PricesalesPrice', find_str, 'E57')

b59 = Site('https://bat.by/', 'https://bat.by/catalog/akkumulators/akom/ultimatum-60-agm-evro-60-ah')
find_str = "find('span', class_='PricesalesPrice').get_text(strip=True)"
b59.parser('span', 'PricesalesPrice', find_str, 'E59')

b60 = Site('https://bat.by/', 'https://bat.by/catalog/akkumulators/akom/ultimatum-70-agm-evro-70-ah')
find_str = "find('span', class_='PricesalesPrice').get_text(strip=True)"
b60.parser('span', 'PricesalesPrice', find_str, 'E60')

b62 = Site('https://bat.by/', 'https://bat.by/catalog/akkumulators/akom/ultimatum-95-agm-evro-95-ah')
find_str = "find('span', class_='PricesalesPrice').get_text(strip=True)"
b62.parser('span', 'PricesalesPrice', find_str, 'E62') 