import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


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

C_ID='client_secret_116786478100-jkagqb7p4g6u2b9o3l2pchqtva3jsse9.apps.googleusercontent.com.json'
API_NAME='drive'
API_VERSION='v3'
SCOPES= ['https://www.googleapis.com/auth/drive']
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

#downfile('1FIKyr97GwztQ37fcRHSbFCCvDg5ftYPQ','success.pdf')




import pandas
import os
import requests

def printhead():
    
    data = pandas.read_csv('Enrollment Data CS-A1, 2020-21.csv', nrows=1)
    print("THE CSV FILE IS READ SUCCESFULLY")
    
    n=1
    for i in data:
        print(n,i,sep='. ',end="\n\n")
        n+=1
    return list(data)

x=printhead()
print("\n\n\tSELECT THE COLUMN(S) NUMBER FOR FOLDER NAMES SEPERATED BY SPACE \n\n\n NOTICE:PLEASE SELECT THE COLUMNS UNIQUELY IDENTIFYING THE FOLDERS NAME \n\n")
xl=list(map(int,input().split()))
print("\tENTER SEPERATOR CHARACTER")
sep=input()
       


colnames=list(map(lambda x:str('f'+str(x)),(range(1,len(x)+1))))
#print(colnames)
#print(colnames)
#input()
data = pandas.read_csv('Enrollment Data CS-A1, 2020-21.csv', names=colnames)

names=list()
for i in xl:
    names.append(eval(str("data.f"+str(i)+".tolist()[1:]")))
names=list(zip(*names))
folders=list()
for i in names:
    folders.append(sep.join(i))

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
        fname=str(folders[i]+'_'+st)
        if os.path.exists(fname):
            print(fname +" Exists")
            os.chdir("..")
            continue
        downfile(l[i].split('=')[-1], str(folders[i]+'_'+st))
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
        
        
        
    

    
    
    



















