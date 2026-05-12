from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=200, description="Product name")
    description: str | None = Field(None, max_length=1000, description="Product description")
    price: float = Field(..., gt=0, description="Product price (RUB)")
    category_id: int = Field(..., gt=0, description="Category ID")
    supplier_id: int = Field(..., gt=0, description="Supplier ID")


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=200, description="Product name")
    description: str | None = Field(None, max_length=1000, description="Product description")
    price: float | None = Field(None, gt=0, description="Product price (RUB)")
    category_id: int | None = Field(None, gt=0, description="Category ID")
    supplier_id: int | None = Field(None, gt=0, description="Supplier ID")


class ProductRead(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
