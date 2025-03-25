from instagram_bot import InstaBot
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


try:
    bot = InstaBot()
    bot.open_browser()
    bot.login()

    time.sleep(5)

    try:
        WebDriverWait(bot.driver, 5).until(EC.presence_of_element_located((By.NAME, "verificationCode")))
        code = input("Enter the 6-digit verification code: ")
        bot.enter_code(code)
        time.sleep(3)
    except:
        print("Two-step verification is not required.")

    # bot.click_reels()
    # time.sleep(10)
    # bot.scroll_through_reels().click()
    # time.sleep(3)
    # start = 1
    # for _ in range(10):
    #     bot.actions.move_to_element(bot.scroll_through_reels()).send_keys(Keys.ARROW_DOWN).perform()
        
    #     time.sleep(2)
    #     bot.like_reel().click()
    #     print(f"{start}✅ Reel Liked Successfully!")
    #     start += 1
    # Save login info prompt
    bot.save_login_info()
    time.sleep(2)

    bot.scroll_and_like()
    time.sleep(5)

 

    # # Open Messenger
    # bot.click_messenger()
    # time.sleep(5)

    # # Disable notification prompt
    # bot.turn_off_notifications()
    # time.sleep(5)




except Exception as e:
    print(f"Error: {e}")

finally:
    bot.close_browser()
