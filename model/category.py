"""
Model Category
"""
from datetime import datetime

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Category(Base):
    """
    Class Category
    Args:
        Base (_type_): Base class for SQLAlchemy models
    """
    __tablename__ = 'category'
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Category {self.name} at {self.date_created}>"

    def to_dict(self):
        """Convert to Dict

        Returns:
            _type_: Dict
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date_created': self.date_created.isoformat() if self.date_created else None
        }
