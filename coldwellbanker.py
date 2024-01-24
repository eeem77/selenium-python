from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy = Proxy({ 
    'proxyType': ProxyType.MANUAL, 
    'httpProxy': '117.160.250.130:80', 
    'ftpProxy': '', 
    'sslProxy': '', 
    'noProxy': '' # set this value as per your requirement 
})

chrome_options = webdriver.FirefoxOptions() 
chrome_options.add_argument('--proxy-server={0}'.format(proxy.httpProxy)) 
 
driver = webdriver.Firefox(chrome_options) 
for x in range(79,80):
    driver.get(f"https://www.era.com/city/ca/san-mateo/agents?page={x}")
    driver.implicitly_wait(30)
    # assert "Python" in driver.title
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h6[@data-testid='office-name']")))
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='license-number']")))
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='phoneLink']")))
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='emailLink']")))
    name = driver.find_elements(By.XPATH, "//h6[@data-testid='office-name']")
    reg = driver.find_elements(By.XPATH, "//span[@data-testid='license-number']")
    number = driver.find_elements(By.XPATH, "//a[@data-testid='phoneLink']")
    email = driver.find_elements(By.XPATH, "//a[@data-testid='emailLink']")
    i = 0

    for element in name:
        agent = [element.text,reg[i].text,number[i].get_attribute("href"),email[i].get_attribute("href")]
        #agent = [element]
        with open('data.txt', 'a') as f:
            f.write(f'\n{agent}')
        print(agent)
        i = i + 1
    
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//svg[@data-testid='NavigateNextIcon'"))).click()
    
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# print(elem)
driver.close()



# https://www.coldwellbanker.com/
# https://www.era.com/
# https://exitrealty.com/
# https://www.bhgre.com/city/ca/santa-clara/agents

# County: Santa Clara, San Mateo, Alameda