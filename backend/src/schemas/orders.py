from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class OrderBase(BaseModel):
    customer_id: int = Field(..., gt=0, description="Customer ID")
    status: str = Field("pending", max_length=50, description="Order status")
    total_amount: float = Field(0.0, ge=0, description="Total order amount")


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_id: int | None = Field(None, gt=0, description="Customer ID")
    status: str | None = Field(None, max_length=50, description="Order status")
    total_amount: float | None = Field(None, ge=0, description="Total order amount")


class OrderRead(OrderBase):
    id: int
    order_date: datetime

    model_config = ConfigDict(from_attributes=True)
