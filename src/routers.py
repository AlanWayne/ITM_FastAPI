from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from database import get_db
import services

router = APIRouter()


@router.post("/", tags=["document"])
async def upload(data: UploadFile = None, db: Session = Depends(get_db)):
    """
    Args:
    - data (UploadFile, optional): File to upload on server. Defaults to None.
    - db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
    - str: A record in the database.
    """
    return services.upload_doc(data, db)


@router.delete("/", tags=["document"])
async def delete(id: int = None, db: Session = Depends(get_db)):
    """
    Args:
    - id (int, optional): ID of the entity in database. Defaults to None.
    - db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
    - str: A record in the database.
    """
    return services.remove_doc(id, db)


@router.put("/", tags=["document"])
async def analys(id: int = None, db: Session = Depends(get_db)):
    """
    Args:
    - id (int, optional): ID of the entity in database. Defaults to None.
    - db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
    - str: A record in the database.
    """
    return services.analyse_doc(id, db)


@router.get("/", tags=["document"])
async def extract(id: int = None, db: Session = Depends(get_db)):
    """
    Args:
    - id (int, optional): ID of the entity in database. Defaults to None.
    - db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
    - str: A record in the database.
    """
    return services.get_text(id, db)
