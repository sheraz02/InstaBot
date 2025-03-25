from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import environ
import os
from selenium.webdriver.common.action_chains import ActionChains
import time


env = environ.Env()
environ.Env.read_env()

class InstaBot:
    def __init__(self):
        self.url = 'https://www.instagram.com/'
        self.username = env('INSTAUSERNAME')
        self.password = env('PASSWORD')
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)


    def open_browser(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.quit()

    def login(self, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(self.username)
        wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(self.password)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    def enter_code(self, code):
        wait = WebDriverWait(self.driver, 15)
        code_input = wait.until(EC.presence_of_element_located((By.NAME, "verificationCode")))
        code_input.send_keys(code)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]").click()

    def save_login_info(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            not_now_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Not now']")))
            not_now_btn.click()
        except:
            pass 

    def click_messenger(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            messenger_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Direct messaging - 0 new notifications link']")))
            messenger_icon.click()
        except:
            pass  

    def turn_off_notifications(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            not_now_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Not now']")))
            not_now_btn.click()
        except:
            pass  
    
    def click_reels(self):
        reels_link = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Reels']]")))
        reels_link.click()
    
    def scroll_through_reels(self):
        reels_container = self.driver.find_element(By.CLASS_NAME, "x1qjc9v5")
        return reels_container
    
    def like_reel(self):
        like_button = self.driver.find_element(By.XPATH, "//svg[@aria-label='Like']/ancestor::div[@role='button']")
        return like_button
    
    def like_post(self):
        try:
            like_button = self.driver.find_element(By.XPATH, "//span[@aria-label='Like']")  
            like_button.click()
            print("Liked the post!")
        except Exception as e:
            print("Like button not found:", e)

        self.driver.save_screenshot("liked_post.png")
    
    def main_click(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "main[role='main']").click()
        except:
            print('failed to click')

    def scroll_and_like(self):
  

        for _ in range(10):  # Scroll through 10 posts
            try:
            # Find the Like button (modify XPath if needed)
                like_buttons = self.driver.find_elements(By.XPATH, "//span[@aria-label='Like']")
            
                for like_button in like_buttons:
                    like_button.click()
                    print("Liked a post!")
                    time.sleep(2)  # Pause before scrolling

            # Scroll down using Arrow Down key
                body = self.driver.find_element(By.TAG_NAME, "body")
                body.send_keys(Keys.ARROW_DOWN)
                time.sleep(3)  # Wait for new content to load

            except Exception as e:
                print("Error:", e)

    

