from sqlalchemy import String, ForeignKey, Float, Boolean, Integer, DateTime, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime
from typing import List, Optional
import enum
from ..core.database import Base

class UserRole(enum.Enum):
    CLIENT = "client"
    MANAGER = "manager"

class MandateType(enum.Enum):
    DISCRETIONARY = "discretionary"
    ADVISED = "advised"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[Optional[str]] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), default=UserRole.CLIENT)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    client_profile: Mapped["Client"] = relationship(back_populates="user", uselist=False)

class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    manager_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    risk_profile: Mapped[Optional[str]] = mapped_column(String(50)) # Low, Medium, High
    kyc_status: Mapped[str] = mapped_column(default="pending")

    # Relationships
    user: Mapped["User"] = relationship(back_populates="client_profile")
    portfolios: Mapped[List["Portfolio"]] = relationship(back_populates="client")

class Portfolio(Base):
    __tablename__ = "portfolios"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    name: Mapped[str] = mapped_column(String(100))
    mandate_type: Mapped[MandateType] = mapped_column(SQLEnum(MandateType), default=MandateType.DISCRETIONARY)
    
    # Fee Structure
    management_fee_rate: Mapped[float] = mapped_column(Float, default=0.01) # Default 1%
    performance_fee_rate: Mapped[float] = mapped_column(Float, default=0.20) # Default 20%
    high_water_mark: Mapped[float] = mapped_column(Float, default=0.0)
    
    total_value: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    client: Mapped["Client"] = relationship(back_populates="portfolios")
    holdings: Mapped[List["Holding"]] = relationship(back_populates="portfolio")
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="portfolio")

class Holding(Base):
    __tablename__ = "holdings"

    id: Mapped[int] = mapped_column(primary_key=True)
    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolios.id"))
    symbol: Mapped[str] = mapped_column(String(20))
    quantity: Mapped[float] = mapped_column(Float)
    average_price: Mapped[float] = mapped_column(Float)
    
    # Relationships
    portfolio: Mapped["Portfolio"] = relationship(back_populates="holdings")

class TransactionType(enum.Enum):
    BUY = "buy"
    SELL = "sell"

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolios.id"))
    symbol: Mapped[str] = mapped_column(String(20))
    type: Mapped[TransactionType] = mapped_column(SQLEnum(TransactionType))
    quantity: Mapped[float] = mapped_column(Float)
    price: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    portfolio: Mapped["Portfolio"] = relationship(back_populates="transactions")

class WatchlistItem(Base):
    __tablename__ = "watchlist_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    symbol: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
