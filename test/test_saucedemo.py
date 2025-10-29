# import pytest
# from selenium.webdriver.common.by import By
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

# from utils.helpers import login_saucedemo, get_driver



# @pytest.fixture
# def driver():
#     # configuracion para consultar a selenium web driver
#     driver = get_driver()
#     yield driver
#     driver.quit()

# def test_login(driver):

#     login_saucedemo(driver)
#     assert "/inventory.html" in driver.current_url
#     titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
#     assert titulo == 'Products'

# def test_catalogo( driver ):
#     login_saucedemo( driver )

#     products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
#     assert len(products) > 0

#     # products[0] = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
#     # assert products[0] == 'Sauce Labs Backpack' 

#     first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
#     assert first_product_name == "Sauce Labs Backpack"

#     second_product_price = products[1].find_element(By.CLASS_NAME, "inventory_item_price").text
#     assert second_product_price == '$9.99' 

# def test_carrito( driver ):
#     login_saucedemo( driver )

#     products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
#     total_productos = len(products)
#     assert len(products) > 0

# #     products[0].find_element(By.TAG_NAME, 'button').click()

# #     badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
# #     assert badge == "1"  

#     if total_productos >= 3:
#         products[0].find_element(By.TAG_NAME, 'button').click()
#         products[1].find_element(By.TAG_NAME, 'button').click()
#         products[2].find_element(By.TAG_NAME, 'button').click()


#         badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
#         assert badge == "3"

#         #captura manual
#         # driver.save_screenshot("../screenshots/carrito3.png") 