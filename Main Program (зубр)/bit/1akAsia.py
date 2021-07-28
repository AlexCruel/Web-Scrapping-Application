from main import Site

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-asia-45-a/h.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B29')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-asia-60-a/h.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B30')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-asia-68-a/h-r.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B31')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-80-a/h-r.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B32')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/akkumulyator-zubr-asia-91-a/h-r.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B33')