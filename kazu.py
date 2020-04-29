import websocket, json, time, datetime,requests
from datetime import datetime

import time, requests, random


	print('gunakan dengan bijak')
else:
    ws.close()
xz = 1
status = 'tidur'
nama = 'xyx'
judul = 'xyz'
timeh = datetime.today()
response3 = '{"div":"hai"}'
createdl = datetime.today()
z = 0
namal = 'xyz'
judull = 'xwx'
timehl2 = datetime.today()


botauthtoken2 = 'f2403d5c8c8a51ad7dba69e1c75f72e75349d5aa' #token lu disini

rscode=0
while rscode!=1:
	#nomor = "06802143801"
	nomor="085705873584"
	###nomor = input("masukkan nomor telepon : ")
	password="kambing1"
	###password = input("masukkan password : ")
	headers={"User-Agent":"Mozilla/5.0"}
	response=requests.post('https://id-api.spooncast.net/signin/?version=2',headers=headers,json={"sns_type":"phone","sns_id":nomor,"password":password})
	#print(response.json())
	rscode = response.json()['results'][0]['result_code']
	if rscode !=1:
		print("nomor atau password salah , ulangi lagi")
print("berhasil login")
tirublock=response.json()['results'][0]['tag']
#time.sleep(100)
tokenl=response.json()['results'][0]['token']
print(response.json()['results'][0]['nickname'])
botauthtoken2=tokenl

txtid = input('Link Live nya  : ')
response = requests.get(txtid)
urlo = response.url
slink = urlo[34:-59]
socketstring = ("wss://id-heimdallr.spooncast.net/" + slink)
print(socketstring)

mypesan = '{"live_id":'+slink+',"token":"'+botauthtoken2+'","event":"live_join","appversion":"4.3.16","useragent":"Android"}'###### end 



def on_message(ws, message):
        global judul
        global nama
        global response3
        global status
        global timeh
        global timehl2
        global xz
        global z
        global response2
        chat = json.loads(message)
        uid = chat['data']['author']['id']
        nick = chat['data']['author']['nickname']
        evn = chat['event']
        kesurupan = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"HAI TUANKU PANPAN...."}'
        if 1 == 1:
            if z == 0:
                ws.send(kesurupan)
                z = 1
        if evn == 'live_message':
            psn = chat['data']['message']
            tag = chat['data']['author']['tag']
            print(chat['data']['author']['tag'])
        emot = ['🤭🤭🤭', '🙄🙄🙄', '😝😝😝', '😇😇😇', '😌😌😌', '😔😔😔', '🥺🥺🥺']
        ya = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"' + nick + '   Sokap Lau Nanya Mulu💆  ' + random.choice(emot) + '"}'
        tidak = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"' + nick + '  Tanyakan Saja Pada Rumput Yang Bergoyang ' + random.choice(emot) + '"}'
        bisajadi = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"' + nick + '  Saya Tidak Perduli Dengan Pertanyaan Anda ' + random.choice(emot) + '"}'
        bodoamat = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"' + nick + ' bodo amat 😝 ga peduli 😚 ' + random.choice(emot) + '"}'
        listjawaban = [
         ya, tidak, bisajadi, bodoamat]
        if evn == 'live_message' and psn[:1].lower() == 'a' and psn[-1:] == '?':
           kambeng = random.choice(listjawaban)
           print(kambeng)
           ws.send(kambeng)
        hantu = [' Ku Kasih Tau Ya... Kau Itu Nge Ghost [👻] ',' Astagaa Malah Nge Ghost [👻] ','  Jangan Nge Ghost [👻] Anjiir" ','  Kamu Nge Ghost [👻] Ku Kick" ' ]
        lsjoin = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":" ' + nick + random.choice(hantu) + '😕' + '"}'
        sapa = ['   Hii, Kamu Imut 😙 . Tapi Boong 🤣 ','   Gimana Kabar Nya😉 ','   Long Time No See..🙆 ','   Semoga Harimu Menyenangkan ','    Hi. Rindu aku Ya😄 ','   kamu Apa Kabar ','  Tap❤️ Ya Atau Ngga Kasih Gift Bgsd ','  Hai Jangan Lupa Bahagia Yaa sayang 💕🙃  ','  salam ANAK SPOON INDONESIA😇😘 ','  Aciieeeeeee😍 balik lagi kesini kangen yah 😝 ',' yang baru masuk jangan lupa taplop yah😇💕',' Hai Kak Jangan Lupa klik tombol 🎁 di pojok kanan bawah!!! ya🤕🤘 ']
        ljoin = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":" ' + nick + random.choice(sapa) + ' '+ '"}'
        likee = ['   Yaaah Tap❤️ Doang ','  Gada Akhlak, 😒Baru Tap❤️ ','   Uuuwaaaah, Maacih Tap❤️ Nya🙆 ','   Kenapa Harus Tap❤️, kalau Akhirnya Keluar Juga ','  Jangan Tap❤️ Doang. Kasih Gift Dong ','  Thanks For Tap❤️ Nya, I Love U🥰, Tapi Boong 🤣']
        llike = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":" ' + nick + random.choice(likee) + '❤️' + '"}'
        tidur = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":" ' + nick + ' [SERVER]~[MJ COISHT IN ROOM]~OFF  "}'
        kalem = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"waalaikumsalam😇"}'
        bangun = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":" ' + nick + '  [SERVER]~[MJ COISHT IN ROOM]~ON PROSES "}'
        bangun2 = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"Apasih  ' + nick + ' panggil panggil MJ 😏 kek yang mau ngasih duit ajah 😝 "}'
        johnson = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"eeeeeeh siapa?🤔  ' + nick + '  Ku Kasih Tau Ya ~Panpan~ Itu Emang Gada Otak " "}'
        jun =  '{"appversion": "4.3.16", "event": "live_message", "token": "", "useragent": "Android", "message": " woooooooooooy' +  nick  + ' jangan panggil bos gw😒 dia lagi jomblo kasian😖😖  "}'
        ljeen =  '{"appversion": "4.3.16", "event": "live_message", "token": "", "useragent": "Android", "message": "Hai ' +  nick  + ' Siang Juga manusia 💞 kamu udah mandi blm?🙄 bau 🙊"}'
        fans = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"' + nick + ' pagi juga kaka semoga hari mu menyenangkan yah💞💞😚"}'
        promot = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"u cp y ' + nick + ' jangan panggil panggil aku😏 ga level😌 "}'
        ig = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"Hai ' + nick + ' Malam Juga Kamu, Jangan bergadang kak !! 😊"}'
        makasih = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"' + nick + ' iya sore lah😒 kata siapa malam🙄 dasar 🚮"}'
        jawab = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":" aku kasih tau yah  ' + nick + ' bos aku itu 🙈🙈🙈🙈 ? kepo bet sih anda "}'
        rank = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"  {control}  ' + nick + ' cek in -(RANK 1/30 SUKSES UPDATE)-"}'
        if evn == 'live_message' and (psn == '•status' or psn == '•durasi' or psn == '•info'):
        	headers2 = {'User-Agent': 'Mozilla/5.0'}
        	response2 = requests.get(('https://id-api.spooncast.net/lives/' + slink + ''), headers=headers2)
        	createdl = response2.json()['results'][0]['created']
        	tanggal = datetime.today()
        	cre = createdl[:-17]
        	crea = createdl[11:-8]
        	creat = cre + ' ' + crea
        	creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
        	selisih = tanggal - creatdt
        	s1 = '07:00:00'
        	s2 = str(selisih)[:-7]
        	formatss = '%H:%M:%S'
        	timehl2 = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
        	ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":" [info durasi ~ in room ] : 💖🖤 '+ str(timehl2) +' 🖤💖 "}')
        	
        	
        
        
        
        
        
        
        if evn == 'live_message' and psn == '•control rank':
            headers3 = {'User-Agent': 'Mozilla/5.0'}
            response3 = requests.get('https://id-api.spooncast.net/lives/popular/', headers=headers3)
            ws.send(rank)
        if evn == 'live_message' and psn[:-3] == '•rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"Info rank ' + str(xz + 1) + '  nama: ' + nama + ' judul: ' + judul + '  durasi -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn[:-2] == '•rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"Info rank ' + str(xz + 1) + '  nama: ' + nama + ' judul: ' + judul + '  durasi -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn == '•my akun':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = tag
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"Info username ' + nn + ' tanggal akun dibuat -> ' + str(tangga) + ' GMT +0 "}')
        if evn == 'live_message' and psn[:4] == '•cek':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = psn[5:]
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"Info username ' + nn + ' tanggal akun dibuat -> ' + str(tangga) + ' GMT +0 "}')
            
            
            
            
        if evn == 'live_message' and psn == '•on' and status == 'tidur':
            status = 'bangun'
            ws.send(bangun)
        if evn == 'live_message' and psn == "•off" and status == 'bangun':
        	print("aaaaaaaaajajqiajaiaja")
        	status = 'tidur'
        	ws.send(tidur)
        if evn == 'live_message' and psn == 'assalamualaikum':
                ws.send(kalem)
        if evn == 'live_message' and psn == 'hai mj':
                ws.send(bangun2)
        if evn == 'live_message' and psn == 'apa ya':
            ws.send(johnson)
        if evn == 'live_message' and psn == 'panpan':
            ws.send(jun)
        if evn == 'live_message' and psn == 'siang':
            ws.send(ljeen)
        if evn == 'live_message' and psn == 'pagi':
            ws.send(fans)
        if evn == 'live_message' and psn == 'pan':
            ws.send(promot)
        if evn == 'live_message' and psn == 'malam':
            ws.send(ig)
        if evn == 'live_message' and psn == 'sore':
            ws.send(makasih)
        if evn == 'live_message' and psn == 'bos':
            ws.send(jawab)
        
        
        
        if evn == 'live_shadowjoin':
        	ws.send(lsjoin)
        if evn == 'live_join' and status == 'bangun':
            if status == 'bangun':
                ws.send(ljoin)
       
        if evn == 'live_like' and status == 'bangun':
        	ws.send(llike)
        if evn == 'live_message':
           if psn == 'out pan' and uid == '211608489':
               ws.close()
        print(status)
def on_close(ws): #on close of the bot.
    print ("### closed ###")
    
def on_open(ws): #when the bot initially connects.
 print ("open")
 time.sleep(1)
 ws.send(mypesan)
 time.sleep(1)
 gblk = """
 Connected
 """
 print(gblk)
 time.sleep(1)

if __name__ == "__main__":
 
 websocket.enableTrace(True)
 ws = websocket.WebSocketApp("wss://id-heimdallr.spooncast.net/"+slink,                                           
                              on_message = on_message,
                              on_close = on_close)
ws.on_open = on_open
ws.run_forever()
