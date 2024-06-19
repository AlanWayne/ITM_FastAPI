from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from database import get_db
from services import *

router = APIRouter()


@router.post("/document/", tags=["document"])
async def upload(data: UploadFile = None, db: Session = Depends(get_db)):
    return upload_doc(data, db)


@router.delete("/document/", tags=["document"])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return remove_doc(id, db)


@router.put("/document/", tags=["document"])
async def analys(id: int = None, db: Session = Depends(get_db)):
    return analyse_doc(id, db)


@router.get("/document/", tags=["document"])
async def extract(id: int = None, db: Session = Depends(get_db)):
    return get_text(id, db)


@router.get("/api/", tags=["healthcheck"])
async def health_check():
    return {"status": True}
