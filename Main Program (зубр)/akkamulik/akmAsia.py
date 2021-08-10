from main import Site

akm23 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/atlant-black-60-a-ch/')
find_str = "find_all('div', class_='product-info__cost')[1].get_text(strip=True)"
akm23.parser('div', 'product-info__cost', find_str, 'D23')

akm24 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/forward-green-60-r-60a-ch/')
find_str = "find_all('div', class_='product-info__cost')[1].get_text(strip=True)"
akm24.parser('div', 'product-info__cost', find_str, 'D24')