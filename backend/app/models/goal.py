import enum
from sqlalchemy import Column, Integer, String, Numeric, Enum, ForeignKey, DateTime, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class GoalStatus(str, enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    target_amount = Column(Numeric(15, 2), nullable=False)
    current_amount = Column(Numeric(15, 2), default=0)
    deadline = Column(Date, nullable=True)
    icon = Column(String(50), nullable=True)
    color = Column(String(7), nullable=True)
    status = Column(Enum(GoalStatus), default=GoalStatus.ACTIVE)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="goals")

    @property
    def progress_percentage(self) -> float:
        if self.target_amount == 0:
            return 0
        return min(float(self.current_amount / self.target_amount * 100), 100)