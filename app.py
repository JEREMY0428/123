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
            outStr += '簡易計算進出場的賺賠\n折扣為選填，格式為0.28，預設2.8折\n'
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
            outStr += 'E) 懶人版理論亞當\n'
            outStr += '輸入高/低點跟中間K棒開收，簡單試算滿足區大約在哪\n'
            outStr += '格式為三個數字中間空白隔開，第一個為高/低點\n'
            outStr += '後面兩個數字為中間K棒的開/收盤價(順序不重要)\n'
            outStr += 'ex: 23.5 30 30.8\n\n'
            outStr += 'F) 今日三關價\n'
            outStr += '輸入昨日高/低點，簡單試算今日三關價大約在哪\n'
            outStr += 'ex: Q 110 107\n\n'
            outStr += 'G) 出場價格參考\n'
            outStr += '輸入 k/K 加上開盤價格，提供出場方式的參考點位\n'
            outStr += 'ex: k 50.4 / K 121.5\n\n'
            outStr += '111/01/28 ver 1.0.0'
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
                            fee = (targetValue + valueList[k]) * 1.425 * 0.28
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
        elif splitStrArray[0] == 'q' or splitStrArray[0] == 'Q':
            if is_number(splitStrArray[1]):
                #return 'test'
                High = float(splitStrArray[1])
                Low = float(splitStrArray[2])
                outStr = ''
                outStr += '昨日高點為 :' + splitStrArray[1] +  '低點 :' splitStrArray[2] +"\n"
                #return 'test'
                return outStr
            else:
                #return 'test2'
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
