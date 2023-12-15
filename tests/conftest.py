import os
import requests
import time


from dotenv import load_dotenv
load_dotenv()




environment = input('''Test yapılacak ortamı seçin ( 1, 2, 3, 4 ) \n
1 - Oracle Development\n
2 - Oracle Production\n
3 - Postgre Development\n
4 - Postgre Production\n
''')

## general variables
base_url_ora_dev = os.getenv("ORADEVURL")
base_url_ora_prod = os.getenv("ORAPRODURL")
base_url_pgre_dev = os.getenv("PGREDEVURL")
base_url_pgre_prod = os.getenv("PGREPRODURL")

if environment == "1" :
    baseURL = base_url_ora_dev
    report_title = " Locationbox Oracle Dev "
elif environment == "2":
    baseURL = base_url_ora_prod
    report_title = " Locationbox Oracle Prod "
elif environment == "3":
    baseURL = base_url_pgre_dev
    report_title = " Locationbox Postgre Dev "
elif environment == "4":
    baseURL=base_url_pgre_prod
    report_title = " Locationbox Postgre Prod "

locationboxAppVersion = ""
addressDataSetVersion = ""
addressCleanerVersion =""

lbsKey= os.getenv("LBSKEY")

def pytest_html_report_title(report):
    report.title = report_title

def Get_Version():
    global locationboxAppVersion
    global addressDataSetVersion
    global addressCleanerVersion
    request = requests.get(f"{baseURL}Key={lbsKey}&Cmd=getversion",verify=False)
    response = request.json()
    locationboxAppVersion = response["version"]
    request2 = requests.get(f"{baseURL}Key={lbsKey}&Cmd=Geocode&Address=Tu%C4%9F%C3%A7e%20Cad.",verify=False)
    response2 = request2.json()
    addressDataSetVersion = response2["dataversion"]
    addressCleanerVersion = response2["adrcleanver"]

Get_Version()

def pytest_configure(config):
    from platform import python_version
    py_version = python_version()
    config._metadata = {
        "Test yapılan ortam" : report_title,
        "Locationbox version" : locationboxAppVersion,
        "Address Cleaner version" : addressCleanerVersion,
        "Adres Database version" : addressDataSetVersion
    }
