import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# //指定chromediver的位置，如果在默认路径，这两行可以省略。
# os.environ["webdriver.chrome.driver"] = executable_path
# options = webdriver.ChromeOptions()
# # options.add_argument("--user-data-dir="+r"C:/Users/Setsuna/AppData/Local/Google/Chrome/User Data")
# # driver = webdriver.Chrome(chrome_options=options)

# C:\Users\Setsuna\AppData\Roaming\Mozilla\Firefox\Profiles\zqkc9rzc.dev-edition-default
profile = webdriver.FirefoxProfile(r'C:\Users\Setsuna\zqkc9rzc.dev-edition-default')
driver = webdriver.Firefox(firefox_profile=profile)

# set wait time
wait = WebDriverWait(driver, 10, 1)
driver.implicitly_wait(10)
# main url
driver.get("https://scifinder.cas.org/")
# 点yes
a = wait.until(
    EC.presence_of_element_located((By.ID, "popupYes"))
)
a.click()
# 等加载完首页
time.sleep(3)
# 输入CAS
driver.switch_to.frame(0)
b = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".expMenuItem:nth-child(5)"))
)
b.click()
driver.find_element(By.ID, "substanceIds").click()
time.sleep(1)
driver.find_element(By.ID, "substanceIds").send_keys("50-00-0")
# c = wait.until(
#     EC.element_to_be_clickable((By.ID, "substanceIds"))
# )
# c.send_keys("25163-48-8")
# 点search
driver.find_element(By.CSS_SELECTOR, "#substanceId .searchButton").click()
# 进入化合物详情页
time.sleep(5)
# d = wait.until(
#     EC.presence_of_element_located((By.ID, "HotspotMod_hotspotwidgethighlight"))
# )
# d.click()
driver.find_element(By.ID, "detail_1").click()
time.sleep(5)
# # 下载pdf
# driver.find_element(By.CSS_SELECTOR, ".menuBarTopItem:nth-child(4)").click()
# driver.find_element(By.CSS_SELECTOR, ".FormattedTextOptions_PDF > .printInclude > .clickAreaWrapper input").click()
# driver.find_element(By.ID, "FileExportMod_ExportModDialog_doactionbutton").click()

actions = ActionChains(driver)
element1 = wait.until(
    EC.presence_of_element_located((By.ID, "HOTSPOT_hotspotwidgethighlight"))
)
actions.move_to_element(element1).perform()
element2 = driver.find_element(By.ID, "HOTSPOT_hotspotwidget_menu_contextmenu")
actions.move_to_element(element2).perform()
driver.find_element(By.ID, "HOTSPOT_hotspotwidget_menu_contextmenu").click()
driver.find_element(By.ID, "main_cm_ExportasImage").click()
