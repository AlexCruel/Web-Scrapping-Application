from main import Site

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr_premium_57a_ch/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C16')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr_premium_63a_ch/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C17')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-premium-63-a-h-550a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C18')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-premium-77-a-h-730a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C19')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr_premium_77a_ch/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C20')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-premium-80-a-h-780a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C21')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-premium-105-a-h-1000a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C22')