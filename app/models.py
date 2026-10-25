from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Rezept(Base):
    __tablename__ = "rezepte"

    id: Mapped[int] = mapped_column(primary_key=True)
    titel: Mapped[str] = mapped_column(String(100))
    beschreibung: Mapped[Optional[str]] = mapped_column(Text)
    dauer_minuten: Mapped[Optional[int]] = mapped_column
    schwierigkeit: Mapped[str] = mapped_column(String(10))
    erstellt_am: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

