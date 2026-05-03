from sqlalchemy.orm import Session
from ..repositories.categories import CategoryRepository
from ..schemas.categories import CategoryCreate, CategoryUpdate, CategoryRead


class CategoryService:
    def __init__(self, db: Session):
        self.repo = CategoryRepository(db)

    def get_all(self) -> list[CategoryRead]:
        categories = self.repo.get_all()
        return [CategoryRead.model_validate(c) for c in categories]

    def get_by_id(self, category_id: int) -> CategoryRead:
        category = self.repo.get_by_id(category_id)
        if not category:
            raise ValueError(f"Category with id {category_id} not found")
        return CategoryRead.model_validate(category)

    def create(self, data: CategoryCreate) -> CategoryRead:
        existing = self.repo.get_by_name(data.name)
        if existing:
            raise ValueError(f"Category '{data.name}' already exists")
        category = self.repo.create(data)
        return CategoryRead.model_validate(category)

    def update(self, category_id: int, data: CategoryUpdate) -> CategoryRead:
        category = self.repo.get_by_id(category_id)
        if not category:
            raise ValueError(f"Category with id {category_id} not found")
        updated = self.repo.update(category, data)
        return CategoryRead.model_validate(updated)

    def delete(self, category_id: int) -> None:
        category = self.repo.get_by_id(category_id)
        if not category:
            raise ValueError(f"Category with id {category_id} not found")
        self.repo.delete(category)
