from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy = Proxy({ 
    'proxyType': ProxyType.MANUAL, 
    'httpProxy': '117.160.250.133:8899', 
    'ftpProxy': '', 
    'sslProxy': '', 
    'noProxy': '' # set this value as per your requirement 
})

chrome_options = webdriver.FirefoxOptions() 
chrome_options.add_argument('--proxy-server={0}'.format(proxy.httpProxy)) 
 
driver = webdriver.Firefox(chrome_options) 

driver.get(f"https://www.era.com/city/ca/san-mateo/agents")
driver.implicitly_wait(30)

for x in range(1,4):

    name = driver.find_elements(By.CSS_SELECTOR,"h3.MuiTypography-root.MuiTypography-subtitle1_md.css-1nj5942")
    subtitle = driver.find_elements(By.CSS_SELECTOR,"span.MuiTypography-root.MuiTypography-body6.css-14q0kqp")
    serial = driver.find_elements(By.CSS_SELECTOR,"span.MuiTypography-root.MuiTypography-body6.css-q6wjqd")
    email = driver.find_elements(By.CSS_SELECTOR,"p.MuiTypography-root.MuiTypography-body2.css-kp2fog")
    phone = driver.find_elements(By.CSS_SELECTOR,"p.MuiTypography-root.MuiTypography-body2.css-kp2fog")
    btn = driver.find_element(By.CSS_SELECTOR,"svg.MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.MuiPaginationItem-icon.css-n8417t-MuiSvgIcon-root-MuiPaginationItem-icon")

    i = 0

    for element in name:
        if(not serial[i].text):
            serialAgent = ''
        else:
            serialAgent = serial[i].text
        agent = [element.text, subtitle[i].text, serialAgent, email[i].text, phone[i].text]
        
        with open('data.txt', 'a') as f:
            f.write(f'\n{agent}')
        print(agent)
        i = i + 1

    btn.click()
    driver.implicitly_wait(30)

driver.close()



# https://www.coldwellbanker.com/
# https://www.era.com/
# https://exitrealty.com/
# https://www.bhgre.com/city/ca/santa-clara/agents

# County: Santa Clara, San Mateo, Alameda