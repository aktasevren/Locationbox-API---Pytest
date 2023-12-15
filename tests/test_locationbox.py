## import libraries

import requests
import xmltodict
import cx_Oracle
from datetime import date
import pytest
import psycopg2
import time
from .conftest import environment
from .conftest import lbsKey
import os

from dotenv import load_dotenv
load_dotenv()

set_poi_attribute_value = "0"
typ = ["JSON", "XML"]

base_url_ora_dev = os.getenv("ORADEVURL")
base_url_ora_prod = os.getenv("ORAPRODURL")
base_url_pgre_dev = os.getenv("PGREDEVURL")
base_url_pgre_prod = os.getenv("PGREPRODURL")

## DB connection details

# Oracle Dev
connUsername_ora_dev = os.getenv("USERORADEV")
connPassword_ora_dev = os.getenv("PASSORADEV")
connHost_ora_dev = os.getenv("HOSTORADEV")
connPort_ora_dev = os.getenv("PORTORADEV")
connSID_ora_dev = os.getenv("SIDORADEV")

# Oracle Prod
connUsername_ora_prod = os.getenv("USERORAPROD")
connPassword_ora_prod = os.getenv("PASSORAPROD")
connHost_ora_prod = os.getenv("HOSTORAPROD")
connPort_ora_prod = os.getenv("PORTORAPROD")
connServiceName_ora_prod = os.getenv("SERVICEORAPROD")

# Postgre Dev
connUsername_pgre_dev = os.getenv("USERPGREDEV")
connPassword_pgre_dev = os.getenv("PASSPGREDEV")
connHost_pgre_dev = os.getenv("HOSTPGREDEV")
connDatabase_pgre_dev = os.getenv("DBPGREDEV")

# Postgre Prod
connUsername_pgre_prod = os.getenv("USERPGREPROD")
connPassword_pgre_prod = os.getenv("PASSPGREPROD")
connHost_pgre_prod = os.getenv("HOSTPGREPROD")
connDatabase_pgre_prod = os.getenv("DBPGREPROD")

## functions

def print_req_res(req,res):
    print("-- REQUEST --")
    print(req.url)
    print("-- RESPONSE --")
    print(res)


# ----------------------------------------  SERVICES  ----------------------------------------
if environment == "1" :
    baseURL = base_url_ora_dev
    connUsername = connUsername_ora_dev
    connPassword =connPassword_ora_dev
    connHost = connHost_ora_dev
    connPort = connPort_ora_dev
    connSID = connSID_ora_dev
elif environment == "2":
    baseURL = base_url_ora_prod
    connUsername = connUsername_ora_prod
    connPassword =connPassword_ora_prod
    connHost = connHost_ora_prod
    connPort = connPort_ora_prod
    connSID = connServiceName_ora_prod
elif environment == "3":
    baseURL = base_url_pgre_dev
    connUsername = connUsername_pgre_dev
    connPassword = connPassword_pgre_dev
    connHost = connHost_pgre_dev
    connDatabase = connDatabase_pgre_dev
elif environment == "4":
    baseURL=base_url_pgre_prod
    connUsername = connUsername_pgre_prod
    connPassword = connPassword_pgre_prod
    connHost = connHost_pgre_prod
    connDatabase = connDatabase_pgre_prod


def test_Get_Version():
    cmd = "Getversion"
    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None

def test_Get_Key_Status():
    cmd = "GetKeyStatus"
    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
            assert response["requestLimit"] > 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["request_limit"] > "0"
            assert response["response"]["errno"] == None

@pytest.mark.address
@pytest.mark.geocoding
def test_Geocode():
    cmd = "Geocode"
    address = "Altayçeşme Mah. Kiraz Sok. No:15 Maltepe İstanbul"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&Address={address}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&Address={address}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.geocoding
def test_Global_Geocode():
    cmd = "GlobalGeocode"
    address = "Lodz,Gdanska Street, 106-8, Poland"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&Address={address}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&Address={address}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.reversegeocoding
def test_Reverse_Geocode():
    cmd = "Geocode"
    latitude = "40.93351"
    longitude = "29.13095"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&Latitude={latitude}&Longitude={longitude}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&Latitude={latitude}&Longitude={longitude}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Il_List():
    cmd = "IlList"

    for type in typ:
        if type == "JSON":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON")
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML")
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Il_List_With_Extend():
    cmd = "IlListWİthExtent"

    minlat = "40.357822"
    minlong = "28.521057"
    maxlat = "41.327673"
    maxlong = "30.034842"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Ilce_List():
    cmd = "IlceList"

    ilId = "6"
    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&IlId={ilId}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&IlId={ilId}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Ilce_List_With_Extend():
    cmd = "IlceListWİthExtent"

    minlat = "40.357822"
    minlong = "28.521057"
    maxlat = "41.327673"
    maxlong = "30.034842"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Mahalle_List():
    cmd = "MahalleList"

    ilceId = "6000986000"
    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&IlceId={ilceId}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&IlceId={ilceId}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Mahalle_List_With_Extend():
    cmd = "MahalleListWİthExtent"

    minlat = "40.357822"
    minlong = "28.521057"
    maxlat = "41.327673"
    maxlong = "30.034842"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Yol_List():
    cmd = "YolList"

    mahalleId = "6000986059"
    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&MahalleId={mahalleId}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&MahalleId={mahalleId}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Yol_List_With_Extend():
    cmd = "YolListWİthExtent"

    minlat = "40.357822"
    minlong = "28.521057"
    maxlat = "41.327673"
    maxlong = "30.034842"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Kapi_List():
    cmd = "KapiList"

    yolId = "1000035901"
    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&YolId={yolId}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&YolId={yolId}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Kapi_List_With_Extend():
    cmd = "KapiListWithExtent"

    minlat = "40.357822"
    minlong = "28.521057"
    maxlat = "41.327673"
    maxlong = "30.034842"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlat}&MinLongitude={minlong}&MaxLatitude={maxlat}&MaxLongitude={maxlong}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Get_Coordinate():
    cmd = "GetCoordinate"
    ilceId = "6000986000"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&IlceId={ilceId}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&IlceId={ilceId}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Get_Bagimsiz_Birim():
    cmd = "GetBagimsizBirim"
    adresKodu = "3749201855"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&AdresKodu={adresKodu}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&AdresKodu={adresKodu}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.addresselements
def test_Get_Bagimsiz_Birim_List():
    cmd = "GetBagimsizBirimList"
    kapiId = "15051836"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&KapiId={kapiId}"
            )
            response = request.json()
            print_req_res(request,response)

            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=XML&KapiId={kapiId}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)

            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.getsuggestions
def test_Get_Suggestions():
    # ADRESKODU package must be defined for your API key in order to retrieve "addresscode" fields.
    # WHAT3WORDS package must be defined for your API key in order to retrieve what3words.

    cmd = "GetSuggestions"
    latitude = "41.111"
    longitude = "29.023"
    keyword = "Bostancı"
    count = "5"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Count={count}&Keyword={keyword}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Count={count}&Keyword={keyword}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.elementsinfo
def test_Get_Il_Info():
    cmd = "GetIlInfo"
    ilId = "1"
    geometry = "1"
    encode = "0"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&IlId={ilId}&Encode={encode}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&IlId={ilId}&Encode={encode}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.elementsinfo
def test_Get_Ilce_Info():
    cmd = "GetIlceInfo"
    ilceId = "10000441000"
    geometry = "1"
    encode = "0"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&IlceId={ilceId}&Encode={encode}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&IlceId={ilceId}&Encode={encode}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.elementsinfo
def test_Get_Mahalle_Info():
    cmd = "GetMahalleInfo"
    mahalleId = "10000441003"
    geometry = "1"
    encode = "0"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&MahalleId={mahalleId}&Encode={encode}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&MahalleId={mahalleId}&Encode={encode}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.elementsinfo
def test_Get_Yol_Info():
    cmd = "GetYolInfo"
    yolId = "1000035901"
    geometry = "1"
    encode = "0"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&YolId={yolId}&Encode={encode}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&YolId={yolId}&Encode={encode}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.address
@pytest.mark.elementsinfo
def test_Get_Kapi_Info():
    cmd = "GetKapiInfo"
    kapiId = "15051836"
    geometry = "1"
    encode = "0"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&KapiId={kapiId}&Encode={encode}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}&KapiId={kapiId}&Encode={encode}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


# @pytest.mark.address
# @pytest.mark.what3words
# def test_What_3_Words():
#     cmd = "What3Words"
#     lang = "en"
#     words = "index.home.raft"

#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&lang={lang}&Words={words}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0
#         elif type == "XML":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&lang={lang}&Words={words}"
#             )
#             response = xmltodict.parse(request.content)
#             print_req_res(request,response)
#             assert response["response"]["status"] == "0"
#             assert response["response"]["errno"] == None


# @pytest.mark.address
# @pytest.mark.what3words
# def test_What_3_Words_2():
#     cmd = "What3Words"
#     lang = "en"
#     position = "51.52152,0.203586"

#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&lang={lang}&Position={position}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0
#         elif type == "XML":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&lang={lang}&Position={position}"
#             )
#             response = xmltodict.parse(request.content)
#             print_req_res(request,response)
#             assert response["response"]["status"] == "0"
#             assert response["response"]["errno"] == None


@pytest.mark.poi
@pytest.mark.search
def test_Poi_Search():
    cmd = "PoiSearch"
    latitude = "40.93351"
    longitude = "29.13095"
    radius = "8000"
    category = "ECZANE"
    keyword = "AYA"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Radius={radius}&Category={category}&Keyword={keyword}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Radius={radius}&Category={category}&Keyword={keyword}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.poi
@pytest.mark.search
def test_Poi_Search_With_Extend():
    cmd = "PoiSearchWithExtent"
    minlatitude = "40.357822"
    minlongitude = "28.521057"
    maxlatitude = "41.327673"
    maxlongitude = "30.034842"
    category = "MARKET"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlatitude}&MinLongitude={minlongitude}&MaxLatitude={maxlatitude}&MaxLongitude={maxlongitude}&Category={category}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlatitude}&MinLongitude={minlongitude}&MaxLatitude={maxlatitude}&MaxLongitude={maxlongitude}&Category={category}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.poi
@pytest.mark.list
def test_Poi_List():

    cmd = "PoiList"
    ilId = "34"
    ilceId = "34000019000"
    category = "ECZANE"

    if (environment=="3"):
        lbsKey= os.getenv("LBSKEY1")
        category ='TURKCELL'
    else:   
        lbsKey = os.getenv("LBSKEY")

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilId}&IlceId={ilceId}&Category={category}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilId}&IlceId={ilceId}&Category={category}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.poi
@pytest.mark.list
def test_Get_Poi():
    cmd = "GetPoi"
    poiId = "34200143722"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={poiId}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={poiId}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.poi
@pytest.mark.categorylist
def test_Poi_Category_List():
    cmd = "CategoryList"

    for type in typ:
        if type == "JSON":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}")
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}")
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.poi
@pytest.mark.brandlist
def test_Poi_Brand_List():
    cmd = "BrandList"

    for type in typ:
        if type == "JSON":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}")
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}")
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.poi
@pytest.mark.count
def test_Poi_Count():
    cmd = "PoiCount"
    ilId = "34"
    ilceId = "34000015000"
    brand = "TEKNOSA"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilId}&IlceId={ilceId}&Brand={brand}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilId}&IlceId={ilceId}&Brand={brand}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.poi
@pytest.mark.count
def test_Poi_Count_With_Extend():
    cmd = "BrandList"
    minlatitude = "40.357822"
    maxlatitude = "41.327673"
    minlongitude = "28.521057"
    maxlongitude = "29.034842"
    brand = "TEKNOSA"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlatitude}&MaxLatitude={maxlatitude}&MinLongitude={minlongitude}&MaxLongitude={maxlongitude}&Brand={brand}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minlatitude}&MaxLatitude={maxlatitude}&MinLongitude={minlongitude}&MaxLongitude={maxlongitude}&Brand={brand}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


# @pytest.mark.poi
# @pytest.mark.attribute
# @pytest.mark.needDbConnection
# def test_Set_Poi_Attribute():
#     cmd = "SetPoiAttribute"
#     poiId = "3420004679325"
#     poiId1 = "27200016663"
#     tarih = date.today()
#     attribute = f"EVREN_TEST_{tarih}"
#     type2 = "1"

#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&PoiId={poiId}&Attribute={attribute}&Type={type2}&Value={setPoiAttributevalue}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0

#             try:
#                 connection = cx_Oracle.connect(
#                     connUsername,
#                     connPassword,
#                     cx_Oracle.makedsn(connHost, connPort, connSID),
#                 )

#                 cur = connection.cursor()

#                 cur.execute(
#                     f"select (ATTRIBUTE) from LOCATIONBOX.LBS_POI_ATTRIBUTE where POI_ID = '{poiId}' and ATTRIBUTE='EVREN_TEST_{tarih}'"
#                 )
#                 print(f"select (ATTRIBUTE) from LOCATIONBOX.LBS_POI_ATTRIBUTE where POI_ID = '{poiId}' and ATTRIBUTE='EVREN_TEST_{tarih}'")
#                 for row in cur.fetchall():
#                     sonuc = (
#                         str(row)
#                         .replace("(", "")
#                         .replace(")", "")
#                         .replace(",", "")
#                         .replace("'", "")
#                     )
#                     assert attribute == sonuc
#                 cur.close()
#             except cx_Oracle.Error as error:
#                 print(error)
#             finally:
#                 # release the connection
#                 if connection:
#                     connection.close()

#         elif type == "XML":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&PoiId={poiId1}&Attribute={attribute}&Type={type2}&Value={setPoiAttributevalue}"

#             )
#             response = xmltodict.parse(request.content)
#             print_req_res(request,response)
#             assert response["response"]["status"] == "0"
#             assert response["response"]["errno"] == None

#             try:
#                 connection = cx_Oracle.connect(
#                     connUsername,
#                     connPassword,
#                     cx_Oracle.makedsn(connHost, connPort, connSID),
#                 )
#                 cur = connection.cursor()
#                 cur.execute(
#                     f"select (ATTRIBUTE) from LOCATIONBOX.LBS_POI_ATTRIBUTE where POI_ID = '{poiId1}' and ATTRIBUTE='EVREN_TEST_{tarih}'"
#                 )
#                 for row in cur.fetchall():
#                     sonuc = (
#                         str(row)
#                         .replace("(", "")
#                         .replace(")", "")
#                         .replace(",", "")
#                         .replace("'", "")
#                     )
#                     assert attribute == sonuc
#                 cur.close()
#             except cx_Oracle.Error as error:
#                 print(error)
#             finally:
#                 # release the connection
#                 if connection:
#                     connection.close()


# @pytest.mark.poi
# @pytest.mark.attribute
# @pytest.mark.needDbConnection
# def test_Increment_Poi_Attribute():
#     cmd = "IncrementPoiAttribute"
#     poiId = "3420004679325"
#     poiId1 = "27200016663"

#     tarih = date.today()
#     attribute = f"EVREN_TEST_{tarih}"
#     type2 = "1"
#     value = 34

#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&PoiId={poiId}&Attribute={attribute}&Type={type2}&Value={value}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0

#             try:
#                 connection = cx_Oracle.connect(
#                     connUsername,
#                     connPassword,
#                     cx_Oracle.makedsn(connHost, connPort, connSID),
#                 )
#                 cur = connection.cursor()
#                 cur.execute(
#                     f"select (NUMBER_VALUE) from LOCATIONBOX.LBS_POI_ATTRIBUTE where POI_ID = '{poiId}' and ATTRIBUTE='EVREN_TEST_{tarih}'"
#                 )
#                 for row in cur.fetchall():
#                     sonuc = (
#                         str(row)
#                         .replace("(", "")
#                         .replace(")", "")
#                         .replace(",", "")
#                         .replace("'", "")
#                     )
#                     assert "34" == sonuc
#                 cur.close()
#             except cx_Oracle.Error as error:
#                 print(error)
#             finally:
#                 # release the connection
#                 if connection:
#                     connection.close()

#         # elif type == "XML":
#         #     request = requests.get(
#         #         f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&PoiId={poiId1}&Attribute={attribute}&Type={type2}&Value={value}"

#         #     )
#         #     response = xmltodict.parse(request.content)
#         #     print_req_res(request,response)
#         #     assert response["response"]["status"] == "0"
#         #     assert response["response"]["errno"] == None

#         #     try:
#         #         connection = cx_Oracle.connect(
#         #             connUsername,
#         #             connPassword,
#         #             cx_Oracle.makedsn(connHost, connPort, connSID),
#         #         )
#         #         cur = connection.cursor()
#         #         cur.execute(
#         #             f"select (NUMBER_VALUE) from LOCATIONBOX.LBS_POI_ATTRIBUTE where POI_ID = '{poiId1}' and ATTRIBUTE='EVREN_TEST_{tarih}'"
#         #         )
#         #         for row in cur.fetchall():
#         #             sonuc2 = (
#         #                 str(row)
#         #                 .replace("(", "")
#         #                 .replace(")", "")
#         #                 .replace(",", "")
#         #                 .replace("'", "")
#         #             )
#         #             assert 34 == sonuc2

#         #         cur.close()
#         #     except cx_Oracle.Error as error:
#         #         print(error)
#         #     finally:
#         #         # release the connection
#         #         if connection:
#         #             connection.close()


# @pytest.mark.poi
# @pytest.mark.attribute
# @pytest.mark.needDbConnection
# def test_Decrement_Poi_Attribute():
#     cmd = "DecrementPoiAttribute"
#     poiId = "3420004679325"
#     poiId1 = "27200016663"

#     tarih = date.today()
#     attribute = f"EVREN_TEST_{tarih}"
#     type2 = "1"
#     value = 5

#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&PoiId={poiId}&Attribute={attribute}&Type={type2}&Value={value}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0

#             try:
#                 connection = cx_Oracle.connect(
#                     connUsername,
#                     connPassword,
#                     cx_Oracle.makedsn(connHost, connPort, connSID),
#                 )
#                 cur = connection.cursor()
#                 cur.execute(
#                     f"select (NUMBER_VALUE) from LOCATIONBOX.LBS_POI_ATTRIBUTE where POI_ID = '{poiId}' and ATTRIBUTE='EVREN_TEST_{tarih}'"
#                 )
#                 for row in cur.fetchall():
#                     sonuc1 = (
#                         str(row)
#                         .replace("(", "")
#                         .replace(")", "")
#                         .replace(",", "")
#                         .replace("'", "")
#                     )
#                     assert "29" == sonuc1
#                 cur.close()
#             except cx_Oracle.Error as error:
#                 print(error)
#             finally:
#                 # release the connection
#                 if connection:
#                     connection.close()

#         # elif type == "XML":
#         #     request = requests.get(
#         #         f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&PoiId={poiId1}&Attribute={attribute}&Type={type2}&Value={value}"
#         #     )
#         #     response = xmltodict.parse(request.content)
#         #     print_req_res(request,response)
#         #     assert response["response"]["status"] == "0"
#         #     assert response["response"]["errno"] == None

#         #     try:
#         #         connection = cx_Oracle.connect(
#         #             connUsername,
#         #             connPassword,
#         #             cx_Oracle.makedsn(connHost, connPort, connSID),
#         #         )
#         #         cur = connection.cursor()
#         #         cur.execute(
#         #             f"select (NUMBER_VALUE) from LOCATIONBOX.LBS_POI_ATTRIBUTE where POI_ID = '{poiId1}' and ATTRIBUTE='EVREN_TEST_{tarih}'"
#         #         )
#         #         for row in cur.fetchall():
#         #             sonuc = (
#         #                 str(row)
#         #                 .replace("(", "")
#         #                 .replace(")", "")
#         #                 .replace(",", "")
#         #                 .replace("'", "")
#         #             )
#         #             assert "29" == sonuc
#         #         cur.close()
#         #     except cx_Oracle.Error as error:
#         #         print(error)
#         #     finally:
#         #         # release the connection
#         #         if connection:
#         #             connection.close()

# @pytest.mark.poi
# @pytest.mark.attribute
# def test_Remove_Poi_Attribute():
#     cmd = "RemovePoiAttribute"
#     poiId = "3420004679325"
#     poiId1 = "27200016663"

#     tarih = date.today()
#     attribute = f"EVREN_TEST_{tarih}"


#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&PoiId={poiId}&Attribute={attribute}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0

#         elif type == "XML":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&PoiId={poiId1}&Attribute={attribute}"
#             )
#             response = xmltodict.parse(request.content)
#             print_req_res(request,response)
#             assert response["response"]["status"] == "0"
#             assert response["response"]["errno"] == None

        
# @pytest.mark.xfail(reason="network server")
@pytest.mark.route
# @pytest.mark.skipif(networkServer == "off", reason=" Network Server is not running ")
def test_Route():
    cmd = "Rota"

    points = "41.0075/29.0174,40.9971/29.0366,40.9815/29.0967,40.9602/29.0765"
    cons = "KAMYON,FERIBOT"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Cons={cons}&Points={points}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Cons={cons}&Points={points}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.route
@pytest.mark.onroute
def test_On_Route():
    cmd = "OnRoute"
    typ = ["XML", "JSON"]
    latitude = "40.9815"
    longitude = "29.0967"
    pathId = "3500529"
    distance = "10000"
    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&PathId={pathId}&Distance={distance}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&PathId={pathId}&Distance={distance}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.route
@pytest.mark.distancematrix
def test_Distance_Matrix():
    cmd = "DistanceMatrix"
    typ = ["XML", "JSON"]
    criteria = "FAST"
    cons = "KAMYON,FERIBOT"
    positions = "PointA/41.1/29.1,PointB/40.984818/29.083635,PointC/40.948784/29.170496"
    route = "0"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Criteria={criteria}&Cons={cons}&Route={route}&Positions={positions}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Criteria={criteria}&Cons={cons}&Route={route}&Positions={positions}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.map
@pytest.mark.skipif((environment=="3"), reason="Postgre method not supported")
@pytest.mark.skipif((environment=="4"), reason="Postgre method not supported")

def test_Map():
    cmd = "Map"
    typ = ["XML", "JSON"]
    latitude = "40.93351"
    longitude = "29.13095"
    zoomLevel = "4"
    pan = "0"
    width = "600"
    height = "400"
    points = "40.9602/29.0765,40.93351/29.13095"
    basemap = "101"
    userDataId = "1"
    userData = "REGION"
    userDataStyle = "10001"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&ZoomLevel={zoomLevel}&Pan={pan}&Width={width}&Height={height}&Points={points}&Basemap={basemap}&UserDataId={userDataId}&UserData={userData}&UserDataStyle={userDataStyle}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&ZoomLevel={zoomLevel}&Pan={pan}&Width={width}&Height={height}&Points={points}&Basemap={basemap}&UserDataId={userDataId}&UserData={userData}&UserDataStyle={userDataStyle}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.map
@pytest.mark.skipif(environment=="3", reason="Postgre method not supported")
@pytest.mark.skipif(environment=="4", reason="Postgre method not supported")

def test_Map_Image():
    cmd = "MapImage"
    typ = ["XML", "JSON"]
    latitude = "40.93351"
    longitude = "29.13095"
    zoomLevel = "10"
    pan = "0"
    width = "600"
    height = "400"
    points = "40.9602/29.0765,40.93351/29.13095"
    basemap = "101"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&ZoomLevel={zoomLevel}&Pan={pan}&Width={width}&Height={height}&Points={points}&Basemap={basemap}"
            )
            assert request.headers["Content-Type"] == "image/png;"
            print(request)
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&ZoomLevel={zoomLevel}&Pan={pan}&Width={width}&Height={height}&Points={points}&Basemap={basemap}"
            )
            assert request.headers["Content-Type"] == "image/png;"
            print(request)


@pytest.mark.map
@pytest.mark.distance
def test_Distance():
    cmd = "Distance"
    typ = ["XML", "JSON"]
    fromLatitude = "41.1"
    fromLongitude = "29.1"
    toLatitude = "41.16"
    toLongitude = "29.05"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&FromLatitude={fromLatitude}&FromLongitude={fromLongitude}&ToLatitude={toLatitude}&ToLongitude={toLongitude}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&FromLatitude={fromLatitude}&FromLongitude={fromLongitude}&ToLatitude={toLatitude}&ToLongitude={toLongitude}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.map
@pytest.mark.elevation
def test_Get_Elevation():
    cmd = "GetElevation"
    typ = ["XML", "JSON"]
    latitude = "41.1"
    longitude = "29.05"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.map
@pytest.mark.encodedecodegeometry
def test_Encode_Geometry():
    cmd = "EncodeGeometry"
    typ = ["XML", "JSON"]
    geometry = "41.1/29.1,41.2/29.1"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.map
@pytest.mark.encodedecodegeometry
def test_Decode_Geometry():
    cmd = "DecodeGeometry"
    typ = ["XML", "JSON"]
    geometry = "_jzyF_rrpD_pR?"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Geometry={geometry}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.map
@pytest.mark.clusterpoints
def test_Cluster_Points():
    cmd = "ClusterPoints"
    typ = ["XML", "JSON"]
    cluster = "5"
    coors = "A/29.13095/40.96958,B/29.18985/40.02025,C/29.409/40.795, D/29.5485/40.954,E/29.110655/40.9663799,F/29.16678341/40.926578923,G/29.5596/40.976827"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Cluster={cluster}&Coors={coors}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Cluster={cluster}&Coors={coors}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.indoor
@pytest.mark.indoorvenuelist
def test_Indoor_Venue_List():
    cmd = "IndoorVenueList"
    typ = ["XML", "JSON"]

    for type in typ:
        if type == "JSON":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}")
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}")
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.indoor
@pytest.mark.indoorpoilist
def test_Indoor_Poi_List():
    cmd = "IndoorPoiList"

    venueId = "32772327"
    floorlevel = "1"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&VenueId={venueId}&FloorLevel={floorlevel}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&VenueId={venueId}&FloorLevel={floorlevel}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.indoor
@pytest.mark.indoorpoisearch
def test_Indoor_Poi_Search():
    cmd = "IndoorPoiSearch"

    venueId = "32772327"
    floorlevel = "1"
    latitude = "40.96952"
    longitude = "29.09188"
    radius = 100

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&VenueId={venueId}&FloorLevel={floorlevel}&Latitude={latitude}&Longitude={longitude}&Radius={radius}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&VenueId={venueId}&FloorLevel={floorlevel}&Latitude={latitude}&Longitude={longitude}&Radius={radius}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.dynamicinformation
@pytest.mark.poilistex
@pytest.mark.skipif(environment=="3", reason="No Data")
@pytest.mark.skipif(environment=="4", reason="No Data")

def test_Poi_List_Ex():
    cmd = "PoiListEx"
    if environment=="1":
            extype = "FUELPRICES"
    else:
        extype = "PHARMACYONDUTY"
    ilid = "34"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}&ExType={extype}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}&ExType={extype}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.dynamicinformation
@pytest.mark.poisearchex
@pytest.mark.skipif(environment=="3", reason="No Data")
@pytest.mark.skipif(environment=="4", reason="No Data")

def test_Poi_Search_Ex():
    cmd = "PoiSearchEx"

    latitude = "41.1"
    longitude = "29.1"
    if environment=="1":
            extype = "FUELPRICES"
    else:
        extype = "PHARMACYONDUTY"
    radius = 2000

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&ExType={extype}&Radius={radius}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&ExType={extype}&Radius={radius}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.dynamicinformation
@pytest.mark.poisearchexwithextend
@pytest.mark.skipif(environment=="3", reason="No Data")
@pytest.mark.skipif(environment=="4", reason="No Data")

def test_Poi_Search_Ex_With_Extend():
    cmd = "PoiSearchExWithExtent"

    minLatitude = "40.357822"
    minLongitude = "28.521057"
    maxLatitude = "41.327673"
    maxLongitude = "30.034842"
    if environment=="1":
            extype = "FUELPRICES"
    else:
        extype = "PHARMACYONDUTY"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minLatitude}&MinLongitude={minLongitude}&MaxLatitude={maxLatitude}&MaxLongitude={maxLongitude}&ExType={extype}"
            )
            response = request.json()
            print_req_res(request,response)

            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minLatitude}&MinLongitude={minLongitude}&MaxLatitude={maxLatitude}&MaxLongitude={maxLongitude}&ExType={extype}"
            )
            response = xmltodict.parse(request.content)

            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.dynamicinformation
@pytest.mark.socialeventlist
@pytest.mark.skipif(environment=="3", reason="select * from locationbox.DAKICK_EVENTS table not found")
@pytest.mark.skipif(environment=="4", reason="select * from locationbox.DAKICK_EVENTS table not found")

def test_Social_Event_List():
    cmd = "SocialEventList"

    for type in typ:
        if type == "JSON":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}")
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}")
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.dynamicinformation
@pytest.mark.socialeventsearch
@pytest.mark.skipif(environment=="3", reason="select * from locationbox.DAKICK_EVENTS table not found")
@pytest.mark.skipif(environment=="4", reason="select * from locationbox.DAKICK_EVENTS table not found")

def test_Social_Event_Search():
    cmd = "SocialEventSearch"

    latitude = "41.0961"
    longitude = "29.0619"
    radius = 10000

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Radius={radius}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Radius={radius}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.dynamicinformation
@pytest.mark.weatherreport
def test_Weather_Report():
    cmd = "WeatherReport"

    ilid = "34"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.campaign
@pytest.mark.campaignlist
@pytest.mark.skipif(environment=="3", reason="Postgre method not supported")
@pytest.mark.skipif(environment=="4", reason="Postgre method not supported")
@pytest.mark.skipif(environment=="2", reason="Kontrol Edilecek")
def test_Camp_Campaign_List():
    cmd = "CampCampaignList"

    category = "Elektronik"
    poiId = "1200005164"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Category={category}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Category={category}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.campaign
@pytest.mark.nearcampaigns
@pytest.mark.skipif(environment=="3", reason="Postgre method not supported")
@pytest.mark.skipif(environment=="4", reason="Postgre method not supported")
@pytest.mark.skipif(environment=="2", reason="Kontrol Edilecek")
def test_Camp_Near_Campaigns():
    cmd = "CampNearCampaigns"

    category = "Elektronik"
    radius = "10000"
    latitude = "39.94558"
    longitude = "32.73019"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Category={category}&radius={radius}&Latitude={latitude}&Longitude={longitude}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Category={category}&radius={radius}&Latitude={latitude}&Longitude={longitude}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.demography
@pytest.mark.demographicinfo
def test_Get_Demographic_Info():
    cmd = "GetDemographicInfo"

    ilid = "34"
    infoType = "OKUMAYAZMA"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}&InfoType={infoType}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}&InfoType={infoType}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.traffic
@pytest.mark.maptrafficimage
@pytest.mark.skipif(environment=="3", reason="Postgre method not supported")
@pytest.mark.skipif(environment=="4", reason="Postgre method not supported")

def test_Map_Traffic_Image():
    cmd = "MapTrafficImage"

    minLatitude = "40.740817"
    minLongitude = "28.844374"
    maxLatitude = "41.238385"
    maxLongitude = "29.283827"
    width = "600"
    height = "400"
    flow = "1"
    tmc = "1"
    event = "1"
    basemap = "101"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minLatitude}&MinLongitude={minLongitude}&MaxLatitude={maxLatitude}&MaxLongitude={maxLongitude}&Width={width}&Height={height}&Flow={flow}&Tmc={tmc}&Event={event}&Basemap={basemap}"
            )
            print("-- JSON RESPONSE --")
            assert request.headers["Content-Type"] == "image/png;"
            print(request)
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minLatitude}&MinLongitude={minLongitude}&MaxLatitude={maxLatitude}&MaxLongitude={maxLongitude}&Width={width}&Height={height}&Flow={flow}&Tmc={tmc}&Event={event}&Basemap={basemap}"
            )
            print("-- XML RESPONSE --")
            assert request.headers["Content-Type"] == "image/png;"


@pytest.mark.traffic
@pytest.mark.trafficeventsearch
def test_Traffic_Event_Search():
    cmd = "TrafficEventSearch"

    latitude = "41.0961"
    longitude = "29.0619"
    radius = "10000"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Radius={radius}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Radius={radius}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.traffic
@pytest.mark.trafficroutelist
def test_Traffic_Route_List():
    cmd = "TrafficRouteList"

    ilid = "34"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.traffic
@pytest.mark.trafficroute
def test_Traffic_Route():
    cmd = "TrafficRoute"

    ilid = "34"
    startName = "Kadıköy"
    endName = "Beşiktaş"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}&StartName={startName}&EndName={endName}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}&StartName={startName}&EndName={endName}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.traffic
@pytest.mark.trafficstartlistendlist
def test_Traffic_Start_List():
    cmd = "TrafficStartList"

    ilid = "34"
    endName = "Maslak"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}&EndName={endName}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&IlId={ilid}&EndName={endName}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.traffic
@pytest.mark.trafficinfo
def test_Traffic_Info():
    cmd = "TrafficInfo"
    if (environment=="3" or environment=="4"):
        latitude = "38.784438"
        longitude = "35.45475588"
    else:
        latitude = "40.95154"
        longitude = "29.06991"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


# @pytest.mark.userdata
# @pytest.mark.point
# def test_Add_User_Point():
#     cmd = "AddUserPoint"

#     id = "987654321"
#     id2 = "9876543212"
#     name = "evren-test"
#     address = "test mah. test cad. no:Test"
#     tel = "05555555555"
#     faxNo = "02163620507"
#     string1 = "www.infotech.com.tr"
#     string2 = "kurumsal @ infotech.com.tr"
#     num1 = "101"
#     num2 = "102"
#     latitude = "40.9686"
#     longitude = "29.1005"
#     tarih = date.today()

#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Name={name}&Address={address}&TelNo={tel}&FaxNo={faxNo}&String1={string1}&String2={string2}&Number1={num1}&Number2={num2}&Latitude={latitude}&Longitude={longitude}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0

#             try:
#                 connection = cx_Oracle.connect(
#                     connUsername,
#                     connPassword,
#                     cx_Oracle.makedsn(connHost, connPort, connSID),
#                 )
#                 cur = connection.cursor()
#                 cur.execute(
#                     f"select (ADDRESS) from LOCATIONBOX.LBS_POI_ATTRIBUTE where where POINT_ID= '{id}' and ATTRIBUTE='EVREN_TEST_{tarih}'"
#                 )
#                 for row in cur.fetchall():
#                     sonuc = (
#                         str(row)
#                         .replace("(", "")
#                         .replace(")", "")
#                         .replace(",", "")
#                         .replace("'", "")
#                     )
#                     assert address == sonuc
#                 cur.close()
#             except cx_Oracle.Error as error:
#                 print(error)
#             finally:
#                 # release the connection
#                 if connection:
#                     connection.close()

#         elif type == "XML":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id2}&Name={name}&Address={address}&TelNo={tel}&FaxNo={faxNo}&String1={string1}&String2={string2}&Number1={num1}&Number2={num2}&Latitude={latitude}&Longitude={longitude}"
#             )
#             response = xmltodict.parse(request.content)
#             print_req_res(request,response)
#             assert response["response"]["status"] == "0"
#             assert response["response"]["errno"] == None

#             try:
#                 connection = cx_Oracle.connect(
#                     connUsername,
#                     connPassword,
#                     cx_Oracle.makedsn(connHost, connPort, connSID),
#                 )
#                 cur = connection.cursor()
#                 cur.execute(
#                     f"select (ADDRESS) from LOCATIONBOX.LBS_POI_ATTRIBUTE where where POINT_ID= '{id2}' and ATTRIBUTE='EVREN_TEST_{tarih}'"
#                 )
#                 for row in cur.fetchall():
#                     sonuc = (
#                         str(row)
#                         .replace("(", "")
#                         .replace(")", "")
#                         .replace(",", "")
#                         .replace("'", "")
#                     )
#                     assert address == sonuc
#                 cur.close()
#             except cx_Oracle.Error as error:
#                 print(error)
#             finally:
#                 # release the connection
#                 if connection:
#                     connection.close()


@pytest.mark.userdata
@pytest.mark.point
def test_Add_User_Points():
    cmd = "AddUserPoints"

    dataJSON = """
    {
 "userpoints": [
  {
   "id": "1",
   "name": "Ada Apartman?",
   "type": 0,
   "address": "",
   "telno": "",
   "faxno": "",
   "string1": "StringValue",
   "string2": "3,4,5,6",
   "string3": "1,7,12",
   "string4": "",
   "string5": "",
   "string6": "",
   "string7": "",
   "string8": "",
   "string9": "",
   "number1": 4,
   "number2": 3,
   "number3": 0,
   "number4": 0,
   "number5": 0,
   "number6": 0,
   "number7": 0,
   "number8": 0,
   "number9": 0,
   "latitude": 40.9686,
   "longitude": 29.1005,
   "angle": 0
  },
  {
   "id": "2",
   "name": "Ada Apartman?",
   "type": 0,
   "address": "",
   "telno": "",
   "faxno": "",
   "string1": "StringValue",
   "string2": "3,4,5,6",
   "string3": "1,7,12",
   "string4": "",
   "string5": "",
   "string6": "",
   "string7": "",
   "string8": "",
   "string9": "",
   "number1": 4,
   "number2": 3,
   "number3": 0,
   "number4": 0,
   "number5": 0,
   "number6": 0,
   "number7": 0,
   "number8": 0,
   "number9": 0,
   "latitude": 40.9686,
   "longitude": 29.1005,
   "angle": 0
  }
 ]
} """
    dataXML = '<?xml version="1.0"?><userpoints><userpoint><id>1</id><name>Ada Apartman?</name><type>0</type><address>Kadikoy</address><telno>02163620500</telno><faxno>02163620500</faxno><string1>StringValue</string1><string2>StringValue</string2><string3>StringValue</string3><string4>StringValue</string4><string5>StringValue</string5><string6>StringValue</string6><string7>StringValue</string7><string8>StringValue</string8><string9>StringValue</string9><number1>4</number1><number2>3</number2><number3>0</number3><number4>0</number4><number5>0</number5><number6>0</number6><number7>0</number7><number8>0</number8><number9>0</number9><latitude>40.9686</latitude><longitude>29.1005</longitude><angle>0.0</angle></userpoint><userpoint><id>2</id><name>Ada Apartman?</name><type>0</type><address>Kadikoy</address><telno>02163620500</telno><faxno>02163620500</faxno><string1>StringValue</string1><string2>StringValue</string2><string3>StringValue</string3><string4>StringValue</string4><string5>StringValue</string5><string6>StringValue</string6><string7>StringValue</string7><string8>StringValue</string8><string9>StringValue</string9><number1>4</number1><number2>3</number2><number3>0</number3><number4>0</number4><number5>0</number5><number6>0</number6><number7>0</number7><number8>0</number8><number9>0</number9><latitude>40.9686</latitude><longitude>29.1005</longitude><angle>0.0</angle></userpoint></userpoints>'

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&DataType=JSON&Data={dataJSON}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&DataType=XML&Data={dataXML}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.point
def test_Get_User_Point():
    cmd = "GetUserPoint"

    pointID = "1"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={pointID}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={pointID}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


# @pytest.mark.userdata
# @pytest.mark.point
# def test_Remove_User_Point():
#     cmd = "RemoveUserPoint"

#     pointID = "987654321"
#     pointID2 = "9876543212"

#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={pointID}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0
#         elif type == "XML":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={pointID2}"
#             )
#             response = xmltodict.parse(request.content)
#             print_req_res(request,response)
#             assert response["response"]["status"] == "0"
#             assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.point
@pytest.mark.skipif(environment=="3", reason="Postgre method not supported")
@pytest.mark.skipif(environment=="4", reason="Postgre method not supported")

def test_User_Point_List():
    cmd = "UserPointList"

    regionID = "987654321"
    detailed = "5"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&RegionID={regionID}&Detailed={detailed}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&RegionID={regionID}&Detailed={detailed}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.point
def test_User_Point_List_With_Extent():
    cmd = "UserPointListWithExtent"

    count = "5"
    minLatitude = "39.357822"
    minlongitude = "28.521057"
    maxLatitude = "41.327673"
    maxLongitude = "30.034842"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Count={count}&MinLatitude={minLatitude}&minLongitude={minlongitude}&MaxLatitude={maxLatitude}&MaxLongitude={maxLongitude}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0
        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Count={count}&MinLatitude={minLatitude}&minLongitude={minlongitude}&MaxLatitude={maxLatitude}&MaxLongitude={maxLongitude}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.region
def test_Add_User_Region():
    cmd = "AddUserRegion"

    id = "987654321"
    id2 = "9876543212"
    name = "evren-test-region"
    type1 = "4"
    coors = "29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0792,40.9631,29.0606,40.9889"
    tarih = date.today()

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Name={name}&Type={type1}&Coors={coors}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id2}&Name={name}&Type={type1}&Coors={coors}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.region
def test_Add_User_Regions():
    cmd = "AddUserRegions"

    dataJSON = """
    {"userregions": [
    {
      "id": "1",
      "name": "NameOfRegion",
      "type": 99,
      "string1": "",
      "string2": "",
      "string3": "",
      "string4": "",
      "string5": "",
      "string6": "",
      "string7": "",
      "string8": "",
      "string9": "",
      "number1": 0,
      "number2": 0,
      "number3": 0,
      "number4": 0,
      "number5": 0,
      "number6": 0,
      "number7": 0,
      "number8": 0,
      "number9": 0,
      "coors": "29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0792,40.9631,29.0606,40.9889"
    },
    {
      "id": "2",
      "name": "NameOfRegion",
      "type": 99,
      "string1": "",
      "string2": "",
      "string3": "",
      "string4": "",
      "string5": "",
      "string6": "",
      "string7": "",
      "string8": "",
      "string9": "",
      "number1": 0,
      "number2": 0,
      "number3": 0,
      "number4": 0,
      "number5": 0,
      "number6": 0,
      "number7": 0,
      "number8": 0,
      "number9": 0,
      "coors": "29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0792,40.9631,29.0606,40.9889"
    }
  ]
}"""
    dataXML = """<?xml version="1.0"?>
<userregions>
 <userregion>
  <id>1</id>
  <name>NameOfLine</name>
  <type>0</type>
  <coors>29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0606,40.9889</coors>
  <string1>StringValue</string1>
  <string2>StringValue</string2>
  <string3>StringValue</string3>
  <string4>StringValue</string4>
  <string5>StringValue</string5>
  <string6>StringValue</string6>
  <string7>StringValue</string7>
  <string8>StringValue</string8>
  <string9>StringValue</string9>
  <number1>4</number1>
  <number2>3</number2>
  <number3>0</number3>
  <number4>0</number4>
  <number5>0</number5>
  <number6>0</number6>
  <number7>0</number7>
  <number8>0</number8>
  <number9>0</number9>
 </userregion>
 <userregion>
  <id>2</id>
  <name>NameOfLine</name>
  <type>0</type>
  <coors>29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0606,40.9889</coors>
  <string1>StringValue</string1>
  <string2>StringValue</string2>
  <string3>StringValue</string3>
  <string4>StringValue</string4>
  <string5>StringValue</string5>
  <string6>StringValue</string6>
  <string7>StringValue</string7>
  <string8>StringValue</string8>
  <string9>StringValue</string9>
  <number1>4</number1>
  <number2>3</number2>
  <number3>0</number3>
  <number4>0</number4>
  <number5>0</number5>
  <number6>0</number6>
  <number7>0</number7>
  <number8>0</number8>
  <number9>0</number9>
 </userregion>
</userregions>"""

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&DataType=JSON&Data={dataJSON}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&DataType=XML&Data={dataXML}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.region
def test_Add_User_Region_By_Union():
    cmd = "AddUserRegionByUnion"
    id = "987654321"
    name = "evren-test-region"
    type1 = "4"
    coors = "29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0792,40.9631,29.0606,40.9889"
    idList = "177681,177682"
    fromType = "ILCE"
    tarih = date.today()

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Name={name}&Type={type1}&Coors={coors}&IdList={idList}&FromType={fromType}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Name={name}&Type={type1}&Coors={coors}&IdList={idList}&FromType={fromType}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.region
def test_Get_User_Region():
    cmd = "GetUserRegion"

    id = "987654321"
    withCoors = "coordinates"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&WithCoors={withCoors}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&WithCoors={withCoors}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.region
def test_Remove_User_Region():
    cmd = "RemoveUserRegion"

    id = "987654321"
    id2 = "9876543212"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id2}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.region
def test_User_Region_List():
    cmd = "UserRegionList"

    whereClause = ""
    detailed = "5"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&WhereClause={whereClause}&Detailed={detailed}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&WhereClause={whereClause}&Detailed={detailed}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.line
def test_Add_User_Line():
    cmd = "AddUserLine"

    id = "987654321"
    id2 = "9876543212"

    name = "evren-test-line"
    type1 = "4"
    coors = "29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0792,40.9631"
    tarih = date.today()

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Name={name}&Type={type1}&Coors={coors}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id2}&Name={name}&Type={type1}&Coors={coors}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.line
def test_Add_User_Lines():
    cmd = "AddUserLines"

    dataJSON = """
    {"userlines": [
    {
      "id": "1",
      "name": "NameOfLine",
      "type": 99,
      "string1": "",
      "string2": "",
      "string3": "",
      "string4": "",
      "string5": "",
      "string6": "",
      "string7": "",
      "string8": "",
      "string9": "",
      "number1": 0,
      "number2": 0,
      "number3": 0,
      "number4": 0,
      "number5": 0,
      "number6": 0,
      "number7": 0,
      "number8": 0,
      "number9": 0,
      "coors": "29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0792,40.9631"
    },
    {
      "id": "2",
      "name": "NameOfLine",
      "type": 99,
      "string1": "",
      "string2": "",
      "string3": "",
      "string4": "",
      "string5": "",
      "string6": "",
      "string7": "",
      "string8": "",
      "string9": "",
      "number1": 0,
      "number2": 0,
      "number3": 0,
      "number4": 0,
      "number5": 0,
      "number6": 0,
      "number7": 0,
      "number8": 0,
      "number9": 0,
      "coors": "29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0792,40.9631"
    }
  ]
}"""
    dataXML = """<?xml version="1.0"?>
<userlines>
 <userline>
  <id>1</id>
  <name>NameOfLine</name>
  <type>0</type>
  <coors>29.0606,40.9889,29.1609,40.9858,29.1624,40.9453</coors>
  <string1>StringValue</string1>
  <string2>StringValue</string2>
  <string3>StringValue</string3>
  <string4>StringValue</string4>
  <string5>StringValue</string5>
  <string6>StringValue</string6>
  <string7>StringValue</string7>
  <string8>StringValue</string8>
  <string9>StringValue</string9>
  <number1>4</number1>
  <number2>3</number2>
  <number3>0</number3>
  <number4>0</number4>
  <number5>0</number5>
  <number6>0</number6>
  <number7>0</number7>
  <number8>0</number8>
  <number9>0</number9>
 </userline>
 <userline>
  <id>2</id>
  <name>NameOfLine</name>
  <type>0</type>
  <coors>29.0606,40.9889,29.1609,40.9858,29.1624,40.9453</coors>
  <string1>StringValue</string1>
  <string2>StringValue</string2>
  <string3>StringValue</string3>
  <string4>StringValue</string4>
  <string5>StringValue</string5>
  <string6>StringValue</string6>
  <string7>StringValue</string7>
  <string8>StringValue</string8>
  <string9>StringValue</string9>
  <number1>4</number1>
  <number2>3</number2>
  <number3>0</number3>
  <number4>0</number4>
  <number5>0</number5>
  <number6>0</number6>
  <number7>0</number7>
  <number8>0</number8>
  <number9>0</number9>
 </userline>
</userlines>"""

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&DataType=JSON&Data={dataJSON}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&DataType=XML&Data={dataXML}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.line
def test_Get_User_Line():
    cmd = "GetUserLine"

    id = "987654321"
    withCoors = "coordinates"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&WithCoors={withCoors}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&WithCoors={withCoors}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.line
def test_Remove_User_Line():
    cmd = "RemoveUserLine"

    id = "987654321"
    id2 = "9876543212"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id2}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.userdata
@pytest.mark.line
def test_User_Line_List():
    cmd = "UserLineList"

    whereClause = ""
    detailed = "5"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&WhereClause={whereClause}&Detailed={detailed}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&WhereClause={whereClause}&Detailed={detailed}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


# RISK SCORE


# RISK SCORE


@pytest.mark.risk
@pytest.mark.earthquakeinfo
def test_Get_Earthquake_Info():
    cmd = "GetEarthquakeInfo"

    latitude = "40.57"
    longitude = "29.13"
    radius = "20000"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Radius={radius}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}&Radius={radius}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.analysis
@pytest.mark.spatialanalysis
@pytest.mark.xfail(reason="type some reason")
def test_Spatial_Analysis():
    cmd = "SpatialAnalysis"

    type1 = "Interact"
    targetLayer = "Poi"
    targetBrand = "BIMEKS"
    searchLayer = "Poi"
    searchCategory = "BANKA"
    searchDistance = "1000"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Type={type1}&TargetLayer={targetLayer}&TargetBrand={targetBrand}&SearchLayer={searchLayer}&SearchCategory={searchCategory}&SearchDistance={searchDistance}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Type={type1}&TargetLayer={targetLayer}&TargetBrand={targetBrand}&SearchLayer={searchLayer}&SearchCategory={searchCategory}&SearchDistance={searchDistance}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None

# 13.11.2023 Oracle dev ortamında çalışmıyor
# @pytest.mark.analysis
# @pytest.mark.addservicearea
# def test_Add_Service_Area_To_User_Region():
#     cmd = "AddServiceAreaToUserRegion"

#     regionName = "evrenServiceArea-Test"
#     latitude = "40.95154"
#     longitude = "29.06991"
#     networkType = "3"
#     distance = "2000"

#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&RegionName={regionName}&Latitude={latitude}&Longitude={longitude}&NetworkType={networkType}&Distance={distance}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0

#         elif type == "XML":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&RegionName={regionName}&Latitude={latitude}&Longitude={longitude}&NetworkType={networkType}&Distance={distance}"
#             )
#             response = xmltodict.parse(request.content)
#             print_req_res(request,response)
#             assert response["response"]["status"] == "0"
#             assert response["response"]["errno"] == None


# @pytest.mark.analysis
# @pytest.mark.addbufferedlinetouserregion
# def test_Add_Buffered_Line_To_User_Region():
#     cmd = "AddBufferedLineToUserRegion"

#     id = "987654321"
#     name = "test-buffered-line"
#     coors = "29.0606,40.9889,29.1609,40.9858,29.1624,40.9453,29.0792,40.9631,29.0606,40.9889"
#     bufferDist = 200
#     string1 = "www.infotech.com.tr"
#     string2 = "kurumsal@infotech.com.tr"
#     number1 = 2
#     number2 = 1

#     for type in typ:
#         if type == "JSON":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Name={name}&Coors={coors}&BufferDist={bufferDist}&String1={string1}&String2={string2}&Number1={number1}&Number2={number2}"
#             )
#             response = request.json()
#             print_req_res(request,response)
#             for keys, value in response.items():
#                 assert keys != "errno"
#             assert response["status"] == 0

#         elif type == "XML":
#             request = requests.get(
#                 f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Name={name}&Coors={coors}&BufferDist={bufferDist}&String1={string1}&String2={string2}&Number1={number1}&Number2={number2}"
#             )
#             response = xmltodict.parse(request.content)
#             print_req_res(request,response)
#             assert response["response"]["status"] == "0"
#             assert response["response"]["errno"] == None


@pytest.mark.analysis
@pytest.mark.addbufferedroutetouserregion
@pytest.mark.xfail(reason="type some reason")
def test_Add_Buffered_Route_To_User_Region():
    cmd = "AddBufferedRouteToUserRegion"

    id = "12"
    name = "Rota1-test"
    pathId = "7851655"
    bufferDist = "200"
    string1 = "www.infotech.com.tr"
    string2 = "kurumsal@infotech.com.tr"
    number1 = "1"
    number2 = "2"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Name={name}&PathId={pathId}&BufferDist={bufferDist}&String1={string1}&String2={string2}&Number1={number1}&Number2={number2}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Name={name}&PathId={pathId}&BufferDist={bufferDist}&String1={string1}&String2={string2}&Number1={number1}&Number2={number2}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.analysis
@pytest.mark.addroutetouserregion
@pytest.mark.xfail(reason="type some reason")
def test_Add_Route_To_User_Line():
    cmd = "AddRouteToUserLine"

    id = "6"
    pathId = "446275"


    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&PathId={pathId}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&PathId={pathId}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.tmc
def test_TMC_Hat_Info():
    cmd = "TMCHatInfo"

    tmcKod = "41"
    zoomLevel = "6"
    geometry = "1"
    encode = "0"
    SRID = "8307"
    reverse = "0"

    for type in typ:
        if type == "JSON":
            if (environment=="3" or environment=="4"):
                request = requests.get(
                    f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&TmcKod={tmcKod}"
                )
            else:
                request = requests.get(
                    f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&TmcKod={tmcKod}&ZoomLevel={zoomLevel}&Geometry={geometry}&Encode={encode}&SRID={SRID}&Reverse={reverse}"
                )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            if (environment=="3" or environment=="4"):
                request = requests.get(
                        f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&TmcKod={tmcKod}"
                    )
            else:
                request = requests.get(
                    f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&TmcKod={tmcKod}&ZoomLevel={zoomLevel}&Geometry={geometry}&Encode={encode}&SRID={SRID}&Reverse={reverse}"
                )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.tmc
def test_TMC_Hat_List_With_Extend():
    cmd = "TMCHatListWithExtent"

    minLatitude = "37.65940398"
    minLongitude = "31.23677412"
    maxLatitude = "39.31071399"
    maxLongitude = "33.444854"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minLatitude}&MinLongitude={minLongitude}&MaxLatitude={maxLatitude}&MaxLongitude={maxLongitude}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&MinLatitude={minLatitude}&MinLongitude={minLongitude}&MaxLatitude={maxLatitude}&MaxLongitude={maxLongitude}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.tmc
def test_TMC_Hat_Search():
    cmd = "TMCHatSearch"

    latitude = "41.1"
    longitude = "29.1"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Latitude={latitude}&Longitude={longitude}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None


@pytest.mark.tmc
@pytest.mark.tmctrafficflow
def test_Traffic_TMC_Flow_Data():
    cmd = "TrafficTmcFlowData"

    tmcKodList = "40,41"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&TmcKodList={tmcKodList}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&TmcKodList={tmcKodList}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None

##Postgre Prod ortamda tablolar yok 14 12 2023
@pytest.mark.feedback
def test_Add_Feedback():
    cmd = "BBolumFeedback"
    if (environment=="3" or environment=="4"):
        id="10001"
    else:
        id = "1"
    bBolumUavt = "2554938874"
    address = "Boğaziçi mah. Yazlık siteler sok. no:25/41E Milas Muğla"
    adbVersion = "ADRES_DATABASE_V23Q3"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Address={address}&AdbVersion={adbVersion}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}&Address={address}&AdbVersion={adbVersion}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None

##Postgre Prod ortamda tablolar yok 14 12 2023

@pytest.mark.feedback
def test_Get_Feedback():
    cmd = "BBolumFeedback"

    if (environment=="3" or environment=="4"):
        id="10001"
    else:
        id = "1"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None

##Postgre Prod ortamda tablolar yok 14 12 2023

@pytest.mark.feedback
def test_List_Feedback():
    cmd = "ListFeedback"

    id = "987654321"

    for type in typ:
        if type == "JSON":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}"
            )
            response = request.json()
            print_req_res(request,response)
            for keys, value in response.items():
                assert keys != "errno"
            assert response["status"] == 0

        elif type == "XML":
            request = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ={type}&Id={id}"
            )
            response = xmltodict.parse(request.content)
            print_req_res(request,response)
            assert response["response"]["status"] == "0"
            assert response["response"]["errno"] == None

lbsKey2 = os.getenv("LBSKEY2")

def test_Get_Risk_Skor():
    cmd = "GetRiskSkor"

    for type in typ:
        if type == "JSON":
            request0 = requests.get(
                f"{baseURL}Key={lbsKey2}&Cmd={cmd}&Typ=JSON&TeminatTuru=2&Latitude=39.390874635463064&Longitude=42.75836917943332&AdresSeviyesi=6&Beyan1=1&Beyan2=2"
            )
            response0 = request0.json()
            for keys, value in response0.items():
                assert keys != "errno"

            assert response0["status"] == 0
            assert response0["beyan1"] == 5
            assert response0["beyan2"] == 15

            request1 = requests.get(
                f"{baseURL}Key={lbsKey2}&Cmd={cmd}&Typ=JSON&TeminatTuru=2&Latitude=39.390874635463064&Longitude=42.75836917943332&AdresSeviyesi=6&Beyan1=2&Beyan2=5"
            )
            response1 = request1.json()
            for keys, value in response1.items():
                assert keys != "errno"


            assert response1["status"] == 0
            assert response1["beyan1"] == 10
            assert response1["beyan2"] == 3.75
        elif type == "XML":
            request0 = requests.get(
                f"{baseURL}Key={lbsKey2}&Cmd={cmd}&Typ=XML&TeminatTuru=2&Latitude=39.390874635463064&Longitude=42.75836917943332&AdresSeviyesi=6&Beyan1=1&Beyan2=2"
            )
            response0 = xmltodict.parse(request0.content)
            assert response0["response"]["status"] == "0"
            assert response0["response"]["beyan1"] == "5.0"
            assert response0["response"]["beyan2"] == "15.0"

            request1 = requests.get(
                f"{baseURL}Key={lbsKey2}&Cmd={cmd}&Typ=XML&TeminatTuru=2&Latitude=39.390874635463064&Longitude=42.75836917943332&AdresSeviyesi=6&Beyan1=2&Beyan2=5"
            )
            response1 = xmltodict.parse(request1.content)



            assert response1["response"]["status"] == "0"
            assert response1["response"]["beyan1"] == "10.0"
            assert response1["response"]["beyan2"] == "3.75"



def test_Get_Risk_Value():
    cmd = "GetRiskValue"
    address1 = "Gölyazı Mah. 62615. Sokak 42855 Cihanbeyli Konya"
    address2 = "Cumhuriyet Mah. Atatürk Bulvarı No: 75 D: 67 06420 Çankaya Ankaraa"
    for type in typ:
        if type == "JSON":
            request0 = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&Address={address1}"
            )
            response0 = request0.json()
            print_req_res(request0,response0)
            for keys, value in response0.items():
                assert keys != "errno"
            assert response0["status"] == 0
            assert response0["riverFlood_riskvalues"][0]["value"] == 8


            request1 = requests.get(
                f"{baseURL}Key={lbsKey}&Cmd={cmd}&Typ=JSON&Address={address2}"
            )
            response1 = request1.json()
            print_req_res(request1,response1)
            for keys, value in response0.items():
                assert keys != "errno"
            assert response1["status"] == 0
            assert response1["surfaceFlood_riskvalues"][0]["minvalue"] == 5
