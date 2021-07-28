from main import Site

akb53 = Site('https://1akb.by/', 'https://1akb.by/catalog/akkumulyator_akom_6st_55_reaktor/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb53.parser('span', 'detail_price', find_str, 'H53')

akb54 = Site('https://1akb.by/', 'https://1akb.by/catalog/akkumulyator_akom_6st_62_reaktor/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb54.parser('span', 'detail_price', find_str, 'H54')

akb55 = Site('https://1akb.by/', 'https://1akb.by/catalog/akkumulyator_akom_6st_75_reaktor/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb55.parser('span', 'detail_price', find_str, 'H55')

akb57 = Site('https://1akb.by/', 'https://1akb.by/catalog/akkumulyator_akom_6st_100_reaktor/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb57.parser('span', 'detail_price', find_str, 'H57')

akb59 = Site('https://1akb.by/', 'https://1akb.by/catalog/akom-ultimatum-60-agm-evro-60-a-h-680a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb59.parser('span', 'detail_price', find_str, 'H59')

akb60 = Site('https://1akb.by/', 'https://1akb.by/catalog/akom-ultimatum-70-agm-evro-70-a-h-760a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb60.parser('span', 'detail_price', find_str, 'H60')

akb62 = Site('https://1akb.by/', 'https://1akb.by/catalog/akom-ultimatum-90-agm-evro-90-a-h-850a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb62.parser('span', 'detail_price', find_str, 'H62')