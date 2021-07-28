from main import Site

akby54 = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-premium-63-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby54.parser('div', 'page-product__basket__info js-cart-info', find_str, 'K54')

akby55 = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-premium-77-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby55.parser('div', 'page-product__basket__info js-cart-info', find_str, 'K55')

akby56 = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-premium-80-ah-r-6st80r.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby56.parser('div', 'page-product__basket__info js-cart-info', find_str, 'K56')

akby57 = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-premium-105-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby57.parser('div', 'page-product__basket__info js-cart-info', find_str, 'K57')