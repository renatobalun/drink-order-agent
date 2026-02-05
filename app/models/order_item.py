from __future__ import annotations
from sqlalchemy import Integer, String
from app.db.database import Base

from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    Index,
    CheckConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # šifra/SKU iz MD kataloga (NE mora biti unique po narudžbi)
    item_id: Mapped[str] = mapped_column(String(80), nullable=False, index=True)

    unit: Mapped[str] = mapped_column(String(20), nullable=False)        # gajba/paket/bačva
    packaging: Mapped[str] = mapped_column(String(60), nullable=False)   # npr 0.5L staklo
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    order: Mapped["Order"] = relationship(back_populates="items")

    __table_args__ = (
        CheckConstraint("quantity > 0", name="ck_order_items_quantity_gt_0"),
        # Indeks za brže dohvaćanje i GROUP BY pri izradi PDF-a
        Index("idx_order_items_order_item", "order_id", "item_id"),
    )