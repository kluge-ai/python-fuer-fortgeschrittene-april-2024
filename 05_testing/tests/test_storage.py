"""
Aufgabe 1: Übertrage die Testaufrufe aus der Datei "check_storage.py" in Tests.

Aufgabe 2: Schreibe Tests, die die Ablage im Dateisystem überprüfen.

Aufgabe 3: Bringe die Testabdeckung auf 100%, indem du Tests für die Ausnahmebehandlung schreibst.
"""
import pytest
from my_cloud.storage import StorageClient
from my_cloud.exceptions import ResourceAlreadyExistsException


@pytest.mark.parametrize("foo", [1, 2, 3])
def test_that_bucket_can_be_created(tmp_path, foo):
    # GIVEN
    c = StorageClient(tmp_path)

    # THEN
    c.create_bucket("my-test-bucket")

    assert "my-test-bucket" in c.list_buckets()


def test_that_bucket_names_must_be_unique(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)
    c.create_bucket("my-test-bucket")

    # WHEN/THEN
    with pytest.raises(ResourceAlreadyExistsException):
        c.create_bucket("my-test-bucket")


def test_that_bucket_creation_creates_folder(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)

    # WHEN
    c.create_bucket("my-test-bucket")

    # THEN
    assert (tmp_path / "my-test-bucket").exists()
    assert (tmp_path / "my-test-bucket").is_dir()


def test_that_storage_client_discovers_existing_files(tmp_path):
    ...


def test_that_storage_client_deletes_data_from_disk(tmp_path):
    ...

