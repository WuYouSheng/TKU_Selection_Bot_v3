import argparse
import base64
from tkinter import messagebox

import cryptocode
import json
import logging
import os
import pathlib
import platform
import sys
import time

import chromedriver_autoinstaller_max
from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,NoSuchWindowException,UnexpectedAlertPresentException,WebDriverException)
from selenium.webdriver.chrome.service import Service



# Const Variable Definition
CONST_COMPILE_TIME = "2024.01.27"
CONST_APP_VERSION = "WYSHBot" + "(" + CONST_COMPILE_TIME + ")"
CONST_WYSHBOT_CONFIG_FILE = "settings.json"
CONST_SELECTION_FILE = "SelectionList.json"
CONST_LICENSE = "LICENSE"
CONST_WYSHBOT_LOGFILE_FILE = "log.txt"
# Tab_advance_const
CONST_WEB_LANGUAGW_CHINESE = "中文"
CONST_WEB_LANGUAGW_ENGLISH = "English"
CONST_UI_LANGUAGE_CHINESE = "繁體中文"
CONST_UI_LANGUAGE_ENGLISH = "English"
CONST_WEB_BROWSER_CHROME = "Chrome"
CONST_WEB_BROWSER_FIREFOX = "FireFox"
CONST_WEB_BROWSER_EDGE = "Edge"
CONST_WEB_BROWSER_BRAVE = "Brave"
CONST_CHROME_FAMILY = [CONST_WEB_BROWSER_CHROME,CONST_WEB_BROWSER_EDGE,CONST_WEB_BROWSER_BRAVE]
CONST_WEBDRIVER_TYPE_SELENIUM = "Selenium"
CONST_WEBDRIVER_TYPE_UC = "Undetected_ChromeDriver"
CONST_WEBDRIVER_TYPE_DP = "DrissionPage"  # For headless Mode
CONST_WYSHBOT_INT28_FILE = "WYSHBot_INT28_IDLE"
CONST_WYSHBOT_LAST_URL_FILE = "WYSHBOT_LAST_URL.txt"
CONST_WYSHBOT_QUESTION_FILE = "WYSHBOT_QUESTION.txt"

AddToList_Action = [] # Record every action of course
AddToList_OpenCourse = [] # Record code of course
AddToList_CourseName = [] # Record Name of course
AddToList_CourseTeacher = [] # Record Teacher of course
CycleList_OpenCourse = [] # Record Cycle List

Account  = ""
Password = ""
homepage = ""
language_code = ""
webLanguage = ""
logFileMode = False

CONST_CHROME_VERSION_NOT_MATCH_EN="Please download the WebDriver version to match your browser version."
CONST_CHROME_VERSION_NOT_MATCH_TW="請下載與您瀏覽器相同版本的WebDriver版本，或更新您的瀏覽器版本。"
CONST_CHROME_DRIVER_WEBSITE = 'https://chromedriver.chromium.org/'
URL_Chinese = "https://www.ais.tku.edu.tw/EleCos/login.aspx"
URL_English = "https://www.ais.tku.edu.tw/EleCos_English/loginE.aspx"
ChineseScript = "javascript: (function(){ var numHash={b6589fc6ab0dc82cf12099d1c2d40ab994e8410c:\"0\",\"356a192b7913b04c54574d18c28d46e6395428ab\":\"1\",da4b9237bacccdf19c0760cab7aec4a8359010b0:\"2\",\"77de68daecd823babbb58edb1c8e14d7106e83bb\":\"3\",\"1b6453892473a467d07372d45eb05abc2031647a\":\"4\",ac3478d69a3c81fa62e60f5c3696165a4e5e6ac4:\"5\",c1dfd96eea8cc2b62785275bca38ac261256e278:\"6\",\"902ba3cda1883801594b6e1b452790cc53948fda\":\"7\",fe5dbbcea5ce7e2988b8c69bcfdfde8904aabc1f:\"8\",\"0ade7c2cf97f75d009975f4d720d1fa6c19f4897\":\"9\"};$.ajax({url:\"https://www.ais.tku.edu.tw/EleCos/Handler1.ashx\",type:\"post\",async:false,success:function(voice){document.getElementById(\"txtCONFM\").value=numHash[voice[0]]+numHash[voice[1]]+numHash[voice[2]]+numHash[voice[3]]+numHash[voice[4]]+numHash[voice[5]];}}); })();"
EnglishScript = "javascript: (function(){ var numHash={b6589fc6ab0dc82cf12099d1c2d40ab994e8410c:\"0\",\"356a192b7913b04c54574d18c28d46e6395428ab\":\"1\",da4b9237bacccdf19c0760cab7aec4a8359010b0:\"2\",\"77de68daecd823babbb58edb1c8e14d7106e83bb\":\"3\",\"1b6453892473a467d07372d45eb05abc2031647a\":\"4\",ac3478d69a3c81fa62e60f5c3696165a4e5e6ac4:\"5\",c1dfd96eea8cc2b62785275bca38ac261256e278:\"6\",\"902ba3cda1883801594b6e1b452790cc53948fda\":\"7\",fe5dbbcea5ce7e2988b8c69bcfdfde8904aabc1f:\"8\",\"0ade7c2cf97f75d009975f4d720d1fa6c19f4897\":\"9\"};$.ajax({url:\"https://www.ais.tku.edu.tw/EleCos_English/Handler1.ashx\",type:\"post\",async:false,success:function(voice){document.getElementById(\"txtCONFM\").value=numHash[voice[0]]+numHash[voice[1]]+numHash[voice[2]]+numHash[voice[3]]+numHash[voice[4]]+numHash[voice[5]];}}); })();"


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.184 Safari/537.36"
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, filename='Log.log', filemode='a', format=FORMAT)

# Common function
def load_translate():
    translate = {}
    en_us = {}
    #Enable/Disable label
    en_us["enable"]='Enable'
    en_us["disable"]='Disable'

    #Tab Name
    en_us["lessonList"] = 'CourseSet'
    en_us["advanced"] = 'Advanced'
    en_us["account"] = 'Account'
    en_us["runtime"] = 'RunTime'
    en_us["about"] = 'About'


    #Tab-lessonList item
    en_us["addLesson"] = 'Add'
    en_us["removeLesson"] = 'Drop'
    en_us["cycleLesson"] = 'Cycle'
    en_us["lessonCode"] = 'OpenCode'
    en_us["lessonName"] = 'CourseName'
    en_us["lessonTeacher"] = 'Teacher'
    en_us["addToList"] = 'Enter'
    en_us["quicklyRevise"] = 'Quick Edit'
    en_us["exchange"] = 'Exchange'
    en_us["remove"] = 'Remove'
    en_us["clean"] = 'Clean'
    en_us["action"] = 'Oper.'
    en_us["lessonCodeShow"] = 'Code'
    en_us["lessonNameShow"] = 'Name'
    en_us["lessonTeacherShow"] = 'Teacher'
    en_us["edit"] = 'Edit'
    en_us["saveList"] = 'Save'
    en_us["EditUp"] = 'Up'
    en_us["EditDown"] = 'Down'

    # Tab-Advanced item
    en_us["UILanguage"] = 'UI Language'
    en_us["browser"] = 'Browser'
    en_us["webdriver_type"] = 'WebDriver Type'
    en_us["webLanguage"] = 'Web Language'
    en_us["refleshGAP"] = 'Refresh Time(Sec.)'
    en_us["headlessMode"] = 'Headless Mode'
    en_us["headlessModeExplain"] = 'Without a graphical user interface, you can directly add or drop courses even when there is no graphical interface. It is recommended to use this mode when using a public cloud platform or a lower-performance computer.'
    en_us["logFileMode"] = 'Detail Log'
    en_us["logFileModeExplain"] = 'Detailed logs should provide clear visibility into the timing of adjustments made, including login times and the times when courses were added.'
    en_us["speedyCycle"] = 'SpeedyCycle'
    en_us["speedyCycleExplain"] = 'The \"SpeedyCycle Mode\" automatically logs out and resets the system after each round of course swiping to maintain the original speed. However, it is recommended not to enable it during peak course enrollment periods.'
    en_us["reviewTable"] = 'Show Table'
    en_us["reviewTableExplain"] = 'Show table after finishing execution'
    en_us["SingleSignOn"] = 'Single Sign On'
    en_us["SingleSignOnExplain"] = 'If your account be sign up, this mode can help you force sign up your account to continue execution'

    #Tab-Account item
    en_us["saveAccountPassword"] = 'Save'
    en_us["saveAccountPasswordExplain"] = 'WYSHBot will save your account in encryption, account can not revise but password.'

    #Tab-Runtime item
    en_us["runningStatus"] = 'Status：'
    en_us["runningEnable"] = 'Running'
    en_us["runningDisable"] = 'Stop'
    en_us["stopRunning"] = 'Stop'
    en_us["continueRunning"] = 'Resume'
    en_us["TaipeiTime"] = 'Taipei Time：'
    en_us["TotalTime"] = 'Total Execution TIme：'
    en_us["TotalTimeSecond"] = '(Sec.)'
    en_us["AppVersion"] = 'App Version：'
    en_us["OSVersion"] = 'System Version：'
    en_us["SystemPythonVersion"] = 'Python Version：'
    en_us["runningTime"] = 'Total Execution Time：'
    en_us["usingMode"] = 'Using Mode：'
    en_us["System"] = 'System：'
    en_us["System_architecture"] = 'Architecture：'

    #Tab-About item
    en_us["Explain1"] = 'WYSHBot was developed by TKU CSIE WYSH'
    en_us["Explain2"] = 'Developed on Python '+platform.python_version()+"  "+ CONST_COMPILE_TIME + ' Compiled'
    en_us["Explain3"] = 'Computer eccentric, with formidable skills;\n do not underestimate. Dare to challenge?'
    en_us["Explain4"] = 'The only courses you don\'t get are the ones\n you don\'t aim for.'
    en_us["help"] = 'HELP：'
    en_us["chromedriver"] = 'Chrome Driver：'
    en_us["FireFoxdriver"] = 'FireFox Driver：'
    en_us["Edgedriver"] = 'Edge Driver：'
    en_us["Contribution"] = 'Contribution'
    en_us["BotArchitectureProvider"] = 'Robot Architecture：'
    en_us["MaxBot"] = 'MAXBot'
    en_us["DIYBrowser"] = 'DIY Browser：'
    en_us["CPY"] = 'TKU CSIE CPY(陳水喔)'
    en_us["TestGroup"] = 'Quality Assurance：'
    en_us["emilylee"] = 'Emily Lee'
    en_us["LINK"] = 'Link'

    #Function
    en_us["run"]='Run'
    en_us["save"]='Save'
    en_us["exit"]='Exit'
    en_us["restore_defaults"]='Reset'


    # Inform
    en_us["Infor"] = 'Warning'
    en_us["done"] = 'Done'
    en_us["CheckCourceCode"] = 'Please enter 4 digits number of open code'
    en_us["CourseCodeNotEmpty"] = 'Open code can not be empty'
    en_us["CheckDeleteNumber"] = 'Error! Please enter correct # number which you want to delete'
    en_us["ExchangeUnsuccessfully"] = 'Fail! Please correct enter'
    en_us["SystemUnavail"] = 'System is not open now!'
    en_us["SSOlimit"] = 'Single Sign On limit, trying to enable Single Sign On'
    en_us["Finish"] = 'Execution Finished, browser will be closed automatically'

    # Default List
    en_us["DefaultOpenCourseName"] = 'Sample'
    en_us["DefaultOpenCourseTeacher"] = 'Sample'

    # Warning
    en_us["NoAccount"] = 'There are no account and password setting record, so go to set your account information.'
    en_us["NoSelectionList"] = 'There are no selection list setting record, so go to set your selection list.'

    zh_tw = {}
    #Enable/Disable label
    zh_tw["enable"]='已啟用'
    zh_tw["disable"]='未啟用'

    #Tab Name
    zh_tw["lessonList"] = '選課清單'
    zh_tw["advanced"] = '進階設定'
    zh_tw["account"] = '帳號設定'
    zh_tw["runtime"] = '執行階段'
    zh_tw["about"] = '關於機器人'


    #Tab-lessonList item
    zh_tw["addLesson"] = '加選'
    zh_tw["removeLesson"] = '退選'
    zh_tw["cycleLesson"] = '刷課'
    zh_tw["lessonCode"] = '開課代碼(必填)'
    zh_tw["lessonName"] = '課程名稱(選填)'
    zh_tw["lessonTeacher"] = '授課老師(選填)'
    zh_tw["addToList"] = '加入清單'
    zh_tw["quicklyRevise"] = '快速調整'
    zh_tw["exchange"] = '對調'
    zh_tw["remove"] = '刪除'
    zh_tw["clean"] = '清空清單'
    zh_tw["action"] = '操作'
    zh_tw["lessonCodeShow"] = '開課代碼'
    zh_tw["lessonNameShow"] = '課程名稱'
    zh_tw["lessonTeacherShow"] = '授課老師'
    zh_tw["edit"] = '調整'
    zh_tw["saveList"] = '儲存清單'
    zh_tw["EditUp"] = '上移'
    zh_tw["EditDown"] = '下移'

    # Tab-Advanced item
    zh_tw["UILanguage"] = '介面語言'
    zh_tw["browser"] = '瀏覽器'
    zh_tw["webdriver_type"] = 'WebDriver類別'
    zh_tw["webLanguage"] = '選課網頁語言'
    zh_tw["refleshGAP"] = '自動刷新網頁間隔(秒)'
    zh_tw["headlessMode"] = '無圖形介面模式'
    zh_tw["headlessModeExplain"] = '無圖形化介面可以在沒有圖形化介面的情況下直接加退選課程，若使用公雲平台或效能較低電腦，推薦使用該模式'
    zh_tw["logFileMode"] = '輸出詳細記錄'
    zh_tw["logFileModeExplain"] = '輸出詳細記錄可以清楚看到什麼時間點做了哪些調整，包含登入時間、課程加選的時間'
    zh_tw["speedyCycle"] = '極速刷課模式'
    zh_tw["speedyCycleExplain"] = '極速刷課模式是在每次把課刷完一輪後強制重新登入系統，保持原始的速度，但建議搶課高峰期不要開啟'
    zh_tw["reviewTable"] = '結束後顯示課表'
    zh_tw["reviewTableExplain"] = '結束後畫面會停留在課表上'
    zh_tw["SingleSignOn"] = '單一裝置登入'
    zh_tw["SingleSignOnExplain"] = '如果你的帳號在其他地方被登入後，會重新強制登入，避免影響你搶課'

    #Tab-Account item
    zh_tw["saveAccountPassword"] = '儲存帳號與密碼'
    zh_tw["saveAccountPasswordExplain"] = '機器人帳號密碼將加密儲存，帳號已經綁定無法修改，密碼可以任意修改'

    #Tab-Runtime item
    zh_tw["runningStatus"] = '執行狀態：'
    zh_tw["runningEnable"] = '已啟用'
    zh_tw["runningDisable"] = '已停止'
    zh_tw["stopRunning"] = '暫停搶課'
    zh_tw["continueRunning"] = '繼續搶課'
    zh_tw["TaipeiTime"] = '台北標準時間：'
    zh_tw["TotalTime"] = '啟動時間總計：'
    zh_tw["TotalTimeSecond"] = '(秒)'
    zh_tw["AppVersion"] = 'App版本：'
    zh_tw["OSVersion"] = '系統版本：'
    zh_tw["SystemPythonVersion"] = '系統Python版本：'
    zh_tw["runningTime"] = '連續使用時間：'
    zh_tw["usingMode"] = '使用模式：'
    zh_tw["System"] = '系統：'
    zh_tw["System_architecture"] = '系統架構：'

    #Tab-About item
    zh_tw["Explain1"] = '本機器人由淡江大學 資訊工程學系 WYSH開發製作'
    zh_tw["Explain2"] = '使用Python '+platform.python_version()+ ' 開發製作，' + CONST_COMPILE_TIME + '編譯'
    zh_tw["Explain3"] = '電腦怪傑，實力不容小覷，不服來戰'
    zh_tw["Explain4"] = '只有不想搶的課，沒有搶不到的課'
    zh_tw["help"] = '使用教學：'
    zh_tw["chromedriver"] = 'Chrome Driver：'
    zh_tw["FireFoxdriver"] = 'FireFox Driver：'
    zh_tw["Edgedriver"] = 'Edge Driver：'
    zh_tw["Contribution"] = '貢獻榜'
    zh_tw["BotArchitectureProvider"] = '機器人架構參考：'
    zh_tw["MaxBot"] = 'MAXBot'
    zh_tw["DIYBrowser"] = '自製瀏覽器:'
    zh_tw["CPY"] = 'TKU CSIE CPY(陳水喔)'
    zh_tw["TestGroup"] = '測試團隊：'
    zh_tw["emilylee"] = 'Emily Lee'
    zh_tw["LINK"] = '連結網址'


    #Function
    zh_tw["run"]='開始搶課'
    zh_tw["save"]='儲存設定檔'
    zh_tw["exit"]='關閉'
    zh_tw["restore_defaults"]='恢復預設值'


    # Inform
    zh_tw["Infor"] = '提示'
    zh_tw["done"] = '完成'
    zh_tw["CheckCourceCode"] = '請正確填寫開課代碼4個數字'
    zh_tw["CourseCodeNotEmpty"] = '開課代碼不能留白'
    zh_tw["CheckDeleteNumber"] = '輸入錯誤，請正確輸入欲刪除課程之序號(非開課代碼)'
    zh_tw["ExchangeUnsuccessfully"] = '交換失敗，請檢查是否填寫正確'
    zh_tw["SystemUnavail"] = '系統尚未開放，請於系統開放時間加退選'
    zh_tw["SSOlimit"] = '單一裝置登入限制，您的帳號已在別的地方登入，或要改善勾選單一裝置登入選項並重新執行'
    zh_tw["Finish"]='操作全數都已經完成，瀏覽器將自動關閉'

    # Default List
    zh_tw["DefaultOpenCourseName"] = '我是範例'
    zh_tw["DefaultOpenCourseTeacher"] = '我是範例'

    # Warning
    zh_tw["NoAccount"] = '沒有設定帳號密碼是跟人家選什麼課啦！請去設定帳號密碼'
    zh_tw["NoSelectionList"] = '沒有設定選課清單是跟人家選什麼課啦！請去設定選課清單'

    translate['en_us'] = en_us
    translate['zh_tw'] = zh_tw

    return translate

def get_app_root():
    # 讀取檔案裡的參數值
    basis = ""
    if hasattr(sys, 'frozen'):
        basis = sys.executable
    else:
        basis = sys.argv[0]
    app_root = os.path.dirname(basis)
    logging.info("App_root"+app_root)
    return app_root
def get_default_config():
    config_dict={}

    config_dict["homepage"] = URL_Chinese
    config_dict["advanced"] = {}
    config_dict["advanced"]["browser"] = "Chrome"
    config_dict["advanced"]["UILanguage"] = "繁體中文"
    config_dict["advanced"]["webdriver_type"] = CONST_WEBDRIVER_TYPE_UC
    config_dict["advanced"]["webLanguage"] = CONST_WEB_LANGUAGW_CHINESE
    config_dict["advanced"]["refleshGAP"] = '0.3'

    config_dict["advanced"]["headlessMode"] = {}
    config_dict["advanced"]["headlessMode"]["enable"] = False
    config_dict["advanced"]["logFileMode"] = {}
    config_dict["advanced"]["logFileMode"]["enable"] = True
    config_dict["advanced"]["speedyCycle"] = {}
    config_dict["advanced"]["speedyCycle"]["enable"] = False
    config_dict["advanced"]["reviewTable"] = {}
    config_dict["advanced"]["reviewTable"]["enable"] = True
    config_dict["advanced"]["SingleSignOn"] = {}
    config_dict["advanced"]["SingleSignOn"]["enable"] = False

    return config_dict
def load_json():
    app_root = get_app_root()
    # overwrite config path.
    config_filepath = os.path.join(app_root, CONST_WYSHBOT_CONFIG_FILE)
    global config_dict
    config_dict = None
    if os.path.isfile(config_filepath):
        print("Load json successfully")
        with open(config_filepath) as json_data:
            config_dict = json.load(json_data)
    else:
        print("There is no json exist, so load default setting")
        config_dict = get_default_config()

    return config_filepath, config_dict
def load_selection_list():
    app_root = get_app_root()
    # overwrite config path.
    Selection_filepath = os.path.join(app_root, CONST_SELECTION_FILE)
    selection_dict = None
    if os.path.isfile(Selection_filepath):
        with open(Selection_filepath) as json_data:
            selection_dict = json.load(json_data)
        for i in range(len(selection_dict)):
            index = str(i)
            AddToList_Action.append(selection_dict[index]["Action"])
            AddToList_OpenCourse.append(selection_dict[index]["OpenCode"])
            AddToList_CourseTeacher.append(selection_dict[index]["Teacher"])
            AddToList_CourseName.append(selection_dict[index]["CourseName"])
        return True
    else:
        messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["NoSelectionList"])
        return False
def load_save_account():
    app_root = get_app_root()
    global Account
    global Password
    # overwrite config path.
    License_filepath = os.path.join(app_root, CONST_LICENSE)
    Account_dict = None
    if os.path.isfile(License_filepath):
        with open(License_filepath) as json_data:
            Account_dict = json.load(json_data)
        Account = Account_dict["Account"]
        Password = Account_dict["Password"]
        return True
    else:
        messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["NoAccount"])
        return False
def account_login(driver):
    global Account
    global Password
    global language_code
    global webLanguage
    try:
        account = driver.find_element("xpath", "//*[@id=\"txtStuNo\"]")
        account.clear()
        account.send_keys(Account)  # 學號
        password = driver.find_element("xpath", "//*[@id=\"txtPSWD\"]")
        password.clear()
        password.send_keys(Password)  # 密碼
        ConfirmNumber = driver.find_element("xpath", "//*[@id=\"txtCONFM\"]")
        ConfirmNumber.clear()
        # Execution script
        if webLanguage=="中文":
            driver.execute_script(ChineseScript) # Chinese Script
        else:
            driver.execute_script(EnglishScript) # English Script
        return True
    except:
        print("System Unavailable")
        print("系統尚未開放")
        driver.refresh()
        return False

def AddCourse(driver,OpenCode,config_dict):
    #Add
    #要加的課程
    Add_Number = driver.find_element("xpath","//*[@id=\"txtCosEleSeq\"]")
    Add_Number.clear()
    Add_Number.send_keys(OpenCode)
    driver.find_element("xpath","//*[@id=\"btnAdd\"]").click()
    return True

def DropCourse(driver, OpenCode, config_dict):
    # Drop
    # 要刪除的課程
    Remove_Number = driver.find_element("xpath", "//*[@id=\"txtCosEleSeq\"]")
    Remove_Number.clear()
    Remove_Number.send_keys(OpenCode)
    driver.find_element("xpath", "//*[@id=\"btnDel\"]").click()
    return True
def Result(driver):
    TEXT = driver.page_source
    return TEXT

def pause_test():
    filepath = get_app_root() + "/" + CONST_WYSHBOT_INT28_FILE
    if os.path.isfile(filepath):
        return True
    else:
        return False
def execution_function(driver, url, config_dict):
    global homepage
    global logFileMode
    driver.get(homepage)

    if logFileMode:
        logging.info('GoTo'+homepage)
    else:
        pass

    wyshbot_last_reset_time = time.time()

    #Dealing with login
    while(True):
        is_login = False
        #Cycle flash login
        while not is_login:
            is_pause = pause_test()
            while (is_pause):
                is_pause = pause_test()
                logging.info("機器人中斷，已被暫停")
            if float(config_dict["advanced"]["refleshGAP"]) > 0:
                wyshbot_running_time = time.time() - wyshbot_last_reset_time
                if wyshbot_running_time > float(config_dict["advanced"]["refleshGAP"]):
                    is_login = account_login(driver)
                    wyshbot_last_reset_time = time.time()
        driver.find_element("xpath", "//*[@id=\"btnLogin\"]").click()
        try:
            driver.find_element("xpath", "//*[@id=\"txtCosEleSeq\"]")#Successfully get textbox
            if logFileMode:
                logging.info("登入成功 Logging Successfully")
            print("登入成功")
            break
        except:
            TEXT = Result(driver)
            if ("目前不是您的選課開放時間" in TEXT) or ("Currently not open for you" in TEXT):
                print("It's not your opening time, retrying......")
                print("您的選課時間還沒有到，機器人重刷中........")
                logging.info("時間未到，機器人重刷中")
                continue
            elif("每日系統維護時間" in TEXT) or ("The daily maintain hour" in TEXT):
                print("It's maintain time, retrying......")
                print("現在是系統維護時間，機器人重刷中........")
                logging.info("時間未到，機器人重刷中")
                continue
            else:
                pass

    is_perfect_working = True
    # normal add and remove
    for i in range(len(AddToList_Action)):
        temp = AddToList_OpenCourse[i]
        if (AddToList_Action[i]=="加選" or AddToList_Action[i]=="Add") and is_perfect_working:
            is_perfect_working = AddCourse(driver,AddToList_OpenCourse[i],config_dict)
            TEXT = Result(driver)
            if "加選成功" in TEXT or "Add successfully" in TEXT:
                if logFileMode:
                    logging.info(temp+"加選成功")

                print(temp + " Successful")
                print(temp + " 加選成功")
                AddToList_OpenCourse.remove(temp)
                break
            elif ("加選失敗" in TEXT and "序號已選" in TEXT) or ("Add Failed" in TEXT and "duplicated" in TEXT):
                if logFileMode:
                    logging.info(temp+"已選")

                print(temp + " Already Selected")
                print(temp + " 課程已選")
                AddToList_OpenCourse.remove(temp)
                break
            elif ("加選失敗" in TEXT and "人數額滿" in TEXT) or ("Add Failed" in TEXT and "No seats remaining"):
                print(temp + " Fail!")
                print(temp + " 人數已滿")
            else:
                try:
                    print("Also use WYSHBot Flash")
                    print("重複使用機器人搶課")
                except:
                    print("Other Result")
                    print("其他原因")
        elif (AddToList_Action[i]=="退選" or AddToList_Action[i]=="Drop") and is_perfect_working:
            TEXT = Result(driver)
            is_perfect_working = DropCourse(driver,AddToList_OpenCourse[i],config_dict)
            if ("退選成功" in TEXT) or ("Drop successfully" in TEXT):
                if logFileMode:
                    logging.info(temp+"退選成功")
                print(temp + " Drop Successful")
                print(temp + " 退選成功")
                AddToList_OpenCourse.remove(temp)
                break
            elif ("退選失敗???" in TEXT and "開課序號未選或已退選" in TEXT) or ("Drop Failed!!!" in TEXT and "The number of the dropped course does not exist" in TEXT):
                if logFileMode:
                    logging.info(temp+"無法退選，可能未選或已退選")
                print(temp + " Already Dropped or not selected")
                print(temp + " 課程已退選或根本沒選")
                AddToList_OpenCourse.remove(temp)
                break
            else:
                try:
                    print("Also use WYSHBot Flash")
                    print("重複使用機器人搶課")
                except:
                    print("Other Result")
                    print("其他原因")
        elif not is_perfect_working:
            break

    # Show final table
    if logFileMode:
        logging.info("顯示課表")

    if (config_dict["advanced"]["reviewTable"]["enable"]):
        driver.find_element("xpath", "//*[@id=\"btnEleCos\"]").click()

    messagebox.showinfo(translate[language_code]["Infor"],translate[language_code]["Finish"])

    if logFileMode:
        logging.info("所有課程操作都已完成")

def t_or_f(arg):
    ret = False
    ua = str(arg).upper()
    if 'TRUE'.startswith(ua):
        ret = True
    elif 'YES'.startswith(ua):
        ret = True
    return ret
def get_config_dict(args):
    app_root = get_app_root()
    config_filepath = os.path.join(app_root, CONST_WYSHBOT_CONFIG_FILE)

    # allow assign config by command line.
    if not args.input is None:
        if len(args.input) > 0:
            config_filepath = args.input

    config_dict = None
    if os.path.isfile(config_filepath):
        # start to overwrite config settings.
        with open(config_filepath) as json_data:
            config_dict = json.load(json_data)

            if not args.headless is None:
                headless_flag = t_or_f(args.headless)
                if headless_flag:
                    config_dict["advanced"]["headlessMode"]["enable"] = True

            if not args.browser is None:
                if len(args.browser) > 0:
                    config_dict["browser"] = args.browser

    return config_dict
def get_chromedriver_path(webdriver_path):
    chromedriver_path = os.path.join(webdriver_path,"chromedriver")
    if platform.system().lower()=="windows":
        chromedriver_path = os.path.join(webdriver_path,"chromedriver.exe")
    return chromedriver_path
def load_chromdriver_normal(config_dict, driver_type):
    show_debug_message = True       # debug.
    show_debug_message = False      # online

    if config_dict["advanced"]["logFileMode"]["enable"]:
        show_debug_message = True

    driver = None

    Root_Dir = get_app_root()
    webdriver_path = os.path.join(Root_Dir, "webdriver")
    chromedriver_path = get_chromedriver_path(webdriver_path)

    if not os.path.exists(webdriver_path):
        os.mkdir(webdriver_path)

    if not os.path.exists(chromedriver_path):
        print("WebDriver not exist, try to download to:", webdriver_path)
        chromedriver_autoinstaller_max.install(path=webdriver_path, make_version_dir=False)

    if not os.path.exists(chromedriver_path):
        print("Please download chromedriver and extract zip to webdriver folder from this url:")
        print("請下在面的網址下載與你chrome瀏覽器相同版本的chromedriver,解壓縮後放到webdriver目錄裡：")
        print(CONST_CHROME_DRIVER_WEBSITE)
    else:
        chrome_service = Service(chromedriver_path)
        chrome_options = get_chrome_options(webdriver_path, config_dict)
        try:
            driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        except Exception as exc:
            error_message = str(exc)
            if show_debug_message:
                print(exc)
            left_part = None
            if "Stacktrace:" in error_message:
                left_part = error_message.split("Stacktrace:")[0]
                print(left_part)

            if "This version of ChromeDriver only supports Chrome version" in error_message:
                print(CONST_CHROME_VERSION_NOT_MATCH_EN)
                print(CONST_CHROME_VERSION_NOT_MATCH_TW)

                # remove exist chromedriver, download again.
                try:
                    print("Deleting exist and download ChromeDriver again.")
                    os.unlink(chromedriver_path)
                except Exception as exc2:
                    print(exc2)
                    pass

                chromedriver_autoinstaller_max.install(path=webdriver_path, make_version_dir=False)
                chrome_service = Service(chromedriver_path)
                try:
                    chrome_options = get_chrome_options(webdriver_path, config_dict)
                    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
                except Exception as exc2:
                    print("Selenium 4.11.0 Release with Chrome For Testing Browser.")
                    try:
                        chrome_options = get_chrome_options(webdriver_path, config_dict)
                        driver = webdriver.Chrome(service=Service(), options=chrome_options)
                    except Exception as exc3:
                        print(exc3)
                        pass

    return driver
def clean_uc_exe_cache():
    exe_name = "chromedriver%s"

    platform = sys.platform
    if platform.endswith("win32"):
        exe_name %= ".exe"
    if platform.endswith(("linux", "linux2")):
        exe_name %= ""
    if platform.endswith("darwin"):
        exe_name %= ""

    d = ""
    if platform.endswith("win32"):
        d = "~/appdata/roaming/undetected_chromedriver"
    elif "LAMBDA_TASK_ROOT" in os.environ:
        d = "/tmp/undetected_chromedriver"
    elif platform.startswith(("linux", "linux2")):
        d = "~/.local/share/undetected_chromedriver"
    elif platform.endswith("darwin"):
        d = "~/Library/Application Support/undetected_chromedriver"
    else:
        d = "~/.undetected_chromedriver"
    data_path = os.path.abspath(os.path.expanduser(d))

    is_cache_exist = False
    p = pathlib.Path(data_path)
    files = list(p.rglob("*chromedriver*?"))
    for file in files:
        if os.path.exists(str(file)):
            is_cache_exist = True
            try:
                os.unlink(str(file))
            except Exception as exc2:
                print(exc2)
                pass

    return is_cache_exist
def get_brave_bin_path():
    brave_path = ""
    if platform.system() == 'Windows':
        brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        if not os.path.exists(brave_path):
            brave_path = os.path.expanduser('~') + "\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        if not os.path.exists(brave_path):
            brave_path = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        if not os.path.exists(brave_path):
            brave_path = "D:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

    if platform.system() == 'Linux':
        brave_path = "/usr/bin/brave-browser"

    if platform.system() == 'Darwin':
        brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

    return brave_path
def get_uc_options(uc, config_dict, webdriver_path):
    options = uc.ChromeOptions()
    options.page_load_strategy = 'eager'
    #options.page_load_strategy = 'none'
    options.unhandled_prompt_behavior = "accept"
    #print("strategy", options.page_load_strategy)


    if config_dict["advanced"]["headlessMode"]["enable"]:
        #options.add_argument('--headless')
        options.add_argument('--headless=new')
        options.add_argument("--user-agent=%s" % (USER_AGENT))

    options.add_argument("--disable-animations")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-print-preview")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-site-isolation-trials")
    options.add_argument("--disable-smooth-scrolling")
    options.add_argument("--disable-sync")
    options.add_argument("--no-sandbox");
    options.add_argument('--disable-features=TranslateUI')
    options.add_argument('--disable-translate')
    options.add_argument('--disable-web-security')
    options.add_argument('--lang=zh-TW')

    options.add_argument("--password-store=basic")
    options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False, "translate":{"enabled": False}})


    if config_dict["browser"]==CONST_WEB_BROWSER_BRAVE:
        brave_path = get_brave_bin_path()
        if os.path.exists(brave_path):
            options.binary_location = brave_path

    return options
def load_chromdriver_uc(config_dict):
    import undetected_chromedriver as uc

    show_debug_message = True       # debug.
    show_debug_message = False      # online

    if config_dict["advanced"]["logFileMode"]["enable"]:
        show_debug_message = True

    Root_Dir = get_app_root()
    webdriver_path = os.path.join(Root_Dir, "webdriver")
    chromedriver_path = get_chromedriver_path(webdriver_path)

    if not os.path.exists(webdriver_path):
        os.mkdir(webdriver_path)

    if not os.path.exists(chromedriver_path):
        print("ChromeDriver not exist, try to download to:", webdriver_path)
        try:
            chromedriver_autoinstaller_max.install(path=webdriver_path, make_version_dir=False)
            if not os.path.exists(chromedriver_path):
                print("check installed chrome version fail, download last known good version.")
                chromedriver_autoinstaller_max.install(path=webdriver_path, make_version_dir=False, detect_installed_version=False)
        except Exception as exc:
            print(exc)
    else:
        print("ChromeDriver exist:", chromedriver_path)


    driver = None
    if os.path.exists(chromedriver_path):
        # use chromedriver_autodownload instead of uc auto download.
        is_cache_exist = clean_uc_exe_cache()

        try:
            options = get_uc_options(uc, config_dict, webdriver_path)
            driver = uc.Chrome(driver_executable_path=chromedriver_path, options=options, headless=config_dict["advanced"]["headless"]["enable"])
        except Exception as exc:
            print(exc)
            error_message = str(exc)
            left_part = None
            if "Stacktrace:" in error_message:
                left_part = error_message.split("Stacktrace:")[0]
                print(left_part)

            if "This version of ChromeDriver only supports Chrome version" in error_message:
                print(CONST_CHROME_VERSION_NOT_MATCH_EN)
                print(CONST_CHROME_VERSION_NOT_MATCH_TW)

            # remove exist chromedriver, download again.
            try:
                print("Deleting exist and download ChromeDriver again.")
                os.unlink(chromedriver_path)
            except Exception as exc2:
                print(exc2)
                pass

            try:
                chromedriver_autoinstaller_max.install(path=webdriver_path, make_version_dir=False)
                options = get_uc_options(uc, config_dict, webdriver_path)
                driver = uc.Chrome(driver_executable_path=chromedriver_path, options=options)
            except Exception as exc2:
                print(exc2)
                pass
    else:
        print("WebDriver not found at path:", chromedriver_path)

    if driver is None:
        print('WebDriver object is still None..., try download by uc.')
        try:
            options = get_uc_options(uc, config_dict, webdriver_path)
            driver = uc.Chrome(options=options)
        except Exception as exc:
            print(exc)
            error_message = str(exc)
            left_part = None
            if "Stacktrace:" in error_message:
                left_part = error_message.split("Stacktrace:")[0]
                print(left_part)

            if "This version of ChromeDriver only supports Chrome version" in error_message:
                print(CONST_CHROME_VERSION_NOT_MATCH_EN)
                print(CONST_CHROME_VERSION_NOT_MATCH_TW)
            pass

    if driver is None:
        print("create web drive object by undetected_chromedriver fail!")

        if os.path.exists(chromedriver_path):
            print("Unable to use undetected_chromedriver, ")
            print("try to use local chromedriver to launch chrome browser.")
            driver_type = "selenium"
            driver = load_chromdriver_normal(config_dict, driver_type)
        else:
            print("建議您自行下載 ChromeDriver 到 webdriver 的資料夾下")
            print("you need manually download ChromeDriver to webdriver folder.")

    return driver
def get_chrome_options(webdriver_path, config_dict):
    chrome_options = webdriver.ChromeOptions()
    if config_dict["advanced"]["browser"]==CONST_WEB_BROWSER_EDGE:
        chrome_options = webdriver.EdgeOptions()

    if config_dict["advanced"]["headlessMode"]["enable"]:
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument("--user-agent=%s" % (USER_AGENT))

    chrome_options.add_argument("--disable-animations")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-print-preview")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-site-isolation-trials")
    chrome_options.add_argument("--disable-smooth-scrolling")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--no-sandbox");
    chrome_options.add_argument('--disable-features=TranslateUI')
    chrome_options.add_argument('--disable-translate')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--lang=zh-TW')

    # for navigator.webdriver
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # Deprecated chrome option is ignored: useAutomationExtension
    #chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False, "translate":{"enabled": False}})

    if config_dict["advanced"]["browser"]==CONST_WEB_BROWSER_BRAVE:
        brave_path = get_brave_bin_path()
        if os.path.exists(brave_path):
            chrome_options.binary_location = brave_path

    chrome_options.page_load_strategy = 'eager'
    #chrome_options.page_load_strategy = 'none'
    chrome_options.unhandled_prompt_behavior = "accept"

    return chrome_options
def get_driver_by_config(config_dict):
    global homepage
    driver = None

    # read config.
    homepage = config_dict["homepage"]

    # output config:
    print("maxbot app version:", CONST_APP_VERSION)
    print("python version:", platform.python_version())
    print("platform:", platform.platform())
    print("homepage:", homepage)
    print("browser:", config_dict["advanced"]["browser"])

    '''if config_dict["advanced"]["logFileMode"]["enable"]:
        print(config_dict["advanced"])'''
    print("webdriver_type:", config_dict["advanced"]["webdriver_type"])

    # entry point
    if homepage is None:
        homepage = ""

    Root_Dir = get_app_root()
    webdriver_path = os.path.join(Root_Dir, "webdriver")
    # print("platform.system().lower():", platform.system().lower())

    if config_dict["advanced"]["browser"] in [CONST_WEB_BROWSER_CHROME, CONST_WEB_BROWSER_BRAVE]:
        # method 6: Selenium Stealth
        if config_dict["advanced"]["webdriver_type"] == CONST_WEBDRIVER_TYPE_SELENIUM:
            driver = load_chromdriver_normal(config_dict, config_dict["advanced"]["webdriver_type"])
        if config_dict["advanced"]["webdriver_type"] == CONST_WEBDRIVER_TYPE_UC:
            # method 5: uc
            # multiprocessing not work bug.
            if platform.system().lower() == "windows":
                if hasattr(sys, 'frozen'):
                    from multiprocessing import freeze_support
                    freeze_support()
            driver = load_chromdriver_uc(config_dict)

    if config_dict["advanced"]["browser"] == CONST_WEB_BROWSER_FIREFOX:
        # default os is linux/mac
        # download url: https://github.com/mozilla/geckodriver/releases
        chromedriver_path = os.path.join(webdriver_path, "geckodriver")
        if platform.system().lower() == "windows":
            chromedriver_path = os.path.join(webdriver_path, "geckodriver.exe")

        if "macos" in platform.platform().lower():
            if "arm64" in platform.platform().lower():
                chromedriver_path = os.path.join(webdriver_path, "geckodriver_arm")

        webdriver_service = Service(chromedriver_path)
        driver = None
        try:
            from selenium.webdriver.firefox.options import Options
            options = Options()
            if config_dict["advanced"]["headlessMode"]["enable"]:
                options.add_argument('--headless')
                # options.add_argument('--headless=new')
            if platform.system().lower() == "windows":
                binary_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                if not os.path.exists(binary_path):
                    binary_path = os.path.expanduser('~') + "\\AppData\\Local\\Mozilla Firefox\\firefox.exe"
                if not os.path.exists(binary_path):
                    binary_path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
                if not os.path.exists(binary_path):
                    binary_path = "D:\\Program Files\\Mozilla Firefox\\firefox.exe"
                options.binary_location = binary_path

            driver = webdriver.Firefox(service=webdriver_service, options=options)
        except Exception as exc:
            error_message = str(exc)
            left_part = None
            if "Stacktrace:" in error_message:
                left_part = error_message.split("Stacktrace:")[0]
                print(left_part)
            else:
                print(exc)

    if config_dict["advanced"]["browser"] == CONST_WEB_BROWSER_EDGE:
        # default os is linux/mac
        # download url: https://developer.microsoft.com/zh-tw/microsoft-edge/tools/webdriver/
        chromedriver_path = os.path.join(webdriver_path, "msedgedriver")
        if platform.system().lower() == "windows":
            chromedriver_path = os.path.join(webdriver_path, "msedgedriver.exe")

        webdriver_service = Service(chromedriver_path)
        chrome_options = get_chrome_options(webdriver_path, config_dict)

        driver = None
        try:
            driver = webdriver.Edge(service=webdriver_service, options=chrome_options)
        except Exception as exc:
            error_message = str(exc)
            # print(error_message)
            left_part = None
            if "Stacktrace:" in error_message:
                left_part = error_message.split("Stacktrace:")[0]
                print(left_part)
    if driver is None:
        print("create web driver object fail @_@;")
    else:
            print("goto url:", homepage)
            driver.get(homepage)
            time.sleep(3.0)
    return driver
def get_current_url(driver):
    DISCONNECTED_MSG = ': target window already closed'

    url = ""
    is_quit_bot = False

    try:
        url = driver.current_url
    except NoSuchWindowException:
        print('NoSuchWindowException at this url:', url )
        #print("last_url:", last_url)
        #print("get_log:", driver.get_log('driver'))
        window_handles_count = 0
        try:
            window_handles_count = len(driver.window_handles)
            #print("window_handles_count:", window_handles_count)
            if window_handles_count >= 1:
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to.default_content()
                time.sleep(0.2)
        except Exception as excSwithFail:
            #print("excSwithFail:", excSwithFail)
            pass
        if window_handles_count==0:
            try:
                driver_log = driver.get_log('driver')[-1]['message']
                #print("get_log:", driver_log)
                if DISCONNECTED_MSG in driver_log:
                    print('quit bot by NoSuchWindowException')
                    is_quit_bot = True
                    driver.quit()
                    sys.exit()
            except Exception as excGetDriverMessageFail:
                #print("excGetDriverMessageFail:", excGetDriverMessageFail)
                except_string = str(excGetDriverMessageFail)
                if 'HTTP method not allowed' in except_string:
                    print('quit bot by close browser')
                    is_quit_bot = True
                    driver.quit()
                    sys.exit()

    except UnexpectedAlertPresentException as exc1:
        print('UnexpectedAlertPresentException at this url:', url )
        # PS: do nothing...
        # PS: current chrome-driver + chrome call current_url cause alert/prompt dialog disappear!
        # raise exception at selenium/webdriver/remote/errorhandler.py
        # after dialog disappear new excpetion: unhandled inspector error: Not attached to an active page
        is_pass_alert = False
        is_pass_alert = True
        if is_pass_alert:
            try:
                driver.switch_to.alert.accept()
            except Exception as exc:
                pass

    except Exception as exc:

        #UnicodeEncodeError: 'ascii' codec can't encode characters in position 63-72: ordinal not in range(128)
        str_exc = ""
        try:
            str_exc = str(exc)
        except Exception as exc2:
            pass

        if len(str_exc)==0:
            str_exc = repr(exc)

        exit_bot_error_strings = ['Max retries exceeded'
        , 'chrome not reachable'
        , 'unable to connect to renderer'
        , 'failed to check if window was closed'
        , 'Failed to establish a new connection'
        , 'Connection refused'
        , 'disconnected'
        , 'without establishing a connection'
        , 'web view not found'
        , 'invalid session id'
        ]
        for each_error_string in exit_bot_error_strings:
            if isinstance(str_exc, str):
                if each_error_string in str_exc:
                    print('quit bot by error:', each_error_string, driver)
                    is_quit_bot = True
                    driver.quit()
                    sys.exit()

        # not is above case, print exception.
        print("Exception:", str_exc)
        pass

    return url, is_quit_bot
def write_string_to_file(filename, data):
    outfile = None
    if platform.system() == 'Windows':
        outfile = open(filename, 'w', encoding='UTF-8')
    else:
        outfile = open(filename, 'w')

    if not outfile is None:
        outfile.write("%s" % data)
def write_last_url_to_file(url):
    working_dir = os.path.dirname(os.path.realpath(__file__))
    target_path = os.path.join(working_dir, CONST_WYSHBOT_LAST_URL_FILE)
    write_string_to_file(target_path, url)
def reset_webdriver(driver, config_dict, url):
    new_driver = None
    try:
        driver.close()
        config_dict["homepage"]=url
        new_driver = get_driver_by_config(config_dict)
        new_driver.get(url)
        driver = new_driver
    except Exception as e:
        pass
    return new_driver
def main(args):
    # load config data, account data and selection list
    config_dict = get_config_dict(args)

    if (logFileMode):
        print("config_dict load successfully!")
        print("設定檔載入成功")
    else:
        pass

    is_Account_Setting = load_save_account()  # True/False
    if (logFileMode):
        if(is_Account_Setting):
            print("Account information load successfully!")
            print("登入帳號密碼資訊載入成功")
        else:
            print("Account information load unsuccessfully!")
            print("登入帳號密碼資訊載入失敗")
    else:
        pass

    # load selection list
    is_Selection_Setting = load_selection_list() # True/False
    if (logFileMode):
        if(is_Selection_Setting):
            print("Selection information load successfully!")
            print("選課資訊載入成功")
            '''print("現有清單")
                print(AddToList_Action)
                print(AddToList_CourseName)
                print(AddToList_OpenCourse)
                print(AddToList_CourseTeacher)
                print(CycleList_OpenCourse)'''
        else:
            print("Selection information load unsuccessfully!")
            print("選課資訊載入失敗")
    else:
        pass
    global translate
    global language_code
    global webLanguage

    # setting language code and load translate
    translate = load_translate()
    if (config_dict["advanced"]["UILanguage"] == "繁體中文"):
        language_code = "zh_tw"
    elif (config_dict["advanced"]["UILanguage"] == "English"):
        language_code = "en_us"
    webLanguage = config_dict["advanced"]["webLanguage"]

    if (logFileMode):
        print("UI Language："+language_code)
        print("介面語言："+language_code)

        print("webLanguage："+webLanguage)
        print("網頁語言："+webLanguage)
    else:
        pass

    driver = None
    if not config_dict is None:
        driver = get_driver_by_config(config_dict)
    else:
        print("Load config error!")



    # internal variable.
    url = ""
    last_url = ""

    wyshbot_last_reset_time = time.time()
    # Waiting For logging
    while True:
        time.sleep(0.05)

        if is_Selection_Setting:
            pass
        else:
            print("Quit")
            break
        if is_Account_Setting:
            pass
        else:
            print("Quit")
            break

        # pass if driver not loaded.
        if driver is None:
            print("web driver not accessible!")
            break

        url, is_quit_bot = get_current_url(driver)
        if is_quit_bot:
            break

        if url is None:
            continue
        else:
            if len(url) == 0:
                continue

        if float(config_dict["advanced"]["refleshGAP"]) > 0:
            wyshbot_running_time = time.time() - wyshbot_last_reset_time
            if wyshbot_running_time > float(config_dict["advanced"]["refleshGAP"]):
                driver = reset_webdriver(driver, config_dict, url)
                wyshbot_last_reset_time = time.time()

        execution_function(driver, url, config_dict)
        break
def cli():
    parser = argparse.ArgumentParser(prog="WYSHBot",description="WYSHBot Aggument Parser")

    parser.add_argument("--input",help="config file path",type=str)

    parser.add_argument("--headless",help="headless mode",default='False',type=str)

    parser.add_argument("--browser",help="overwrite browser setting",default='',choices=['Chrome','Edge','Brave'],type=str)

    args = parser.parse_args()
    main(args)
if __name__ == "__main__":
    print("app_root：" + get_app_root())
    cli()