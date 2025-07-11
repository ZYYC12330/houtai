from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from router.crm_utils import CRMRequestBuilder, get_token

router = APIRouter()

@router.post("/import_clue/")
async def import_clue(
    file: UploadFile = File(...),
    token: str = Depends(get_token),
    inpool = 0
):
    

    file_content = await file.read()
    files = {
        'file': (file.filename, file_content, file.content_type or 'application/vnd.ms-excel'),
    }
    url = "https://testcrm.xhd.cn/api/clue/import"
    crm_builder = CRMRequestBuilder()
    status_code, content = crm_builder.make_post_request(
        url,token,inpool, "4645a321f95b4bce992685253bf01147", files=files
    )
    return JSONResponse(status_code=status_code, content=content)