from main import Site

sivana649 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-moto-2t-1l')
find_str = "find('span', class_='single-product-price')"
sivana649.parser('div', 'single-product-price-block-content', find_str, 'C649')

sivana650 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-moto-2t-4l')
find_str = "find('span', class_='single-product-price')"
sivana650.parser('div', 'single-product-price-block-content', find_str, 'C650')

sivana653 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-moto-4t-10w-40-800ml')
find_str = "find('span', class_='single-product-price')"
sivana653.parser('div', 'single-product-price-block-content', find_str, 'C653')

sivana662 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-moto-4t-30-800ml')
find_str = "find('span', class_='single-product-price')"
sivana662.parser('div', 'single-product-price-block-content', find_str, 'C662')

sivana669 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-promo-3-5l')
find_str = "find('span', class_='single-product-price')"
sivana669.parser('div', 'single-product-price-block-content', find_str, 'C669')