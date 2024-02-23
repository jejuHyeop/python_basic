# 여기서 말하는 요소 즉, Element 란
# HTML 을 이루는 "태그"들을 말합니다.
# a, span, button, div, ... 이런것들이 전부 Element 라고 합니다.

# 요소지정을 위해서 몇 가지를 알아야하는데요
# class, id, css selector 표현(셀렉터표현), name 으로 크게 나눌 수 있습니다.

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("chromedriver.exe")

# 어차피 class, id, Tag 같은 경우에 셀렉터 표현으로 뭉쳐서 사용하면 효과적이기 때문에 셀렉터로 사용하고
# 추가적으로 name 을 사용할것입니다.

# 저희가 Element 를 지정하고 주로했던 것은
# 1.     .click()               > 요소를 클릭       ( Button, input Tag 의 경우 대부분 사용됨 )
# 2.     .send_keys(A)   > A 를 넣음          ( input , textarea 와 같은 곳에서 주로 사용 )
# 3.     .text                   > 텍스트를 반환


driver.find_element_by_css_selector(selector 표현)
driver.find_element_by_name(name속성값)

# element, elements 의 차이는
# 뽑히는 element 가 한개, 다수의 차이입니다.
# elements 는 다수 즉, 리스트의 형태로 반환되기 때문에
# 인덱싱을 지정해줘야합니다.
driver.find_elements_by_css_selector()
driver.find_elements_by_name()

