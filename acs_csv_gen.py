import sys

# File dump.txt oeffnen  (C:\Users\ederg\PythonProjects\ACS_User_parser\acs-user-parser)
try:
    d = open("dump.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(O)

# Das gesamte File in "allezeilen" laden
allezeilen = d.readlines()
d.close()

#Variablen Initialisieren

Username = ""
Passworttype = ""
LastLogin = ""
Gruppe = ""
AccessList = ""
ACE = ""
REALNAME = ""

# Zeilen Parsen
print ("Username" , ";" , "REALNAME" , ";" , "Gruppe" , ";" , "Passworttype" , ";" , "AccessList", ";" , "LastLogin" , ";" , "ACE", ";" , "Status" )
for zeile in allezeilen:
    if zeile.startswith("Name          :"):         #Zeile beginnt mit  "Name  :"
        Name = zeile.partition("Name          :")   #Zeile Splitten nach "Name   :"
        Username = (Name[2])                        # Username ist der 3. Teil nach der Splittung
        Username = Username[:-1]                    # Das Letze Zeichen (CR/LF abschnieden)
    if zeile.startswith("Type          :"):
        PWDType = zeile.partition("Type          :")
        Passworttype = PWDType[2]
        Passworttype = Passworttype[:-1]
    if zeile.startswith("App00	LAST_SUCCESS_LOGIN	STRING"):
        LLogin = zeile.partition("App00	LAST_SUCCESS_LOGIN	STRING")
        LastLogin = LLogin[2]
        LastLogin = LastLogin[:-1]
    if zeile.startswith("Aging policy  :"):
        GRP = zeile.partition("Aging policy  :")
        Gruppe = GRP[2]
        Gruppe = Gruppe[:-1]
    if zeile.startswith("App02	SPCACL	STRING	"):
        ACL = zeile.partition("App02	SPCACL	STRING	")
        AccessList = ACL[2]
        AccessList = AccessList[:-1]
    if zeile.startswith("App00	USER_DEFINED_FIELD_0	STRING"):
        Relname = zeile.partition("App00	USER_DEFINED_FIELD_0	STRING")
        REALNAME = Relname[2]
        REALNAME = REALNAME[:-1]
    if zeile.find("shell:Admin") > 10:
        ACE = "ACE-Policy"
    if zeile.startswith("Status        :"):
        ENA = zeile.partition("Status        :")
        enablestatus = ENA[2]
        enablestatus = enablestatus[:-1]
        ENABLE = enablestatus
    if zeile.startswith("##--- Values End"):
        print (Username , ";" , REALNAME , ";" , Gruppe , ";" , Passworttype , ";" , AccessList, ";" , LastLogin , ";" , ACE ,";", ENABLE)
        # print ("--------------------------------------------")
        Username = ""
        REALNAME = ""
        Passworttype = ""
        LastLogin = ""
        Gruppe = ""
        AccessList = ""
        ACE = ""
        ENABLE = ""





