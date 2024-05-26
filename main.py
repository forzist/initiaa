import fake_useragent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pyperclip
from fake_useragent import UserAgent
from seleniumwire import webdriver
import pyautogui as gui

a = int(input('введите кол-во кошельков '))
b = str(input('введите api ключ для капчи '))
c = str(input('введите ссылку для смены прокси '))
k = 0
while k < (a):
    try:
        with open('proxy.txt', 'r') as file:
            for line in file:
                if line:
                    parts = line.split(':')
                    ip, port, login, password = parts
        print(ip, port, login, password)

        options = Options()
        options.add_argument(f'user-agent={UserAgent().random}')
        options.add_extension('captcha.crx')
        options.add_extension('wallet.crx')
        proxy_options = {
            'proxy': {
                'http': f'http://{login}:{password}@{ip}:{port}',
                'https': f'https://{login}:{password}@{ip}:{port}',
            }
        }
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=options,
                                  seleniumwire_options=proxy_options
                                  )
        driver.implicitly_wait(1)
        useragent = fake_useragent.UserAgent().random
        headers = {
            'user-agent': useragent
        }
        sleep(2)
        driver.switch_to.window(window_name=driver.window_handles[0])
        driver.close()
        sleep(2)
        driver.switch_to.window(window_name=driver.window_handles[0])
        sleep(1)
        driver.get("chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html")
        sleep(2)
        driver.find_element(by=By.XPATH,
                            value=('/ html / body / div / div[1] / table / tbody / tr[1] / td[2] / input')).send_keys(b)
        driver.find_element(by=By.XPATH,
                            value=('/ html / body / div / div[1] / table / tbody / tr[1] / td[3] / button')).click()
        sleep(2)
        gui.press('enter')
        sleep(1)
        driver.get('chrome-extension://ffbceckpkpbcmgiaehlloocglmijnpmp/index.html')
        sleep(2)
        driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div/div/div[2]/div[3]/a[1]/div/span')).click()
        driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div/div/div[2]/form/div[1]/div[1]/div/input')).send_keys("1234554321")
        driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div/div/div[2]/form/div[1]/div[2]/div/input')).send_keys("1234554321")
        driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div/div/div[2]/form/div[1]/div[3]/div/div[1]')).click()
        driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div/div/div[2]/form/div[2]/div/div/div/button[2]/div/span')).click()
        driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/button/div/div')).click()
        driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/button/div/div')).click()
        driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span')).click()

        wallet = pyperclip.paste()
        words = wallet.strip().split()
        i=0
        sleep(1)
        for i in range(1, 13):
            xpath_main = f'/html/body/div[1]/div/div/div[2]/form/div[1]/div[{i}]/div/div/input'
            try:
                input_element = driver.find_element(by=By.XPATH, value=xpath_main)
                input_element.send_keys(words[i-1])
            except:
                continue
        driver.find_element(by=By.XPATH, value=('/html/body/div[1]/div/div/div[2]/form/div[2]/div/div/div/button[2]/div/span')).click()
        sleep(0.5)
        driver.find_element(by=By.XPATH,
                            value=('/html/body/div[1]/div/div[1]/div/a[2]/div/div[1]/button')).click()
        address = pyperclip.paste()
        sleep(0.5)
        driver.get('https://faucet.testnet.initia.xyz/')
        sleep(10)
        driver.find_element(by=By.XPATH,
                            value=('/html/body/div[1]/div/div/main/form/div/div[2]/div')).click()
        sleep(2)
        driver.find_element(by=By.XPATH,
                            value=('/html/body/div[1]/div/div/main/form/div/div[3]/altcha-widget/div/div/div[1]/input')).click()
        driver.find_element(by=By.XPATH,
                            value=(
                                '/html/body/div[1]/div/div/main/form/div/div[4]/div/div[1]/div/input')).send_keys(address)
        sleep(1)
        try:
            button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-button="true"]')))
            button.click()
        except Exception as e:
            print("Произошла ошибка")
        driver.get(c)
        sleep(15)
        with open('wallets.txt', "a") as file:
            file.write(wallet + "\n")
            file.close
        sleep(0.5)
        with open('address.txt', "a") as file:
            file.write(address + "\n")
            file.close
        k += 1
        print(f'создано {k} кошельков ')
        sleep(1)
        driver.quit()
    except:
        driver.quit()
        continue
