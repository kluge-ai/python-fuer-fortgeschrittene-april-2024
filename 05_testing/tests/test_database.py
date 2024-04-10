"""
Aufgabe 1: Schreibe Unit-Tests, die mit einem gemockten StorageClient arbeiten.

Aufgabe 2: Schreibe Integrations-Tests, die mit einem echten StorageClient arbeiten.
           Lagere dabei die Initialisierung des DatabaseClients in eine Fixture aus.
"""

import pytest

from my_cloud.database import DatabaseClient
from my_cloud.exceptions import ResourceNotFoundException


def test_database_initialization(mocker):
    # GIVEN
    storage_mock = mocker.Mock()

    # WHEN
    db = DatabaseClient(storage_client=storage_mock)

    # THEN
    name, args, kwargs = storage_mock.create_bucket.mock_calls[0]
    assert args[0] == "_meta"


def test_table_creation(mocker):
    # GIVEN
    storage_mock = mocker.Mock()

    # WHEN
    db = DatabaseClient(storage_client=storage_mock)
    db.create_table("my-first-table", ("id",))

    # THEN
    name, args, kwargs = storage_mock.create_bucket.mock_calls[1]
    assert args[0] == "my-first-table"


def test_list_tables(mocker):
    # GIVEN
    storage_mock = mocker.Mock()
    storage_mock.list_buckets.return_value = ["table_1", "_meta"]
    db = DatabaseClient(storage_client=storage_mock)

    # WHEN
    tables = db.list_tables()

    # THEN
    assert "table_1" in tables
    assert "_meta" not in tables


def test_get_item(mocker):
    # GIVEN
    storage_mock = mocker.Mock()


def test_that_getting_item_that_doesnt_exist_raises_exception(mocker):
    # GIVEN
    storage_mock = mocker.Mock()




