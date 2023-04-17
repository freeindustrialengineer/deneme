from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import logging
import datetime
import os
import tkinter.messagebox as mbox


logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
if not os.path.exists('logs'):
    os.makedirs('logs')
file_handler = logging.FileHandler(f'logs/{datetime.date.today()}.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class InstagramBot:
    #GİRİŞ YAPMA,BİLGİLERİN KAYDEDİLMESİ
    def __init__(self, username, password, login_choice,background_choice):
        logger.info("****************** %s Bot başladı. Username: %s Password: %s ******************", datetime.datetime.now(), username, password)
        #Log In
        self.username = username
        self.password = password
        self.login_choice = login_choice
        self.background_choice = background_choice
        self.should_stop = False
        if login_choice=="1":
            chrome_options = Options()
            if self.background_choice==True:
                 chrome_options.headless = True
                 chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument("user-data-dir=C:\\Users\\merta\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
            self.driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
            self.driver.maximize_window()
            self.driver.get('https://instagram.com')
            time.sleep(1)
            self.username2=self.driver.find_element(By.CSS_SELECTOR,".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._aak1._a6hd").text


        elif login_choice=="2":
            chrome_options = Options()
            self.driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
            if self.background_choice==True:
                 chrome_options.headless = True
            self.driver.get('https://www.instagram.com/')
            time.sleep(10)
            username_form = self.driver.find_element(By.NAME, 'username')
            password_form = self.driver.find_element(By.NAME, 'password')
            username_form.click()
            username_form.send_keys(username)
            password_form.click()
            password_form.send_keys(password)
            self.driver.implicitly_wait(5)
            time.sleep(10)
            log_in_form = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            log_in_form.click()
            time.sleep(10)

        elif login_choice=="3":
            chrome_options = Options()
            chrome_options.add_argument("user-data-dir=C:\\Users\\merta\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
            self.driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
            self.driver.get('https://instagram.com')
            mbox.showinfo("Saving Credentials", "Please log in your instagram account and after saving your credentials restart the bot.")

    #Profil analizi, takipçi, takip edilen ve aradaki farkların görüntülenmesi
    def compare_profile(self,profile):
        self.should_stop = False
        while self.should_stop==False:
            print("Profil analiz fonksiyonu başladı.")
            self.driver.get(f'https://www.instagram.com/{profile}/')
            if self.should_stop == True:
                break
            time.sleep(10)
            self.driver.get(f'https://www.instagram.com/{profile}/followers/')
            if self.should_stop == True:
                break
            time.sleep(10)
            followers_panel = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
            last_ht, ht = 0, 1
            while last_ht != ht:
                if self.should_stop == True:
                    break
                last_ht = ht
                ht = self.driver.execute_script(""" arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight; """,followers_panel)
                try:
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_aanq"]')))
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "_ab8w  _ab94 _ab97 _ab9f _ab9m _ab9p  _abc0 _abcm")))
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH, '(//div[@class="_aano"])')))
                except:
                    if self.should_stop == True:
                        break
                    time.sleep(random.randint(6,10))
                if self.should_stop == True:
                    break
                time.sleep(random.randint(4,8))
                if self.should_stop == True:
                    break
                WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH, '(//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"])')))
                if self.should_stop == True:
                    break
            WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH,'(//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"])')))
            if self.should_stop == True:
                break
            list_of_followers = list(map(lambda x: x.text, self.driver.find_elements(By.XPATH, '(//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"])')))
            if self.should_stop == True:
                break
            time.sleep(5)
            print("Takipçiler çekildi")
            print("Toplam takipçi: ",len(list_of_followers))
            # Following List
            if self.should_stop == True:
                break
            self.driver.get(f'https://www.instagram.com/{profile}/')
            time.sleep(10)
            if self.should_stop == True:
                break
            self.driver.get(f'https://www.instagram.com/{profile}/following/')
            time.sleep(10)
            following_panel = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
            last_ht, ht = 0, 1
            while last_ht != ht:
                if self.should_stop == True:
                    break
                last_ht = ht
                ht = self.driver.execute_script(""" arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight; """,following_panel)
                try:
                    WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_aanq"]')))
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "_ab8w  _ab94 _ab97 _ab9f _ab9m _ab9p  _abc0 _abcm")))
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH, '(//div[@class="_aano"])')))
                except:
                    if self.should_stop == True:
                        break
                    time.sleep(random.randint(6,10))
                if self.should_stop == True:
                    break
                time.sleep(random.randint(4,8))
                WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH,'(//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"])')))
                if self.should_stop == True:
                    break
            WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH,'(//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"])')))
            if self.should_stop == True:
                break
            list_of_followings = list(map(lambda x: x.text, self.driver.find_elements(By.XPATH, '(//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"])')))
            print("Takip edilenler çekildi")
            print("Toplam takip edilen: ",len(list_of_followings))

            # Data Frame listesi oluşturma
            if self.should_stop == True:
                break
            yoursnofollow = list(set(list_of_followers) - set(list_of_followings))
            theynofollow = list(set(list_of_followings) - set(list_of_followers))
            ltheynofollow, lyoursnofollow, llist_of_followers, llist_of_followings = len(theynofollow), len(
                yoursnofollow), len(list_of_followers), len(list_of_followings)
            max_len = max(ltheynofollow, lyoursnofollow, llist_of_followers, llist_of_followings)
            if self.should_stop == True:
                break
            if not max_len == ltheynofollow:
                theynofollow.extend([''] * (max_len - ltheynofollow))
            if not max_len == lyoursnofollow:
                yoursnofollow.extend([''] * (max_len - lyoursnofollow))
            if not max_len == llist_of_followers:
                list_of_followers.extend([''] * (max_len - llist_of_followers))
            if not max_len == llist_of_followings:
                list_of_followings.extend([''] * (max_len - llist_of_followings))
            if self.should_stop == True:
                break
            tablo = {'Takipçiler': list_of_followers, 'Takip Ettiklerin': list_of_followings,
                     'Seni Takip Etmeyenler': theynofollow, 'Senin Takip Etmediklerin': yoursnofollow}
            df = pd.DataFrame(data=tablo)
            print(df)
            df.to_excel(f"{profile}.xlsx")
            self.driver.get('https://www.instagram.com/')
        if self.should_stop == True:
            mbox.showinfo("Stopped", "The bot has stopped.")

    #Seni takip etmeyenlerin takipten çıkartılması
    def unfollow_excel(self,file_path):
        self.should_stop = False
        while self.should_stop==False:
            print("Takipten çıkma fonksiyonu başladı.")
            if self.should_stop == True:
                break
            df = pd.read_excel(file_path)
            unfollowlist = df['Usernames'].tolist()
            if self.should_stop == True:
                break
            self.driver.get('https://www.instagram.com/')
            time.sleep(2)
            if self.should_stop == True:
                break
            self.driver.get(f'https://www.instagram.com/{self.username}/following/')
            time.sleep(5)
            following_panel = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
            last_ht, ht = 0, 1
            c = 0
            if self.should_stop == True:
                break
            while last_ht != ht:
                last_ht = ht
                if self.should_stop == True:
                    break
                ht = self.driver.execute_script( """ arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight; """,following_panel)
                if self.should_stop == True:
                    break
                WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "_ab8w  _ab94 _ab97 _ab9f _ab9m _ab9p  _abc0 _abcm")))
                if self.should_stop == True:
                    break
                time.sleep(random.randint(4,8))
                try:
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_aanq"]')))
                except:
                    if self.should_stop == True:
                        break
                    time.sleep(random.randint(8, 12))
                WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH, '(//div[@class="_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm"])')))
                time.sleep(random.randint(2, 3))
                if self.should_stop == True:
                    break
                time.sleep(random.randint(4,8))
                elements = self.driver.find_elements(By.XPATH, '//div[@class="_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm"]')[-12:]
                for element in elements:
                    if self.should_stop == True:
                        break
                    button = element.find_element(By.XPATH, ".//div[text()='Takiptesin']")
                    if element.text.split('\n')[0] in unfollowlist:
                        c+=1
                        print(element.text.split('\n')[0]," Çıkartıldı. Toplam çıkarılan: ",c)
                        if self.should_stop == True:
                            break
                        self.driver.execute_script('arguments[0].click()', button)
                        if self.should_stop == True:
                            break
                        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH,"//button[@class='_a9-- _a9-_']")))
                        if self.should_stop == True:
                            break
                        time.sleep(random.randint(3,5))
                        if self.should_stop == True:
                            break
                        button2 =self.driver.find_element(By.XPATH, "//button[@class='_a9-- _a9-_']")
                        #button2.click()
                        actions = ActionChains(self.driver)
                        if self.should_stop == True:
                            break
                        actions.move_to_element(button2).click().perform()
                        try:
                            # Find the element representing the pop-up
                            if self.should_stop == True:
                                break
                            time.sleep(4)
                            ok_button = self.driver.find_element(By.XPATH, "//button[text()='Tamam']")
                            # Click the "OK" button
                            ok_button.click()
                        except NoSuchElementException:
                            if self.should_stop == True:
                                break
                            pass
                        if self.should_stop == True:
                            break
                        time.sleep(random.randint(38, 55))
                    else:
                        if self.should_stop == True:
                            break
                        continue
        if self.should_stop == True:
            mbox.showinfo("Stopped", "The bot has stopped.")

    #Takipçi çıkarma fonksiyonu excel olmadan

    def unfollow(self):
        self.should_stop = False
        while self.should_stop==False:
            print("Takipten çıkma fonksiyonu başladı.")
            if self.should_stop == True:
                break
            self.driver.get('https://www.instagram.com/')
            time.sleep(2)
            if self.should_stop == True:
                break
            self.driver.get(f'https://www.instagram.com/{self.username}/following/')
            time.sleep(5)
            following_panel = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
            last_ht, ht = 0, 1
            c = 0
            if self.should_stop == True:
                break
            while last_ht != ht:
                last_ht = ht
                if self.should_stop == True:
                    break
                ht = self.driver.execute_script( """ arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight; """,following_panel)
                if self.should_stop == True:
                    break
                WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "_ab8w  _ab94 _ab97 _ab9f _ab9m _ab9p  _abc0 _abcm")))
                if self.should_stop == True:
                    break
                time.sleep(random.randint(4,8))
                try:
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_aanq"]')))
                except:
                    if self.should_stop == True:
                        break
                    time.sleep(random.randint(8, 12))
                WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH, '(//div[@class="_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm"])')))
                time.sleep(random.randint(2, 3))
                if self.should_stop == True:
                    break
                time.sleep(random.randint(4,8))
                elements = self.driver.find_elements(By.XPATH, '//div[@class="_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm"]')[-12:]
                for element in elements:
                    if self.should_stop == True:
                        break
                    button = element.find_element(By.XPATH, ".//div[text()='Takiptesin']")
                    c += 1
                    print(element.text.split('\n')[0], " Çıkartıldı. Toplam çıkarılan: ", c)
                    if self.should_stop == True:
                        break
                    self.driver.execute_script('arguments[0].click()', button)
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 60).until(
                        EC.visibility_of_element_located((By.XPATH, "//button[@class='_a9-- _a9-_']")))
                    if self.should_stop == True:
                        break
                    time.sleep(random.randint(3, 5))
                    if self.should_stop == True:
                        break
                    button2 = self.driver.find_element(By.XPATH, "//button[@class='_a9-- _a9-_']")
                    # button2.click()
                    actions = ActionChains(self.driver)
                    if self.should_stop == True:
                        break
                    actions.move_to_element(button2).click().perform()
                    try:
                        # Find the element representing the pop-up
                        if self.should_stop == True:
                            break
                        time.sleep(4)
                        ok_button = self.driver.find_element(By.XPATH, "//button[text()='Tamam']")
                        # Click the "OK" button
                        ok_button.click()
                    except NoSuchElementException:
                        if self.should_stop == True:
                            break
                        pass
                    if self.should_stop == True:
                        break
                    time.sleep(random.randint(38, 55))
        if self.should_stop == True:
            mbox.showinfo("Stopped", "The bot has stopped.")

    #Belirli bir profilin tüm takipçilerinin liste şeklinde çıkartılması
    def get_followers(self, profile_name=None):
        self.should_stop = False
        while self.should_stop==False:
            if self.should_stop == True:
                break
            self.driver.get('https://instagram.com')
            if self.should_stop == True:
                break
            time.sleep(5)
            if self.should_stop == True:
                break
            self.driver.get(f'https://www.instagram.com/{profile_name}/')
            time.sleep(10)
            if self.should_stop == True:
                break
            self.driver.get(f'https://www.instagram.com/{profile_name}/followers/')
            if self.should_stop == True:
                break
            time.sleep(20)
            followers_panel =self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
            last_ht, ht = 0, 1
            while last_ht != ht:

                last_ht = ht
                if self.should_stop == True:
                    break
                ht = self.driver.execute_script(""" arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight; """, followers_panel)
                if self.should_stop == True:
                    break
                WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "_ab8w  _ab94 _ab97 _ab9f _ab9m _ab9p  _abc0 _abcm")))
                if self.should_stop == True:
                    break
                WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH, '(//div[@class="_aano"])')))
                if self.should_stop == True:
                    break
            WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH, '(//div[@class="_aano"])')))
            if self.should_stop == True:
                break
            list_of_followers = list(map(lambda x: x.text, self.driver.find_elements(By.XPATH, '//div[@class="_aano"]//a/span/div')))
            if self.should_stop == True:
                break
            tablo = {'Takipçiler': list_of_followers}
            df = pd.DataFrame(data=tablo)
            if self.should_stop == True:
                break
            df.to_excel(f"{profile_name}.xlsx")
            return list_of_followers
        if self.should_stop == True:
            mbox.showinfo("Stopped", "The bot has stopped.")

    #Belirli bir profilin tüm takipçilerinin biyografilerine göre liste şeklinde çıkartılması
    def filter_profiles(self,words=None,profiles=None):
        print("Profil filtreleme fonksiyonu başladı.")
        if words is None:
                words=list(input("Filtrelemek istediğiniz kelimeleri aralarında ',' olacak şekilde giriniz") )
        self.driver.quit()
        if profiles is None:
            targetprofile=input("Lütfen takipçilerin çekileceği kullanıcı ismini giriniz.")
            profiles=self.get_followers(targetprofile)
        driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver.exe')
        driver.get('https://www.instagram.com/')
        time.sleep(5)
        filteredlist=[]
        a = 0
        b = 0
        for i in profiles:
            try:
                driver.get(f'https://www.instagram.com/{i}/')
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="_aa_c"])')))
                text = driver.find_element(By.XPATH, "//div[@class='_aa_c']").text.upper()
                if text in words:
                    filteredlist.append(i)
                    a = 0
                    b += 1
            except:
                a += 1
                if a == 2:
                    a = 0
                    driver.quit()
                    driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver.exe')
                    continue
                else:
                    continue
        print("Filtreleme işlemi bitti.Bu kadar kişi filtrelendi:", b)
        tablo = {'takipçiler': filteredlist}
        df = pd.DataFrame(data=tablo)
        df.to_excel("filteredlist.xlsx")
        return filteredlist

    #Filtrelenmiş listeye takipçi isteği gönderilmesi, ya da herhangi bir listeye
    def send_requests_filtered(self,file_path):
        df = pd.read_excel(file_path)
        requestlist = df['Usernames'].tolist()
        self.should_stop = False
        while self.should_stop==False:
            b = 0
            c = 0
            if self.should_stop == True:
                break
            for i in requestlist:
                if self.should_stop == True:
                    break
                follower = self.driver.get(f'https://www.instagram.com/{i}/')
                if self.should_stop == True:
                    break
                time.sleep(random.randint(7, 21))
                if self.should_stop == True:
                    break
                if self.driver.find_element(By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade']").text == "Takip Et":
                    if self.should_stop == True:
                        break
                    self.driver.find_element(By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade']").click()
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade']")))
                    b += 1
                    if self.should_stop == True:
                        break
                    time.sleep(random.randint(6, 12))

                elif self.driver.find_element(By.XPATH,
                                              "//div[@class='_aacl _aaco _aacw _aad6 _aade']").text == "İstek Gönderildi":
                    if self.should_stop == True:
                        break
                    self.driver.find_element(By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade']").click()
                    if self.should_stop == True:
                        break
                    time.sleep(4)
                    self.driver.find_element(By.XPATH, "//button[@class='_a9-- _a9-_']").click()
                    if self.should_stop == True:
                        break
                    time.sleep(5)

                    if self.driver.find_element(By.XPATH,
                                                "//div[@class='_aacl _aaco _aacw _aad6 _aade']").text == "Takip Et":
                        self.driver.find_element(By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade']").click()
                        WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade']")))
                        c += 1
                        print(i)
                        time.sleep(random.randint(5, 10))
                    else:
                        time.sleep(random.randint(5, 7))
                        continue
        if self.should_stop == True:
            mbox.showinfo("Stopped", "The bot has stopped.")

    #Profilin takipçilerine girip following boxtan takipçi isteği gönderme
    def send_requests_following(self,profile):
        self.should_stop = False
        while self.should_stop==False:
            logger.info("%s Profilden takip atma fonksiyonu başladı.", datetime.datetime.now())
            print("Profilden takip atma fonksiyonu başladı.")
            if self.should_stop == True:
                break
            df = pd.read_excel('myfollow.xlsx')  # can also index sheet by name or fetch all sheets
            myfollowers = df['takip edilenler'].tolist()
            self.driver.get('https://instagram.com')  # Already authenticated
            if self.should_stop == True:
                break
            time.sleep(15)
            if self.should_stop == True:
                break
            self.driver.get(f'https://www.instagram.com/{profile}/')
            if self.should_stop == True:
                break
            time.sleep(15)
            if self.should_stop == True:
                break
            self.driver.get(f'https://www.instagram.com/{profile}/followers/')
            c = 0
            if self.should_stop == True:
                break
            time.sleep(5)
            followers_panel = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
            last_ht, ht = 0, 1
            i = 1
            while last_ht != ht:
                last_ht = ht
                # scroll down and retrun the height of scroll
                try:
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located(
                        (By.CLASS_NAME, "_ab8w  _ab94 _ab97 _ab9f _ab9m _ab9p  _abc0 _abcm")))
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 45).until(
                        EC.presence_of_all_elements_located((By.XPATH, '(//div[@class="_aano"])')))
                    if self.should_stop == True:
                        break
                    WebDriverWait(self.driver, 45).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                              '(//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"])')))
                except:
                    if self.should_stop == True:
                        break
                    time.sleep(random.randint(4, 8))
                elements = self.driver.find_elements(By.XPATH,'//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"]')[-12:]
                for element in elements:
                    if self.should_stop == True:
                        break
                    i += 1
                    button = element.find_element(By.XPATH,".//div[text()='Takip Et' or text()='Takiptesin' or text()='İstek Gönderildi']")
                    if button.text == "Takip Et" and element.text.split('\n')[0] not in myfollowers:
                        self.driver.execute_script('arguments[0].click()', button)
                        try:
                            # Find the element representing the pop-up
                            if self.should_stop == True:
                                break
                            time.sleep(random.randint(4, 8))
                            ok_button = self.driver.find_element(By.XPATH, "//button[text()='Tamam']")
                            time.sleep(random.randint(1, 2))
                            # Click the "OK" button
                            ok_button.click()
                            if self.should_stop == True:
                                break
                            time.sleep(5)
                        except NoSuchElementException:
                            logger.error("******", datetime.datetime.now(), '- Following', element.text.split('\n')[0],
                                         "******")
                            self.driver.save_screenshot(f'logs/{datetime.date.today()}-error.png')
                            pass
                        c += 1
                        print("Toplam gönderilen takipçi sayısı:", c, "En son gönderilen:", element.text.split('\n')[0])
                        logger.info("%s - Following %s Total: %d", datetime.datetime.now(), element.text.split('\n')[0], c)
                        if self.should_stop == True:
                            break
                        time.sleep(random.randint(41, 55))
                    else:
                        continue
                    if self.should_stop == True:
                        break
                    ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", followers_panel)
                    logger.info("%s Profilden takip atma fonksiyonu bitti. Toplam takipçi sayısı: %d",
                                datetime.datetime.now(), c)
                    print("Profilden takip atma fonksiyonu bitti. Toplam takipçi sayısı:", c)
        if self.should_stop==True:
            mbox.showinfo("Stopped", "The bot has stopped.")

    #Stop fonksiyonu
    def stop(self):
        self.should_stop = True
        print("Bot durduluyor")
        logger.info("****************** %s Bot sona erdi. ******************", datetime.datetime.now())

    #Username field için
    def username_insert(self):
        return self.username2

    #Log için fonksiyon
    def __del__(self):
        logger.info("****************** %s Bot sona erdi. ******************", datetime.datetime.now())

