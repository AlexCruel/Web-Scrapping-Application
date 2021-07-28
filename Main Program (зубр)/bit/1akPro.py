from main import Site

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-gruzovyh-avtomobile/akkumulyator-zubr-professional-(145-a/h)-950a-r.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B36')

akby = Site('https://sivana.by/', 'https://1ak.by/shop/akkumulyatory/dlya-gruzovyh-avtomobile/zubr-professional-190-ah.html')
find_str = "find('input', type='hidden', class_='js-ch-product-price gec-product-price')"
akby.parser('div', 'page-product__basket__info js-cart-info', find_str, 'B37')