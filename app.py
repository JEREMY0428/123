#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('W5FiQ5eJDCN3XcTZd9d3GPTD+5D1iqcYqZBxVj3XJj3kempm7qV9z5w2TSJDo+6UFmiRUdtIQYA/xtKeegljgVZBqmkjqIxz6NllXLVs690y1pWfBxaeTlpLy8cYypKu17GB+XTutLSZXhGMyC0DsgdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('e4dbc1c5f012a8f7ffcd1303eceb82d1')

#line_bot_api.push_message('U878201ff43cf137fffe547e352400c86', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"

#判斷輸入是否為數字
# By : https://www.itread01.com/content/1549772101.html
def is_number(str):
    try:
        # 因為使用float有一個例外是'NaN'
        if str=='NaN':
            return False
        float(str)
        return True
    except ValueError:
        return False

#股價List
startValue = 1000
valueList = []

while startValue < 100000:
    #valueArray.append(round(startValue/100,2))
    valueList.append(startValue/100)
    if startValue < 5000:
        startValue += 5
    elif startValue < 10000:
        startValue += 10
    elif startValue < 50000:
        startValue += 50
    else:
        startValue += 100

import random
def randomGuess(a,b,target):
    r = random.randint(0,2000)
    #print(r)
    if r == 0: # 1/2001
        return 'ALL IN !! (1/2001機率!)'
    elif r > 0 and r < 301: # 300/2001 約= 15%
        return a+target+'我覺得不太妙'
    elif r > 300 and r < 601: # 300/2001 約= 15%
        return a+target+'我覺得不錯喔!'
    elif r > 600 and r < 1001: # 400/2001 約= 20%
        return '等我擲杯看一下'+a+target+'好不好 XD'
    elif r > 1000 and r < 1501: # 500/2001 約= 25%
        return '前面有套牢'+b+'軍嗎!?'
    else: # 500/2001 約= 25%
        return '停損點位設好了嗎!?設定好就勇敢'+a+'吧!'

def randomEat():
    r = random.randint(0,51)
    #print(r)
    if r == 0: 
        return '吃便當～'
    elif r == 1:
        return '吃滷肉飯～'
    elif r == 2:
        return '吃自助餐～'
    elif r == 3:
        return '吃乾麵～'
    elif r == 4:
        return '吃牛肉麵～'
    elif r == 5:
        return '吃麥噹噹～'
    elif r == 6:
        return '吃肯德基～'
    elif r == 7:
        return '吃摩斯～'
    elif r == 8:
        return '吃漢堡王～'
    elif r == 9:
        return '吃21世紀～'
    elif r == 10:
        return '吃炒飯～'
    elif r == 11:
        return '吃義大利麵～'
    elif r == 12:
        return '吃涼麵～'
    elif r == 13:
        return '吃三明治～'
    elif r == 14:
        return '吃沙拉～'
    elif r == 15:
        return '吃PIZZA～'
    elif r == 16:
        return '吃咖喱飯～'
    elif r == 17:
        return '吃御飯糰～'
    elif r == 18:
        return '吃關東煮～'
    elif r == 19:
        return '吃烏龍麵～'
    elif r == 20:
        return '吃壽司～'
    elif r == 21:
        return '吃超商微波食品～'
    elif r == 22:
        return '吃麵包～'
    elif r == 23:
        return '吃泡麵～'
    elif r == 24:
        return '吃小火鍋～'
    elif r == 25:
        return '吃雞排～'
    elif r == 26:
        return '吃鹹酥雞～'
    elif r == 27:
        return '吃麵線～'
    elif r == 28:
        return '吃雞胸肉～'
    elif r == 29:
        return '吃肉圓～'
    elif r == 30:
        return '吃韓式飯捲～'
    elif r == 31:
        return '吃春捲～'
    elif r == 32:
        return '吃河粉～'
    elif r == 33:
        return '吃拉麵～'
    elif r == 34:
        return '吃陽春麵～'
    elif r == 35:
        return '吃焗烤料理～'
    elif r == 36:
        return '吃炸雞～'
    elif r == 37:
        return '吃優格～'
    elif r == 38:
        return '吃水煮青菜～'
    elif r == 39:
        return '吃熱炒～'
    elif r == 40:
        return '吃麻辣燙～'
    elif r == 41:
        return '吃米粉湯～'
    elif r == 42:
        return '吃八方雲集～'
    elif r == 43:
        return '吃四海遊龍～'
    elif r == 44:
        return '吃燒烤～'
    elif r == 45:
        return '吃魷魚羹～'
    elif r == 46:
        return '吃泰式料理～'
    elif r == 47:
        return '喝蛋白粉～'
    elif r == 48:
        return '吃水餃～'
    elif r == 49:
        return '吃永和豆漿～'
    else:
        return '吃土～～'

def parsingStr(pStr):
    splitStrArray = pStr.split(' ')
    
    if len(splitStrArray) == 1:
        if is_number(pStr):
            outStr = ''
            outStr += '============\n'
            outStr += '往上2%為 : '+str(round(float(pStr)*1.02,2))+'\n'
            outStr += '往上1.5%為 : '+str(round(float(pStr)*1.015,2))+'\n'
            outStr += '往上1%為 : '+str(round(float(pStr)*1.01,2))+'\n'
            outStr += '=== 計算價格為 : '+pStr+' ===\n'
            outStr += '往下1%為 : '+str(round(float(pStr)*0.99,2))+'\n'
            outStr += '往下1.5%為 : '+str(round(float(pStr)*0.985,2))+'\n'
            outStr += '往下2%為 : '+str(round(float(pStr)*0.98,2))+'\n'
            outStr += '============'
            return outStr
        elif pStr == 'Help' or pStr == 'help' or pStr == '幫助':
            outStr = ''
            outStr += '====== 指令清單 =====\n'
            outStr += 'A) 空/多 價格 (折扣)\n'
            outStr += '簡易計算進出場的賺賠\n折扣為選填，格式為0.25，預設2.5折\n'
            outStr += 'ex: 多 120.5 / 空 115 / 空 50.5 0.28\n\n'
            outStr += 'B) 價格\n'
            outStr += '簡易計算上下1/1.5/2%大概為多少\n'
            outStr += 'ex: 90 / 215.5\n\n'
            outStr += 'C) count/Count/結算 總成交金額 應收付金額 (折扣)\n'
            outStr += '幫助月退的計算損益\n折扣為選填，格式為2.5，預設2.5折\n'
            outStr += 'ex: Count 123000 365 0.25 / 結算 323000 -1255\n\n'
            outStr += 'D) 猜運勢(?)\n'
            outStr += '用亂數來給建議(?)切勿盲目跟單(?)\n'
            outStr += '指令重點為開頭為多or空，結尾為如何，不用空格\n'
            outStr += 'ex: 空3035如何 / 多台積電如何\n\n'
            outStr += 'E) 懶人翻亞當\n'
            outStr += '輸入高/低點跟中間K棒開收，簡單試算滿足區大約在哪\n'
            outStr += '格式為三個數字中間空白隔開，第一個為高/低點\n'
            outStr += '後面兩個數字為中間K棒的開/收盤價(順序不重要)\n'
            outStr += 'ex: 23.5 30 30.8\n\n'
            outStr += 'F) 出場價格參考\n'
            outStr += '輸入 k/K 加上開盤價格，提供出場方式的參考點位\n'
            outStr += 'ex: k 50.4 / K 121.5\n\n'
            outStr += 'G) 吃啥好勒～\n'
            outStr += '輸入指令包含吃即可(不要有空格)\n\n'
            outStr += '111/01/25 ver 1.0.9'
            return outStr
        elif (pStr[0] == '空' or pStr[0] == '多') and pStr[-2:] == '如何':
            if pStr[0] == '空':
                return(randomGuess('空','多',pStr[1:-2]))
            else:
                return(randomGuess('多','空',pStr[1:-2]))
        elif '吃' in pStr:
            return randomEat()
        elif '帥' in pStr:
            r = random.randint(0,1)
            if r == 0:
                return '本本 本本 好帥'
            else:
                return '酷酷 酷酷 帥爆了～'

            #return '\大榮/\大榮/\大榮/ 帥爆了～'
        elif '美' in pStr:
            r = random.randint(0,1)
            if r == 0:
                return '八寶八寶 耶波搭'
            else:
                return '八寶八寶 耶波搭'
        else:
            return 'Error'
            
    elif len(splitStrArray) == 2:
        if splitStrArray[0] == '空' or splitStrArray[0] == '多':
            if is_number(splitStrArray[1]):
                exists = float(splitStrArray[1]) in valueList
                targetValue = float(splitStrArray[1])
                if exists:
                    targetIndex = valueList.index( targetValue )
                    outStr = ''
                    if splitStrArray[0] == '空':
                        for k in range(targetIndex-5,targetIndex+5):
                            fee = (targetValue + valueList[k]) * 1.425 * 0.25
                            fee = round(fee,2)
                            tax = targetValue * 1.5
                            tax = round(tax,2)
                            endPrice = (targetValue - valueList[k]) * 1000 - fee - tax
                            endPrice = round(endPrice)
                            outStr += repr(valueList[k]) + "  " + repr(endPrice) + "\n"
                        return outStr
                    else:
                        for k in range(targetIndex-5,targetIndex+5):
                            fee = (targetValue + valueList[k]) * 1.425 * 0.25
                            fee = round(fee,2)
                            tax = valueList[k] * 1.5
                            tax = round(tax,2)
                            endPrice = (valueList[k] - targetValue) * 1000 - fee - tax
                            endPrice = round(endPrice)
                            outStr += repr(valueList[k]) + "  " + repr(endPrice) + "\n"
                        return outStr
                else:
                    return 'Error'
            else:
                return 'Error'
        elif splitStrArray[0] == 'k' or splitStrArray[0] == 'K':
            if is_number(splitStrArray[1]):
                #return 'test'
                targetValue = float(splitStrArray[1])
                outStr = ''
                outStr += '開盤價格為 ' + splitStrArray[1] + "\n"
                outStr += '1) 下跌2%出場價格約為 : ' + str(round(targetValue*0.98,2)) + "\n"
                outStr += '2) 盤中漲超過4%(' + str(round(targetValue*1.04,2)) + ")後，\n    出場點為 : " + str(round(targetValue*1.015,2)) + "\n"
                outStr += '3) 盤中漲超過6%(' + str(round(targetValue*1.06,2)) + ")後，\n    出場點為 : " + str(round(targetValue*1.02,2)) + "\n"
                outStr += '4) 盤中漲超過8%(' + str(round(targetValue*1.08,2)) + ")後，\n    出場點為 : " + str(round(targetValue*1.04,2)) + "\n"
                outStr += '5) 盤中漲停解開下殺後，\n    出場點為 : ' + str(round(targetValue*1.05,2)) + "\n"
                #return 'test'
                return outStr
            else:
                #return 'test2'
                return 'Error'
        else:
            return 'Error'
    elif len(splitStrArray) == 3:
        if splitStrArray[0] == 'count' or splitStrArray[0] == 'Count' or splitStrArray[0] == '結算':
            if is_number(splitStrArray[1]) and is_number(splitStrArray[2]):
                outStr = ''
                outStr += '總成交金額 : '+splitStrArray[1]+'\n'
                outStr += '應收付金額 : '+splitStrArray[2]+'\n'
                outStr += '折數 : 2.5 折\n'
                saveValue = round(float(splitStrArray[1]) * 0.001425 * 0.75,2)
                outStr += '折讓金額約為 : '+str(saveValue)+'\n'
                finalValue = float(splitStrArray[2]) + saveValue
                outStr += '結算金額約為 : '+str(finalValue)+'\n'
                return outStr
            else:
                return 'Error'
        elif is_number(splitStrArray[0]) and is_number(splitStrArray[1]) and is_number(splitStrArray[2]):
            num0 = float(splitStrArray[0])
            num1 = float(splitStrArray[1])
            num2 = float(splitStrArray[2])
            mid = (num1 + num2) / 2
            # 往上翻(true) or 下(false)
            isUp = mid > num0

            outStr = ''
            outStr += '=== 中間K棒 ====\n高點 : ' + str(num2) + '\n低點 : ' + str(num1) + '\n'
            outStr += '=== 從 ' + str(num0) + ' 往'
            if isUp:
                outStr += '上'
            else:
                outStr += '下'
            outStr += '翻 ===\n滿足區約在 ' + str(round((mid+mid-num0),2)) + '\n'
            return outStr
        elif is_number(splitStrArray[2]):
            per = float(splitStrArray[2])
            if splitStrArray[0] == '空' or splitStrArray[0] == '多':
                if is_number(splitStrArray[1]):
                    exists = float(splitStrArray[1]) in valueList
                    targetValue = float(splitStrArray[1])
                    if exists:
                        targetIndex = valueList.index( targetValue )
                        outStr = ''
                        if splitStrArray[0] == '空':
                            for k in range(targetIndex-5,targetIndex+5):
                                fee = (targetValue + valueList[k]) * 1.425 * per
                                fee = round(fee,2)
                                tax = targetValue * 1.5
                                tax = round(tax,2)
                                endPrice = (targetValue - valueList[k]) * 1000 - fee - tax
                                endPrice = round(endPrice)
                                outStr += repr(valueList[k]) + "  " + repr(endPrice) + "\n"
                            return outStr
                        else:
                            for k in range(targetIndex-5,targetIndex+5):
                                fee = (targetValue + valueList[k]) * 1.425 * per
                                fee = round(fee,2)
                                tax = valueList[k] * 1.5
                                tax = round(tax,2)
                                endPrice = (valueList[k] - targetValue) * 1000 - fee - tax
                                endPrice = round(endPrice)
                                outStr += repr(valueList[k]) + "  " + repr(endPrice) + "\n"
                            return outStr
                    else:
                        return 'Error'
                else:
                    return 'Error'
            else:
                return 'Error'
        else:
            return 'Error'
    elif len(splitStrArray) == 4:
        if splitStrArray[0] == 'count' or splitStrArray[0] == 'Count' or splitStrArray[0] == '結算':
            if is_number(splitStrArray[1]) and is_number(splitStrArray[2]) and is_number(splitStrArray[3]):
                outStr = ''
                outStr += '總成交金額 : '+splitStrArray[1]+'\n'
                outStr += '應收付金額 : '+splitStrArray[2]+'\n'
                outStr += '折數 : '+splitStrArray[3]+' 折\n'
                saveValue = round(float(splitStrArray[1]) * 0.001425 * (1 - float(splitStrArray[3])/10),2)
                outStr += '折讓金額約為 : '+str(saveValue)+'\n'
                finalValue = float(splitStrArray[2]) + saveValue
                outStr += '結算金額約為 : '+str(finalValue)+'\n'
                return outStr
            else:
                return 'Error'
        else:
            return 'Error'
    else:
        return 'Error'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
import re
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text

    #srcUserID = event.source.useId
    #srcGroupID = event.source.groupId
    #profile = line_bot_api.get_group_member_profile(srcGroupID, srcUserID)
    #member_ids_res = line_bot_api.get_group_member_ids(srcGroupID)

    #if message == 'ID':
    #    line_bot_api.reply_message(event.reply_token,TextSendMessage(member_ids_res))
    if parsingStr(message) != 'Error':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(parsingStr(message)))
    #else:
    #    line_bot_api.reply_message(event.reply_token,TextSendMessage('大榮帥爆惹～～'))
    #if is_number(message):
    #    inputNum = float(message)
    #    msg = '計算金額為 : ' + str(inputNum) + '\n往上1.5%為 : ' + str(round(inputNum*1.015,2)) + '\n往下1.5%為 : ' + str(round(inputNum*0.985,2)) 
    #    line_bot_api.reply_message(event.reply_token,TextSendMessage(msg))
    #else:
    #    line_bot_api.reply_message(event.reply_token,TextSendMessage('哩公蝦'))

    #if re.match("你是誰",message):
    #    line_bot_api.reply_message(event.reply_token,TextSendMessage("才不告訴你勒~~"))
    #else:
    #    line_bot_api.reply_message(event.reply_token,TextSendMessage(message*1.015))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


