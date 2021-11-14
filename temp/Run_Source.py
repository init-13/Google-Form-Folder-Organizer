
import pandas
import csv
import json
import os
import requests
import glob
import pickle
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


def wrtcnf(string,c):
    with open('config.txt', c) as the_file:
        the_file.write(string+'\n')
    
    
def choext(ext):
    result = glob.glob('*.{}'.format(ext))

    if not result:
        
        print("NO", ext, "FILE FOUND")

    if ext =='json':
        try:
            result.remove('config.json')
        except:
            pass

    if len(result)==1:
        return result[0]


    else:
        for i in range(len(result)):
            print(i+1,result[i],sep='. ')
        print("CHOOSE", ext, "FILE NUMBER")
        return result[int(input())-1]
        
    	
        
        
def Create_Service(client_secret_file, api_name, api_version, *scopes):
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt

import os
import io
from googleapiclient.http import MediaIoBaseDownload


API_NAME='drive'
API_VERSION='v3'
SCOPES= ['https://www.googleapis.com/auth/drive']


#downfile('1FIKyr97GwztQ37fcRHSbFCCvDg5ftYPQ','success.pdf')



def takeinputfromfile():
    
    try:
        file=open('config.json',)
        data = json.load(file)
            
        file.close()
        C_ID=choext('json')
        return [C_ID,data['folderC'],data['sep'],data['filesC'],data['filesN']]
    except:
        
        return takeinput()
    

    
def takeinput():
    C_ID=choext('json')
    wrtcnf(C_ID,'w')
    csvfile=choext('csv')
    def printhead():
        
        data = pandas.read_csv(csvfile, nrows=1)
        print("THE CSV FILE IS READ SUCCESFULLY")
        
        n=1
        for i in data:
            print(n,i,sep='. ',end="\n\n")
            n+=1
        return list(data)

    x=printhead()
    print("\n\n\tSELECT THE COLUMN(S) NUMBER FOR FOLDER NAMES SEPERATED BY SPACE \n\n\n NOTICE:PLEASE SELECT THE COLUMNS UNIQUELY IDENTIFYING THE FOLDERS NAME \n\n")
    xl=list(map(int,input().split()))
    wrtcnf(" ".join(list(map(str,xl))),'a')
    print("\tENTER SEPERATOR CHARACTER")
    sep=input()
    wrtcnf(sep,'a')
           




    print("\tENTER DOWNLOADABLE COLUMN(S) NUMBER SEPERATED BY FILE NAME\n\n\tEXAMPLE:\n 2 file1_name.file1_type \n 5 acrobat.pdf \n 9 image.jpg\n")
    filescol=[]
    filesname=[]
    try:
        while(1):
            m,n=input().split()
            filescol.append(int(m))
            filesname.append(n)
    except:
        print("FINISH")

    wrtcnf(" ".join(list(map(str,filescol))),'a')
    wrtcnf(" ".join(filesname),'a')
    print("DO YOU WANT TO SAVE THESE SETTINGS? \n\t NOTE: THE PROGRAM WILL RUN AUTOMATIC WITH THE CREDENTIALS PROVIDED ABOVE.")
    if (input()[0].lower()!= 'y'):
        try:
            os.remove("config.txt")
        except:
            print("DONE")
    return [C_ID,xl,sep,filescol,filesname]

var_list=takeinputfromfile()
print(var_list)
C_ID = var_list[0]
xl= var_list[1]
sep= var_list[2]
filescol= var_list[3]
filesname= var_list[4]
service= Create_Service(C_ID,API_NAME,API_VERSION,SCOPES)



def downfile(file_id,file_name):
    request= service.files().get_media(fileId=file_id)
    fh=io.BytesIO()
    downloader= MediaIoBaseDownload(fd=fh, request=request)

    done=False
    while not done:
        status, done=downloader.next_chunk()

    fh.seek(0)

    with open(file_name,'wb') as f:
        f.write(fh.read())
        f.close    

csvfile=choext('csv')
xmax=len(pandas.read_csv(csvfile).axes[1])
colnames=list(map(lambda x:str('f'+str(x)),(range(1,xmax+1))))
#print(colnames)
#print(colnames)
#input()

data=pandas.read_csv(csvfile,names=colnames)

#print(data)
names=list()

for i in xl:
    names.append(eval(str("data.f"+str(i)+".tolist()[1:]")))
names=list(zip(*names))
print(names)
folders=list()
for i in names:
    folders.append(sep.join(i))    
gh = folders
#print(gh)
#input()
for folder in gh:
    try:
        os.mkdir(str(folder))
    except:
        continue



                
def downloadfile(l,st):
    n=len(l)
    for i in range(n):
        if type(l[i])!=str:
            continue
        os.chdir(str(folders[i]))
        print(l[i].split('=')[-1])
        fname=str(st)
        if os.path.exists(fname):
            print(fname +" Exists")
            os.chdir("..")
            continue
        downfile(l[i].split('=')[-1], str(st))
        print(fname+" Downloaded")
        os.chdir("..")
        #print(os.getcwd())
#filescol=[9,12,15,18,21,24,27,30,33,36,37,38]
#filesname=["Aadhar.pdf","10th Marksheet.pdf","12th Marksheet.pdf","Category Certificate.pdf","Domicile Certificate.pdf","Migration Certificate.pdf","Income Certificate.pdf","Gap Certificate.pdf","UPSEE Councelling Letter.pdf","Signature.jpg","Photo.jpg","Thumb Impression.jpg",]
filescol=list(map(lambda x:str('f'+str(x)),filescol))
#print(data.file1.tolist()[1:])
#downloadfile(data.f9.tolist()[1:],"Aadhar.pdf")
for j in range(len(filescol)):
    eval(str("downloadfile(data."+filescol[j]+".tolist()[1:],\""+filesname[j])+"\")")
#downloadfile(data.file1.tolist()[1:],"10th Marksheet")
#ownloadfile(data.file2.tolist()[1:],"12th Marksheet")
        
        
        
    

    
    
    



















