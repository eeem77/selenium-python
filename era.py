from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

proxy = Proxy({ 
    'proxyType': ProxyType.MANUAL, 
    'httpProxy': '89.43.31.134:3128', 
    'ftpProxy': '', 
    'sslProxy': '', 
    'noProxy': '' # set this value as per your requirement 
})

chrome_options = webdriver.FirefoxOptions() 
chrome_options.add_argument('--proxy-server={0}'.format(proxy.httpProxy)) 
 
driver = webdriver.Firefox(chrome_options) 


for x in range(1,2):

    driver.get(f"https://www.era.com/city/ca/san-mateo/agents?page={x}")
    driver.implicitly_wait(30)

    blockone = driver.find_elements(By.CSS_SELECTOR,"div.MuiStack-root.css-ea5hw0-MuiStack-root")

    
    for element in blockone:
        print(element.find_element(By.CSS_SELECTOR, "span.MuiTypography-root.MuiTypography-body6.css-q6wjqd").is_displayed())
    # name = driver.find_elements(By.CSS_SELECTOR,"h3.MuiTypography-root.MuiTypography-subtitle1_md.css-1nj5942")
    # subtitle = driver.find_elements(By.CSS_SELECTOR,"span.MuiTypography-root.MuiTypography-body6.css-14q0kqp")
    # serial = driver.find_elements(By.CSS_SELECTOR,"span.MuiTypography-root.MuiTypography-body6.css-q6wjqd")
    # email = driver.find_elements(By.CSS_SELECTOR,"p.MuiTypography-root.MuiTypography-body2.css-kp2fog")
    # phone = driver.find_elements(By.CSS_SELECTOR,"p.MuiTypography-root.MuiTypography-body2.css-kp2fog")
    # i = 0

    # for element in name:

    #     agent = [element.text, subtitle[i].text, serial[i].text, email[i].text, phone[i].text]

    #     with open('data.txt', 'a') as f:
    #         f.write(f'\n{agent}')
    #     print(agent)
    #     i = i + 1

driver.close()



# https://www.coldwellbanker.com/
# https://www.era.com/
# https://exitrealty.com/
# https://www.bhgre.com/city/ca/santa-clara/agents

# County: Santa Clara, San Mateo, Alameda