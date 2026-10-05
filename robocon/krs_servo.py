import serial


#ID番号で指定したサーボに角度を指定して動作します
def krs_setPos_CMD(krs,servo_id, pos):
    
    txCmd = [0x80 | servo_id,   #ポジションコマンド0ｘ80にＩＤ番号を足し合わせてヘッダにします
             pos >> 7 & 0x7f,   #ポジションデータを2バイトに分けます
             pos & 0x7f]
   
    #コマンドを送信
    krs.write(txCmd)

    

    rxCmd = krs.read(6)

    if len(rxCmd) == 0:
        return False,0


    else:


        return True,0



#サーボを脱力した状態にします    
def krs_setFree_CMD(krs,servo_id):
    
    #ポジション0送信すると脱力します
    bl, Value = krs_setPos_CMD(krs,servo_id, 0)
    return bl, Value
    

#サーボのストレッチ、スピード、電流値、温度を読み出します
#※現在位置を取得する場合は、getPos関数を使用してください
#※EEPROM(sc:0x00)の読み出しには対応していません
#※KRS-3301/3302は温度、電流回路が実装されていません
def krs_getValue_CMD(krs,servo_id, sc):
   
    txCmd = [0xA0 | servo_id,   #読み出しコマンド0xA0にＩＤ番号を足し合わせてヘッダにします
             sc]                #sc（サブコマンド）により、読み出すパラメータを指定します
   
    #コマンドを送信
    krs.write(txCmd)

    #サーボからの返事を受け取る
    rxCmd = krs.read(5)
    
    #もしリスト何になにも入っていなかったら正常に受信できていないと判断    
    if len(rxCmd) == 0:
        return False, 0

    #問題なければ返事を返す
    else:
        return True, rxCmd[4]



#サーボの現在位置を読み出します
#サブコマンド0ｘ05により現在位置を読み出すことができますが、このコマンドはＩＣＳ3.6のみ対応しています
#ICS3.5をご利用の場合は、getPos35関数を使用してください
def krs_getPos36_CMD(krs,servo_id):
   
    txCmd = [0xA0 | servo_id,   #読み出しコマンド0xA0にＩＤ番号を足し合わせてヘッダにします
             0x05]              #sc（サブコマンド）により、現在位置を読み出します
   
    #コマンドを送信
    krs.write(txCmd)

    #サーボからの返事を受け取る
    rxCmd = krs.read(6)
    
    #もしリスト何になにも入っていなかったら正常に受信できていないと判断    
    if len(rxCmd) == 0:
        return False, 0

    #問題なければ返事を返す        
    else:
        
        #読み出した2バイトのデータを１つのデータにまとめて戻り値とします
        return True, (rxCmd[4] << 7) + rxCmd[5]


#サーボの現在位置を読み出します
#ICS3.5は現在位置を取得するコマンドが実装されていないため
#ポジションコマンドを送信した際に返事で取得できる角度を利用します
def krs_getPos35_CMD(krs,servo_id):
   
    #ポジションコマンドの戻り値で現在位置を取得するため、ポジション0でサーボから戻り値を取得する
    bl, Value = krs_setPos_CMD(krs,servo_id, 0)
        
    #フリー状態のサーボに取得したポジションと同じポジションを送信し、トルクオン状態に戻します
    bl, Value = krs_setPos_CMD(krs,servo_id, Value)
    
    return bl, Value



#サーボのストレッチ、スピード、電流制限値、温度制限値を書き換えます
#※EEPROM(sc:0x00)の書き込みには対応していません
def krs_setValue(krs,servo_id, sc, Value):
    
    #サブコマンドがEEPROM(sc:0x00)の場合は処理を停止する
    if (sc == 0x00) :
        return False
    
    txCmd = [0xC0 | servo_id,   #書き込みコマンド0ｘC0にＩＤ番号を足し合わせてヘッダにします
             sc,                #sc（サブコマンド）により、書き込み先を指定します
             Value]             #書き込むパラメータ
   
    #コマンドを送信
    krs.write(txCmd)

    #サーボからの返事を受け取る
    rxCmd = krs.read(6)
    
    #もしリスト何になにも入っていなかったら正常に受信できていないと判断    
    if len(rxCmd) == 0:
        return False

    #問題なければ返事を返す
    else:
        
        #サーボからの返事で書き込んだデータが返ってきます。指定したデータと合っているか確認します
        if rxCmd[5] == Value:
            return True
        
        else:
            return False



#サーボのIDを読み出します
#ホストとサーボを1対1の状態で使用してください
#IDは複数のサーボを同時に接続して読み込むことはできません
def krs_getID_CMD(krs):
    
    txCmd = [0xFF,  #IDコマンド0ｘFF
             0x00,  #ID読み出しのサブコマンド0x00を3回送ります
             0x00,
             0x00]
   
    #コマンドを送信
    krs.write(txCmd)

    #サーボからの返事を受け取る
    rxCmd = krs.read(5)
    
    #もしリスト何になにも入っていなかったら正常に受信できていないと判断    
    if len(rxCmd) == 0:
        return False, 0

    #問題なければ返事を返す        
    else:
        
        #読み出したからIDのみを残して戻り値とします
        return True, rxCmd[4] & 0x1F




#読み出し、書き込み用のサブコマンド
STRETCH = 0x01          #ストレッチ（サーボの保持力を指定するパラメータ）
SPEED = 0x02            #スピード　※スピードのパラメータを下げるとトルクも下がります
CURRENT = 0x03          #電流値（書き込みの時は電流制限値）
TEMPERATURE = 0x04      #温度（書き込みの時は温度制限値）

#電流制限値、温度制限値の閾値を超えるとサーボが脱力します。閾値を下回れば復帰します
#※KRS-3301/3302は温度、電流回路が実装されていません

#EEPROMに間違えた値を書き込むと正常に動作しません。
#EEPROMのデータを変更する場合はICS3.5/3.6マネージャをご利用ください
#https://kondo-robot.com/faq/ics35mag



"""
#サブコマンド(sc)で指定したパラメータを書き換えます
#krs_setValue(servo_id, sc, Value)
reData = krs_setValue(0, STRETCH, 60)
print(reData)

reData = krs_setValue(0, SPEED, 127)
print(reData)


#サブコマンド(sc)で指定したパラメータを読み出します
#krs_getValue_CMD(servo_id, sc)
bl, reData = krs_getValue_CMD(0, STRETCH)
print("STRC", reData)

bl, reData = krs_getValue_CMD(0, SPEED)
print("SPD", reData)

bl, reData = krs_getValue_CMD(0, CURRENT)
print("CUR", reData)

bl, reData = krs_getValue_CMD(0, TEMPERATURE)
print("TMP", reData)
"""
