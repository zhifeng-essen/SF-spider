import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_exist_element(by, el):
    s = driver.find_elements(by, el)
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True


def my_init():
    # 加载本地Firefox设置
    profile = webdriver.FirefoxProfile(
        r'C:\Users\Setsuna\AppData\Roaming\Mozilla\Firefox\Profiles\zqkc9rzc.dev-edition-default')
    global driver
    driver = webdriver.Firefox(firefox_profile=profile)
    # set wait time
    global wait
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


def save(driver, filename):
    driver.find_element(By.CSS_SELECTOR, "#answerPersistenceId > .menuBarTopItem:nth-child(3) > .label").click()
    driver.find_element(By.CSS_SELECTOR, ".dataTypeAKTXT:nth-child(1)").click()
    driver.find_element(By.ID, "fileName").clear()
    driver.find_element(By.ID, "fileName").send_keys(filename)
    driver.find_element(By.ID, "FileExportMod_ExportModDialog_doactionbutton").click()
    time.sleep(5)


my_init()
inchidict = {
    "MOL1": "InChI=1S/C30H48O2/c1-20(19-31)9-8-10-21(2)22-13-17-29(6)23(22)11-12-25-28(5)16-15-26(32)27(3,4)24(28)14-18-30(25,29)7/h9,22-25,31H,2,8,10-19H2,1,3-7H3/b20-9+/t22-,23-,24-,25-,28+,29-,30-/m1/s1",
    "MOL2": "InChI=1S/C27H40O11/c1-14(2)8-20(29)37-19-10-26(32)18(12-34-25(36-17(7)28)23(26)27(19)13-35-27)11-33-24(31)22(16(5)6)38-21(30)9-15(3)4/h12,14-16,19,22-23,25,32H,8-11,13H2,1-7H3/t19-,22-,23+,25+,26-,27+/m0/s1",
    "MOL3": "InChI=1S/C16H28O2/c1-13(2)10-16-9-11(13)5-7-14(16,3)8-6-12(17)15(16,4)18/h11-12,17-18H,5-10H2,1-4H3/t11-,12-,14+,15+,16-/m0/s1"

}
for mol in inchidict:
    # 等加载完首页
    driver.get("https://scifinder.cas.org/scifinder/defaultPage")
    time.sleep(5)
    driver.switch_to.frame(0)
    k = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#structureCasDrawArea > div:nth-child(1) > div:nth-child(2) > div:nth-child(3)"))
    )
    k.click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".cdTextToStructure").click()
    inchi = inchidict[mol]
    driver.find_element(By.NAME, "cdAddToEditorText").send_keys(inchi)
    driver.find_element(By.CSS_SELECTOR, "#cdAddToEditorDlg .cdButton:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#cdSearchTypeSTRUCTURE > label:nth-child(2)").click()
    driver.find_element(By.ID, "cdOK").click()
    time.sleep(3)

    if is_exist_element(By.CSS_SELECTOR, "#cdErrorDisplay"):
        print("error")
    else:
        driver.find_element(By.CSS_SELECTOR, "#structure .searchButton").click()
        time.sleep(5)
        if is_exist_element(By.CSS_SELECTOR, "span.selectedCount"):
            save(driver, mol)
        elif is_exist_element(By.CSS_SELECTOR, ".selectOptions"):
            driver.find_element(By.ID, "selectAll").click()
            driver.find_element(By.ID, "submitCandidates").click()
            time.sleep(5)
            save(driver, mol)


# time.sleep(5)
# print(driver.find_element(By.CSS_SELECTOR, "span.selectedCount").text)
# print(str(driver.find_element(By.CSS_SELECTOR, "span.selectedCount").text).split())
