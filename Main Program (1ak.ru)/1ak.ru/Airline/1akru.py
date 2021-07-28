from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/provoda-prikurivaniya-400a-25m-1224v-airline')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C330')