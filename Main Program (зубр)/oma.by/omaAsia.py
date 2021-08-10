from main import Site

auto = Site('https://www.oma.by/', 'https://www.oma.by/akkumulyator-zubr-ultra-75ah-r-760a-en-2-271426-p')
find_str = "find('div', 'product-info-box_price strong-price 1').get_text(strip=True)"
auto.parser('div', 'product-info-box_price strong-price 1', find_str, 'E3')