from main import Site

auto = Site('https://einhell.by/', 'https://einhell.by/avtomobilnye_akkumulyatory/zubr_belarus-polsha_/zubr_heavy_duty_/avtomobilnyy_akkumulyator_zubr_heavy_duty_190ah_/')
find_str = "find('span', 'ok-product__price-main').get_text(strip=True)"
auto.parser('span', 'ok-product__price-main', find_str, 'E3')