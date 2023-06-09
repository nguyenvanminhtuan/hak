from typing import TypeVar, Generic, Type, Any, Optional, List, Union, Dict

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from hak.databases.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class RepositoryBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    # noinspection PyShadowingBuiltins
    def get(self, session: Session, id: Any) -> Optional[ModelType]:
        return session.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, session: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        # noinspection PyTypeChecker
        return session.query(self.model).offset(skip).limit(limit).all()

    def create(self, session: Session, *, data: CreateSchemaType) -> ModelType:
        obj = self.model(**data.json())  # type: ignore
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    # noinspection PyMethodMayBeStatic
    def update(self, session: Session, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    # noinspection PyShadowingBuiltins
    def remove(self, session: Session, *, id: Any) -> ModelType:
        obj = session.query(self.model).get(id)
        session.delete(obj)
        session.commit()
        return obj
