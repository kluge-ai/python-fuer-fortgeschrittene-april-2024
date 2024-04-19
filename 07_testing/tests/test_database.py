"""
Aufgabe 1: Schreibe Unit-Tests, die mit einem gemockten StorageClient arbeiten.

Aufgabe 2: Schreibe Integrations-Tests, die mit einem echten StorageClient arbeiten.
           Lagere dabei die Initialisierung des DatabaseClients in eine Fixture aus.
"""

import pytest

from my_cloud.database import DatabaseClient
from my_cloud.exceptions import ResourceNotFoundException
from my_cloud.storage import StorageClient


@pytest.mark.unit
def test_database_initialization(mocker):
    # GIVEN
    storage_mock = mocker.Mock()

    # WHEN
    db = DatabaseClient(storage_client=storage_mock)

    # THEN
    name, args, kwargs = storage_mock.create_bucket.mock_calls[0]
    assert args[0] == "_meta"


@pytest.mark.unit
def test_table_creation(mocker):
    # GIVEN
    storage_mock = mocker.Mock()

    # WHEN
    db = DatabaseClient(storage_client=storage_mock)
    db.create_table("my-first-table", ("id",))

    # THEN
    name, args, kwargs = storage_mock.create_bucket.mock_calls[1]
    assert args[0] == "my-first-table"


@pytest.mark.unit
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


@pytest.mark.unit
def test_get_item(mocker):
    # GIVEN
    storage_mock = mocker.Mock()
    storage_mock.list_buckets.return_value = ["my-table", "_meta"]
    storage_mock.get_object.return_value = '{"key": "value"}'
    db = DatabaseClient(storage_client=storage_mock)

    get_key_schema_mock = mocker.patch.object(db, "_get_key_schema")
    get_key_mock = mocker.patch.object(db, "_get_key")
    get_key_mock.return_value = "my-hashed-key"

    # WHEN
    item = db.get_item("my-table", ("my-item",))

    # THEN
    get_key_schema_mock.assert_called_once_with("my-table")
    get_key_mock.assert_called_once()

    name, args, kwargs = storage_mock.get_object.mock_calls[0]
    assert args == ("my-table", "my-hashed-key")

    assert item == {"key": "value"}


@pytest.mark.unit
def test_that_getting_item_that_doesnt_exist_raises_exception(mocker):
    # GIVEN
    storage_mock = mocker.Mock()
    storage_mock.list_buckets.return_value = ["my-table", "_meta"]
    storage_mock.get_object.side_effect = ResourceNotFoundException

    db = DatabaseClient(storage_client=storage_mock)

    mocker.patch.object(db, "_get_key_schema")
    get_key_mock = mocker.patch.object(db, "_get_key")
    get_key_mock.return_value = "my-hashed-key"

    # WHEN
    with pytest.raises(ResourceNotFoundException):
        _ = db.get_item("my-table", ("my-item",))


@pytest.fixture
def tmp_database_client(tmp_path):
    storage_client = StorageClient(tmp_path)
    db = DatabaseClient(storage_client=storage_client)
    yield db


@pytest.mark.integration
def test_that_items_can_be_fetched_as_a_batch(tmp_database_client):
    # GIVEN
    tmp_database_client.create_table("my-table", ("name", "age"))

    alice = {"name": "Alice", "age": 30, "location": "Hannover"}
    bob = {"name": "Bob", "age": 50, "location": "Lehrte"}
    for person in [alice,
                   bob]:
        tmp_database_client.put_item("my-table", person)

    # WHEN
    result = tmp_database_client.batch_get_items("my-table", [("Alice", 30),
                                                              ("Bob", 50)])

    # THEN
    result = list(result)
    assert len(result) == 2
    assert alice in result
    assert bob in result


@pytest.mark.integration
def test_that_item_keys_are_unique(tmp_database_client):
    # GIVEN
    tmp_database_client.create_table("my-table", ("id",))

    # WHEN
    tmp_database_client.put_item("my-table", {"id": "abc-123", "name": "Chris"})
    tmp_database_client.put_item("my-table", {"id": "abc-123", "name": "Derek"})

    # THEN
    assert tmp_database_client.describe_table("my-table")["items"] == 1

    item = tmp_database_client.get_item("my-table", ("abc-123",))
    assert item["name"] == "Derek"
