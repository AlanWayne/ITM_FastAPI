from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from database import get_db
import services

router = APIRouter()


@router.post("/document/", tags=["document"])
async def upload(data: UploadFile = None, db: Session = Depends(get_db)):
    return services.upload_doc(data, db)


@router.delete("/document/", tags=["document"])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return services.remove_doc(id, db)


@router.put("/document/", tags=["document"])
async def analys(id: int = None, db: Session = Depends(get_db)):
    return services.analyse_doc(id, db)


@router.get("/document/", tags=["document"])
async def extract(id: int = None, db: Session = Depends(get_db)):
    return services.get_text(id, db)