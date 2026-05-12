from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class CustomerBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=100, description="Customer first name")
    last_name: str = Field(..., min_length=2, max_length=100, description="Customer last name")
    patronymic: str | None = Field(None, min_length=2, max_length=100, description="Customer patronymic")
    email: str = Field(..., max_length=255, description="Customer email")
    phone: str = Field(..., max_length=15, description="Customer phone number")
    address: str | None = Field(None, max_length=255, description="Customer address")


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    first_name: str | None = Field(None, min_length=2, max_length=100, description="Customer first name")
    last_name: str | None = Field(None, min_length=2, max_length=100, description="Customer last name")
    patronymic: str | None = Field(None, min_length=2, max_length=100, description="Customer patronymic")
    email: str | None = Field(None, max_length=255, description="Customer email")
    phone: str | None = Field(None, max_length=15, description="Customer phone number")
    address: str | None = Field(None, max_length=255, description="Customer address")


class CustomerRead(CustomerBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
