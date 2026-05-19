from pydantic import BaseModel, field_validator
from datetime import datetime, date
from typing import Optional
from decimal import Decimal

from app.models.transaction import TransactionType, RecurrenceType


# ── Category Schemas ──────────────────────────────────────────

class CategoryBase(BaseModel):
    name: str
    icon: Optional[str] = None
    color: Optional[str] = "#6366f1"
    type: TransactionType


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None


class CategoryResponse(CategoryBase):
    id: int
    is_default: bool
    user_id: Optional[int]

    class Config:
        from_attributes = True


# ── Transaction Schemas ───────────────────────────────────────

class TransactionBase(BaseModel):
    description: str
    amount: Decimal
    type: TransactionType
    date: date
    notes: Optional[str] = None
    recurrence: RecurrenceType = RecurrenceType.NONE
    category_id: Optional[int] = None

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Amount must be greater than zero")
        return v


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    description: Optional[str] = None
    amount: Optional[Decimal] = None
    type: Optional[TransactionType] = None
    date: Optional[date] = None
    notes: Optional[str] = None
    recurrence: Optional[RecurrenceType] = None
    category_id: Optional[int] = None


class TransactionResponse(TransactionBase):
    id: int
    user_id: int
    created_at: datetime
    category: Optional[CategoryResponse] = None

    class Config:
        from_attributes = True


# ── Pagination ────────────────────────────────────────────────

class TransactionListResponse(BaseModel):
    items: list[TransactionResponse]
    total: int
    page: int
    size: int
    pages: int