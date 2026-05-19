from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.transaction import Category, TransactionType
from app.schemas.transaction import CategoryCreate, CategoryUpdate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])

DEFAULT_CATEGORIES = [
    # Income
    {"name": "Salário", "icon": "💼", "color": "#10b981", "type": TransactionType.INCOME, "is_default": True},
    {"name": "Freelance", "icon": "💻", "color": "#06b6d4", "type": TransactionType.INCOME, "is_default": True},
    {"name": "Investimentos", "icon": "📈", "color": "#8b5cf6", "type": TransactionType.INCOME, "is_default": True},
    {"name": "Outros (Receita)", "icon": "💰", "color": "#f59e0b", "type": TransactionType.INCOME, "is_default": True},
    # Expense
    {"name": "Alimentação", "icon": "🍔", "color": "#ef4444", "type": TransactionType.EXPENSE, "is_default": True},
    {"name": "Transporte", "icon": "🚗", "color": "#f97316", "type": TransactionType.EXPENSE, "is_default": True},
    {"name": "Moradia", "icon": "🏠", "color": "#eab308", "type": TransactionType.EXPENSE, "is_default": True},
    {"name": "Saúde", "icon": "❤️", "color": "#ec4899", "type": TransactionType.EXPENSE, "is_default": True},
    {"name": "Educação", "icon": "📚", "color": "#3b82f6", "type": TransactionType.EXPENSE, "is_default": True},
    {"name": "Lazer", "icon": "🎮", "color": "#a855f7", "type": TransactionType.EXPENSE, "is_default": True},
    {"name": "Vestuário", "icon": "👕", "color": "#14b8a6", "type": TransactionType.EXPENSE, "is_default": True},
    {"name": "Outros (Despesa)", "icon": "📦", "color": "#6b7280", "type": TransactionType.EXPENSE, "is_default": True},
]


@router.get("/", response_model=list[CategoryResponse])
def list_categories(
    type: Optional[TransactionType] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Return global defaults + user-created categories
    query = db.query(Category).filter(
        (Category.user_id == current_user.id) | (Category.is_default == True)
    )
    if type:
        query = query.filter(Category.type == type)
    return query.order_by(Category.is_default.desc(), Category.name).all()


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(
    payload: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    category = Category(**payload.model_dump(), user_id=current_user.id, is_default=False)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    payload: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    category = db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == current_user.id,
    ).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(category, field, value)

    db.commit()
    db.refresh(category)
    return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    category = db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == current_user.id,
        Category.is_default == False,
    ).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found or cannot delete default")

    db.delete(category)
    db.commit()