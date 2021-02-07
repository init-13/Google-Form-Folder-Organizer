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

#input()
Bcode="110CE_"
colnames = ['Reg', 'Name']
colnames.extend(list(map(lambda x:str('f'+str(x)),(range(3,39)))))

#print(colnames)
#input()
data = pandas.read_csv('Enrollment Data CS-A2L, 2020-21.csv', names=colnames)
name = data.Name.tolist()[1:]
regno=data.Reg.tolist()[1:]
folders=list()
for i in range(len(name)):
    folders.append(str(Bcode+regno[i]+'_'+name[i]))
    

#root_path = 'C:\Users\Del\Desktop\TESTING'

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
filescol=[9,12,15,18,21,24,27,30,33,36,37,38]
filesname=["Aadhar.pdf","10th Marksheet.pdf","12th Marksheet.pdf","Category Certificate.pdf","Domicile Certificate.pdf","Migration Certificate.pdf","Income Certificate.pdf","Gap Certificate.pdf","UPSEE Councelling Letter.pdf","Signature.jpg","Photo.jpg","Thumb Impression.jpg",]
filescol=list(map(lambda x:str('f'+str(x)),filescol))
#print(data.file1.tolist()[1:])
#downloadfile(data.f9.tolist()[1:],"Aadhar.pdf")
for j in range(len(filescol)):
    eval(str("downloadfile(data."+filescol[j]+".tolist()[1:],\""+filesname[j])+"\")")
#downloadfile(data.file1.tolist()[1:],"10th Marksheet")
#ownloadfile(data.file2.tolist()[1:],"12th Marksheet")
        
