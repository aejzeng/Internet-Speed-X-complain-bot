from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

# Set Up Variables
PROMISE_UP = 50 # Set by your UP speed agreement with internet provider
PROMISE_DOWN = 150 # Set by your DOWN speed agreement with internet provider
X_ACCOUNT = os.environ.get("YOUR_OWN_ACCOUNT")
X_USERNAME = os.environ.get("YOUR_OWN_USERNAME")
X_PASSCODE = os.environ.get("YOUR_OWN_PASSCODE")
INTERNET_SPEED_TEST = "https://www.speedtest.net/result/16338400732"
X_URL = "https://x.com/i/flow/login"
#Create a class
class InternetSpeedXBot:

    def __init__(self):
        self.DOWN = 0
        self.UP = 0
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self):
        self.driver.get(INTERNET_SPEED_TEST)

        time.sleep(1)
        button_reject = self.driver.find_element(By.ID, "onetrust-reject-all-handler")
        button_reject.click()

        try:
            button_go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            button_go.click()
        except NoSuchElementException:
            print("go button not found")

        try:
            # Wait to get the internet speed check running
            time.sleep(45)
            # Fetch the down/up speed data
            self.DOWN = self.driver.find_element(By.CLASS_NAME, "download-speed").text
            print(f"down: {self.DOWN}")
            self.UP = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
            print(f"up: {self.UP}")
        except NoSuchElementException:
            print("Down/Up data not found.")

    def internet_speed_compare(self, down, up):
        if float(down) > float(self.DOWN) or float(up) > float(self.UP):
            bot.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get(X_URL)
        time.sleep(5)

        try:
            # Type in account
            account = self.driver.find_element(By.NAME, "text")
            account.send_keys(X_ACCOUNT)
        except NoSuchElementException:
            print("account input label not found")

        try:
            #After account, click NEXT button
            button_next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
            button_next.click()
            time.sleep(2)
        except NoSuchElementException:
            print("Next button not found")

        try:
            # Type in the username
            username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys(X_USERNAME)
            button_next_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
            button_next_username.click()
            time.sleep(1)
        except NoSuchElementException:
            print("username not found")

        try:
            passcode = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            passcode.send_keys(X_PASSCODE)
            button_login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
            button_login.click()
            time.sleep(5)
        except NoSuchElementException:
            print("passcode label not found")

        try:
            x = f"Hey Internet Provider, why is my internet speed {self.DOWN} down/{self.UP} up when I pay for {PROMISE_DOWN}down/{PROMISE_UP}UP?"
            cancel_cookie_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]/div/span/span')
            cancel_cookie_button.click()
            tweet_label = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweet_label.send_keys(x)
            post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
            post_button.click()

        except NoSuchElementException:
            print("tweet label not found.")

bot = InternetSpeedXBot()
bot.get_internet_speed()
# bot.tweet_at_provider()
bot.internet_speed_compare(PROMISE_DOWN, PROMISE_UP)
