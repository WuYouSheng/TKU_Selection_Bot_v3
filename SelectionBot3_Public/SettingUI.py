#!/usr/bin/env python3
# encoding=utf-8
import random
import tkinter
try:
    # for Python2
    import tkMessageBox as messagebox
    import ttk
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
    from tkinter import ttk
    import tkinter.font as tkfont
    from tkinter import messagebox
    from tkinter.filedialog import asksaveasfilename
    import tkinter as tk

import cryptocode
import asyncio
import base64
import json
import os
import platform
import psutil
import socket
import ssl
import subprocess
import sys
import threading
import time
import warnings
import webbrowser
from datetime import datetime
from typing import Optional
from PIL import Image, ImageTk

import requests
import tornado
from tornado.web import Application
from urllib3.exceptions import InsecureRequestWarning

# Const Variable Definition
CONST_COMPILE_TIME = "2024.02.22"
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
CONST_WEBDRIVER_TYPE_SELENIUM = "Selenium"
CONST_WEBDRIVER_TYPE_UC = "Undetected_ChromeDriver"
CONST_WEBDRIVER_TYPE_DP = "DrissionPage"  # For headless Mode
CONST_WYSHBOT_INT28_FILE = "WYSHBot_INT28_IDLE"
CONST_WYSHBOT_LAST_URL_FILE = "WYSHBOT_LAST_URL.txt"
CONST_UI_PADDING_X = 10

#URL Setting
URL_HELP = 'https://github.com/WuYouSheng/TKU_SelectionBot'
URL_CHROME_DRIVER = 'https://chromedriver.chromium.org/'
URL_FIREFOX_DRIVER = 'https://github.com/mozilla/geckodriver/releases'
URL_EDGE_DRIVER = 'https://reurl.cc/mrpjaj'
MAXBot_URL = 'https://github.com/max32002/tixcraft_bot'
URL_Chinese = "https://www.ais.tku.edu.tw/EleCos/login.aspx"
URL_English = "https://www.ais.tku.edu.tw/EleCos_English/loginE.aspx"

# Global Variable
root = Tk()

AddToList_Action = [] # Record every action of course
AddToList_OpenCourse = [] # Record code of course
AddToList_CourseName = [] # Record Name of course
AddToList_CourseTeacher = [] # Record Teacher of course

#global language_code
language_code = "zh_tw"
ProModeCount = 0

#global Default_GUI_SIZE_WIDTH
Default_GUI_SIZE_WIDTH = 600
#global Default_GUI_SIZE_HEIGHT
Default_GUI_SIZE_HEIGHT = 570
current_time_show = tk.StringVar()
execution_time_total = tk.StringVar()
global start_execution
global process


# Common function
def clearFrame(frame):
    # destroy all widgets from frame
    for widget in frame.winfo_children():
        widget.destroy()
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
    en_us["running_url"] = 'Running URL'
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

    # Default List
    en_us["DefaultOpenCourseName"] = 'Sample'
    en_us["DefaultOpenCourseTeacher"] = 'Sample'


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
    zh_tw["running_url"] = '執行網址：'
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

    # Default List
    zh_tw["DefaultOpenCourseName"] = '我是範例'
    zh_tw["DefaultOpenCourseTeacher"] = '我是範例'

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
    print(app_root)
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
def applyNewLanguage():
    #global language_code
    Set_Language_Code(UILanguageSelection.get().strip())
    # LessonList Tab
    Optional_Selective.config(values=[translate[language_code]['addLesson'], translate[language_code]['removeLesson'], translate[language_code]['cycleLesson']])
    Optional_Selective.current(0)

    # If List ==0, inisert sample to four list and show
    if len(AddToList_Action) == 0:
        quick_btn_cleanAll()
        initialList()
        showList()
    else:
        pass

    OpenCourseBox.delete(0,END)
    OpenCourseBox.insert(index=0, string=translate[language_code]["lessonCode"])
    OpenCourseName.delete(0,END)
    OpenCourseName.insert(index=0,string=translate[language_code]["lessonName"])
    OpenCourseTeacher.delete(0,END)
    OpenCourseTeacher.insert(index=0,string=translate[language_code]["lessonTeacher"])
    AddButton.config(text=translate[language_code]["addToList"])
    QuickChangeLabel.config(text=translate[language_code]["quicklyRevise"])
    QuickChange.config(text=translate[language_code]["exchange"])
    DeleteButton.config(text=translate[language_code]["remove"])
    CleanButton.config(text=translate[language_code]["clean"])
    SelectionListBarAction.config(text=" "+translate[language_code]["action"])
    SelectionListBarLessonCode.config(text=translate[language_code]["lessonCodeShow"])
    SelectionListBarLessonName.config(text=translate[language_code]["lessonNameShow"])
    SelectionListBarLessonTeacher.config(text=translate[language_code]["lessonTeacherShow"])
    SelectionListBarEdit.config(text=translate[language_code]["edit"])
    SaveListButton.config(text=translate[language_code]["saveList"])

    # advanced Tab
    browserLabel.config(text=translate[language_code]["browser"])
    UILanguageLabel.config(text=translate[language_code]["UILanguage"])
    WebDriverLabel.config(text=translate[language_code]["webdriver_type"])
    WebLanguageLabel.config(text=translate[language_code]["webLanguage"])
    AutoRefreshLabel.config(text=translate[language_code]["refleshGAP"])
    HeadlessModeLabel.config(text=translate[language_code]["headlessMode"])
    HeadlessModeConfirm.config(text=translate[language_code]["enable"])
    OutputLogLabel.config(text=translate[language_code]["logFileMode"])
    OutputModeConfirm.config(text=translate[language_code]["enable"])
    SpeedyFlashLabel.config(text=translate[language_code]["speedyCycle"])
    SpeedyFlashModeConfirm.config(text=translate[language_code]["enable"])
    ReviewTableLabel.config(text=translate[language_code]["reviewTable"])
    ReviewTableModeConfirm.config(text=translate[language_code]["enable"])
    SingleSignOnLabel.config(text=translate[language_code]["SingleSignOn"])
    SingleSignOnModeConfirm.config(text=translate[language_code]["enable"])

    #AccountTab
    SaveLoginIngormation.config(text=translate[language_code]["saveAccountPassword"])
    SSO_Picture_Setting(None)

    #runtime Tab
    StatusTitle.config(text=translate[language_code]["runningStatus"])
    lbl_wyshbot_last_url.config(text=translate[language_code]["running_url"])
    StopButton.config(text=translate[language_code]["stopRunning"])
    ResumeButton.config(text=translate[language_code]["continueRunning"])
    sys_clock.config(text=translate[language_code]["TaipeiTime"])
    execution_total_title.config(text=translate[language_code]["TotalTime"])
    execution_total_second.config(text=translate[language_code]["TotalTimeSecond"])
    AppVersionTitle.config(text=translate[language_code]["AppVersion"])
    SystemTypeTitle.config(text=translate[language_code]["System"])
    OSVersionTitle.config(text=translate[language_code]["OSVersion"])
    SystemArchitectureTitle.config(text=translate[language_code]["System_architecture"])
    PythonVersionTitle.config(text=translate[language_code]["SystemPythonVersion"])

    #about Tab
    slogan_1.config(text=translate[language_code]["Explain1"])
    slogan_2.config(text=translate[language_code]["Explain2"])
    slogan_3.config(text=translate[language_code]["Explain3"])
    slogan_4.config(text=translate[language_code]["Explain4"])

    Help_URL_Tilte.config(text=translate[language_code]["help"])
    ContributionTilte.config(text=translate[language_code]["Contribution"])
    ArchitectureTitle.config(text= translate[language_code]["BotArchitectureProvider"])
    MaxBot.config(text= translate[language_code]["MaxBot"])
    MaxBotLink.config(text=translate[language_code]["LINK"])
    DIYBrowserTitle.config(text=translate[language_code]["DIYBrowser"])
    CPY.config(text=translate[language_code]["CPY"])
    QualityTitle.config(text=translate[language_code]["TestGroup"])
    emilylee.config(text="Beauty－"+ translate[language_code]["emilylee"])

    # Act Bar
    global btn_run
    global btn_save
    global btn_restore_defaults
    global btn_exit
    btn_run.config(text=translate[language_code]['run'])
    btn_save.config(text=translate[language_code]['save'])
    btn_restore_defaults.config(text=translate[language_code]['restore_defaults'])
    btn_exit.config(text=translate[language_code]['exit'])

    tabControl.tab(0,text=translate[language_code]['lessonList'])
    tabControl.tab(1, text=translate[language_code]['advanced'])
    tabControl.tab(2, text=translate[language_code]['account'])
    tabControl.tab(3, text=translate[language_code]['runtime'])
    tabControl.tab(4, text=translate[language_code]['about'])
def applyJSONSetting(config_dict):
    browserSelection.set(config_dict["advanced"]["browser"])
    UILanguageSelection.set(config_dict["advanced"]["UILanguage"])
    WebDriverSelection.set(config_dict["advanced"]["webdriver_type"])
    WebLanguageSelection.set(config_dict["advanced"]["webLanguage"])
    AutoRefreshTextbox.delete(0,END)
    AutoRefreshTextbox.insert(0,config_dict["advanced"]["refleshGAP"])
    HeadlessMode.set(config_dict["advanced"]["headlessMode"]["enable"])
    OutputMode.set(config_dict["advanced"]["logFileMode"]["enable"])
    SpeedyFlashMode.set(config_dict["advanced"]["speedyCycle"]["enable"])
    ReviewTableMode.set(config_dict["advanced"]["reviewTable"]["enable"])
    SingleSignOnMode.set(config_dict["advanced"]["SingleSignOn"]["enable"])
def load_json():
    app_root = get_app_root()
    # overwrite config path.
    config_filepath = os.path.join(app_root, CONST_WYSHBOT_CONFIG_FILE)
    global config_dict
    config_dict = None
    if os.path.isfile(config_filepath):
        with open(config_filepath) as json_data:
            config_dict = json.load(json_data)
    else:
        config_dict = get_default_config()

    return config_filepath, config_dict
def get_language_code_by_name(new_language):
    global language_code
    language_code = "en_us"
    if u'繁體中文' in new_language:
        language_code = 'zh_tw'
    if u'簡体中文' in new_language:
        language_code = 'zh_cn'
    return language_code
def Set_Language_Code(new_Language):
    global language_code
    if u'繁體中文' in new_Language:
        language_code = "zh_tw"
    elif "English" in new_Language:
        language_code = "en_us"
    else:
        pass


# LessonList Tab
def OpenCourseBoxtextbox_press(event):
    if OpenCourseBox.get()==translate[language_code]["lessonCode"]:
        OpenCourseBox.delete(0, END)
def OpenCourseBoxtextbox_release(event):
    if not OpenCourseBox.get().isdigit():
        # if the OpenCourseBox has already entered open code, it will not be deleted
        OpenCourseBox.delete(0, END)
        OpenCourseBox.insert(index=0, string=translate[language_code]["lessonCode"])
def OpenCourseNametextbox_press(event):
    if OpenCourseName.get()==translate[language_code]["lessonName"]:
        OpenCourseName.delete(0, END)
def OpenCourseNametextbox_release(event):
    if not OpenCourseName.get()!="":
        # if the OpenCourseBox has already entered open code, it will not be deleted
        OpenCourseName.delete(0, END)
        OpenCourseName.insert(index=0, string=translate[language_code]["lessonName"])
def OpenCourseTeachertextbox_press(event):

    if OpenCourseTeacher.get() == translate[language_code]["lessonTeacher"]:
        OpenCourseTeacher.delete(0, END)
def OpenCourseTeachertextbox_release(event):
    if not OpenCourseTeacher.get()!="":
        # if the OpenCourseBox has already entered open code, it will not be deleted
        OpenCourseTeacher.delete(0, END)
        OpenCourseTeacher.insert(index=0, string=translate[language_code]["lessonTeacher"])
def quick_btn_exchange():
    Exchange(QuickChangeFirstTextBox.get(), QuickChangeSecondTextBox.get())
    QuickChangeFirstTextBox.delete(0,END)
    QuickChangeSecondTextBox.delete(0,END)
def quick_btn_cleanAll():
    if (len(AddToList_Action)==0):
        pass
    else:
        for i in range(len(AddToList_Action)):
            RemoveCourse(1)
def quick_btn_remove():
    RemoveCourse(QuickChangeDeleteTextBox.get())
def btn_add_to_List():
    global AddToList_Action
    global AddToList_OpenCourse
    global AddToList_CourseName
    global AddToList_CourseTeacher

    if len(OpenCourseBox.get()) ==4 and OpenCourseBox.get().isdigit():
        AddToList_Action.append(Optional_Selective.get())
        AddToList_OpenCourse.append(OpenCourseBox.get())

        # Deal with no enter OpenCourseName
        if OpenCourseName.get()!=translate[language_code]["lessonName"]:
            AddToList_CourseName.append(OpenCourseName.get())
        else:
            AddToList_CourseName.append("None")

        # Deal with no enter OpenCourse Teacher
        if OpenCourseTeacher.get() != translate[language_code]["lessonTeacher"]:
            AddToList_CourseTeacher.append(OpenCourseTeacher.get())
        else:
            AddToList_CourseTeacher.append("None")

        Optional_Selective.current(0)
        showList()

        # Clean OpenCourseBox TextBox, OpenCourseName TextBox and OpenCourseTeacher TextBox
        OpenCourseBox.delete(0, END)
        OpenCourseBoxtextbox_release(event=None)
        OpenCourseName.delete(0, END)
        OpenCourseNametextbox_release(event=None)
        OpenCourseTeacher.delete(0,END)
        OpenCourseTeachertextbox_release(event=None)
    elif OpenCourseBox.get() == "":
        messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["CourseCodeNotEmpty"])
    else:
        messagebox.showinfo(translate[language_code]["Infor"],translate[language_code]["CheckCourceCode"])
def Enter_add_to_List(event):
    global AddToList_Action
    global AddToList_OpenCourse
    global AddToList_CourseName
    global AddToList_CourseTeacher

    if len(OpenCourseBox.get()) ==4 and OpenCourseBox.get().isdigit():
        AddToList_Action.append(Optional_Selective.get())
        AddToList_OpenCourse.append(OpenCourseBox.get())

        # Deal with no enter OpenCourseName
        if OpenCourseName.get()!=translate[language_code]["lessonName"]:
            AddToList_CourseName.append(OpenCourseName.get())
        else:
            AddToList_CourseName.append("None")

        # Deal with no enter OpenCourse Teacher
        if OpenCourseTeacher.get() != translate[language_code]["lessonTeacher"]:
            AddToList_CourseTeacher.append(OpenCourseTeacher.get())
        else:
            AddToList_CourseTeacher.append("None")

        Optional_Selective.current(0)
        showList()

        # Clean OpenCourseBox TextBox, OpenCourseName TextBox and OpenCourseTeacher TextBox
        OpenCourseBox.delete(0, END)
        OpenCourseBoxtextbox_release(event=None)
        OpenCourseName.delete(0, END)
        OpenCourseNametextbox_release(event=None)
        OpenCourseTeacher.delete(0,END)
        OpenCourseTeachertextbox_release(event=None)
        OpenCourseBox.delete(0, END) # Point to the Course Code textbox
    elif OpenCourseBox.get() == "":
        messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["CourseCodeNotEmpty"])
    else:
        messagebox.showinfo(translate[language_code]["Infor"],translate[language_code]["CheckCourceCode"])
def Exchange(ExchangeIndex_1,ExchangeIndex_2):
    if (ExchangeIndex_1 and ExchangeIndex_2):
        FirstIndex = int(ExchangeIndex_1) - 1
        SecondIndex = int(ExchangeIndex_2) - 1
        if (FirstIndex < len(AddToList_Action) and FirstIndex >= 0 and SecondIndex < len(AddToList_Action) and SecondIndex >= 0 and SecondIndex != FirstIndex):
            AddToList_Action[FirstIndex], AddToList_Action[SecondIndex] = AddToList_Action[SecondIndex],AddToList_Action[FirstIndex]
            AddToList_OpenCourse[FirstIndex], AddToList_OpenCourse[SecondIndex] = AddToList_OpenCourse[SecondIndex], AddToList_OpenCourse[FirstIndex]
            AddToList_CourseName[FirstIndex], AddToList_CourseName[SecondIndex] = AddToList_CourseName[SecondIndex], AddToList_CourseName[FirstIndex]
            AddToList_CourseTeacher[FirstIndex], AddToList_CourseTeacher[SecondIndex] = AddToList_CourseTeacher[SecondIndex], AddToList_CourseTeacher[FirstIndex]
            showList()
        else:
            messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["ExchangeUnsuccessfully"])
    else:
        messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["ExchangeUnsuccessfully"])
    return
def RemoveCourse(index_value):
    remove_target = int(index_value)-1
    if (remove_target<len(AddToList_Action) and remove_target>=0):
        AddToList_Action.pop(remove_target)
        AddToList_OpenCourse.pop(remove_target)
        AddToList_CourseName.pop(remove_target)
        AddToList_CourseTeacher.pop(remove_target)
        showList()
    else:
        messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["CheckDeleteNumber"])
def showList():
    group_row_count = 1
    global Default_GUI_SIZE_HEIGHT,Default_GUI_SIZE_WIDTH
    global SelectionListDynamicFrame
    clearFrame(SelectionListDynamicFrame)
    for i in range(len(AddToList_Action)):
        # Create temp_row object by class method
        temp_row = SelectionListDynamicRow(i+1,AddToList_Action[i],AddToList_OpenCourse[i],AddToList_CourseName[i],AddToList_CourseTeacher[i],group_row_count,language_code)
        group_row_count += 1

    if len(AddToList_OpenCourse) >= 10:
        ScrollbarSetting()
def btn_savelist():
    app_root = get_app_root()
    Selection_filepath = os.path.join(app_root, CONST_SELECTION_FILE)
    selection_dict = {}
    for i in range(len(AddToList_Action)):
        selection_dict[i]={}
        selection_dict[i]["Action"] = AddToList_Action[i]
        selection_dict[i]["OpenCode"] = AddToList_OpenCourse[i]
        selection_dict[i]["CourseName"] = AddToList_CourseName[i]
        selection_dict[i]["Teacher"] = AddToList_CourseTeacher[i]
    save_json(selection_dict,Selection_filepath)
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
    else:
        pass
def ScrollbarConfigure(event):
    dynamiccanvas.configure(scrollregion=dynamiccanvas.bbox("all"), width=490, height=290)
def ScrollbarSetting():
    # Enable Scrollbar and revise edit area width
    DynamicScrollbar ["command"]=dynamiccanvas.yview
    SelectionListBarEdit["width"]=17


# advacned Tab
def HeadlessModeInformation():
    messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["headlessModeExplain"])
def OutputModeInformation():
    messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["logFileModeExplain"])
def SpeedyFlashModeInformation():
    messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["speedyCycleExplain"])
def ReviewTableModeInformation():
    messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["reviewTableExplain"])
def SingleSignOnModeInformation():
    messagebox.showinfo(translate[language_code]["Infor"], translate[language_code]["SingleSignOnExplain"])


# account Tab
def SSO_Picture_Setting(even):
    SSO_Canvas.delete(ALL)
    global AccountTextbox
    global PasswordTextbox
    global SaveLoginIngormation
    if (language_code=="zh_tw"):
        image_source = ChineseUI
        SSO_Canvas.create_image(0, 0, anchor='nw', image=image_source)
        SSO_Canvas.pack()

        AccountTextbox.place(x=310, y=112, anchor=CENTER)
        PasswordTextbox.place(x=310, y=145, anchor=CENTER)
        SaveLoginIngormation.place(x=300, y=183, anchor=CENTER)
    else:
        image_source = EnglishUI
        SSO_Canvas.create_image(0, 0, anchor='nw', image=image_source)
        SSO_Canvas.pack()

        AccountTextbox.place(x=330, y=107, anchor=CENTER)
        PasswordTextbox.place(x=330, y=140, anchor=CENTER)
        SaveLoginIngormation.place(x=300, y=183, anchor=CENTER)
def btn_save_account():
    app_root = get_app_root()
    License_filepath = os.path.join(app_root, CONST_LICENSE)
    account_str = AccountTextbox.get()
    password_str = PasswordTextbox.get()
    Account_dict = {}
    Account_dict["Account"] = account_str
    Account_dict["Password"] = password_str
    save_json(Account_dict, License_filepath)
def load_save_account():
    app_root = get_app_root()
    # overwrite config path.
    License_filepath = os.path.join(app_root, CONST_LICENSE)
    Account_dict = None
    if os.path.isfile(License_filepath):
        with open(License_filepath) as json_data:
            Account_dict = json.load(json_data)
        AccountTextbox.insert(0, Account_dict["Account"])
        PasswordTextbox.insert(0, Account_dict["Password"])
    else:
        pass
# runtime Tab
def GetCurrentTime():
    # System Clock
    sys_time_data = datetime.now()
    current_time = sys_time_data.strftime('%H:%M:%S')
    current_time_show.set(current_time)
    global execution_time_total
    execution_time = sys_time_data - start_execution
    execution_time_total.set(execution_time)
    root.after(1000,GetCurrentTime)
def do_wyshbot_idle():
    app_root = get_app_root()
    idle_filepath = app_root+"/"+CONST_WYSHBOT_INT28_FILE
    with open(idle_filepath, "w") as text_file:
        text_file.write("")
def read_last_url_from_file():
    ret = ""
    if os.path.exists(CONST_WYSHBOT_LAST_URL_FILE):
        with open(CONST_WYSHBOT_LAST_URL_FILE, "r") as text_file:
            ret = text_file.readline()
    return ret
def update_wyshbot_runtime_status():
    filepath = get_app_root()+"/"+CONST_WYSHBOT_INT28_FILE
    is_paused = False
    if os.path.isfile(filepath):
        is_paused = True
        print("WYSHBot is paused 788")
    try:
        global language_code
        global CurrentStatus
        wyshbot_status = translate[language_code]['runningEnable']
        if is_paused:
            wyshbot_status = translate[language_code]['runningDisable']

        CurrentStatus.config(text=wyshbot_status)

        global StopButton, ResumeButton

        if not is_paused:
            StopButton.grid(column=2, row=0)
            ResumeButton.grid_forget()
        else:
            ResumeButton.grid(column=2, row=0)
            StopButton.grid_forget()

        global lbl_wyshbot_last_url_data
        last_url = read_last_url_from_file()
        if len(last_url) > 20:
            last_url=last_url[:20]+"..."
        lbl_wyshbot_last_url_data.config(text=last_url)

    except Exception as exc:
        #print(exc)
        pass
def btn_idle_clicked(language_code):
    print("wyshbot is paused")
    do_wyshbot_idle()
    update_wyshbot_runtime_status()

# about Tab
def open_url(url):
    webbrowser.open_new(url)



# Action Bar
def btn_run_clicked(language_code):
    print('run button pressed.')
    Root_Dir = ""
    save_ret = btn_save_act(language_code)
    print("save config result:", save_ret)
    if save_ret:
        threading.Thread(target=launch_wyshbot).start()
def launch_wyshbot():
    run_python_script("main")
def run_python_script(script_name):
    global process
    working_dir = get_app_root()
    if hasattr(sys, 'frozen'):
        print("execute in frozen mode")

        # check platform here.
        if platform.system() == 'Darwin':
            print("execute MacOS python script")
            process = subprocess.Popen("./" + script_name, shell=True, cwd=working_dir)
        if platform.system() == 'Linux':
            print("execute linux binary")
            process = subprocess.Popen("./" + script_name, shell=True, cwd=working_dir)
        if platform.system() == 'Windows':
            print("execute .exe binary.")
            process = subprocess.Popen(script_name + ".exe", shell=True, cwd=working_dir)
    else:
        interpreter_binary = 'python'
        interpreter_binary_alt = 'python3'
        if platform.system() == 'Darwin':
            # try python3 before python.
            interpreter_binary = 'python3'
            interpreter_binary_alt = 'python'
        print("execute in shell mode.")
        #print("script path:", working_dir)
        #messagebox.showinfo(title="Debug0", message=working_dir)

        # some python3 binary, running in 'python' command.
        try:
            print('try', interpreter_binary)
            process = subprocess.Popen([interpreter_binary, script_name + '.py'], cwd=working_dir)
            #s=subprocess.Popen(['./chrome_tixcraft'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_dir)
            #s=subprocess.run(['python3', 'chrome_tixcraft.py'], cwd=working_dir)
            #messagebox.showinfo(title="Debug1", message=str(s))
        except Exception as exc:
            print('try', interpreter_binary_alt)
            try:
                process = subprocess.Popen([interpreter_binary_alt, script_name + '.py'], cwd=working_dir)
            except Exception as exc:
                msg=str(exc)
                print("exeption:", msg)
                #messagebox.showinfo(title="Debug2", message=msg)
                pass
def btn_save_clicked(language_code):
    btn_save_act(language_code)
def btn_save_act(language_code):
    app_root = get_app_root()
    config_filepath = os.path.join(app_root, CONST_WYSHBOT_CONFIG_FILE)
    config_dict = get_default_config()
    is_all_data_correct = True

    if is_all_data_correct:
        config_dict["advanced"]["browser"] = browserSelection.get().strip()
        config_dict["advanced"]["UILanguage"] = UILanguageSelection.get().strip()
        Set_Language_Code(UILanguageSelection.get().strip())
        config_dict["advanced"]["webdriver_type"] = WebDriverSelection.get().strip()
        config_dict["advanced"]["webLanguage"] = WebLanguageSelection.get().strip()
        if (config_dict["advanced"]["webLanguage"]=="中文"):
            config_dict["homepage"]=URL_Chinese
        else:
            config_dict["homepage"]=URL_English

        if AutoRefreshTextbox.get().strip()=="":
            is_all_data_correct = False
            messagebox.showerror("Error", "Please enter refresh time gap")
        else:
            config_dict["advanced"]["refleshGAP"] = AutoRefreshTextbox.get().strip()

    if is_all_data_correct:
        config_dict["advanced"]["headlessMode"]["enable"] = bool(HeadlessMode.get())
        config_dict["advanced"]["logFileMode"]["enable"] = bool(OutputMode.get())
        config_dict["advanced"]["speedyCycle"]["enable"] = bool(SpeedyFlashMode.get())
        config_dict["advanced"]["reviewTable"]["enable"] = bool(ReviewTableMode.get())
        config_dict["advanced"]["SingleSignOn"]["enable"] = bool(SingleSignOnMode.get())

    # save config.
    if is_all_data_correct:
        save_json(config_dict, config_filepath)
        btn_savelist()# Save Selection List
        btn_save_account()# Save Account Information

    return is_all_data_correct
def save_json(config_dict, target_path):
    json_str = json.dumps(config_dict, indent=4)
    with open(target_path, 'w') as outfile:
        outfile.write(json_str)
def btn_exit_clicked():
    global process
    root.destroy()
    process.terminate()
    process.wait()
def btn_restore_defaults_clicked(language_code):
    app_root = get_app_root()
    config_filepath = os.path.join(app_root, CONST_WYSHBOT_CONFIG_FILE)
    config_dict = get_default_config()
    quick_btn_cleanAll()
    #initialList()
    with open(config_filepath, 'w') as outfile:
        json.dump(config_dict, outfile)

    # Reload UI
    global root
    load_GUI(root, config_dict)
    initialList() #Reset Course List
    showList() #Show Row
    applyJSONSetting(config_dict)
def force_remove_file(filepath):
    if os.path.exists(filepath):
        try:
            os.remove(filepath)
            print("remove temp file")
        except Exception as exc:
            print(Exception)
            pass
def do_wyshbot_resume():
    idle_filepath = get_app_root()+"/"+CONST_WYSHBOT_INT28_FILE
    print("Remove path")
    print(idle_filepath)
    force_remove_file(idle_filepath)
    print("Remove idele file")
    '''for i in range(3):
        force_remove_file(idle_filepath)'''
def btn_resume_clicked(language_code):
    print("wyshbot is resumed")
    do_wyshbot_resume()
    update_wyshbot_runtime_status()
# Every Tab
def lessonListTab(root, config_dict, language_code, UI_PADDING_X):
    clearFrame(root)
    row_count = 0

    CourseActionFrame = Frame(root)
    group_row_count = 0

    # Options 下拉式選單(加選、退選、刷課)
    # first row need padding Y
    global Optional_Selective
    Optional_Selective = ttk.Combobox(CourseActionFrame, state="readonly", width=5, values=[translate[language_code]['addLesson'], translate[language_code]['removeLesson']])
    Optional_Selective.grid(column=0, row=group_row_count)
    Optional_Selective.current(0)

    # OpenCourseCode textbox
    global OpenCourseBox
    OpenCourseBox = ttk.Entry(CourseActionFrame,width=10)
    OpenCourseBox.insert(index=0,string=translate[language_code]["lessonCode"])
    OpenCourseBox.grid(column=1, row=group_row_count)
    OpenCourseBox.bind("<Button-1>", OpenCourseBoxtextbox_press)#Press Mouse left to delete insert text
    OpenCourseBox.bind("<FocusOut>", OpenCourseBoxtextbox_release)
    OpenCourseBox.bind("<Return>", Enter_add_to_List)

    # OpenCourse Name textbox
    global OpenCourseName
    OpenCourseName = ttk.Entry(CourseActionFrame,width=15)
    OpenCourseName.insert(index=0, string=translate[language_code]["lessonName"])
    OpenCourseName.grid(column=2, row=group_row_count)
    OpenCourseName.bind("<Button-1>", OpenCourseNametextbox_press)  # Press Mouse left to delete insert text
    OpenCourseName.bind("<FocusOut>", OpenCourseNametextbox_release)

    # OpenCourse Teacher Textbox
    global OpenCourseTeacher
    OpenCourseTeacher = ttk.Entry(CourseActionFrame, width=10)
    OpenCourseTeacher.insert(index=0, string=translate[language_code]["lessonTeacher"])
    OpenCourseTeacher.grid(column=3, row=group_row_count)
    OpenCourseTeacher.bind("<Button-1>", OpenCourseTeachertextbox_press)  # Press Mouse left to delete insert text
    OpenCourseTeacher.bind("<FocusOut>", OpenCourseTeachertextbox_release)

    # Add To List Button
    global AddButton
    AddButton = tk.Button(CourseActionFrame,text=translate[language_code]["addToList"], command=btn_add_to_List)
    AddButton.grid(column=4, row=group_row_count)

    CourseActionFrame.grid(column=0,row=row_count,sticky=W, padx=UI_PADDING_X)

    # ==============================================================================================================================
    # Quick Revise Area, so row_count++ and group_row_count set 0
    row_count += 1
    group_row_count = 0

    ReviseAreaFrame = Frame(root)

    # Revise Area Title
    global QuickChangeLabel
    QuickChangeLabel = tk.Label(ReviseAreaFrame, text=translate[language_code]["quicklyRevise"])
    QuickChangeLabel.grid(column=2,row=group_row_count,sticky = N)

    group_row_count+=1
    # Revise Area First #
    QuickChangeLabelFirstSharp = tk.Label(ReviseAreaFrame, text="#")
    QuickChangeLabelFirstSharp.grid(column=0, row=group_row_count, sticky=E)

    # Revise Area First Textbox
    global QuickChangeFirstTextBox
    QuickChangeFirstTextBox = ttk.Entry(ReviseAreaFrame, width=5)
    QuickChangeFirstTextBox.grid(column=1, row=group_row_count)

    # Revise Area Second #
    QuickChangeLabelSecondSharp = tk.Label(ReviseAreaFrame, text="#")
    QuickChangeLabelSecondSharp.grid(column=2, row=group_row_count, sticky=E)

    # Revise Area Second Textbox
    global QuickChangeSecondTextBox
    QuickChangeSecondTextBox = ttk.Entry(ReviseAreaFrame, width=5)
    QuickChangeSecondTextBox.grid(column=3, row=group_row_count)

    # Revise Area Exchange Button
    global QuickChange
    QuickChange = tk.Button(ReviseAreaFrame, text=translate[language_code]["exchange"], command=quick_btn_exchange)
    QuickChange.grid(column=4, row=group_row_count)

    group_row_count+=1

    # Revise Area Delete #
    QuickChangeLabelDeleteSharp = tk.Label(ReviseAreaFrame, text="#")
    QuickChangeLabelDeleteSharp.grid(column=1, row=group_row_count, sticky=E)

    # Revise Area Delete Textbox.
    global QuickChangeDeleteTextBox
    QuickChangeDeleteTextBox = ttk.Entry(ReviseAreaFrame, width=5)
    QuickChangeDeleteTextBox.grid(column=2, row=group_row_count)

    # Revise Area Delete Button
    global DeleteButton
    DeleteButton = tk.Button(ReviseAreaFrame, text=translate[language_code]["remove"], command=quick_btn_remove)
    DeleteButton.grid(column=3, row=group_row_count)

    # Revise Area Clean Button
    global CleanButton
    CleanButton = tk.Button(ReviseAreaFrame, text=translate[language_code]["clean"], command=quick_btn_cleanAll)
    CleanButton.grid(column=4, row=group_row_count)

    ReviseAreaFrame.grid(column=0, row=row_count, sticky=N, padx=UI_PADDING_X)

    # ==============================================================================================================================
    # ReviseAreaFrame finish, so row_count++
    row_count += 1
    group_row_count = 0
    global SelectionListFrame
    SelectionListFrame = Frame(root)

    # SelectionList Bar #
    # There is a space bafore #, because it can help line up more perfect
    SelectionListBarSharp = tk.Label(SelectionListFrame, text=" #")
    SelectionListBarSharp.grid(column=0, row=group_row_count, sticky=E)

    # SelectionList Bar Action
    # There is a space bafore action label, because it can help line up more perfect
    global SelectionListBarAction
    SelectionListBarAction = tk.Label(SelectionListFrame, text=" "+translate[language_code]["action"],width=8)
    SelectionListBarAction.grid(column=1, row=group_row_count, sticky=E)

    # SelectionList Bar Lesson Code
    global SelectionListBarLessonCode
    SelectionListBarLessonCode = tk.Label(SelectionListFrame, text=translate[language_code]["lessonCodeShow"],width=5)
    SelectionListBarLessonCode.grid(column=2, row=group_row_count, sticky=E)

    # SelectionList Bar Lesson Name
    global SelectionListBarLessonName
    SelectionListBarLessonName = tk.Label(SelectionListFrame, text=translate[language_code]["lessonNameShow"],width=10)
    SelectionListBarLessonName.grid(column=3, row=group_row_count, sticky=E)

    # SelectionList Bar Lesson Teacher
    global SelectionListBarLessonTeacher
    SelectionListBarLessonTeacher = tk.Label(SelectionListFrame, text=translate[language_code]["lessonTeacherShow"],width=8)
    SelectionListBarLessonTeacher.grid(column=4, row=group_row_count, sticky=E)

    # SelectionList Bar edit
    global SelectionListBarEdit
    SelectionListBarEdit = tk.Label(SelectionListFrame, text=translate[language_code]["edit"],width=19)
    SelectionListBarEdit.grid(column=5, row=group_row_count)

    SelectionListFrame.grid(column=0, row=row_count, sticky=N, padx=UI_PADDING_X)

    # ==============================================================================================================================
    # SelectionListFrame Finish, row_count++ and group_row_count set 0
    # SelectionListContent
    row_count+=1
    group_row_count = 0
    # Create Canvas
    global dynamiccanvas
    dynamiccanvas = Canvas(root)
    dynamiccanvas.grid(column=0, row=row_count, sticky=N, padx=UI_PADDING_X)

    global DynamicScrollbar
    DynamicScrollbar = Scrollbar(root, orient="vertical")
    DynamicScrollbar.place(x=515, y=130, height=290)
    dynamiccanvas.configure(yscrollcommand=DynamicScrollbar.set)

    global SelectionListDynamicFrame
    SelectionListDynamicFrame = Frame(dynamiccanvas)
    dynamiccanvas.create_window((0, 0), window=SelectionListDynamicFrame, anchor='nw')
    SelectionListDynamicFrame.bind("<Configure>", ScrollbarConfigure)
    #SelectionListDynamicFrame.grid(column=0, row=row_count, sticky=N, padx=UI_PADDING_X)


    # ==============================================================================================================================
    # SelectionListContent Finish, row_count++ and group_row_count set 0
    row_count += 1
    group_row_count = 0
    global SaveButtonFrame
    SaveButtonFrame = Frame(root)
    # Selection List Save Button
    global SaveListButton
    SaveListButton= tk.Button(SaveButtonFrame, fg='red', command=btn_savelist,text=translate[language_code]["saveList"])
    SaveListButton.grid(column=0, row=group_row_count)
    SaveButtonFrame.grid(column=0, row=row_count, sticky=N, padx=UI_PADDING_X)
def advancedTab(root, config_dict, language_code, UI_PADDING_X):
    clearFrame(root)
    row_count = 0
    group_row_count = 0
    # Selection Frame Set
    SelectionFrame = Frame(root)
    # Browser Selection Title
    global browserLabel
    browserLabel= tk.Label(SelectionFrame, text=translate[language_code]["browser"])
    browserLabel.grid(column=0,row=group_row_count,sticky=E)

    # Browser Selection values
    global browserSelection
    browserSelection = ttk.Combobox(SelectionFrame, state="readonly", values=[CONST_WEB_BROWSER_CHROME, CONST_WEB_BROWSER_EDGE, CONST_WEB_BROWSER_BRAVE])
    browserSelection.grid(column=1,row=group_row_count,sticky=W)
    browserSelection.current(0)

    group_row_count+=1

    # UI Language
    global UILanguageLabel
    UILanguageLabel = tk.Label(SelectionFrame, text=translate[language_code]["UILanguage"])
    UILanguageLabel.grid(column=0, row=group_row_count, sticky=E)

    # Browser Selection values
    global UILanguageSelection
    UILanguageSelection = ttk.Combobox(SelectionFrame, state="readonly",values=[CONST_UI_LANGUAGE_CHINESE,CONST_UI_LANGUAGE_ENGLISH])
    UILanguageSelection.grid(column=1, row=group_row_count, sticky=W)
    UILanguageSelection.current(0)
    UILanguageSelection.bind("<<ComboboxSelected>>", lambda e:applyNewLanguage())


    group_row_count += 1

    # WebDriver Type
    # WebDriver
    global WebDriverLabel
    WebDriverLabel= tk.Label(SelectionFrame, text=translate[language_code]["webdriver_type"])
    WebDriverLabel.grid(column=0, row=group_row_count, sticky=E)

    # Browser Selection values
    global WebDriverSelection
    WebDriverSelection = ttk.Combobox(SelectionFrame, state="readonly",values=[CONST_WEBDRIVER_TYPE_UC, CONST_WEBDRIVER_TYPE_SELENIUM])
    WebDriverSelection.grid(column=1, row=group_row_count, sticky=W)
    WebDriverSelection.current(0)

    group_row_count += 1

    # Web Language
    global WebLanguageLabel
    WebLanguageLabel= tk.Label(SelectionFrame, text=translate[language_code]["webLanguage"])
    WebLanguageLabel.grid(column=0, row=group_row_count, sticky=E)

    # Browser Language values
    global WebLanguageSelection
    WebLanguageSelection = ttk.Combobox(SelectionFrame, state="readonly",values=[CONST_WEB_LANGUAGW_CHINESE,CONST_WEB_LANGUAGW_ENGLISH])
    WebLanguageSelection.grid(column=1, row=group_row_count, sticky=W)
    WebLanguageSelection.current(0)

    group_row_count += 1

    # Auto Refresh Web Time
    global AutoRefreshLabel
    AutoRefreshLabel = tk.Label(SelectionFrame, text=translate[language_code]["refleshGAP"])
    AutoRefreshLabel.grid(column=0, row=group_row_count, sticky=E)

    # Auto Refresh Web Time Textbox
    global AutoRefreshTextbox
    AutoRefreshTextbox = ttk.Entry(SelectionFrame, width=15)
    number = str(random.randint(3, 10))
    AutoRefreshTextbox.insert(index=0, string=number)
    AutoRefreshTextbox.config(state= "disabled")
    AutoRefreshTextbox.grid(column=1, row=group_row_count, sticky=W)

    SelectionFrame.grid(column=0,row=row_count,sticky=W, padx=UI_PADDING_X)
    row_count+=1
    #===================================================================================================================================
    group_row_count = 0
    OptionalSelectiveFrame = Frame(root)

    # Headless Mode
    global HeadlessModeLabel
    HeadlessModeLabel = tk.Label(OptionalSelectiveFrame, text=translate[language_code]["headlessMode"])
    #HeadlessModeLabel.grid(column=0,row=group_row_count,sticky=E)

    global HeadlessMode
    HeadlessMode = BooleanVar()

    global HeadlessModeConfirm
    HeadlessModeConfirm = Checkbutton(OptionalSelectiveFrame, text=translate[language_code]["enable"], variable=HeadlessMode, state= "disabled")
    #HeadlessModeConfirm.grid(column=1,row=group_row_count,sticky=W)


    HeadlessModeInforbutton = tk.Button(OptionalSelectiveFrame, text="i",command=HeadlessModeInformation)
    #HeadlessModeInforbutton.grid(column=2,row=group_row_count,sticky=W)

    group_row_count+=1

    # Output full log
    global OutputLogLabel
    OutputLogLabel = tk.Label(OptionalSelectiveFrame, text=translate[language_code]["logFileMode"])
    OutputLogLabel.grid(column=0, row=group_row_count, sticky=E)

    global OutputMode
    OutputMode = BooleanVar()

    global OutputModeConfirm
    OutputModeConfirm = Checkbutton(OptionalSelectiveFrame, text=translate[language_code]["enable"],variable=OutputMode)
    OutputModeConfirm.grid(column=1, row=group_row_count, sticky=W)

    OutputModeInforbutton = tk.Button(OptionalSelectiveFrame, text="i", command=OutputModeInformation)
    OutputModeInforbutton.grid(column=2, row=group_row_count, sticky=W)

    group_row_count += 1

    # SpeedyFlashMode
    global SpeedyFlashLabel
    SpeedyFlashLabel = tk.Label(OptionalSelectiveFrame, text=translate[language_code]["speedyCycle"])
    #SpeedyFlashLabel.grid(column=0,row=group_row_count,sticky=E)

    global SpeedyFlashMode
    SpeedyFlashMode = BooleanVar()
    global SpeedyFlashModeConfirm
    SpeedyFlashModeConfirm = Checkbutton(OptionalSelectiveFrame, text=translate[language_code]["enable"],variable=SpeedyFlashMode, state="disable")
    #SpeedyFlashModeConfirm.grid(column=1, row=group_row_count, sticky=W)

    SpeedyFlashModeInforbutton = tk.Button(OptionalSelectiveFrame, text="i", command=SpeedyFlashModeInformation)
    #SpeedyFlashModeInforbutton.grid(column=2, row=group_row_count, sticky=W)

    group_row_count+=1

    # ReviewTable
    global ReviewTableLabel
    ReviewTableLabel = tk.Label(OptionalSelectiveFrame, text=translate[language_code]["reviewTable"])
    ReviewTableLabel.grid(column=0, row=group_row_count, sticky=E)

    global ReviewTableMode
    ReviewTableMode = BooleanVar()
    global ReviewTableModeConfirm
    ReviewTableModeConfirm = Checkbutton(OptionalSelectiveFrame, text=translate[language_code]["enable"],variable=ReviewTableMode)
    ReviewTableModeConfirm.grid(column=1, row=group_row_count, sticky=W)

    ReviewTableModeInforbutton = tk.Button(OptionalSelectiveFrame, text="i", command=ReviewTableModeInformation)
    ReviewTableModeInforbutton.grid(column=2, row=group_row_count, sticky=W)

    group_row_count+=1

    # Single Sign On
    global SingleSignOnLabel
    SingleSignOnLabel = tk.Label(OptionalSelectiveFrame, text=translate[language_code]["SingleSignOn"])
    #SingleSignOnLabel.grid(column=0, row=group_row_count, sticky=E)

    global SingleSignOnMode
    SingleSignOnMode = BooleanVar()
    global SingleSignOnModeConfirm
    SingleSignOnModeConfirm = Checkbutton(OptionalSelectiveFrame, text=translate[language_code]["enable"],variable=SingleSignOnMode, state="disable")
    #SingleSignOnModeConfirm.grid(column=1, row=group_row_count, sticky=W)

    SingleSignOnModeInforbutton = tk.Button(OptionalSelectiveFrame, text="i", command=SingleSignOnModeInformation)
    #SingleSignOnModeInforbutton.grid(column=2, row=group_row_count, sticky=W)

    group_row_count += 1
    OptionalSelectiveFrame.grid(column=0,row=row_count,sticky=W, padx=UI_PADDING_X)
def accountTab(root, config_dict, language_code, UI_PADDING_X):
    clearFrame(root)
    row_count = 0
    group_row_count = 0
    global SSO_Canvas
    SSO_Canvas = Canvas(root, width=550, height=500)

    # Account Textbox
    global AccountTextbox
    AccountTextbox = ttk.Entry(SSO_Canvas, width=15)
    # Password Textbox
    global PasswordTextbox
    PasswordTextbox = ttk.Entry(SSO_Canvas, width=15)
    # SaveButton
    global SaveLoginIngormation
    SaveLoginIngormation= tk.Button(SSO_Canvas,font=("normal",15),compound="center",text=translate[language_code]["saveAccountPassword"],borderwidth=0,command=btn_save_account)

    if (language_code == "zh_tw"):
        AccountTextbox.place(x=310, y=112, anchor=CENTER)
        PasswordTextbox.place(x=310, y=145, anchor=CENTER)
        SaveLoginIngormation.place(x=300, y=183, anchor=CENTER)
    else:
        AccountTextbox.place(x=330, y=107, anchor=CENTER)
        PasswordTextbox.place(x=330, y=140, anchor=CENTER)
        SaveLoginIngormation.place(x=300, y=183, anchor=CENTER)

    SSO_Picture_Setting(None)
def runtimeTab(root, config_dict, language_code, UI_PADDING_X):
    clearFrame(root)
    row_count = 0
    group_row_count = 0
    global status_frame
    status_frame = Frame(root)

    # Status Title
    global StatusTitle
    StatusTitle = tk.Label(status_frame, text=translate[language_code]["runningStatus"])
    StatusTitle.grid(column=0, row=group_row_count, sticky=E)

    # Current Status
    CurrentStatus_Label = ""
    global CurrentStatus
    CurrentStatus = tk.Label(status_frame,text=CurrentStatus_Label)
    CurrentStatus.grid(column=1, row=group_row_count, sticky=W)

    # Status Button
    global StopButton,ResumeButton

    StopButton = ttk.Button(status_frame, text=translate[language_code]['stopRunning'], command=lambda: btn_idle_clicked(language_code))
    StopButton.grid(column=2, row=group_row_count, sticky=W)

    ResumeButton = ttk.Button(status_frame, text=translate[language_code]['continueRunning'],command=lambda: btn_resume_clicked(language_code))
    ResumeButton.grid(column=3, row=group_row_count, sticky=W)

    group_row_count +=1

    #Current url
    global lbl_wyshbot_last_url
    lbl_wyshbot_last_url = Label(status_frame, text=translate[language_code]['running_url'])
    lbl_wyshbot_last_url.grid(column=0, row=group_row_count, sticky=E)

    last_url = ""
    global lbl_wyshbot_last_url_data
    lbl_wyshbot_last_url_data = Label(status_frame, text=last_url)
    lbl_wyshbot_last_url_data.grid(column=1, row=group_row_count, sticky=W)

    group_row_count += 1

    # System Clock Title
    global sys_clock
    sys_clock = tk.Label(status_frame, text=translate[language_code]["TaipeiTime"])
    sys_clock.grid(column=0, row=group_row_count, sticky=E)
    # System Current Clock
    lbl_sys_time_data = tk.Label(status_frame, textvariable=current_time_show)
    lbl_sys_time_data.grid(column=1, row=group_row_count, sticky=W)
    group_row_count += 1

    #Execution Time Title
    global execution_total_title
    execution_total_title = tk.Label(status_frame, text=translate[language_code]["TotalTime"])
    #execution_total_title.grid(column=0, row=group_row_count, sticky=E)
    #Execution Time Total
    execution_total = tk.Label(status_frame,textvariable=execution_time_total)
    #execution_total.grid(column=1, row=group_row_count, sticky=W)
    #Execution Time Second
    global execution_total_second
    execution_total_second = tk.Label(status_frame,text=translate[language_code]["TotalTimeSecond"])
    #execution_total_second.grid(column=2, row = group_row_count,sticky=W)
    status_frame.grid(column=0, row=row_count, sticky=W, padx=UI_PADDING_X)
    row_count+=1

    # System Detail
    SystemDetail = Frame(root,background='black')
    OSDetail = platform.platform().split("-")

    #AppVersion Title
    global AppVersionTitle
    AppVersionTitle = tk.Label(SystemDetail, text=translate[language_code]["AppVersion"], background='black', foreground='#7cfc00')
    AppVersionTitle.grid(column=0,row=group_row_count,sticky=W,padx=UI_PADDING_X)
    #AppleVerion
    AppVersion = tk.Label(SystemDetail, text=CONST_APP_VERSION, background='black', foreground='#7cfc00')
    AppVersion.grid(column=1,row=group_row_count,sticky=W,padx=UI_PADDING_X)
    group_row_count+=1

    #System Type Title
    global SystemTypeTitle
    SystemTypeTitle = tk.Label(SystemDetail, text=translate[language_code]["System"], background='black', foreground='#7cfc00')
    SystemTypeTitle.grid(column=0,row=group_row_count,sticky=W,padx=UI_PADDING_X)
    #System Type
    SystemType = tk.Label(SystemDetail, text=OSDetail[0], background='black', foreground='#7cfc00')
    SystemType.grid(column=1,row=group_row_count,sticky=W,padx=UI_PADDING_X)
    group_row_count+=1

    # OSVersion_Title
    global OSVersionTitle
    OSVersionTitle = tk.Label(SystemDetail, text=translate[language_code]["OSVersion"], background='black', foreground='#7cfc00')
    OSVersionTitle.grid(column=0,row=group_row_count,sticky=W,padx=UI_PADDING_X)
    #OSVersion
    OSVersion = tk.Label(SystemDetail, text=OSDetail[1], background='black', foreground='#7cfc00')
    OSVersion.grid(column=1,row=group_row_count,sticky=W,padx=UI_PADDING_X)
    group_row_count += 1

    #OS architecture Title
    global SystemArchitectureTitle
    SystemArchitectureTitle = tk.Label(SystemDetail, text=translate[language_code]["System_architecture"], background='black', foreground='#7cfc00')
    SystemArchitectureTitle.grid(column=0,row=group_row_count,sticky=W,padx=UI_PADDING_X)
    #OS architecture
    SystemArchitecture = tk.Label(SystemDetail,text=platform.machine(), background='black', foreground='#7cfc00')
    SystemArchitecture.grid(column=1,row=group_row_count,sticky=W,padx=UI_PADDING_X)
    group_row_count+=1

    #PythonVersion_Title
    global PythonVersionTitle
    PythonVersionTitle = tk.Label(SystemDetail, text=translate[language_code]["SystemPythonVersion"], background='black', foreground='#7cfc00')
    PythonVersionTitle.grid(column=0,row=group_row_count,sticky=W,padx=UI_PADDING_X)
    #PythonVersion
    PythonVersion = tk.Label(SystemDetail, text=platform.python_version(),background='black', foreground='#7cfc00')
    PythonVersion.grid(column=1, row=group_row_count, sticky=W, padx=UI_PADDING_X)
    group_row_count+=1

    SystemDetail.grid(column=0, row=row_count, sticky=N, padx=UI_PADDING_X)
def aboutTab(root, language_code):
    clearFrame(root)
    row_count = 0
    group_row_count = 0

    about_Frame = Frame(root)

    #Logo
    logo = tk.Label(about_Frame, image=ICON_Picture)
    logo.grid(column=0,row=group_row_count, padx=UI_PADDING_X,rowspan=4)
    #group_row_count += 1

    #Slogan
    global slogan_1
    slogan_1 = tk.Label(about_Frame, text=translate[language_code]["Explain1"])
    slogan_1.grid(column=1, row=group_row_count, sticky=N, padx=UI_PADDING_X)
    group_row_count += 1
    global slogan_2
    slogan_2 = tk.Label(about_Frame, text=translate[language_code]["Explain2"])
    slogan_2.grid(column=1, row=group_row_count, sticky=N, padx=UI_PADDING_X)
    group_row_count += 1
    global slogan_3
    slogan_3 = tk.Label(about_Frame, text=translate[language_code]["Explain3"])
    slogan_3.grid(column=1, row=group_row_count, sticky=N, padx=UI_PADDING_X)
    group_row_count+=1
    global slogan_4
    slogan_4 = tk.Label(about_Frame, text=translate[language_code]["Explain4"])
    slogan_4.grid(column=1, row=group_row_count, sticky=N, padx=UI_PADDING_X)
    group_row_count += 1

    # Space Gap
    spacetitle_2 = tk.Label(about_Frame, text="")
    spacetitle_2.grid(column=0, row=group_row_count)
    about_Frame.grid(row=row_count, sticky=N, padx=UI_PADDING_X)
    group_row_count += 1
    #URL Help
    global Help_URL_Tilte
    Help_URL_Tilte = tk.Label(about_Frame, text=translate[language_code]["help"])
    Help_URL_Tilte.grid(column=0, row=group_row_count, sticky=E, padx=UI_PADDING_X)
    Help_URL = tk.Label(about_Frame, text=URL_HELP, fg="blue", bg="gray", cursor="hand2")
    Help_URL.grid(column=1, row=group_row_count, sticky=W, padx=UI_PADDING_X,columnspan=2)
    Help_URL.bind("<Button-1>", lambda e: open_url(URL_HELP))
    group_row_count += 1
    #URL ChromeDrive
    ChromeDrive_URL_Tilte = tk.Label(about_Frame, text=translate[language_code]["chromedriver"])
    ChromeDrive_URL_Tilte.grid(column=0, row=group_row_count, sticky=E, padx=UI_PADDING_X)
    ChromeDrive_URL = tk.Label(about_Frame, text=URL_CHROME_DRIVER, fg="blue", bg="gray", cursor="hand2")
    ChromeDrive_URL.grid(column=1, row=group_row_count, sticky=W, padx=UI_PADDING_X,columnspan=2)
    ChromeDrive_URL.bind("<Button-1>", lambda e: open_url(URL_CHROME_DRIVER))
    group_row_count += 1
    #URL_FIREFOX_DRIVER
    FireFoxDriver_URL_Tilte = tk.Label(about_Frame, text=translate[language_code]["FireFoxdriver"])
    FireFoxDriver_URL_Tilte.grid(column=0, row=group_row_count, sticky=E, padx=UI_PADDING_X)
    FireFoxDriver_URL = tk.Label(about_Frame, text=URL_FIREFOX_DRIVER, fg="blue", bg="gray", cursor="hand2")
    FireFoxDriver_URL.grid(column=1, row=group_row_count, sticky=W, padx=UI_PADDING_X,columnspan=2)
    FireFoxDriver_URL.bind("<Button-1>", lambda e: open_url(URL_FIREFOX_DRIVER))
    group_row_count += 1
    # URL_EDGE_DRIVER
    EdgeDriver_URL_Tilte = tk.Label(about_Frame, text=translate[language_code]["Edgedriver"])
    EdgeDriver_URL_Tilte.grid(column=0, row=group_row_count, sticky=E, padx=UI_PADDING_X)
    EdgeDriver_URL = tk.Label(about_Frame, text=URL_EDGE_DRIVER, fg="blue", bg="gray", cursor="hand2")
    EdgeDriver_URL.grid(column=1, row=group_row_count, sticky=W, padx=UI_PADDING_X,columnspan=2)
    EdgeDriver_URL.bind("<Button-1>", lambda e: open_url(URL_EDGE_DRIVER))
    group_row_count += 1
    # Space Gap
    spacetitle_1 = tk.Label(about_Frame,text="")
    spacetitle_1.grid(column = 0,row=group_row_count)
    about_Frame.grid(row=row_count, sticky=N, padx=UI_PADDING_X)
    row_count += 1

    # Contribution
    ContributionFrame = Frame(root, background='black',width=550)


    global ContributionTilte
    ContributionTilte = tk.Label(ContributionFrame, text=translate[language_code]["Contribution"], font=('楷體', 20), background='black',foreground='#7cfc00')
    ContributionTilte.grid(column=0, row=group_row_count, sticky=W, padx=UI_PADDING_X)
    group_row_count+=1

    #First Row
    global ArchitectureTitle
    ArchitectureTitle= tk.Label(ContributionFrame, text= translate[language_code]["BotArchitectureProvider"], font=('楷體',15),background='black',foreground='#7cfc00')
    ArchitectureTitle.grid(column=0, row=group_row_count, sticky=W, padx=UI_PADDING_X)
    global MaxBot
    MaxBot = tk.Label(ContributionFrame,text= translate[language_code]["MaxBot"], font=('楷體',15),background='black',foreground='#7cfc00')
    MaxBot.grid(column=1, row=group_row_count, sticky=W, padx=UI_PADDING_X)
    global MaxBotLink
    MaxBotLink = tk.Label(ContributionFrame, text=translate[language_code]["LINK"], fg="blue",background='black', cursor="hand2")
    MaxBotLink.grid(column=2, row=group_row_count, sticky=W, padx=UI_PADDING_X)
    MaxBotLink.bind("<Button-1>", lambda e: open_url(MAXBot_URL))
    group_row_count += 1

    #Second Row
    global DIYBrowserTitle
    DIYBrowserTitle = tk.Label(ContributionFrame, text=translate[language_code]["DIYBrowser"], font=('楷體',15),background='black',foreground='#7cfc00')
    DIYBrowserTitle.grid(column=0, row=group_row_count, sticky=W, padx=UI_PADDING_X)
    global CPY
    CPY = tk.Label(ContributionFrame, text=translate[language_code]["CPY"], font=('楷體',15),background='black',foreground='#7cfc00')
    CPY.grid(column=1, row=group_row_count, sticky=W, padx=UI_PADDING_X)
    group_row_count += 1

    #Third Pow
    global QualityTitle
    QualityTitle = tk.Label(ContributionFrame, text=translate[language_code]["TestGroup"], font=('楷體',15),background='black',foreground='#7cfc00')
    QualityTitle.grid(column=0, row=group_row_count, sticky=W, padx=UI_PADDING_X)
    global emilylee
    emilylee= tk.Label(ContributionFrame, text="Beauty－"+ translate[language_code]["emilylee"], font=('楷體',15),background='black',foreground='#7cfc00')
    emilylee.grid(column=1,row=group_row_count,sticky=W,padx=UI_PADDING_X)

    ContributionFrame.grid(column=0, row=row_count, sticky=N, padx=UI_PADDING_X)
    row_count+=1

    # Hind Area
    global HideFrame
    HideFrame = Frame(root)
    HideFrame.grid(column = 0,row = row_count, sticky=N, padx=UI_PADDING_X)
def get_action_bar(root, language_code):
    frame_action = Frame(root)

    global btn_run
    global btn_save
    global btn_exit
    global btn_restore_defaults
    global btn_launcher

    btn_run = ttk.Button(frame_action, text=translate[language_code]['run'], command= lambda: btn_run_clicked(language_code))
    btn_run.grid(column=0, row=0)

    btn_save = ttk.Button(frame_action, text=translate[language_code]['save'], command= lambda: btn_save_clicked(language_code) )
    btn_save.grid(column=1, row=0)

    btn_restore_defaults = ttk.Button(frame_action, text=translate[language_code]['restore_defaults'],command=lambda: btn_restore_defaults_clicked(language_code))
    btn_restore_defaults.grid(column=2, row=0)

    btn_exit = ttk.Button(frame_action, text=translate[language_code]['exit'], command=btn_exit_clicked)
    btn_exit.grid(column=3, row=0)

    return frame_action


# Main Function
def load_GUI(root, config_dict):
    clearFrame(root)
    row_count = 0

    #load language
    language_code = get_language_code_by_name(config_dict["advanced"]["UILanguage"])

    #Setting Tab
    global tabControl
    tabControl = ttk.Notebook(root,height=460,width=550)
    tab1 = Frame(tabControl)
    tabControl.add(tab1, text=translate[language_code]['lessonList'])

    tab2 = Frame(tabControl)
    tabControl.add(tab2, text=translate[language_code]['advanced'])

    tab3 = Frame(tabControl)
    tabControl.add(tab3, text=translate[language_code]['account'])

    tab4 = Frame(tabControl)
    tabControl.add(tab4, text=translate[language_code]['runtime'])

    tab5 = Frame(tabControl)
    tabControl.add(tab5, text=translate[language_code]['about'])

    tabControl.grid(column=0, row=row_count)
    tabControl.select(tab1)# Default show tab1

    row_count += 1

    # Call Action Bar
    frame_action = get_action_bar(root, language_code)
    frame_action.grid(column=0, row=row_count)


    global UI_PADDING_X
    lessonListTab(tab1, config_dict, language_code, UI_PADDING_X)
    advancedTab(tab2, config_dict, language_code, UI_PADDING_X)
    accountTab(tab3, config_dict, language_code, UI_PADDING_X)
    runtimeTab(tab4, config_dict, language_code, UI_PADDING_X)
    aboutTab(tab5, language_code)

def initialList():
    AddToList_Action.append(translate[language_code]["addLesson"])  # Record every action of course
    AddToList_OpenCourse.append("0000")  # Record code of course
    AddToList_CourseName.append(translate[language_code]["DefaultOpenCourseName"])  # Record Name of course
    AddToList_CourseTeacher.append(translate[language_code]["DefaultOpenCourseTeacher"])  # Record Teacher of course
def main():
    global Default_GUI_SIZE_WIDTH
    global Default_GUI_SIZE_HEIGHT
    global translate
    # only need to load translate once.
    translate = load_translate()
    load_selection_list()

    global config_filepath
    global config_dict


    global root
    root.title(CONST_APP_VERSION)

    # Get Chinese SSO Picture and English SSO Picture
    global Chinese_img,English_img,ChineseUI,EnglishUI
    work_dir = get_app_root()
    Chinese_img = Image.open(work_dir+'/ChineseSSO.png')
    NewChinesePicture = Chinese_img.resize((550,250))
    English_img = Image.open(work_dir+'/EnglishSSO.png')
    NewEnglishPicture = English_img.resize((550,250))
    ChineseUI = ImageTk.PhotoImage(NewChinesePicture)
    EnglishUI = ImageTk.PhotoImage(NewEnglishPicture)

    # Get Logo Picture
    global ICON_Picture
    ICON_Picture = ImageTk.PhotoImage(Image.open(work_dir+'/WYSHBot_logo.jpg').resize((150,150)))

    global UI_PADDING_X
    UI_PADDING_X = CONST_UI_PADDING_X

    # only need to load json file once.
    config_filepath,config_dict = load_json()
    load_GUI(root, config_dict)
    applyJSONSetting(config_dict)
    showList()
    load_save_account()

    GUI_SIZE_WIDTH = Default_GUI_SIZE_WIDTH
    GUI_SIZE_HEIGHT = Default_GUI_SIZE_HEIGHT

    # Revise for platform
    GUI_SIZE_MACOS = str(GUI_SIZE_WIDTH) + 'x' + str(GUI_SIZE_HEIGHT)
    GUI_SIZE_WINDOWS = str(GUI_SIZE_WIDTH - 60) + 'x' + str(GUI_SIZE_HEIGHT - 70)

    # Default use macOS
    GUI_SIZE = GUI_SIZE_MACOS

    #Check Platform
    if platform.system() == 'Windows':
        GUI_SIZE = GUI_SIZE_WINDOWS

    # If List ==0, inisert sample to four list and show
    if len(AddToList_Action)==0:
        initialList()
        showList()

    # Set GUI Windows Width * Height
    root.geometry(GUI_SIZE)
    global start_execution
    start_execution = datetime.now()
    GetCurrentTime()
    update_wyshbot_runtime_status()
    root.mainloop()
    print("exit settings")

# Class Object
class SelectionListDynamicRow:
    def __init__(self,index, AddToList_Action,AddToList_OpenCourse,AddToList_CourseName,AddToList_CourseTeacher,group_row_count,language_code):
        # Constructor
        self.index_value = index
        self.temp = tk.Label(SelectionListDynamicFrame, text=self.index_value, compound="center")
        self.temp.grid(column=0, row=group_row_count, sticky=E)

        self.temp_1 = tk.Label(SelectionListDynamicFrame, width=8, text=AddToList_Action, compound="center")
        self.temp_1.grid(column=1, row=group_row_count, sticky=E)

        self.temp_2 = tk.Label(SelectionListDynamicFrame, width=5, text=AddToList_OpenCourse, compound="center")
        self.temp_2.grid(column=2, row=group_row_count, sticky=E)

        # Deal with too long course name
        self.DisplayName = AddToList_CourseName
        if len(AddToList_CourseName) > 6:
            self.DisplayName = self.DisplayName[0:5] + "..."
        self.temp_3 = tk.Label(SelectionListDynamicFrame, width=10, text=self.DisplayName, compound="center")
        self.temp_3.grid(column=3, row=group_row_count, sticky=E)

        self.temp_4 = tk.Label(SelectionListDynamicFrame, width=8, text=AddToList_CourseTeacher, compound="center")
        self.temp_4.grid(column=4, row=group_row_count, sticky=E)

        self.temp_5 = tk.Button(SelectionListDynamicFrame, text="X", fg='red', command=self.edit_btn_Remove)
        self.temp_5.grid(column=5, row=group_row_count, sticky=W)

        self.temp_6 = tk.Button(SelectionListDynamicFrame, text=translate[language_code]["EditUp"], fg='red', command=self.edit_btn_up)
        self.temp_6.grid(column=6, row=group_row_count, sticky=N)

        self.temp_7 = tk.Button(SelectionListDynamicFrame, text=translate[language_code]["EditDown"], fg='red', command=self.edit_btn_down)
        self.temp_7.grid(column=7, row=group_row_count, sticky=E)

    def edit_btn_Remove(self):
        RemoveCourse(self.index_value)
    def edit_btn_up(self):
        if(self.index_value==1):
            pass
        else:
            Exchange(int(self.index_value), int(self.index_value)-1)
    def edit_btn_down(self):
        if int(self.index_value)==len(AddToList_Action):
            pass
        else:
            Exchange(int(self.index_value), int(self.index_value) + 1)
def clean_tmp_file():
    filepath = get_app_root()+"/"+CONST_WYSHBOT_INT28_FILE
    force_remove_file(filepath)

if __name__ == "__main__":
    clean_tmp_file()
    print("app_root："+get_app_root())
    main()