import mysql.connector as s1
from datetime import date
from datetime import datetime
import random

def database():
    con1 = s1.connect(host="localhost", user="root", passwd="1234")
    cursor1 = con1.cursor()
    cursor1.execute("create database if not exists DOMESTIC_FLIGHT;")
    con1.commit()
    con1.close()

def traveldate():
    today = date.today()
    today2 = today.strftime("%d-%m-%Y")
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")
    fmonth = (int(month) + 5) % 12
    fyear = int(year) + (int(month) + 5) // 12
    if int(day) == 29 and int(fmonth) == 2 and (int(fyear) % 4) != 0:
        day = int(day) - 1
        fdate = str(fyear) + "-" + str(fmonth) + "-" + str(day)
    else:
        fdate = str(fyear) + "-" + str(fmonth) + "-" + str(day)
    fd = datetime.strptime(fdate, "%Y-%m-%d")
    fd2 = fd.strftime("%d-%m-%Y")
    end = fd.date()
    try:
        print("Enter the date between", today2, "and", fd2)
        enterdate = str(input("Enter the Date Of Travel in the format(DD-MM-YYYY): "))
        datelist = enterdate.split("-")
        usery = int(datelist[2])
        userm = int(datelist[1])
        userd = int(datelist[0])
        userdate = date(usery, userm, userd)
        while True:
            if len(datelist[2]) != 4:
                print("please enter a right year in the format YYYY")
                enterdate = str(input("Enter the Date Of Travel in the format(DD-MM-YYYY): "))
                datelist = enterdate.split("-")
                usery = int(datelist[2])
                userm = int(datelist[1])
                userd = int(datelist[0])
                userdate = date(usery, userm, userd)
                continue
            elif len(datelist[2]) == 4 and today <= userdate <= end:
                # another function for user details comees in this
                break
            else:
                print("PLEASE ENTER THE DATE BETWEEN", today2, "AND", fd2)
                enterdate = str(input("Enter the Date Of Travel in the format(DD-MM-YYYY): "))
                datelist = enterdate.split("-")
                usery = int(datelist[2])
                userm = int(datelist[1])
                userd = int(datelist[0])
                userdate = date(usery, userm, userd)
                continue
    except:
        print("PLEASE ENTER THE DATE IN THE SPECIFIED FORMAT DD-MM-YYYY AND THE CORRECT RANGE")
        userdate = traveldate()
    return userdate


def flightlist(usertablename):
    con1 = s1.connect(host="localhost", user="root", passwd="1234", database="DOMESTIC_FLIGHT")
    cursor1 = con1.cursor()
    q = "create table if not exists " + usertablename + """(flightno varchar(25) NOT NULL Primary Key , cityfrom varchar(25) NOT NULL , cityto varchar(25) NOT NULL , flightdate date NOT NULL , estmd_travelling_time varchar(25) NOT NULL ,airlinename varchar(25) NOT NULL ,depttime varchar(25) NOT NULL , arrivaltime varchar(25) NOT NULL , gateno int NOT NULL check(gateno between 1 and 12) , dt varchar(30) NOT NULL , at varchar(30) NOT NULL);"""
    cursor1.execute(q)
    con1.commit()
    con1.close()

def flightno():
    import random
    a = random.randint(1, 6)
    b = random.randint(100, 9999)
    airline = ["6E", "SG", "9W", "AI", "UK", "G8"]
    c = airline[a - 1]
    flightnum = c + str(b)
    airlines = ["Indigo", "SpiceJet", "Jet Airways", "Air India", "Vistara", "Go Air"]
    airline = airlines[a - 1]
    return flightnum , airline

def fromtoanddeptarrivalestmd(userdate):
    import random
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    cities = ["SRINAGAR", "SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "NOIDA", "GAYA", "INDORE", "DELHI",
              "AHMEDABAD", "RAIPUR", "RANCHI", "KOLKATA", "PAKYONG",
              "BHUBANESWAR", "MUMBAI", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI", "TEZU",
              "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR",
              "LENGPUI"]
    if a != b:
        ffrom = cities[a - 1]
        tto = cities[b - 1]
    elif a == b:
        a = b - 1
        ffrom = cities[a - 1]
        tto = cities[b - 1]
    import random
    from datetime import timedelta
    import datetime
    now = datetime.datetime.now()

    currrenttime = now.strftime("%Y-%m-%d")
    currenttimelst = currrenttime.split("-")

    timeranh1 = random.randint(0, 23)
    timeranm1 = random.randint(0, 59)
    timestr = str(timeranh1) + ":" + str(timeranm1)

    times1 = datetime.datetime.strptime(timestr, "%H:%M")
    times2 = times1.strftime("%H:%M %p")

    h = times1.strftime("%H")
    m = times1.strftime("%M")
    timeh = int(h)
    timem = int(m)
    ranval1 = 23 - timeh
    ranval2 = 59 - timem

    if ranval1 < 2:
        ranh = random.randint(2, 3)
        ranm = random.randint(0, ranval2)
    else:
        ranh = random.randint(2, ranval1)
        ranm = random.randint(0, ranval2)

    dt = times1 + timedelta(hours=ranh, minutes=ranm)  # dept time in type datetime()

    cities = ["SRINAGAR", "SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "NOIDA", "GAYA", "INDORE", "DELHI",
              "AHMEDABAD", "RAIPUR", "RANCHI", "KOLKATA", "PAKYONG",
              "BHUBANESWAR", "MUMBAI", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI", "TEZU",
              "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR",
              "LENGPUI"]

    # 1 JAMMU AND KASHMIR (SRINAGAR)
    jandkc = ["SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "DELHI"]
    jandkm = ["JAIPUR", "NOIDA", "PAKYONG"]
    jandkf = ["GAYA", "INDORE", "AHMEDABAD", "RAIPUR", "RANCHI", "KOLKATA", "BHUBANESWAR", "MUMBAI", "GOA",
              "HYDERABAD", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA",
              "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 2  HIMACHAL PRADESH (SHIMLA)
    himachalc = ["CHANDIGARH", "PANTNAGAR", "NOIDA", "JAIPUR", "AMRITSAR", "SRINAGAR", "DELHI"]
    himachalm = ["AHMEDABAD", "INDORE", "RANCHI", "RAIPUR", "GAYA"]
    himachalf = ["KOLKATA", "PAKYONG", "BHUBANESWAR", "MUMBAI", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU",
                 "KOCHI",
                 "CHENNAI", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    #  3 PUNJAB (AMRITSAR)
    punjabc = ["SHIMLA", "PANTNAGAR", "CHANDIGARH", "NOIDA", "JAIPUR", "AHMEDABAD", "INDORE", "SRINAGAR",
               "DELHI"]
    punjabm = ["RAIPUR", "RANCHI", "KOLKATA", "PAKYONG", "GAYA"]
    punjabf = ["BHUBANESWAR", "MUMBAI", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI", "TEZU",
               "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 4 UTTARAKHAND (PANTNAGAR)
    uttarakhandc = ["SHIMLA", "AMRITSAR", "CHANDIGARH", "NOIDA", "JAIPUR", "GAYA", "PAKYONG", "SRINAGAR", "DELHI"]
    uttarakhandm = ["INDORE", "AHMEDABAD", "RAIPUR", "RANCHI", "KOLKATA"]
    uttarakhandf = ["BHUBANESWAR", "MUMBAI", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI",
                    "TEZU",
                    "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 5  HARYANA (CHANDIGARH)
    haryanac = ["SHIMLA", "AMRITSAR", "PANTNAGAR", "JAIPUR", "NOIDA", "GAYA", "INDORE", "AHMEDABAD", "SRINAGAR",
                "DELHI"]
    haryanam = ["RAIPUR", "RANCHI", "KOLKATA", "PAKYONG", "MUMBAI"]
    haryanaf = ["BHUBANESWAR", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI", "TEZU",
                "GUWAHATI",
                "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 6 RAJASTHAN (JAIPUR)
    rajasthanc = ["SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "NOIDA", "GAYA", "INDORE", "AHMEDABAD", "MUMBAI",
                  "DELHI"]
    rajasthanm = ["RAIPUR", "RANCHI", "KOLKATA", "PAKYONG", "SRINAGAR"]
    rajasthanf = ["BHUBANESWAR", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI", "TEZU",
                  "GUWAHATI",
                  "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 7 UTTAR PRADESH (NOIDA)
    uttarc = ["SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "GAYA", "INDORE", "RAIPUR", "RANCHI",
              "KOLKATA",
              "PAKYONG", "DELHI", "SRINAGAR"]
    uttarm = ["AHMEDABAD", "BHUBANESWAR", "MUMBAI", "HYDERABAD", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL",
              "DIMAPUR", "LENGPUI"]
    uttarf = ["GOA", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI"]

    # 8 BIHAR (GAYA)
    biharc = ["TEZU", "GUWAHATI", "DIMAPUR", "IMPHAL", "LENGPUI", "AGARTALA", "SHILLONG", "PAKYONG", "KOLKATA",
              "RANCHI","SHIMLA", "SRINAGAR" ,
              "BHUBANESWAR", "NOIDA", "RAIPUR", "INDORE", "DELHI"]
    biharm = ["VISAKHAPATNAM", "HYDERABAD", "CHANDIGARH", "PANTNAGAR"]
    biharf = ["CHENNAI", "KOCHI", "BENGALURU", "MUMBAI", "GOA", "AHMEDABAD", "JAIPUR", "AMRITSAR", ]

    # 9 MADHYA PRADESH (INDORE)
    madhyac = ["SHIMLA", "AMRITSAR", "DELHI", "NOIDA", "CHANDIGARH", "GAYA", "PANTNAGAR", "AHMEDABAD", "MUMBAI",
               "RAIPUR",
               "RANCHI", "BHUBANESWAR", "GOA", "HYDERABAD", "JAIPUR"]
    madhyam = ["KOLKATA", "PAKYONG", "VISAKHAPATNAM", "BENGALURU"]
    madhyaf = ["KOCHI", "SRINAGAR", "CHENNAI", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR",
               "LENGPUI"]

    # 10 DELHI
    delhic = ["SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "GAYA", "INDORE", "RAIPUR", "RANCHI",
              "PAKYONG", "NOIDA", "SRINAGAR"]
    delhim = ["AHMEDABAD", "BHUBANESWAR", "MUMBAI", "HYDERABAD" , "KOLKATA"]
    delhif = ["GOA", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA",
              "IMPHAL",
              "DIMAPUR", "LENGPUI"]

    # 11 GUJRAT (AHMEDABAD)
    gujratc = ["JAIPUR", "INDORE", "RAIPUR", "MUMBAI", "GOA", "HYDERABAD", "NOIDA"]
    gujratm = ["AMRITSAR", "PANTNAGAR", "CHANDIGARH", "RANCHI", "VISAKHAPATNAM", "BENGALURU", "DELHI"]
    gujratf = ["SRINAGAR", "SHIMLA", "GAYA", "KOLKATA", "PAKYONG", "BHUBANESWAR", "KOCHI", "CHENNAI", "TEZU",
               "GUWAHATI",
               "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 12 CHATTISGARH (RAIPUR)
    chattisgarhc = ["NOIDA", "GAYA", "INDORE", "RANCHI", "KOLKATA", "BHUBANESWAR", "MUMBAI", "HYDERABAD",
                    "VISAKHAPATNAM"]
    chattisgarhm = ["CHANDIGARH", "JAIPUR", "AHMEDABAD", "PAKYONG", "GOA", "BENGALURU", ]
    chattisgarhf = ["DELHI", "SRINAGAR", "SHIMLA", "AMRITSAR", "PANTNAGAR", "KOCHI", "CHENNAI", "TEZU", "GUWAHATI",
                    "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 13 JHARKHAND (RANCHI)
    jharkhandc = ["NOIDA", "GAYA", "INDORE", "RAIPUR", "KOLKATA", "PAKYONG", "BHUBANESWAR", "SHILLONG", "AGARTALA"]
    jharkhandm = ["PANTNAGAR", "CHANDIGARH", "AHMEDABAD", "JAIPUR", "MUMBAI", "HYDERABAD", "TEZU", "GUWAHATI", "IMPHAL",
                  "DIMAPUR", "LENGPUI"]
    jharkhandf = ["DELHI", "SRINAGAR", "SHIMLA", "AMRITSAR", "GOA", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI"]

    # 14 WEST BENGAL (KOLKATA)
    bengalc = ["GAYA", "RAIPUR", "RANCHI", "PAKYONG", "BHUBANESWAR", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL",
               "DIMAPUR", "LENGPUI"]
    bengalm = ["NOIDA", "INDORE", "MUMBAI", "HYDERABAD", "TEZU"]
    bengalf = ["DELHI", "SRINAGAR", "SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "GOA", "AHMEDABAD",
               "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI"]

    # 15 SIKKIM (PAKYONG)
    sikkimc = ["TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI", "PANTNAGAR", "GAYA",
               "RANCHI",
               "KOLKATA"]
    sikkimm = ["SHIMLA", "AMRITSAR", "CHANDIGARH", "NOIDA", "INDORE", "RAIPUR", "BHUBANESWAR"]
    sikkimf = ["SRINAGAR", "DELHI", "JAIPUR", "AHMEDABAD", "MUMBAI", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU",
               "KOCHI", "CHENNAI"]

    # 16 ODISHA (BHUBANESHWAR)
    odishac = ["GAYA", "INDORE", "RAIPUR", "RANCHI", "KOLKATA", "HYDERABAD", "VISAKHAPATNAM"]
    odisham = ["NOIDA", "PAKYONG", "MUMBAI", "BENGALURU", "CHENNAI", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA",
               "IMPHAL",
               "DIMAPUR", "LENGPUI"]
    odishaf = ["DELHI", "SRINAGAR", "SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "AHMEDABAD", "GOA",
               "KOCHI"]

    # 17 MAHARASHTRA (MUMBAI)
    mahac = ["JAIPUR", "INDORE", "AHMEDABAD", "RAIPUR", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU"]
    maham = ["CHANDIGARH", "PANTNAGAR", "NOIDA", "RANCHI", "KOLKATA", "BHUBANESWAR", "KOCHI", "CHENNAI"]
    mahaf = ["DELHI", "SHIMLA", "AMRITSAR", "SRINAGAR", "GAYA", "PAKYONG", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA",
             "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 18 GOA
    goac = ["MUMBAI", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU", "KOCHI"]
    goam = ["INDORE", "AHMEDABAD", "RAIPUR", "JAIPUR", "CHENNAI"]
    goaf = ["DELHI", "SRINAGAR", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "SHIMLA", "NOIDA", "GAYA", "RANCHI", "KOLKATA",
            "PAKYONG", "BHUBANESWAR", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 19 TELANGANA (HYDERABAD)
    telanganac = ["INDORE", "RAIPUR", "RANCHI", "BHUBANESWAR", "MUMBAI", "GOA", "VISAKHAPATNAM", "BENGALURU"]
    telanganam = ["GAYA", "AHMEDABAD", "KOCHI", "CHENNAI"]
    telanganaf = ["DELHI", "SRINAGAR", "AMRITSAR", "SHIMLA", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "NOIDA", "KOLKATA",
                  "PAKYONG", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 20 ANDHRA PRADHESH (VISHAKAPATNAM)
    andhrac = ["RAIPUR", "BHUBANESWAR", "GOA", "MUMBAI", "HYDERABAD", "BENGALURU", "KOCHI", "CHENNAI"]
    andhram = ["INDORE", "RANCHI", "KOLKATA"]
    andhraf = ["DELHI", "SRINAGAR", "SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "NOIDA", "GAYA",
               "AHMEDABAD",
               "PAKYONG", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 21 KARNATAKA (BENGALURU)
    karnatakac = ["RAIPUR", "BHUBANESWAR", "GOA", "MUMBAI", "HYDERABAD", "VISAKHAPATNAM", "KOCHI", "CHENNAI"]
    karnatakam = ["INDORE", "RANCHI", "KOLKATA"]
    karnatakaf = ["DELHI", "SRINAGAR", "SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "NOIDA", "GAYA",
                  "AHMEDABAD", "PAKYONG", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI"]

    # 22 KERALA (KOCHI)
    keralac = ["BENGALURU", "CHENNAI", "VISAKHAPATNAM", "GOA", "HYDERABAD"]
    keralam = ["MUMBAI", "RAIPUR", "BHUBANESWAR"]
    keralaf = ["AHMEDABAD", "INDORE", "RANCHI", "KOLKATA", "GAYA", "JAIPUR", "PAKYONG", "NOIDA", "CHANDIGARH",
               "PANTNAGAR",
               "AMRITSAR", "SHIMLA", "SRINAGAR", "DELHI", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL",
               "DIMAPUR",
               "LENGPUI"]

    # 23 TAMIL NADU (CHENNAI)
    tamilc = ["BENGALURU", "KOCHI", "VISAKHAPATNAM", "GOA", "HYDERABAD"]
    tamilm = ["MUMBAI", "RAIPUR", "BHUBANESWAR"]
    tamilf = ["AHMEDABAD", "INDORE", "RANCHI", "KOLKATA", "GAYA", "JAIPUR", "PAKYONG", "NOIDA", "CHANDIGARH",
              "PANTNAGAR",
              "AMRITSAR", "SHIMLA", "SRINAGAR", "DELHI", "TEZU", "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL",
              "DIMAPUR",
              "LENGPUI"]

    # 24 ARUNACHAL PRADESH (TEZU)
    arunachalc = ["GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI", "PAKYONG", "KOLKATA", "GAYA",
                  "RANCHI",
                  "BHUBANESWAR"]
    arunachalm = ["NOIDA", "RAIPUR", "INDORE", "VISAKHAPATNAM", "HYDERABAD", "DELHI", "CHANDIGARH", "PANTNAGAR"]
    arunachalf = ["CHENNAI", "KOCHI", "BENGALURU", "MUMBAI", "GOA", "AHMEDABAD", "JAIPUR", "AMRITSAR", "SHIMLA",
                  "SRINAGAR"]

    # 25 ASSAM (GUWAHATI)
    assamc = ["TEZU", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI", "PAKYONG", "KOLKATA", "GAYA", "RANCHI",
              "BHUBANESWAR"]
    assamm = ["NOIDA", "RAIPUR", "INDORE", "VISAKHAPATNAM", "HYDERABAD", "DELHI", "CHANDIGARH", "PANTNAGAR"]
    assamf = ["CHENNAI", "KOCHI", "BENGALURU", "MUMBAI", "GOA", "AHMEDABAD", "JAIPUR", "AMRITSAR", "SHIMLA", "SRINAGAR"]

    # 26 MEGHALAYA (SHILLONG)
    meghalayac = ["TEZU", "GUWAHATI", "AGARTALA", "IMPHAL", "DIMAPUR", "LENGPUI", "PAKYONG", "KOLKATA", "GAYA",
                  "RANCHI",
                  "BHUBANESWAR"]
    meghalayam = ["NOIDA", "RAIPUR", "INDORE", "VISAKHAPATNAM", "HYDERABAD", "DELHI", "CHANDIGARH", "PANTNAGAR"]
    meghalayaf = ["CHENNAI", "KOCHI", "BENGALURU", "MUMBAI", "GOA", "AHMEDABAD", "JAIPUR", "AMRITSAR", "SHIMLA",
                  "SRINAGAR"]

    # 27 TRIPURA (AGARTALA)
    tripurac = ["TEZU", "SHILLONG", "GUWAHATI", "IMPHAL", "DIMAPUR", "LENGPUI", "PAKYONG", "KOLKATA", "GAYA", "RANCHI",
                "BHUBANESWAR"]
    tripuram = ["NOIDA", "RAIPUR", "INDORE", "VISAKHAPATNAM", "HYDERABAD", "DELHI", "CHANDIGARH", "PANTNAGAR"]
    tripuraf = ["CHENNAI", "KOCHI", "BENGALURU", "MUMBAI", "GOA", "AHMEDABAD", "JAIPUR", "AMRITSAR", "SHIMLA",
                "SRINAGAR"]

    # 28 MANIPUR (IMPHAL)
    manipurc = ["TEZU", "SHILLONG", "GUWAHATI", "AGARTALA", "DIMAPUR", "LENGPUI", "PAKYONG", "KOLKATA", "GAYA", "RANCHI",
                "BHUBANESWAR"]
    manipurm = ["NOIDA", "RAIPUR", "INDORE", "VISAKHAPATNAM", "HYDERABAD", "DELHI", "CHANDIGARH", "PANTNAGAR"]
    manipurf = ["CHENNAI", "KOCHI", "BENGALURU", "MUMBAI", "GOA", "AHMEDABAD", "JAIPUR", "AMRITSAR", "SHIMLA",
                "SRINAGAR"]

    # 29 NAGALAND (DIMAPUR)
    nagalandc = ["TEZU", "SHILLONG", "AGARTALA", "IMPHAL", "GUWAHATI", "LENGPUI", "PAKYONG", "KOLKATA", "GAYA", "RANCHI",
                 "BHUBANESWAR"]
    nagalandm = ["NOIDA", "RAIPUR", "INDORE", "VISAKHAPATNAM", "HYDERABAD", "DELHI", "CHANDIGARH", "PANTNAGAR"]
    nagalandf = ["CHENNAI", "KOCHI", "BENGALURU", "MUMBAI", "GOA", "AHMEDABAD", "JAIPUR", "AMRITSAR", "SHIMLA",
                 "SRINAGAR"]

    # 30 MIZORAM (LENGPUI)
    mizoramc = ["TEZU", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR", "GUWAHATI", "PAKYONG", "KOLKATA", "GAYA", "RANCHI",
                "BHUBANESWAR"]
    mizoramm = ["NOIDA", "RAIPUR", "INDORE", "VISAKHAPATNAM", "HYDERABAD", "DELHI", "CHANDIGARH", "PANTNAGAR"]
    mizoramf = ["CHENNAI", "KOCHI", "BENGALURU", "MUMBAI", "GOA", "AHMEDABAD", "JAIPUR", "AMRITSAR", "SHIMLA",
                "SRINAGAR"]

    closecity = [jandkc, himachalc, punjabc, uttarakhandc, haryanac, rajasthanc, uttarc, biharc, madhyac, delhic,
                 gujratc, chattisgarhc, jharkhandc, bengalc,
                 sikkimc, odishac, mahac, goac, telanganac, andhrac, karnatakac, keralac, tamilc, arunachalc, assamc,
                 meghalayac, tripurac, manipurc, nagalandc,
                 mizoramc]

    midcity = [jandkm, himachalm, punjabm, uttarakhandm, haryanam, rajasthanm, uttarm, biharm, madhyam, delhim, gujratm,
               chattisgarhm, jharkhandm, bengalm,
               sikkimm, odisham, maham, goam, telanganam, andhram, karnatakam, keralam, tamilm, arunachalm, assamm,
               meghalayam, tripuram, manipurm, nagalandm,
               mizoramm]

    farcity = [jandkf, himachalf, punjabf, uttarakhandf, haryanaf, rajasthanf, uttarf, biharf, madhyaf, delhif, gujratf,
               chattisgarhf, jharkhandf, bengalf,
               sikkimf, odishaf, mahaf, goaf, telanganaf, andhraf, karnatakaf, keralaf, tamilf, arunachalf, assamf,
               meghalayaf, tripuraf, manipurf, nagalandf,
               mizoramf]

    if ffrom == cities[0]:
        if tto in closecity[0]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[0]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[0]:
            farh = random.randint(3,
                                  5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[1]:
        if tto in closecity[1]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[1]:
            middleh = random.randint(2, 4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[1]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[2]:
        if tto in closecity[2]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[2]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[2]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[3]:
        if tto in closecity[3]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[3]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[3]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[4]:
        if tto in closecity[4]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[4]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[4]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[5]:
        if tto in closecity[5]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[5]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[5]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[6]:
        if tto in closecity[6]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[6]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[6]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[7]:
        if tto in closecity[7]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[7]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[7]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[8]:
        if tto in closecity[8]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[8]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[8]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[9]:
        if tto in closecity[9]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[9]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[9]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[10]:
        if tto in closecity[10]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[10]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[10]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[11]:
        if tto in closecity[11]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[11]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[11]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[12]:
        if tto in closecity[12]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[12]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[12]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[13]:
        if tto in closecity[13]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[13]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[13]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[14]:
        if tto in closecity[14]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[14]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[14]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[15]:
        if tto in closecity[15]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[15]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[15]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[16]:
        if tto in closecity[16]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[16]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[16]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[17]:
        if tto in closecity[17]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[17]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[17]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[18]:
        if tto in closecity[18]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[18]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[18]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[19]:
        if tto in closecity[19]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[19]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[19]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[20]:
        if tto in closecity[20]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[20]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[20]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[21]:
        if tto in closecity[21]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[21]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[21]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[22]:
        if tto in closecity[22]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[22]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[22]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[23]:
        if tto in closecity[23]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[23]:
            middleh = random.randint(2, 4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[23]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[24]:
        if tto in closecity[24]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[24]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[24]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[25]:
        if tto in closecity[25]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[25]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[25]:
            farh = random.randint(3, 5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[26]:
        if tto in closecity[26]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[26]:
            middleh = random.randint(2,4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[26]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[27]:
        if tto in closecity[27]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[27]:
            middleh = random.randint(2, 4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[27]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[28]:
        if tto in closecity[28]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[28]:
            middleh = random.randint(2, 4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[28]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    elif ffrom == cities[29]:
        if tto in closecity[29]:
            closerh = random.randint(1, 2)  # random int(in hours) generated for states closer to the Departure State
            closerm = random.randint(0, 59)
            at = dt + timedelta(hours=closerh, minutes=closerm)
            estmt = str(closerh) + " Hours " + str(closerm) + " Mins"

        elif tto in midcity[29]:
            middleh = random.randint(2, 4)  # random int(in hours) generated for states at medium distance from the Departure State
            middlem = random.randint(0, 59)
            at = dt + timedelta(hours=middleh, minutes=middlem)
            estmt = str(middleh) + " Hours " + str(middlem) + " Mins"

        elif tto in farcity[29]:
            farh = random.randint(3,5)  # random int(in hours) generated for the states farther than the Departure State
            farm = random.randint(0, 59)
            at = dt + timedelta(hours=farh, minutes=farm)
            estmt = str(farh) + " Hours " + str(farm) + " Mins"

    depttime = dt.strftime("%H:%M %p")  # dept time in str type in the format HH:MM AM/PM
    arrivaltime = at.strftime("%H:%M %p")  # dept time in str type in the format HH:MM AM/PM
    depttimestr = dt.strftime("%H,%M").split(",")
    arrivaltimestr = at.strftime("%H,%M").split(",")
    userdatestr = userdate.strftime("%Y,%m,%d")
    userdatestrlist = userdatestr.split(",")
    dtdate = datetime.datetime(int(userdatestrlist[0]), int(userdatestrlist[1]), int(userdatestrlist[2]) , int(depttimestr[0]) , int(depttimestr[1]) , 00)
    atdate = datetime.datetime(int(userdatestrlist[0]), int(userdatestrlist[1]), int(userdatestrlist[2]) , int(arrivaltimestr[0]) , int(arrivaltimestr[1]) , 00)
    dtstr = str(dtdate)
    atstr = str(atdate)
    return ffrom , tto , estmt , depttime , arrivaltime , dtstr , atstr

def primarykey(usertablename):
    con1 = s1.connect(host="localhost", user="root", passwd="1234", database="DOMESTIC_FLIGHT")
    plist = []
    cursor1 = con1.cursor()
    q = "select flightno from "+ usertablename +";"
    cursor1.execute(q)
    data = cursor1.fetchall()
    for i in data:
        plist.append(i[0])
    return plist


def insertion(userdate , usertablename):
    con1 = s1.connect(host="localhost", user="root", passwd="1234", database="DOMESTIC_FLIGHT")
    cursor1 = con1.cursor()
    print("Wait For 5 - 10 mins As The System Fetches The Required Data For The Provided Date Of Travel ")
    while True:
        flightnum, airline = flightno()
        ffrom, tto, estmt, depttime, arrivaltime , dtstr , atstr = fromtoanddeptarrivalestmd(userdate)
        gateno = random.randint(1, 12)
        plist = primarykey(usertablename)
        if flightnum not in plist:
            if len(plist) == 6500:
                break
            i = (flightnum, ffrom, tto, userdate, estmt, airline, depttime, arrivaltime, gateno , dtstr , atstr)
            q = "insert into "+ usertablename + " values(%s , %s , %s , %s , %s , %s , %s , %s , %s  , %s , %s);"
            cursor1.execute(q, i)
            con1.commit()
        else:
            continue

    con1.close()

def userfromto():
    cities = ["SRINAGAR", "SHIMLA", "AMRITSAR", "PANTNAGAR", "CHANDIGARH", "JAIPUR", "NOIDA", "GAYA", "INDORE", "DELHI",
              "AHMEDABAD", "RAIPUR", "RANCHI", "KOLKATA", "PAKYONG",
              "BHUBANESWAR", "MUMBAI", "GOA", "HYDERABAD", "VISAKHAPATNAM", "BENGALURU", "KOCHI", "CHENNAI", "TEZU",
              "GUWAHATI", "SHILLONG", "AGARTALA", "IMPHAL", "DIMAPUR",
              "LENGPUI"]
    print("List Of Following Cities: ")
    for i in range(1, 31):
        print(i , cities[i-1] )
    userfrom = str(input("ENTER THE ORIGIN CITY  FROM THE ABOVE LIST: "))
    userfromupper = userfrom.upper()

    while True:
        if userfromupper not in cities:
            print("Please Enter the Correct City Name From The List Given Above")
            userfrom = str(input("ENTER THE ORIGIN CITY  FROM THE ABOVE LIST: "))
            userfromupper = userfrom.upper()
            continue
        else:
            break

    userto = str(input("ENTER THE DESTINATION CITY FROM THE ABOVE LIST: "))
    usertoupper = userto.upper()
    while True:
        if usertoupper == userfromupper:
            print("Please Enter A Different City For Destination")
            userto = str(input("ENTER THE DESTINATION CITY FROM THE ABOVE LIST: "))
            usertoupper = userto.upper()
            if usertoupper not in cities:
                print("Please Enter the Correct City Name From The List Given Above")
                userto = str(input("ENTER THE DESTINATION CITY FROM THE ABOVE LIST: "))
                usertoupper = userto.upper()
                continue

        elif usertoupper != userfromupper:
            if usertoupper not in cities:
                print("Please Enter the Correct City Name From The List Given Above")
                userto = str(input("ENTER THE DESTINATION CITY FROM THE ABOVE LIST: "))
                usertoupper = userto.upper()
                continue
            else:
                break

    if userfromupper in cities and usertoupper in cities:
        print("ORIGIN CITY: " , userfromupper)
        print("DESTINATION CITY: " , usertoupper)
        print("LIST OF AVAILABLE FLIGHTS IS AS FOLLOWS: ")
    return userfromupper , usertoupper

def userdisplay(userdate , usertablename):
    from tabulate import tabulate
    from datetime import timedelta
    import datetime
    today = date.today()
    ytoday = today.strftime("%Y")
    mtoday = today.strftime("%m")
    dtoday = today.strftime("%d")
    con1 = s1.connect(host="localhost", user="root", passwd="1234", database="DOMESTIC_FLIGHT")
    cursor1 = con1.cursor()
    userfromupper , usertoupper = userfromto()
    now = datetime.datetime.now()
    a = now.strftime("%H:%M %p")

    timelimit = datetime.datetime(int(ytoday)  , int(mtoday) , int(dtoday) , 23 , 59 , 00)
    nowtwohours = now + timedelta(hours=2)
    nowtwohoursstr = str(nowtwohours)
    if userdate == today:
        i = (userfromupper, usertoupper, nowtwohoursstr)
        q = "select flightno , cityfrom , cityto , flightdate , estmd_travelling_time , airlinename , depttime , arrivaltime , gateno from " + usertablename + " where cityfrom = %s and cityto = %s and dt >= %s  order by dt asc;"
        cursor1.execute(q, i)
        data = cursor1.fetchall()
        if len(data) == 0:
            print("NO AVAILABLE FLIGHTS AT THE MOMENT FOR THE SPECIFIED ORIGIN AND DESTINATION CITY")
        else:
            print(tabulate(data, headers=["FLIGHT NO.", "FROM", "TO", "DATE", "ESTIMATED TRAVELLING TIME", "AIRLINE",
                                      "DEPARTURE TIME", "ARRIVAL TIME", "GATE NO."], tablefmt="double_outline"))

        con1.commit()


    else:
        i = (userfromupper, usertoupper)
        q = "select flightno , cityfrom , cityto , flightdate , estmd_travelling_time , airlinename , depttime , arrivaltime , gateno from " + usertablename + " where cityfrom = %s and cityto = %s order by dt asc;"
        cursor1.execute(q, i)
        data = cursor1.fetchall()
        print(tabulate(data, headers=["FLIGHT NO.", "FROM", "TO", "DATE", "ESTIMATED TRAVELLING TIME", "AIRLINE", "DEPARTURE TIME", "ARRIVAL TIME", "GATE NO."], tablefmt="double_outline"))

        con1.commit()
    con1.close()

def mainfunc():
    print("FLIGHT DATABASE MANAGEMENT SYSTEM")
    ans = "y"
    while ans == "y":
        userdate = traveldate()
        usertablename = userdate.strftime("%d%b%Y")
        database()
        flightlist(usertablename)
        insertion(userdate, usertablename)
        userdisplay(userdate, usertablename)
        ans = input("Do You Want To Fetch Another Record?(y/enter other value to exit code)  ")

    print("Thank You For Using The System")


mainfunc()
