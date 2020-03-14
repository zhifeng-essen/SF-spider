import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 加载本地Firefox设置
profile = webdriver.FirefoxProfile(r'C:\Users\Setsuna\AppData\Roaming\Mozilla\Firefox\Profiles\zqkc9rzc.dev-edition-default')
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

driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, "#structureCasDrawArea > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span:nth-child(2)").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".cdTextToStructure").click()
driver.find_element(By.NAME, "cdAddToEditorText").send_keys("InChI=1S/C30H48O2/c1-20(19-31)9-8-10-21(2)22-13-17-29(6)23(22)11-12-25-28(5)16-15-26(32)27(3,4)24(28)14-18-30(25,29)7/h9,22-25,31H,2,8,10-19H2,1,3-7H3/b20-9+/t22-,23-,24-,25-,28+,29-,30-/m1/s1")
driver.find_element(By.CSS_SELECTOR, "#cdAddToEditorDlg .cdButton:nth-child(1)").click()
# driver.find_element(By.NAME, "cdSearchTypes").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#cdSearchTypeSTRUCTURE > label:nth-child(2)").click()
driver.find_element(By.ID, "cdOK").click()

time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#structure .searchButton").click()
time.sleep(5)

# InChI=1S/C30H48O2/c1-20(19-31)9-8-10-21(2)22-13-17-29(6)23(22)11-12-25-28(5)16-15-26(32)27(3,4)24(28)14-18-30(25,29)7/h9,22-25,31H,2,8,10-19H2,1,3-7H3/b20-9+/t22-,23-,24-,25-,28+,29-,30-/m1/s1
driver.find_element(By.ID, "selectAll").click()
driver.find_element(By.ID, "submitCandidates").click()
# # 下载包含CAS的txt
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#answerPersistenceId > .menuBarTopItem:nth-child(3) > .label").click()
driver.find_element(By.CSS_SELECTOR, ".dataTypeAKTXT:nth-child(1)").click()
driver.find_element(By.ID, "FileExportMod_ExportModDialog_doactionbutton").click()
