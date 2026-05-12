from pydantic import BaseModel, Field, ConfigDict


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Category name")
    description: str | None = Field(None, max_length=500, description="Category description")


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100, description="Category name")
    description: str | None = Field(None, max_length=500, description="Category description")


class CategoryRead(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
