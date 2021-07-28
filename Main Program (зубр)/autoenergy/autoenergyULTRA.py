from main import Site

auto = Site('https://autoenergy.by/', 'https://autoenergy.by/catalog/legkovye/zubr/akkumulyator-zubr-ultra-55-a-h-530a-r/')
find_str = "find('div', class_='product-item-detail-info-container')"
auto.parser('span', 'product-item-detail-price-current', find_str, 'E3')

auto = Site('https://autoenergy.by/', 'https://autoenergy.by/catalog/legkovye/zubr/akkumulyator-zubr-ultra-60-a-h-590a-l/')
find_str = "find('div', class_='product-item-detail-info-container')"
auto.parser('span', 'product-item-detail-price-current', find_str, 'E5')