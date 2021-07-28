from main import Site

akb59 = Site('https://1akb.by/', 'https://1akb.by/catalog/avtomobilnyy_akkumulyator_bosch_s6_005_560_901_068_60_a_ch_680a_/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb59.parser('span', 'detail_price', find_str, 'AD59')

akb60 = Site('https://1akb.by/', 'https://1akb.by/catalog/avtomobilnyy_akkumulyatoravtomobilnyy_akkumulyator_bosch_s6_001_570_901_076_70_a_ch_760a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb60.parser('span', 'detail_price', find_str, 'AD60')

akb61 = Site('https://1akb.by/', 'https://1akb.by/catalog/avtomobilnyy_akkumulyator_bosch_s6_011_580_901_080_80_a_ch_800a_/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb61.parser('span', 'detail_price', find_str, 'AD61')

akb63 = Site('https://1akb.by/', 'https://1akb.by/catalog/avtomobilnyy_akkumulyator_bosch_s6_015_605_901_095_105_a_ch_950a_/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb63.parser('span', 'detail_price', find_str, 'AD63')