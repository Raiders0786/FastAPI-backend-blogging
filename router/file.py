from fastapi import APIRouter,File,UploadFile
import shutil
from fastapi.responses import FileResponse
router = APIRouter(prefix='/file', tags=['file'])


@router.post('/file')
def get_files(files: bytes = File(...)):
    content = files.decode('utf-8')
    lines= content.split('\n')
    return {"Lines":lines}

# uploading the file name locally into a file , if the filename is same it will replace the file present before
@router.post('/uploadFile')
def upload_file(upload_file: UploadFile = File(...)):
    path = f"file/{upload_file.filename}"
    with open(path,"w+b") as buffer:
        shutil.copyfileobj(upload_file.file,buffer)
    
    return {
        "FileName":path,
        "Content-Type": upload_file.content_type
    }

@router.get('/download/{name}',response_class=FileResponse)
def get_files(name: str):
    path= f'file/{name}'
    return path