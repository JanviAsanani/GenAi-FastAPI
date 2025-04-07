from fastapi import APIRouter
from models import CodeFile

router = APIRouter()

@router.post("/", response_model=CodeFile, summary="Create a code file")
async def create_code_file(code_file: CodeFile):
    return code_file