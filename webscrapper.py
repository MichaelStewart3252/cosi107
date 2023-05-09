# Imports for Selenium tester
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time

PATH = "C:\Program Files (x86)\chromedriver.exe" # Path to chrome driver
CHROME_USER = r"C:\Users\gmbab\AppData\Local\Google\Chrome\User Data" #Path to chrome profile

# Configure chrome
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir="+CHROME_USER) 
driver = webdriver.Chrome(executable_path=PATH)
action = ActionChains(driver)


driver.get("https://www.google.com/recaptcha/api2/demo")


def main():
    # Open the page in chrome
    driver.get("https://www.google.com/recaptcha/api2/demo")    
    time.sleep(1)

    # Find the element for submitting captcha 
    submit = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@id, "recaptcha-demo-submit")]')))

    # Move towards the submit key 
    curr = [0,0]                                       # Define current location
    end = [submit.location["x"], submit.location["y"]] # Define final location
    move(curr, end) # Move the cursor
    curr = end      # Ending location is now the current

    # Define the location of the CAPTCHA box (it is 50 units above)
    end = [submit.location["x"], submit.location["y"]-50]

    # Move the clicker towards the location above the for submit button and click
    move(curr, end)
    curr = end
    action.click()
    action.perform()

    # Wait so that the browser does not detect bot
    time.sleep(2)

    # Move back to submit button and click it
    end = [submit.location["x"], submit.location["y"]]
    move(curr, end)
    action.click()
    action.perform()

# Implement random movement
def move(curr, end):
    # loop while locations are not the same
    while curr[0] != end[0] or curr[1] != end[1]:
        rand = randint(0,2)
        # Move in the x axis
        if rand == 0:
            direction = end[0] - curr[0]

            # Define whether it should move one unit up or down
            if direction>10: direction = 10
            elif direction>0: direction = 1
            elif direction<-10: direction =-10
            elif direction<0: direction = -1
            else: direction = 0

            # Move the x value depending on whether x is positive or negative
            curr[0] = curr[0]+ direction
            action.move_by_offset(direction, 0) 

        
        # Move in the y axis
        elif rand == 1:
            direction = end[1] - curr[1]

            # Define whether it should move one unit up or down
            if direction>10: direction = 10
            elif direction>0: direction = 1
            elif direction<-10: direction =-10
            elif direction<0: direction = -1
            else: direction = 0

            # Move the x value depending on whether x is positive or negative
            curr[1] = curr[1]+ direction
            action.move_by_offset(0, direction)
        action.perform()
        print(curr)

if __name__ == '__main__':
      main()
