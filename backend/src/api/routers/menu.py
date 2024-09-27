from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ...models.menu_models import MenuItem
from ...schemas.menu_schemas import MenuItemCreate, MenuItemUpdate, MenuItemResponse
from ...config.database import get_db

router = APIRouter()

@router.post("/menu/add", response_model=MenuItemResponse)
def add_menu_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    db_item = MenuItem(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.put("/menu/update/{item_name}", response_model=MenuItemResponse)
def update_menu_item(item_name: str, item: MenuItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(MenuItem).filter(MenuItem.name == item_name).first()
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/menu/delete/{item_name}")
def delete_menu_item(item_name: str, db: Session = Depends(get_db)):
    db_item = db.query(MenuItem).filter(MenuItem.name == item_name).first()
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"success": True}
