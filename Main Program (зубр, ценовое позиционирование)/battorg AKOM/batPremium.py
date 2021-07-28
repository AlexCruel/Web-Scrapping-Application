from main import Site

bat53 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akom-6st-55-reaktor-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat53.parser('strong', '', find_str, 'D53')

bat54 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akom-6st-62-reaktor-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat54.parser('strong', '', find_str, 'D54')

bat55 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akom-6st-75-reaktor-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat55.parser('strong', '', find_str, 'D55')

bat57 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akom-6st-100-reaktor-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat57.parser('strong', '', find_str, 'D57')

bat59 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/ultimatum-60/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat59.parser('strong', '', find_str, 'D59')

bat60 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/ultimatum-70/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat60.parser('strong', '', find_str, 'D60')

bat62 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/ultimatum-95/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat62.parser('strong', '', find_str, 'D62')