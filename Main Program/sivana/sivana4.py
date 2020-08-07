from main import Site

sivana239 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-motion-2t-1l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana239.parser('div', 'single-product-price-block-content', find_str, 'C239')

sivana247 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-garden-chain-bar-205l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana247.parser('div', 'single-product-price-block-content', find_str, 'C247')