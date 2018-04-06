#A simple Kahoot bot that joins Kahoot game and sits idle
#Version 1.4.4
#ENTech SS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
#Asking for info here:
print("Kahoot spammer v 1.4.4")
pin=input("Please enter a game pin:")
name = input("Please enter a name:")
join = input("Please enter a amount of bots to join(Default is 50):")
tab = 0
nameb = 'name'
bot_num = 0
#Start chrome
print("Starting chrome...")
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
#If join feild is blank, then default is 50
if join=='':
    join=50
def namec():
    #Code for clarifying name
    global join, bot_num, nameb
    num=random.randint(1,999)*3
    if join=='1':
        nameb=name
        bot_num = bot_num + 1
    if int(join)>=2:
        if bot_num==join:
            print("Name generation completed")
        nameb=(name + '.' + str(num))
        bot_num = bot_num + 1
def bot():
    global nameb, driver, tab
    if bot_num==1:
        print("No new window necessary")
        continue
    elif bot_num >=2:
        print("Opening new window...")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[tab])
        continue
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
    #Checking login
    print("Checking if login was succesfull...")
    try:
       content = driver.find_element_by_class_name('ng-binding') 
    except:
        print("Error checking page:\nId could have changed, or connection could have dropped.")
        x=input("Press any key to exit...")
    print("Success!")
    print("Bot [" + bot_num + "] is now in the game ;)")
    tab = tab + 1
#Code for running a set amoun of times
for x in range(int(join)):
    bot()


