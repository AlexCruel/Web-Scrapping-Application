from main import Site

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-oe-original-66-ah-r.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B25')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-oe-original-77-ah-r.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B26')