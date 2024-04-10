"""
Aufgabe: Schreibe mindestens drei weitere Tests für die Funktion "can"
"""

import pytest
import itertools

from my_cloud.identity import generate_user, User, Permission, can


def test_that_user_can_be_generated():
    user = generate_user(name="kilian")
    assert user.name == "kilian"


def test_that_two_users_have_different_ids():
    user1 = generate_user(name="kilian")
    user2 = generate_user(name="otto")

    assert user1.name == "kilian"
    assert user2.name == "otto"
    assert user1.id != user2.id


@pytest.mark.xfail
def test_that_permission_requires_at_least_one_action():
    # GIVEN
    permission = Permission(
        user_name="kilian",
        resource_name="my-bucket",
        resource_kind="bucket",
        actions=[],
    )

    # WHEN/THEN
    assert not permission.is_valid()


def test_that_user_name_has_to_match():
    # GIVEN
    user1 = User(name="kilian")
    user2 = User(name="otto")
    permission = Permission(
        user_name="kilian",
        resource_name="my-bucket",
        resource_kind="bucket",
        actions=["read"],
    )

    # WHEN
    is_user1_allowed = can(
        user=user1,
        permission=permission,
        resource_name="my-bucket",
        resource_kind="bucket",
        action="read",
    )

    is_user2_allowed = can(
        user=user2,
        permission=permission,
        resource_name="my-bucket",
        resource_kind="bucket",
        action="read",
    )
    # THEN
    assert is_user1_allowed
    assert not is_user2_allowed


@pytest.mark.parametrize("resource_kind", [("bucket",), ("table",)])
@pytest.mark.parametrize("action", [("read",), ("write",), ("delete",)])
def test_that_user_can_perform_action_on_resource(resource_kind, action):
    # GIVEN
    user = User(name="kilian")
    permission = Permission(
        user_name="kilian",
        resource_name="my-bucket",
        resource_kind=resource_kind,
        actions=[action],
    )

    # WHEN
    is_user_allowed = can(
        user=user,
        permission=permission,
        resource_name="my-bucket",
        resource_kind=resource_kind,
        action=action,
    )

    # THEN
    assert is_user_allowed


resource_action_pairs = list(
    itertools.product(["bucket", "table"], ["read", "write", "delete", "create"])
)


@pytest.mark.parametrize("resource_kind,action", resource_action_pairs)
def test_that_user_can_perform_action_on_resource_2(resource_kind, action):
    # GIVEN
    user = User(name="kilian")
    permission = Permission(
        user_name="kilian",
        resource_name="my-bucket",
        resource_kind=resource_kind,
        actions=[action],
    )

    # WHEN
    is_user_allowed = can(
        user=user,
        permission=permission,
        resource_name="my-bucket",
        resource_kind=resource_kind,
        action=action,
    )

    # THEN
    assert is_user_allowed
