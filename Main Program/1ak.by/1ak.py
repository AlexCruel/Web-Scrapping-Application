from main import Site

akby354 = Site('https://sivana.by/', 'https://1ak.by/shop/masla/motornye-masla/dlya-legkovyh-avtomobilej/gazpromneft-super-5w-40.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby354.parser('div', 'page-product__basket__info js-cart-info', find_str, 'D354')