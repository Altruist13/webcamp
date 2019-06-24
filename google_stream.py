from PIL import Image
import io
import requests
api_key="AIzaSyDv1Us8Dp2De6nARJy-MbLrd45l9JUfUQ4"
from apiclient.discovery import build
import azure
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings

block_blob_service =BlockBlobService(account_name="hydroponicssa",account_key="aaIPKVI21tc04BRE7DOX9XTTR3CvS8B2l987S8mJ7jdlJ7vNkJuhEqQakDWIpXcj6u9fKihB6xUxlLGspV8Zew==")

resource=build("customsearch","v1",developerKey=api_key).cse()
images=[]


for i in range(1,50,10):
    result=resource.list(q="saplings of spinach",cx="018230972363924914691:cgggxsyqokc",searchType="image",start=i).execute()
    images+=result["items"]

for item in images:
    response=requests.get(item["link"])  
    #(io.IOBase(response.content))
    #mg=Image.open(BytesIO(response.content))
    block_blob_service.create_blob_from_stream('hydroponics','external',io.BytesIO(response.content),content_settings=ContentSettings(content_type='image/Jpeg'))
    
    