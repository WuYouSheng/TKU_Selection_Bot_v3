###### tags: `淡江大學搶課機器人開源專案`
# 開源專案240301更新
## 前言：
搶課機器人在3月及去年8月更新，放出來後收到廣大的迴響，但一直有一些小問題，作者也因為忙著推甄、實習，沒有時間可以更新優化，寒假期間，終於有一段空閒時間，趁著這段時間跟開學加退選測試，終於穩定了，向外發表給大家使用～

**但Windows跟intel版的Mac系統晚上才會更新**

## 適用環境：
* Mac intel 處理器：**macOS Ventura 13.6.4**以上都可以使用
* Mac Apple Silicon 處理器：**macOS Sonoma 14.3.1**以上都可以使用
* Windows 系統：**Windows 10**以上都可以使用


## 使用方式：
### 1. 先進資料夾下載執行檔案
[下載位置](https://1drv.ms/f/s!AvwcoqTkdjpWg8sohv4YWrOiDjNulw?e=GzAZ9t)
* Mac請注意自己使用的CPU類型及系統版本


### 2. 開始執行搶課機器人
* Windows直接點擊start.bat
![](https://i.imgur.com/EaUWGCb.jpg)

* Mac系列直接下載後解壓縮直接放到桌面，點擊SettingUI就可以
![截圖 2024-03-01 11.36.07](https://hackmd.io/_uploads/rkdVp6Rh6.png)
* 若Mac無法成功執行請參考備註1


### 3. 設定基本資料(Windows/Mac使用方式相同)
![截圖 2024-03-01 11.39.27](https://hackmd.io/_uploads/HypeR6C36.png)
* 先設定登入資訊(務必按下儲存登入資訊)

![截圖 2024-03-01 11.41.40](https://hackmd.io/_uploads/BylKCaAna.png)
* 設定加退選資訊
* 設定完加退選資訊務必按下儲存加退選清單

![截圖 2024-03-01 11.45.15](https://hackmd.io/_uploads/S15L1CA36.png)
* 挑選自己喜歡的瀏覽器，新版支援Chrome/Edge/Brave
* 介面如果有英文需求可以直接調整
* WebDrive類別建議不用調整
* 選課系統的語言就看自己需求
* 自動刷新網頁間隔開源版不能調整
* 輸出詳細記錄可以記錄每一筆資料，包含加選到課程的時間
* 結束後顯示課表，顧名思義，選到課之後就直接顯示課表

### 4. 儲存設定檔(Windows/Mac使用方式相同)
### 5. 開始搶課(Windows/Mac使用方式相同)
新版機器人不用設定時間，會一直刷到可以登入為止，避免榮譽學程選課系統時間設定錯誤慘案重演

### 6. 剩下交給上蒼
補充說明：機器人會隨機延遲幾秒鐘，一來是因為學校系統有時候會當機，二來是因為要保障有購買機器人的使用者權利

### Demo影片：

![截圖 2024-03-01 23.55.33](https://hackmd.io/_uploads/ryvRcu1Ta.jpg)
備註，影片中使用Mac做範例，Windows使用介面大同小異

### 備註1(開啟任何來源)：
* 請開啟任終端機：
![](https://i.imgur.com/jJsZZBc.png)

* 在終端機中打入以下指令：
![](https://i.imgur.com/Qbtf4bJ.png)
sudo spctl --master-disable

* 打入密碼(請注意這個密碼不會顯示)：
![](https://i.imgur.com/GOy8pHy.png)

* 打開設定中的隱私權與安全性：
![](https://i.imgur.com/HiaNSls.png)

## 進階功能
本機器人有Premium版本，提供以下功能：
* 支援刷課功能
* 完整的搶課速度
* 極速刷課模式
* 單一裝置登入功能
* 帳號密碼加密，強化安全性
![截圖 2024-03-01 11.55.13](https://hackmd.io/_uploads/Bk12ZCRha.png)

若有需要，可以點擊以下連結：
![](https://hackmd.io/_uploads/H1Xb_N3T3.jpg)

[https://line.me/ti/g2/EQSB4VBKjoVXM0n46GDIrmdTwieWd1LIrtYpJg?utm_source=invitation&utm_medium=link_copy&utm_campaign=default](https://line.me/ti/g2/EQSB4VBKjoVXM0n46GDIrmdTwieWd1LIrtYpJg?utm_source=invitation&utm_medium=link_copy&utm_campaign=default)

## 原始碼開源
> 參見資料夾：
> https://1drv.ms/f/s!AvwcoqTkdjpWg8sohv4YWrOiDjNulw?e=GzAZ9t
> 註：因為tkinter針對Windows還有macOS會有不一樣的排列方式，所以請針對自己的系統版本下載
