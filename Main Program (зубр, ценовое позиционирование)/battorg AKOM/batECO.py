from main import Site

bat5 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akom-bravo-6st-60/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat5.parser('strong', '', find_str, 'D5')

bat6 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akom-bravo-6st-60-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat6.parser('strong', '', find_str, 'D6')

bat7 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akom-bravo-6st-74-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat7.parser('strong', '', find_str, 'D7')

bat8 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akom-bravo-6st-90-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat8.parser('strong', '', find_str, 'D8')

bat12 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akkumulyator-rusbat-6st-55-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat12.parser('strong', '', find_str, 'D12')

bat13 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akkumulyator-rusbat-6st-60-evr/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat13.parser('strong', '', find_str, 'D13')

bat14 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akkumulyator-rusbat-6st-75-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat14.parser('strong', '', find_str, 'D14')

bat15 = Site('https://battorg.by/', 'https://battorg.by/catalog/akkumulyatory-avtomobilnye/akom/akkumulyator-rusbat-6st-90-evro/')
find_str = "find('div', class_='price').find('strong').get_text(strip=True)"
bat15.parser('strong', '', find_str, 'D15')