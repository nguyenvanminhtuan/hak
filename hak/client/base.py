from typing import TypeVar, Generic

ClientT = TypeVar("ClientT")


class BaseClient(Generic[ClientT]):
    pass
