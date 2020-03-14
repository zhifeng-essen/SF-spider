import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_pdf(driver):
    driver.find_element(By.CSS_SELECTOR, ".menuBarTopItem:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, ".FormattedTextOptions_PDF > .printInclude > .clickAreaWrapper input").click()
    driver.find_element(By.ID, "FileExportMod_ExportModDialog_doactionbutton").click()


def input_cas(driver, CAS):
    driver.switch_to.frame(0)
    b = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".expMenuItem:nth-child(5)"))
    )
    b.click()
    driver.find_element(By.ID, "substanceIds").click()
    time.sleep(1)
    driver.find_element(By.ID, "substanceIds").send_keys(CAS)


def myf(driver, CAS):
    # 输入CAS
    input_cas(driver, CAS)
    # 点search
    driver.find_element(By.CSS_SELECTOR, "#substanceId .searchButton").click()
    time.sleep(5)
    # 进入化合物详情页
    driver.find_element(By.ID, "detail_1").click()
    time.sleep(3)
    # 下载pdf
    download_pdf(driver)


# 加载本地Firefox设置
profile = webdriver.FirefoxProfile(r'C:\Users\Setsuna\zqkc9rzc.dev-edition-default')
driver = webdriver.Firefox(firefox_profile=profile)
# set wait time
wait = WebDriverWait(driver, 15, 0.5)
driver.implicitly_wait(10)
# main url
driver.get("https://scifinder.cas.org/")
# 点yes
a = wait.until(
    # EC.presence_of_element_located((By.ID, "popupYes"))
    EC.element_to_be_clickable((By.ID, "popupYes"))
)
a.click()
time.sleep(5)
# 循环处理cas_list中的每个CAS号
cas_list = ["5304-71-2",
            "5262-69-1",
            "1240566-17-9"]
for casi in cas_list:
    driver.get("https://scifinder.cas.org/scifinder/defaultPage")
    # 等加载完首页
    time.sleep(3)
    myf(driver, casi)


