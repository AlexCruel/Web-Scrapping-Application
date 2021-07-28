from main import Site

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr_ultra_55_a_ch/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C3')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-ultra-60-a-h-590a-l/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C5')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr_ultra_66_a_ch_/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C7')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-ulta-74-a-h-710a-r-nizkiy/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C8')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr_ultra_90_a_ch/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C10')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-ultra-90-a-h-720a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C11')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr_ultra_100_a_ch_820a_r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C12')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr_ultra_100_a_ch/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C13')