from main import Site

auto = Site('https://аккумулятор.бел/', 'https://аккумулятор.бел/p75048386-akkumulyator-baren-polar.html')
find_str = "find('p', 'b-product-cost__price').get_text(strip=True)"
auto.parser('p', 'b-product-cost__price', find_str, 'E3')