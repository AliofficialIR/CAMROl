from colorama import Fore, init
from os import system, name
import requests
import re
import time 

init()

len_count = []

def header_os():
    pm = f'''
    \t{Fore.RED}----------------------------------------------------------------------------------------
\t|  ██╗  ██╗   ███████╗ █████╗ ██████╗ ██████╗  █████╗ ██╗     ██╗      █████╗ ██╗  ██╗ |
\t|  ██║  ██║   ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║     ██║     ██╔══██╗██║  ██║ |
\t|  ███████║   ███████╗███████║██████╔╝██████╔╝███████║██║     ██║     ███████║███████║ |
\t|  ██╔══██║   ╚════██║██╔══██║██╔══██╗██╔══██╗██╔══██║██║     ██║     ██╔══██║██╔══██║ |
\t|  ██║  ██║██╗███████║██║  ██║██║  ██║██║  ██║██║  ██║███████╗███████╗██║  ██║██║  ██║ |
\t|  ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ |
\t|                          {Fore.WHITE}==> Coded by A.Vaziri <==                           {Fore.RED}        |
\t{Fore.RED}----------------------------------------------------------------------------------------        
\t!*                        {Fore.GREEN}Telegram Channel : https://t.me/H_SarrAllaH                 {Fore.RED}*!
                      
    '''
    print(pm)
    for i in range(0, 4):
        time.sleep(0.1)
        print('\n')

    
    les = f"""{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}] {Fore.GREEN}choose a country:                                                                     
\t{Fore.YELLOW}1) {Fore.WHITE}United States                {Fore.YELLOW}31) {Fore.WHITE}Mexico                {Fore.YELLOW}61) {Fore.WHITE}Moldova
\t{Fore.YELLOW}2) {Fore.WHITE}Japan                        {Fore.YELLOW}32) {Fore.WHITE}Finland               {Fore.YELLOW}62) {Fore.WHITE}Nicaragua
\t{Fore.YELLOW}3) {Fore.WHITE}Italy                        {Fore.YELLOW}33) {Fore.WHITE}China                 {Fore.YELLOW}63) {Fore.WHITE}Malta
\t{Fore.YELLOW}4) {Fore.WHITE}Korea                        {Fore.YELLOW}34) {Fore.WHITE}Chile                 {Fore.YELLOW}64) {Fore.WHITE}Trinidad And Tobago
\t{Fore.YELLOW}5) {Fore.WHITE}France                       {Fore.YELLOW}35) {Fore.WHITE}South Africa          {Fore.YELLOW}65) {Fore.WHITE}Soudi Arabia
\t{Fore.YELLOW}6) {Fore.WHITE}Germany                      {Fore.YELLOW}36) {Fore.WHITE}Slovakia              {Fore.YELLOW}66) {Fore.WHITE}Croatia
\t{Fore.YELLOW}7) {Fore.WHITE}Taiwan                       {Fore.YELLOW}37) {Fore.WHITE}Hungary               {Fore.YELLOW}67) {Fore.WHITE}Cyprus
\t{Fore.YELLOW}8) {Fore.WHITE}Russian Federation           {Fore.YELLOW}38) {Fore.WHITE}Ireland               {Fore.YELLOW}68) {Fore.WHITE}Pakistan
\t{Fore.YELLOW}9) {Fore.WHITE}United Kingdom               {Fore.YELLOW}39) {Fore.WHITE}Egypt                 {Fore.YELLOW}69) {Fore.WHITE}United Arab Emirates
\t{Fore.YELLOW}10) {Fore.WHITE}Netherlands                 {Fore.YELLOW}40) {Fore.WHITE}Thailand              {Fore.YELLOW}70) {Fore.WHITE}Kazakhstan
\t{Fore.YELLOW}11) {Fore.WHITE}Czech Republic              {Fore.YELLOW}41) {Fore.WHITE}Ukraine               {Fore.YELLOW}71) {Fore.WHITE}Kuwait
\t{Fore.YELLOW}12) {Fore.WHITE}Turkey                      {Fore.YELLOW}42) {Fore.WHITE}Serbia                {Fore.YELLOW}72) {Fore.WHITE}Venezuela
\t{Fore.YELLOW}13) {Fore.WHITE}Austria                     {Fore.YELLOW}43) {Fore.WHITE}Hong Kong             {Fore.YELLOW}73) {Fore.WHITE}Georgia
\t{Fore.YELLOW}14) {Fore.WHITE}Switzerland                 {Fore.YELLOW}44) {Fore.WHITE}Greece                {Fore.YELLOW}74) {Fore.WHITE}Montenegro
\t{Fore.YELLOW}15) {Fore.WHITE}Spain                       {Fore.YELLOW}45) {Fore.WHITE}Portugal              {Fore.YELLOW}75) {Fore.WHITE}El Salvador
\t{Fore.YELLOW}16) {Fore.WHITE}Canada                      {Fore.YELLOW}46) {Fore.WHITE}Latvia                {Fore.YELLOW}76) {Fore.WHITE}Luxembourg
\t{Fore.YELLOW}17) {Fore.WHITE}Sweden                      {Fore.YELLOW}47) {Fore.WHITE}Singapore             {Fore.YELLOW}77) {Fore.WHITE}Curacao
\t{Fore.YELLOW}18) {Fore.WHITE}Israel                      {Fore.YELLOW}48) {Fore.WHITE}Iceland               {Fore.YELLOW}78) {Fore.WHITE}Puerto Rico
\t{Fore.YELLOW}19) {Fore.WHITE}Iran                        {Fore.YELLOW}49) {Fore.WHITE}Malaysia              {Fore.YELLOW}79) {Fore.WHITE}Costa Rica
\t{Fore.YELLOW}20) {Fore.WHITE}Poland                      {Fore.YELLOW}50) {Fore.WHITE}Colombia              {Fore.YELLOW}80) {Fore.WHITE}Belarus
\t{Fore.YELLOW}21) {Fore.WHITE}India                       {Fore.YELLOW}51) {Fore.WHITE}Tunisia               {Fore.YELLOW}81) {Fore.WHITE}Albania
\t{Fore.YELLOW}22) {Fore.WHITE}Norway                      {Fore.YELLOW}52) {Fore.WHITE}Estonia               {Fore.YELLOW}82) {Fore.WHITE}Liechtenstein
\t{Fore.YELLOW}23) {Fore.WHITE}Romania                     {Fore.YELLOW}53) {Fore.WHITE}Dominican Republic    {Fore.YELLOW}83) {Fore.WHITE}Bosnia And Herzegovia
\t{Fore.YELLOW}24) {Fore.WHITE}Viet Nam                    {Fore.YELLOW}54) {Fore.WHITE}Sloveania             {Fore.YELLOW}84) {Fore.WHITE}Paraguay
\t{Fore.YELLOW}25) {Fore.WHITE}Belgium                     {Fore.YELLOW}55) {Fore.WHITE}Ecuador               {Fore.YELLOW}85) {Fore.WHITE}Philippines
\t{Fore.YELLOW}26) {Fore.WHITE}Brazil                      {Fore.YELLOW}56) {Fore.WHITE}Lithuania             {Fore.YELLOW}86) {Fore.WHITE}Faroe Islands
\t{Fore.YELLOW}27) {Fore.WHITE}Bulgaria                    {Fore.YELLOW}57) {Fore.WHITE}Palestinian           {Fore.YELLOW}87) {Fore.WHITE}Guatemala
\t{Fore.YELLOW}28) {Fore.WHITE}Indonesia                   {Fore.YELLOW}58) {Fore.WHITE}New Zealand           {Fore.YELLOW}88) {Fore.WHITE}Nepal
\t{Fore.YELLOW}29) {Fore.WHITE}Denmark                     {Fore.YELLOW}59) {Fore.WHITE}Bangladeh             {Fore.YELLOW}89) {Fore.WHITE}Peru
\t{Fore.YELLOW}30) {Fore.WHITE}Argentina                   {Fore.YELLOW}60) {Fore.WHITE}Panama                {Fore.YELLOW}90) {Fore.WHITE}Uruguay
\t{Fore.YELLOW}91) {Fore.WHITE}Extra                       {Fore.YELLOW}92) {Fore.WHITE}Andorra               {Fore.YELLOW}93) {Fore.WHITE}Antigua And Barbuda
\t{Fore.YELLOW}94) {Fore.WHITE}Armenia                     {Fore.YELLOW}95) {Fore.WHITE}Angola                {Fore.YELLOW}96) {Fore.WHITE}Australia
\t{Fore.YELLOW}97) {Fore.WHITE}Aruba                       {Fore.YELLOW}98) {Fore.WHITE}Azerbaijan            {Fore.YELLOW}99) {Fore.WHITE}Barbados
\t{Fore.YELLOW}100) {Fore.WHITE}Bonaire                    {Fore.YELLOW}101) {Fore.WHITE}Bahamas              {Fore.YELLOW}102) {Fore.WHITE}Botswana
\t{Fore.YELLOW}103) {Fore.WHITE}Congo                      {Fore.YELLOW}104) {Fore.WHITE}Ivory Coast          {Fore.YELLOW}105) {Fore.WHITE}Algeria
\t{Fore.YELLOW}106) {Fore.WHITE}Fiji                       {Fore.YELLOW}107) {Fore.WHITE}Gabon                {Fore.YELLOW}108) {Fore.WHITE}Guernsey
\t{Fore.YELLOW}109) {Fore.WHITE}Greenland                  {Fore.YELLOW}110) {Fore.WHITE}Guadeloupe           {Fore.YELLOW}111) {Fore.WHITE}Guam
\t{Fore.YELLOW}112) {Fore.WHITE}Guyana                     {Fore.YELLOW}113) {Fore.WHITE}Honduras             {Fore.YELLOW}114) {Fore.WHITE}Jersey
\t{Fore.YELLOW}115) {Fore.WHITE}Jamaica                    {Fore.YELLOW}116) {Fore.WHITE}Jordan               {Fore.YELLOW}117) {Fore.WHITE}Kenya
\t{Fore.YELLOW}118) {Fore.WHITE}Cambodia                   {Fore.YELLOW}119) {Fore.WHITE}Saint Kitts          {Fore.YELLOW}120) {Fore.WHITE}Cayman Islands
\t{Fore.YELLOW}121) {Fore.WHITE}Laos                       {Fore.YELLOW}122) {Fore.WHITE}Lebanon              {Fore.YELLOW}123) {Fore.WHITE}Sri Lanka
\t{Fore.YELLOW}124) {Fore.WHITE}Morocco                    {Fore.YELLOW}125) {Fore.WHITE}Madagascar           {Fore.YELLOW}126) {Fore.WHITE}Macedonia
\t{Fore.YELLOW}127) {Fore.WHITE}Mongolia                   {Fore.YELLOW}128) {Fore.WHITE}Macao                {Fore.YELLOW}129) {Fore.WHITE}Martinique
\t{Fore.YELLOW}130) {Fore.WHITE}Mauritius                  {Fore.YELLOW}131) {Fore.WHITE}Namibia              {Fore.YELLOW}132) {Fore.WHITE}New Caledonia
\t{Fore.YELLOW}133) {Fore.WHITE}Nigeria                    {Fore.YELLOW}134) {Fore.WHITE}Qatar                {Fore.YELLOW}135) {Fore.WHITE}Reunion
\t{Fore.YELLOW}136) {Fore.WHITE}Sudan                      {Fore.YELLOW}137) {Fore.WHITE}Senegal              {Fore.YELLOW}138) {Fore.WHITE}Suriname
\t{Fore.YELLOW}139) {Fore.WHITE}Sao Tome And Principe      {Fore.YELLOW}140) {Fore.WHITE}Syria                {Fore.YELLOW}141) {Fore.WHITE}Tanzania
\t{Fore.YELLOW}142) {Fore.WHITE}Uganda                     {Fore.YELLOW}143) {Fore.WHITE}Uzbekistan           {Fore.YELLOW}144) {Fore.WHITE}Saint Vincent And The Grenadines
\t{Fore.YELLOW}145) {Fore.WHITE}Benin
"""
    print(les)
    
def clear ():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

try:
    print()
    clear()
    header_os()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                 "-" , "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB", 
                 "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL",
                 "GP", "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN",
                 "KY", "LA", "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ",
                 "MU", "NA", "NC", "NG", "QA", "RE", "SD", "SN", "SR", "ST",
                 "SY", "TZ", "UG", "UZ", "VC","BJ", ]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 145+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print(Fore.RED+ip)
   
except:
    pass
finally:
    print(Fore.RED)
    exit()
