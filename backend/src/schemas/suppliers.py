from pydantic import BaseModel, Field, ConfigDict


class SupplierBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=200, description="Supplier name")
    contact_person: str | None = Field(None, max_length=100, description="Contact person name")
    email: str | None = Field(None, max_length=255, description="Supplier email")
    phone: str | None = Field(None, max_length=15, description="Supplier phone number")
    address: str | None = Field(None, max_length=255, description="Supplier address")


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=200, description="Supplier name")
    contact_person: str | None = Field(None, max_length=100, description="Contact person name")
    email: str | None = Field(None, max_length=255, description="Supplier email")
    phone: str | None = Field(None, max_length=15, description="Supplier phone number")
    address: str | None = Field(None, max_length=255, description="Supplier address")


class SupplierRead(SupplierBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
