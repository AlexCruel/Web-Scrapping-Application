from main import Site

auto = Site('https://akkumulator.by/', 'https://akkumulator.by/banner-power-bull-62ah-540a-01380/')
find_str = "find('meta', {'itemprop': 'price'})['content']"
auto.parser('meta', 'product-item-detail-price-current', find_str, 'E3')