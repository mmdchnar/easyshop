from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from shop.models import Product, Detail
from django.contrib.postgres.search import SearchVector


# -------------------------------------
# | For Import Data From Digikala.com |
# -------------------------------------

driver = webdriver.Firefox()

while True:

    url = input('Enter URL: ')

    while True:
        product_name = input('Enter product name: ')
        vector = SearchVector('name')
        products = Product.objects.annotate(search=vector).filter(search=product_name)
        if len(products):
            product = products.first()
            print(product.name)
            break

    driver.get(url)

    show_more = driver.find_element(By.CSS_SELECTOR, '#specification > span:nth-child(3) > span:nth-child(1)')
    show_more.click()

    for i in range(1, 100):
        try:
            print(name, detail)
            name = driver.find_element(By.CSS_SELECTOR, f'div.w-full:nth-child({i}) > p:nth-child(1)').text
            detail = driver.find_element(By.CSS_SELECTOR, f'div.w-full:nth-child({i}) > div:nth-child(2) > p:nth-child(1)').text
            
            data = Detail(product=product, name=name, detail=detail)
            data.save()

        except NoSuchElementException:
            break

    if input('press enter to run again...(0 to end)') == '0':
        break


driver.close()
