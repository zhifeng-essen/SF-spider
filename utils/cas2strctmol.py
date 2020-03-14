import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def input_cas(driver, CAS):
    driver.find_element(By.CSS_SELECTOR, ".cdTextToStructure").click()
    driver.find_element(By.NAME, "cdAddToEditorText").send_keys(CAS)
    driver.find_element(By.CSS_SELECTOR, "#cdAddToEditorDlg .cdButton:nth-child(1)").click()


def export_molfile(driver, CAS):
    driver.find_element(By.CSS_SELECTOR, ".cdFileExport").click()
    driver.find_element(By.CSS_SELECTOR, ".cdExportFileNameText").clear()
    driver.find_element(By.CSS_SELECTOR, ".cdExportFileNameText").send_keys(CAS)
    driver.find_element(By.CSS_SELECTOR, ".cdFieldset > label:nth-child(3) > input").click()
    driver.find_element(By.CSS_SELECTOR, ".cdButtonRow:nth-child(5) > .cdButton:nth-child(1)").click()


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
# driver.find_element(By.CSS_SELECTOR, "#structureCasDrawArea > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span:nth-child(2)").click()
# driver.find_element(By.CSS_SELECTOR, "#structureCasDrawArea .editorAvailable > .editorLink:nth-child(1)").click()
k = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#structureCasDrawArea > div:nth-child(1) > div:nth-child(2) > div:nth-child(3)"))
)
k.click()
time.sleep(3)
cas_list = ["5304-71-2",
            "5262-69-1",
            "1240566-17-9"]
for casi in cas_list:
    input_cas(driver, casi)
    time.sleep(3)
    export_molfile(driver, casi)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".cdUndo").click()










