from main import Site

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-ultra-55-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B3')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-ultra-66-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B7')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-ultra-74-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B8')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-ultra-90-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B10')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-legkovyh-avtomobilej/zubr-ultra-100-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B13')