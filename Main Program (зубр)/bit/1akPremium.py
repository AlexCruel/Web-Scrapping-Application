from main import Site

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-premium-57-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B16')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-premium-63-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B17')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-premium-77-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B19')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-premium-80-ah-r-6st80r.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B21')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-premium-105-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B22')