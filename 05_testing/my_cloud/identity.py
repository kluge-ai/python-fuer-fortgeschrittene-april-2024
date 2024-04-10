import uuid
from dataclasses import dataclass, field
from typing import Literal


@dataclass
class User:
    name: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


def generate_user(name: str) -> User:
    return User(name)


RESOURCES = Literal["bucket", "table"]
ACTIONS = Literal["read", "write", "delete", "create"]


@dataclass
class Permission:
    user_name: str
    resource_name: str
    resource_kind: RESOURCES
    actions: list[ACTIONS]

    def is_valid(self) -> bool:
        return True


def can(
    user: User,
    permission: Permission,
    resource_name: str,
    resource_kind: RESOURCES,
    action: ACTIONS,
) -> bool:
    if user.name != permission.user_name:
        return False
    if resource_kind != permission.resource_kind:
        return False
    if resource_name != permission.resource_name:
        return False
    if action not in permission.actions:
        return False
    return True
