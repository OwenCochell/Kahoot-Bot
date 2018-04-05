from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
print("Kahoot spammer v 1.3.1")
pin=input("Please enter a game pin:")
name = input("Please enter a name:")
join = input("Please enter a amount of bots to join(Default is 50):")
nameb = 'noname'
bot_num = 1
if join=='':
    join=50
def namec():
    global join, bot_num, nameb
    num=random.randint(1,999)*3
    if join=='1':
        print("Name change not neccessary.")
    if join>='2':
        if bot_num==join:
            print("Name generation completed")
        nameb=(name + '.' + str(num))
        bot_num = bot_num + 1
def bot():
    global nameb
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    print("Starting chrome...")
    #Start chrome
    driver = webdriver.Chrome(chrome_options=chrome_options)
    print("Navigating to Kahoot...")
    #Navigate to kahoot.com
    driver.get("https://kahoot.it/")
    #Wait untill element is available
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'inputSession')))
    #Finding input box
    inputb = driver.find_element_by_id('inputSession')
    print("Joining game...")
    #Inputting pin
    inputb.send_keys(pin)
    inputb.submit()
    #Entering name
    element = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
    gname = driver.find_element_by_id('username')
    namec()
    gname.send_keys(nameb)
    gname.submit()
    print("Checking if login was succesfull...")
    content = driver.find_element_by_class_name('ng-binding')
    print("Success!")
    print("Bot is now in the game ;)")
for x in range(int(join)):
    bot()


