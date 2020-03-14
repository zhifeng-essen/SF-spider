import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import win32api
import win32con
from taskp3 import p3


def is_exist_element(by, el):
    s = driver.find_elements(by, el)
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True


def is_element_visible(el):
    try:
        the_element = EC.visibility_of_element_located(el)
        assert the_element(driver)
        return True
    except:
        return False


def my_init():
    profile = webdriver.FirefoxProfile(
        r'C:\Users\Oriental Stork\AppData\Roaming\Mozilla\Firefox\Profiles\pz80g50k.dev-edition-default'
    )
    global driver
    driver = webdriver.Firefox(firefox_profile=profile)
    # set wait time
    global wait
    wait = WebDriverWait(driver, 5, 0.5)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://scifinder.cas.org/")
    time.sleep(3)
    if is_exist_element(By.ID, "popupYes"):
        driver.find_element(By.ID, "popupYes").click()
    time.sleep(3)


def counts():
    return str(driver.find_element(By.CSS_SELECTOR, "span.selectedCount").text).split()[2]


def ctrlS():
    win32api.keybd_event(17, 0, 0, 0)  # Ctrl
    win32api.keybd_event(83, 0, 0, 0)  # S
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)


def save(driver, filename):
    time.sleep(5)
    ctrlS()
    time.sleep(3)
    os.system('saveHtmlFiles.exe "D:\\P3HTML\\HTML2\\' + filename + '"')
    time.sleep(5)

    driver.find_element(By.ID, "detail_1").click()
    time.sleep(5)
    ctrlS()
    time.sleep(3)
    os.system('saveHtmlFiles.exe "D:\\P3HTML\\HTML3\\' + filename + '"')
    time.sleep(5)


def main():
    m = ''
    logfile = "Log01.txt"
    try:
        my_init()
        with open(logfile, 'r') as f:
            lines = f.readlines()
            last = lines[-1].split()[0]
        INDEX = p3.index(last) + 1
        for mol in p3[INDEX:]:
            # load index page
            m = mol
            print("Processing " + m)
            driver.get("https://scifinder.cas.org/scifinder/defaultPage")
            time.sleep(5)
            # click draw area
            driver.switch_to.frame(0)
            k = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#structureCasDrawArea > div:nth-child(1) > div:nth-child(2) > div:nth-child(3)"))
            )
            k.click()
            time.sleep(2)
            # upload mol file
            driver.find_element(By.CSS_SELECTOR, ".cdFileImport").click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "#cdFileChooserForm > input:nth-child(2)").send_keys(
                'D:\\newmol\\' + mol + '.mol')
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR, "#cdSearchTypeSTRUCTURE > label:nth-child(2)").click()
            driver.find_element(By.ID, "cdOK").click()
            time.sleep(5)
            if is_element_visible((By.CSS_SELECTOR, "#cdWarningsDlg > div:nth-child(2) > div:nth-child(1)")):
                driver.find_element(By.ID, "cdWarnDlgContinue").click()
                time.sleep(3)
            if is_exist_element(By.CSS_SELECTOR, "#cdErrorDisplay"):
                with open(logfile, 'a') as o:
                    o.write(mol + "\tStrctError\n")
            else:
                driver.find_element(By.ID, "onlySingleComponents").click()
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR, "#structure .searchButton").click()
                time.sleep(10)  # important time point
                if is_exist_element(
                        By.CSS_SELECTOR, ".detailListWrapper"
                ) and driver.find_element(By.CSS_SELECTOR, ".detailListWrapper").text == "No candidates available":
                    with open(logfile, 'a') as o:
                        o.write(mol + "\tWarning|0\n")
                else:
                    if is_exist_element(By.CSS_SELECTOR, "#submitCandidates"):
                        ctrlS()
                        time.sleep(3)
                        os.system('saveHtmlFiles.exe "D:\\P3HTML\\HTML1\\' + mol + '"')
                        time.sleep(5)
                        driver.find_element(By.CSS_SELECTOR, "#selectAll").click()
                        time.sleep(2)
                        driver.find_element(By.CSS_SELECTOR, "#submitCandidates").click()
                        time.sleep(10)
                        answer_count = counts()
                        r = mol + "\tT1|" + answer_count + "\n"
                        save(driver, mol)
                        with open(logfile, 'a') as o:
                            o.write(r)
                    elif is_exist_element(By.CSS_SELECTOR, "#resultsCount"):
                        answer_count = counts()
                        r = mol + "\tT2|" + answer_count + "\n"
                        save(driver, mol)
                        with open(logfile, 'a') as o:
                            o.write(r)
                    elif is_exist_element(
                            By.CSS_SELECTOR, "#analysisArea > div:nth-child(1) > div:nth-child(2) > em:nth-child(1)"
                    ) and driver.find_element(
                        By.CSS_SELECTOR, "#analysisArea > div:nth-child(1) > div:nth-child(2) > em:nth-child(1)"
                    ).text == "No substances available":
                        with open(logfile, 'a') as o:
                            o.write(mol + "\tWarning|1\n")
                        continue

    except Exception as e:
        print(e)
        if m != '':
            with open(logfile, 'a') as o:
                o.write(m + "\tPass\n")
            print("Pass " + m)
        driver.quit()
        main()


if __name__ == '__main__':
    main()
