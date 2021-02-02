import pandas
import os
import requests

#input()
Bcode="110CE_"
colnames = ['Reg', 'Name']
colnames.extend(list(map(lambda x:str('f'+str(x)),(range(3,39)))))

#print(colnames)
#input()
data = pandas.read_csv('Enrollment Data CE-G1, 2020-21.csv', names=colnames)
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


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                
def downloadfile(l,st):
    n=len(l)
    for i in range(n):
        if type(l[i])!=str and isnan(l[i]):
            continue
        os.chdir(str(folders[i]))
        print(l[i].split('=')[-1])
        fname=str(folders[i]+'_'+st)
        if os.path.exists(fname):
            print(fname +" Exists")
            os.chdir("..")
            continue
        download_file_from_google_drive(l[i].split('=')[-1], str(folders[i]+'_'+st))
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
        
        
        
    

    
    
    
