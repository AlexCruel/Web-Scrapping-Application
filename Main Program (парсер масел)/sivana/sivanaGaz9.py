from main import Site

sivana854 = Site('https://sivana.by/', 'https://sivana.by/maslo-transf-gazpromneft-gk-m-2-205l')
find_str = "find('span', class_='single-product-price')"
sivana854.parser('div', 'single-product-price-block-content', find_str, 'C854')