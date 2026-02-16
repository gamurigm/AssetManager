from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import List, Optional
from enum import Enum

class UserRole(str, Enum):
    CLIENT = "client"
    MANAGER = "manager"

class TransactionType(str, Enum):
    BUY = "buy"
    SELL = "sell"

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    role: UserRole = UserRole.CLIENT

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Holding Schemas
class HoldingBase(BaseModel):
    symbol: str
    quantity: float
    average_price: float

class Holding(HoldingBase):
    id: int
    portfolio_id: int
    
    model_config = ConfigDict(from_attributes=True)

# Transaction Schemas
class TransactionBase(BaseModel):
    symbol: str
    type: TransactionType
    quantity: float
    price: float

class Transaction(TransactionBase):
    id: int
    portfolio_id: int
    timestamp: datetime
    
    model_config = ConfigDict(from_attributes=True)

# Portfolio Schemas
class PortfolioBase(BaseModel):
    name: str

class Portfolio(PortfolioBase):
    id: int
    client_id: int
    total_value: float
    created_at: datetime
    holdings: List[Holding] = []
    
    model_config = ConfigDict(from_attributes=True)

# Client Schemas
class ClientBase(BaseModel):
    risk_profile: Optional[str] = None
    kyc_status: str = "pending"

class ClientDetail(ClientBase):
    id: int
    user: User
    portfolios: List[Portfolio] = []
    
    model_config = ConfigDict(from_attributes=True)
