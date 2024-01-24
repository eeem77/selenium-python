from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy = Proxy({ 
    'proxyType': ProxyType.MANUAL, 
    'httpProxy': '117.160.250.130:80', 
    'ftpProxy': '117.160.250.130:80', 
    'sslProxy': '117.160.250.130:80', 
    'noProxy': '' # set this value as per your requirement 
})

chrome_options = webdriver.FirefoxOptions() 
chrome_options.add_argument('--proxy-server={0}'.format(proxy.httpProxy)) 
 
driver = webdriver.Firefox(chrome_options) 

for x in range(1,4):
    driver.get(f"https://www.era.com/city/ca/san-mateo/agents?page={x}")
    driver.implicitly_wait(30)

    name = driver.find_elements(By.CSS_SELECTOR,"h3.MuiTypography-root.MuiTypography-subtitle1_md.css-1nj5942")
    subtitle = driver.find_elements(By.CSS_SELECTOR,"span.MuiTypography-root.MuiTypography-body6.css-14q0kqp")
    serial = driver.find_elements(By.CSS_SELECTOR,"span.MuiTypography-root.MuiTypography-body6.css-q6wjqd")
    email = driver.find_elements(By.CSS_SELECTOR,"p.MuiTypography-root.MuiTypography-body2.css-kp2fog")
    phone = driver.find_elements(By.CSS_SELECTOR,"p.MuiTypography-root.MuiTypography-body2.css-kp2fog")

    i = 0

    for element in name:
        if not name:
            nameAgent = ''
        else:
            nameAgent = element.text
        if not subtitle:
            subtitleAgent = ''
        else:
            subtitleAgent = subtitle[i].text
        if not serial:
            serialAgent = ''
        else:
            serialAgent = serial[i].text
        if not email:
            emailAgent = ''
        else:
            emailAgent = email[i].text
        if not phone:
            phoneAgent = ''
        else:
            phoneAgent = phone[i].text
        
        agent = [nameAgent, subtitleAgent, serialAgent, emailAgent, phoneAgent]
        
        with open('data.txt', 'a') as f:
            f.write(f'\n{agent}')
        print(agent)
        i = i + 1

driver.close()



# https://www.coldwellbanker.com/
# https://www.era.com/
# https://exitrealty.com/
# https://www.bhgre.com/city/ca/santa-clara/agents

# County: Santa Clara, San Mateo, Alameda