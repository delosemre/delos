#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################
#                        #
#Emre Yılmaz (delosemre) #
# 		versiyon4      #
##########################
import sys
import argparse
import os
import time
import httplib
import subprocess
import re, urllib2
import socket
import urllib,sys,json
import telnetlib
import glob
import random
import Queue 
import threading
import base64
import signal
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep
from urllib2 import *


def sigint_handler(signum, frame):
    os.system("clear")
    print ("CTRL+C detected!")
    print(" \033[1;91m@Good bye\033[1;m")
    sys.exit() 
 
signal.signal(signal.SIGINT, sigint_handler)

print ( """\033[1;91m
 _  __                    _ ____  _             
| |/ /___ _ __ _ __   ___| | __ )| | ___   __ _ 
| ' // _ \ '__| '_ \ / _ \ |  _ \| |/ _ \ / _` |
| . \  __/ |  | | | |  __/ | |_) | | (_) | (_| |
|_|\_\___|_|  |_| |_|\___|_|____/|_|\___/ \__, |
Uykusuz Gecelerin Eseri...                 |___/ .org\033[1;m
\033[1;93mDeneyimsizler İçin Bir Penetrasyon Aracı v4\033[1;m 

     \033[1;91m
     KernelBlog.org
     en.kernelblog.org
     ---
     KernelBlog devepoler team
     Kernelblog geliştirici ekibi\033[1;m
      """)

def logo():
     print ( """
\033[1;91m    
 _  __                    _ ____  _             
| |/ /___ _ __ _ __   ___| | __ )| | ___   __ _ 
| ' // _ \ '__| '_ \ / _ \ |  _ \| |/ _ \ / _` |
| . \  __/ |  | | | |  __/ | |_) | | (_) | (_| |
|_|\_\___|_|  |_| |_|\___|_|____/|_|\___/ \__, |
KernelBlog.org Uğramayı Unutma...          |___/ .org
Deneyimsizler İçin Bir Penetrasyon Aracı v4
\033[1;m      """)

def logohack():
     print ("""
\033[1;91m
     )                          (                
  ( /(                   (   (  )\ )             
  )\()) (  (           ( )\( )\(()/(      (  (   
|((_)\ ))\ )(   (     ))((_)((_)/(_)) (   )\))(  
|_ ((_)((_|()\  )\ ) /((_)((_)_(_))   )\ ((_))\  
| |/ (_))  ((_)_(_/((_))| || _ ) |   ((_) (()(_) 
  ' </ -_)| '_| ' \)) -_) || _ \ |__/ _ \/ _` |  
 _|\_\___||_| |_||_|\___|_||___/____\___/\__, |  
               KernelBlog | delosemre v4 |___/   \033[1;m                                     
En Büyük Savaş Cahilliğe Karşı Yapılan Savaştır.
          """)


#giriş kısmı

kullanici = raw_input("    [ > ] Kullanıcı Adı Giriniz : ")
time.sleep(0.5)

#kullanıcı sorgusu

print("")
print("    [ + ] Hoşgeldin " + " " + kullanici) 
print("")
print("    [ * ] Root Erişimi Sorgulanıyor...")
time.sleep(2)




#Menü

def baslangicmenu():
     print ("""
          
    ###### Seçenekler #######
    |                       |
    | 1-) Bilgi Toplama     |
    | 2-) Zafiyet Tarama    |
    | 3-) Hakkımızda        |
    | 4-) Sistemi Güncelle  |
    | 5-) Çıkış             |
    |_______________________| 
     """)

#bilgi menüsü
def bilgi():
     print ("""\033[1;91m
                _____________
     __________|Bilgi Toplama|__________
    |          |_____________|          |
    |                                   |
    |      1 : Dmitry                   |
    |      2 : GoLismero                |
    |      3 : Theharvester             |
    |      4 : Sublist3r                |
    |      5 : Nmap Port Taraması       |
    |      6 : Sn1per                   |
    |      7 : delosemre Bilgi Toplama  |
    |      8 : Geri Dön                 |
    |      9 : Çıkış                    |				
    |___________________________________|
      \033[1;m""")

def delosbilgimenu():
	print("""\033[1;91m                                            
	  (         (                                   
	  )\ )   (  )\            (     )    (      (   
	 (()/(  ))\((_) (   (    ))\   (     )(    ))\  
	  ((_))/((_)_   )\  )\  /((_)  )\  '(()\  /((_) 
	  _| |(_)) | | ((_)((_)(_))  _((_))  ((_)(_))   
	/ _` |/ -_)| |/ _ \(_-</ -_)| '  \()| '_|/ -_)  
	\__,_|\___||_|\___//__/\___||_|_|_| |_|  \___|.xyz v1.5
	delosemre@kernelblog.org | delosemre@outlook.com                                         
		
	#############Bilgi Toplama Aracı#################.
	|                                                .
	|	1-) Whois                                .
	|	2-) DNS Lookup                           .
	|	3-) Ters DNS Arama                       .
	|	4-) DNS Ana Bilgisayar Kayıtlarını Bulma .
	|	5-) Paylaşılan DNS Sunucularını Bulma    .
	|	6-) Zone Transfer                        .
	|	7-) TCP Port Tarama                      .
	|	8-) Geri Dön                             .
	|	9-) Çıkış                                .
	|________________________________________________.
	\033[1;m
	""")

#zaafiyet tarama menüsü
def zaafiyettarama():
     print ("""\033[1;91m
               
        #### Zafiyet Tarama #####
        |  1 : Fimap             |
        |  2 : Uniscan           |
        |  3 : JoomScan          |
        |  4 : WPScan            |
        |  5 : Skipfish          |
        |  6 : Nikto             |
        |  7 : Wapiti            |
        |  8 : Geri Dön          |
        |  9 : Çıkış             |
        |________________________|
      \033[1;m""")


#Bilgi toplama komutlar
def dmitry():
     print ("""
               Bu araç oldukça kullanışlı bir Information Gathering aracıdır. 
               Bu araç ile bir host üzerinden birçok bilgi toplanabilir.
               Bunlar subdomain'ler,email adresleri, port tarama gibi birçok şey olabilir.""")

     secimdmitry = raw_input("       Devam (E/H): ")
     if secimdmitry == "e" or secimdmitry == "E":
               print("   \033[1;91mDmitry ...\033[1;m")
               time.sleep(1)
               os.system("apt-get install dmitry")
               print("   \033[1;91mDmitry Başlatılıyor...\033[1;m")
               time.sleep(1)
               os.system("clear")
               logohack()
               dmitryhedef = raw_input("     Hedef Giriniz: ")
               os.system("dmitry -p -n -i -s -e " + dmitryhedef)
               print("")
               print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimdmitry == "h" or secimdmitry == "H":
               baslangic() 
               os.system("clear")



def golismero():
     print("""
               GoLismero, güvenlik testi ve pentest analizlerinde kullanılan 
               çok fonksiyonlu bir açık kaynaklı yazılımdır.
               Nmap, Sql, Database, dns, bruteforce, 
               harvaster, ssh gibi birçok fonksiyonu vardır.

               """)
     secimgolis = raw_input("       Devam (E/H): ")
     if secimgolis == "e" or secimgolis == "E":
          print("   \033[1;91mGoLismero ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install golismero")
          os.system("clear")
          print("   \033[1;91mGoLismero Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          golishedef = raw_input("     Hedef Giriniz: ")
          os.system("golismero" + golishedef)
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimgolis == "h" or secimgolis == "H":
          baslangic() 
          os.system("clear")


def theharvester():
     print(""" 
          Theharvester
          sub domain ve emailleri tespit etmek için kullanılır.

          """)
     secimtheharvester = raw_input("       Devam (E/H): ")
     if secimtheharvester == "e" or secimtheharvester == "E":
          print("   \033[1;91mTheharvester ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install theharvester")
          os.system("clear")
          print("   \033[1;91mTheharvester Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          theharvesterhedef = raw_input("     Hedef Giriniz: ")
          os.system("theharvester -d " + theharvesterhedef + " -l 50 -b all")
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimtheharvester == "h" or secimtheharvester == "H":
          baslangic()  
          os.system("clear")

def sublist3r():
     print(""" 
          Sublist3r
          OSINT kullanan web sitelerinin alt alanlarını numaralandırmak 
          için tasarlanmış bir python araçtır.
          Penetrasyon test cihazları ve hata avcılarının hedefledikleri
          alan adına alt alanlar toplamaları için yardımcı olur.
          Sublist3r, Google, Yahoo, Bing, Baidu ve Ask gibi birçok arama
          motorunu kullanan alt alanları numaralandırır. Sublist3r ayrıca Netcraft, 
          Virustotal, ThreatCrowd, DNSdumpster ve ReverseDNS'yi 
          kullanarak alt alanları numaralandırır.

          """)
     secimsublist3r = raw_input("       Devam (E/H): ")
     if secimsublist3r == "e" or secimsublist3r == "E":
          print("   \033[1;91mSublist3r ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install sublist3r")
          os.system("clear")
          print("   \033[1;91mSublist3r Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          sublist3rhedef = raw_input("     Hedef Giriniz: ")
          os.system("sublist3r -d "+sublist3rhedef+" -t 3 -e bing")
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimsublist3r == "h" or secimsublist3r == "H":
          baslangic()  
          os.system("clear")

def nmap():
     print(""" 
          Nmap
          Nmap, ağdaki cihazlara ve cihazların portlarına
          çeşitli paketler gönderip ve cevaplara bakarak
          cihazın açık olup olmadığını, açık olan portlar 
          üzerinde hangi servislerin çalıştığını, cihazların
          hangi işletim sistemini kullandığını öğrenmemize
          olanak sağlayan open-source bir araçtır.

          """)
     secimnmap = raw_input("       Devam (E/H): ")
     if secimnmap == "e" or secimnmap == "E":
          print("   \033[1;91mNmap ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install nmap")
          os.system("clear")
          print("   \033[1;91mNmap Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          print ("  varsayılan Tarama")
          nmaphedef = raw_input("     Hedef Giriniz: ")
          os.system("nmap "+nmaphedef)
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimnmap == "h" or secimnmap == "H":
          baslangic()  
          os.system("clear")

def sn1per():
     print(""" 
         	Sn1per

          """)
     secimsn1per = raw_input("       Devam (E/H): ")
     if secimsn1per == "e" or secimsn1per == "E":
          print("   \033[1;91msn1per Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          print ("  varsayılan Tarama")
          sn1perhedef = raw_input("     Hedef Giriniz: ")
          os.system("sn1per -t "+sn1perhedef)
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimnmap == "h" or secimnmap == "H":
          baslangic()  
          os.system("clear")


def delosemre_bilgi():
		
		delosbilgimenu()
		secimdelos = raw_input("    " + kullanici + "" "\033[1;91m@delosemre:~$\033[1;m ")
		print("")



		if secimdelos == "1":
		    url = raw_input("	Alan Adı Veya IP Adres: ")
		    who = "http://api.hackertarget.com/whois/?q=" + url
		    pwho = urlopen(who).read()
		    print (pwho)
		    print("	\033[1;91mSonuçlar Yukarıda\033[1;m")
		    delosbilgimenu()
		    secim = raw_input("    " + kullanici + "" "\033[1;91m@delosemre:~$\033[1;m ")


		if secimdelos == "2":
			url = raw_input("	Alan Adı Veya IP Adres: ")
			dnsl = "http://api.hackertarget.com/dnslookup/?q=" + url
			pdnsl = urlopen(dnsl).read()
			print (pdnsl)
			if "cloudflare" in pdnsl:
						print ("cloudflare Tespit")
		   	else:
		   				print ("cloudflare Koruması Yok")
		   	delosbilgimenu()
		   	print("	\033[1;91mSonuçlar Yukarıda\033[1;m")
			secimdelos = raw_input("    " + kullanici + "" "\033[1;91m@delosemre:~$\033[1;m ")
		    


		if secimdelos == "3":
			url = raw_input("	DNS: ")
			dns = "https://api.hackertarget.com/reversedns/?q=" + url
			pdns = urlopen(dns).read()
			print (pdns)
			delosbilgimenu()
			print("	\033[1;91mSonuçlar Yukarıda\033[1;m")
			secimdelos = raw_input("    " + kullanici + "" "\033[1;91m@delosemre:~$\033[1;m ")
		    

		if secimdelos == "4":
			url = raw_input("	Alan Adı: ")
			host = "https://api.hackertarget.com/hostsearch/?q=" + url
			phost = urlopen(host).read()
			print (phost)
			delosbilgimenu()
			print("	\033[1;91mSonuçlar Yukarıda\033[1;m")
			secimdelos = raw_input("    " + kullanici + "" "\033[1;91m@delosemre:~$\033[1;m ")
		    

		if secimdelos == "5":
			url = raw_input("	DNS Adı: ")
			dnsa = "https://api.hackertarget.com/findshareddns/?q=" + url
			pdnsa = urlopen(dnsa).read()
			print (pdnsa)
			delosbilgimenu()
			print("	\033[1;91mSonuçlar Yukarıda\033[1;m")
			secimdelos = raw_input("    " + kullanici + "" "\033[1;91m@delosemre:~$\033[1;m ")
		    

		if secimdelos == "6":
			url = raw_input("	Alan Adı: ")
			zone = "https://api.hackertarget.com/zonetransfer/?q=" + url
			pzone = urlopen(zone).read()
			print (pzone)
			delosbilgimenu()
			print("	\033[1;91mSonuçlar Yukarıda\033[1;m")
			secimdelos = raw_input("    " + kullanici + "" "\033[1;91m@delosemre:~$\033[1;m ")
		    

		if secimdelos == "7":
			url = raw_input("	Ip Adresi Giriniz: ")
			tcp = "https://api.hackertarget.com/nmap/?q=" + url
			ptcp = urlopen(tcp).read()
			print (ptcp)
			delosbilgimenu()
			print("	\033[1;91mSonuçlar Yukarıda\033[1;m")
			secimdelos = raw_input("    " + kullanici + "" "\033[1;91m@delosemre:~$\033[1;m ")

		if secimdelos == "8":
			baslangic()
		if secimdelos == "9":
			print ("  Güle Güle " + " " + kullanici)
	        time.sleep(1)
	        sys.exit()
		

#Bilgi toplama komutlar son

#Zaafiyet Tarama komutlar Başlangıç
def fimap():
     print(""" 
          fimap, webapps'deki yerel ve uzak dosya içerme
          hataları için otomatik olarak bulabileceğiniz,
          hazırlayabilen, denetleyebilen, kullanabilen 
          ve hatta otomatik olarak kullanabilen küçük 
          bir python aracıdır. 

          """)
     secimfimap = raw_input("       Devam (E/H): ")
     if secimfimap == "e" or secimfimap == "E":
          print("   \033[1;91mFimap ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install fimap")
          print("   \033[1;91mBagımlılıklar ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install python-pip")
          os.system("pip install httplib2")
          os.system("clear")
          print("   \033[1;91mFimap Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          print("   Hedef url 'http://localhost/test.php?file=bang&id=23' şeklinde olmalıdır.")
          fimaphedef = raw_input("     Hedef Giriniz: ")
          os.system("fimap -u "+fimaphedef)
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimfimap == "h" or secimfimap == "H":
          os.system("clear")
          baslangic()

def uniscan():
     print("""
          Uniscan
          hedef sistem üzerindeki XSS ,SQL ,Rfi gibi açıkları tarayabilir,
          Sisteme ait bir çok bilgi bulabilirsiniz
          ( Yedek Dosyalar , E-Mail , Hostlar ).

          """)
     secimuniscan = raw_input("       Devam (E/H): ")
     if secimuniscan == "e" or secimuniscan == "E":
          print("   \033[1;91mUniscan ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install uniscan")
          print("   \033[1;91mUniscan Güncelleniyor...\033[1;m")
          time.sleep(0.5)
          os.system("clear")
          print("   \033[1;91muniscan Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          uniscanhedef = raw_input("     Hedef Giriniz: ")
          os.system("uniscan -u "+ uniscanhedef + " --qweds")
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimuniscan == "h" or secimuniscan == "H":
          os.system("clear")
          baslangic()

def joomscan():
     print(""" 
          Joomscan, joomla sitelerde açık taramaya yarayan bir araçtır.
          Bu araç sayesinde joomla sitelerdeki açıkları tespit edebiliriz
          ve buna ek olarak sitede bulunan açığın türüne göre exploit
          bulup bize sunuyor.

          """)
     secimjoomscan = raw_input("       Devam (E/H): ")
     if secimjoomscan == "e" or secimjoomscan == "E":
          print("   \033[1;91mJoomScan ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install joomscan")
          print("   \033[1;91mJoomScan Güncelleniyor...\033[1;m")
          time.sleep(0.5)
          os.system("clear")
          print("   \033[1;91mJoomScan Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          joomscanhedef = raw_input("     Hedef Giriniz: ")
          os.system("joomscan -u "+joomscanhedef)
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimjoomscan == "h" or secimjoomscan == "H": 
          os.system("clear")
          baslangic()

def wpscan():
     print("""
          WpScan 
          WordPress siteleri üzerinde zafiyet taramaları yapan
          açık kaynak kodlu bir güvenlik uygulamasıdır. 
          Bu uygulamayı kullanmak size saldırganın gözünden
          sitenize bakmanızı sağlıyacaktır.
          WPScan aracı ile bir wordpress sitesinde 
          “kullanıcı Adını bulma, bruteforce saldırısı, 
          wordpress Versiyon numarası , yüklü eklentilerin ve 
          temanın güvenlik açığının” taramasını yapar.

          """)
     secimwpscan = raw_input("       Devam (E/H): ")
     if secimwpscan == "e" or secimwpscan == "E":
          print("   \033[1;91mwpscan ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install wpscan")
          print("   \033[1;91mwpscan Güncelleniyor...\033[1;m")
          time.sleep(0.5)
          os.system("clear")
          print("   \033[1;91mwpscan Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          wpscanhedef = raw_input("     Hedef Giriniz: ")
          os.system("wpscan --url "+wpscanhedef+ " --enumerate p")
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

     elif secimwpscan == "h" or secimwpscan == "H":
          os.system("clear")
          baslangic()

def skipfish():
     print("""
          skipfish
          Skipfish genelde hızlı tarama ve raporlama
          sistemiyle ön plana çıkan bir scanner aracıdır.

          """)
     secimskipfish = raw_input("       Devam (E/H): ")
     if secimskipfish == "e" or secimskipfish == "E":
          print("   \033[1;91mskipfish ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install skipfish")
          print("   \033[1;91mskipfish Güncelleniyor...\033[1;m")
          time.sleep(0.5)
          print("   91mBagımlılıklar ...")
          os.system("clear")
          print("   \033[1;91mskipfish Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          skipfishhedef = raw_input("     Hedef Giriniz: ")
          os.system("skipfish -o /home/skipfishtarama http://"+skipfishhedef)
          print(" ")
          print("   \033[1;91m/home/skipfishtarama/ dizinine tarama çıktısı kaydedildi.\033[1;m")
          


     elif secimsqlsus == "h" or secimsqlsus == "H":
          os.system("clear")
          baslangic()

def nikto():
	print("""
         Nikto belirlediğimiz hedefe internet ortamında
         keşfedilmiş web güvenliği açıkları ile sistemi tarar,
         web güvenliği açıklarınızda tarama yaparken web
         sunucusunu da taramaya dahil eder.

          """)
	secimnikto = raw_input("       Devam (E/H): ")
	if secimnikto == "e" or secimnikto == "E":
          print("   \033[1;91mNikto ...\033[1;m")
          time.sleep(1)
          os.system("apt-get install nikto")
          print("   \033[1;91mNikto Güncelleniyor...\033[1;m")
          time.sleep(0.5)
          os.system("clear")
          print("   \033[1;91mNikto Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          niktohedef = raw_input("     Hedef Giriniz (domain.com): ")
          porthedef = raw_input("     Port Giriniz (80): ")
          os.system("nikto -h "+niktohedef+ " -p "+porthedef)
          print("")
          print("	\033[1;91mSonuçlar Yukarıda\033[1;m")

	elif secimnikto == "h" or secimnikto == "H":
          os.system("clear")
          baslangic()

def wapiti():
	print("""
          Wapiti

          """)
	secimwapiti = raw_input("       Devam (E/H): ")
	if secimwapiti == "e" or secimwapiti == "E":
	          print("   \033[1;91mwapiti ...\033[1;m")
	          time.sleep(1)
	          os.system("apt-get install wapiti")
	          print("   \033[1;91mwapiti Güncelleniyor...\033[1;m")
	          time.sleep(0.5)
	          os.system("clear")
	          print("   \033[1;91mwapiti Başlatılıyor...\033[1;m")
	          time.sleep(1)
	          logohack()
	          wapitihedef = raw_input("     Hedef Giriniz: ")
	          os.system("wapiti "+wapitihedef)
	          print("")
          	  print("	 \033[1;91mSonuçlar Yukarıda\033[1;m")

	elif secimwpscan == "h" or secimwpscan == "H":
	          os.system("clear")
	          baslangic()
#Zaafiyet Tarama komutlar Son
def zafiyetbilgidevam():
	print("		1-) Geri Dön")
	print("		2-) Çık")
	secimzafiyetbilgidevam = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")
	if secimzafiyetbilgidevam == "1":
		os.system("clear")
		baslangic()
	if secimzafiyetbilgidevam == "2":
		print ("  Güle Güle " + " " + kullanici)
		time.sleep(1)
		sys.exit()
#Başlangıç
def baslangic():
	os.system("clear")
	logo()
	baslangicmenu()
	print("   Seçeneklerden Birini Giriniz.")
	secim = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")

	if secim == "1":
	          os.system("clear")
	          logohack()
	          bilgi()
	          
	          print("   Seçeneklerden Birini Giriniz.")
	          secimbilgi = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")

	          if secimbilgi == "1":
	               dmitry()
	          if secimbilgi == "2":
	               golismero()     
	          if secimbilgi == "3":
	               theharvester()
	          if secimbilgi == "4":
	               sublist3r()
	          if secimbilgi == "5":
	               nmap()               
	          if secimbilgi == "6":
	          		sn1per()
	          if secimbilgi == "7":
	          		delosemre_bilgi()
	          if secimbilgi == "8":
	          		baslangic()
	          if secimbilgi == "9":
	               print ("  Güle Güle " + " " + kullanici)
	               time.sleep(1)
	               sys.exit()


	if secim == "2":
	          os.system("clear")
	          logohack()
	          zaafiyettarama()
	          print("   Seçeneklerden Birini Giriniz.")
	          secimzaafiyettarama = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")

	          if secimzaafiyettarama == "1":
	          	os.system("clear")
	          	fimap()     
	          if secimzaafiyettarama == "2":
	          	os.system("clear")
	          	uniscan()
	          if secimzaafiyettarama == "3":
	          	os.system("clear")
	          	joomscan()
	          if secimzaafiyettarama == "4":
	          	os.system("clear")
	          	wpscan()
	          if secimzaafiyettarama == "5":
	          	os.system("clear")
	          	skipfish()
	          if secimzaafiyettarama == "6":
	          	os.system("clear")
	          	nikto()
	          if secimzaafiyettarama == "7":
	          	os.system("clear")
	          	wapiti()
	          if secimzaafiyettarama == "8":
	          	os.system("clear")
	          	baslangic()
	          if secimzaafiyettarama == "9":
	               print ("  Güle Güle " + " " + kullanici)
	               print(" ")
	               time.sleep(1)
	               sys.exit()
	if secim == "3":
		os.system("clear")
		print ("""
Hata, Düzeltmeler ve Öneriler İçin İletişime Geçiniz.
	          \033[1;91m
	          Telegram:
	          @delosemre
	          @kernel_blog

	          Twitter: 
	          @delosemre
	          @kernel_blog
	               ---
               www.emreylmz.com
               www.kernelblog.org
               www.en.kernelblog.org
               info@kernelblog.org
               delosemre@outlook.com
               delosemre@kernelblog.org\033[1;m

	          1-) Geri Dön
	          2-) Çıkış
	          """)
	     
	     
		secim3 = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")
		if secim3 == "1":
	               os.system("clear")
	               baslangic()
		if secim3 == "2":
	               print ("  Güle Güle " + " " + kullanici)
	               time.sleep(0.5)
	               sys.exit()
				
	if secim == "Sistemi Güncelle" or secim == "sistemi güncelle" or secim == "4":
	          print("Sistem Güncelleniyor" + " " + kullanici)
	          os.system("apt-get update")
	          logo()
	          baslangic()

	

	if secim == "çıkış" or secim == "Çıkış" or secim == "5":
	          print ("  Güle Güle " + " " + kullanici)
	          time.sleep(0.5)
	          sys.exit()


def rootkontrol():
     if os.geteuid()==0:
          print("\n    [ + ] Root Erişimi var, Açılıyor...")
          time.sleep(2)
          baslangic()
     else:
          print ("\n  [ * ] Lütfen root erişimi ile çalıştırın.")

rootkontrol()