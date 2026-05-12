from pydantic import BaseModel, Field, ConfigDict


class OrderItemBase(BaseModel):
    order_id: int = Field(..., gt=0, description="Order ID")
    product_id: int = Field(..., gt=0, description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity of product")
    unit_price: float = Field(..., gt=0, description="Unit price at time of order")


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemUpdate(BaseModel):
    order_id: int | None = Field(None, gt=0, description="Order ID")
    product_id: int | None = Field(None, gt=0, description="Product ID")
    quantity: int | None = Field(None, gt=0, description="Quantity of product")
    unit_price: float | None = Field(None, gt=0, description="Unit price at time of order")


class OrderItemRead(OrderItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
