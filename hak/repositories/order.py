from typing import Generic

from hak.databases.models.order import Order
from hak.repositories.base import BaseRepository
from hak.schemas.order import OrderCreate, OrderUpdate


class OrderRepository(BaseRepository, Generic[Order, OrderCreate, OrderUpdate]):
    pass

