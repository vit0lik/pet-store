from pydantic import BaseModel, Field, ConfigDict


class InventoryBase(BaseModel):
    product_id: int = Field(..., gt=0, description="Product ID")
    quantity: int = Field(..., ge=0, description="Quantity in stock")
    warehouse_location: str | None = Field(None, max_length=100, description="Warehouse location")


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(BaseModel):
    product_id: int | None = Field(None, gt=0, description="Product ID")
    quantity: int | None = Field(None, ge=0, description="Quantity in stock")
    warehouse_location: str | None = Field(None, max_length=100, description="Warehouse location")


class InventoryRead(InventoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
