import json
import hashlib

from .exceptions import ResourceAlreadyExistsException, ResourceNotFoundException
from .storage import StorageClient

from typing import Any, Iterable


class DatabaseClient:
    _meta_bucket_name = "_meta"
    _hash_algorithm = hashlib.sha256

    def __init__(self, storage_client: StorageClient):
        """Initialisiere einen neuen DatabaseClient mit einem StorageClient als Backend."""
        self.storage_client = storage_client

        try:
            self.storage_client.create_bucket(self._meta_bucket_name)
        except ResourceAlreadyExistsException:
            pass

    def create_table(self, table_name: str, key_schema: tuple[str, ...]):
        """Lege eine neue Tabelle an.

        `key_schema` enthält mindestens ein Feld, das den Index/Key bildet.
        """
        self.storage_client.create_bucket(table_name)
        self.storage_client.put_object(
            self._meta_bucket_name, table_name, json.dumps(list(key_schema))
        )

    def _get_key_schema(self, table_name: str) -> tuple[str, ...]:
        return tuple(json.loads(self.storage_client.get_object(self._meta_bucket_name, table_name)))

    def describe_table(self, table_name: str) -> dict[str, Any]:
        """Gebe den Key und weitere Informationen zu der Tabelle `table_name` zurück."""
        return {
            "key_schema": self._get_key_schema(table_name),
            "items": len(self.storage_client.list_objects(table_name))
        }

    def list_tables(self) -> list[str]:
        """Gebe eine Liste aller vorhandenen Tabellen zurück."""
        return [bucket_name for bucket_name in self.storage_client.list_buckets()
                if bucket_name != self._meta_bucket_name]

    def _get_key(self, item: dict[str, Any], key_schema: tuple[str, ...]) -> str:
        return "/".join([self._hash_algorithm(str(item[key]).encode()).hexdigest() for key in key_schema])

    def put_item(self, table_name: str, item: dict[str, Any]):
        """Speichere das Item `item` in der Tabelle `table_name`."""
        key_schema = self._get_key_schema(table_name)
        hashed_key = self._get_key(item, key_schema)
        self.storage_client.put_object(table_name, hashed_key, json.dumps(item))

    def batch_put_items(self, table_name: str, items: Iterable[dict[str, Any]]):
        """Speichere alle Items in `items` in der Tabelle `table_name`."""
        for item in items:
            self.put_item(table_name, item)

    def get_item(self, table_name, key: tuple[Any, ...]) -> dict[str, Any]:
        """Hole das Item mit Schlüssel `key` aus der Tabelle `table_name`."""
        key_schema = self._get_key_schema(table_name)
        hashed_key = self._get_key(dict(zip(key_schema, key)), key_schema)
        try:
            return json.loads(self.storage_client.get_object(table_name, hashed_key))
        except ResourceNotFoundException:
            raise ResourceNotFoundException(f"Item with key {key} does not exist in table {table_name}.")

    def batch_get_items(self, table_name: str, keys: Iterable[tuple[Any, ...]]) -> Iterable[dict[str, Any]]:
        """Hole die Items mit Schlüsseln `keys` aus der Tabelle `table_name`."""
        return (self.get_item(table_name, key) for key in keys)

    def delete_item(self, table_name: str, key: tuple[Any, ...]):
        """Lösche das Item mit Schlüssel `key` aus der Tabelle `table_name`."""
        key_schema = self._get_key_schema(table_name)
        hashed_key = self._get_key(dict(zip(key_schema, key)), key_schema)
        try:
            self.storage_client.delete_object(table_name, hashed_key)
        except ResourceNotFoundException:
            raise ResourceNotFoundException(f"Item with key {key} does not exist in table {table_name}.")
