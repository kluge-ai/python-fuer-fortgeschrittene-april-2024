"""
Aufgabe 1: Übertrage die Testaufrufe aus der Datei "check_storage.py" in Tests.

Aufgabe 2: Schreibe Tests, die die Ablage im Dateisystem überprüfen.

Aufgabe 3: Bringe die Testabdeckung auf 100%, indem du Tests für die Ausnahmebehandlung schreibst.
"""

import pytest
from my_cloud.storage import StorageClient
from my_cloud.exceptions import ResourceAlreadyExistsException, ResourceNotFoundException


def test_that_bucket_can_be_created(tmp_path):
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
    # GIVEN
    (tmp_path / "my-test-bucket").mkdir()
    (tmp_path / "my-test-bucket" / "file1.txt").write_text("bla")
    (tmp_path / "my-test-bucket" / "file2.txt").write_text("bla")

    # WHEN
    c = StorageClient(tmp_path)

    # THEN
    assert set(c.list_objects("my-test-bucket")) == {"file1.txt", "file2.txt"}


def test_that_storage_client_writes_data_to_disk(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)
    c.create_bucket("my-test-bucket")

    # WHEN
    c.put_object("my-test-bucket", "file1.txt", "bla")

    # THEN
    assert (tmp_path / "my-test-bucket" / "file1.txt").exists()
    assert (tmp_path / "my-test-bucket" / "file1.txt").read_text() == "bla"


def test_that_storage_client_fetches_data_from_disk(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)
    c.create_bucket("my-test-bucket")
    (tmp_path / "my-test-bucket" / "file1.txt").write_text("bla")

    # WHEN
    data = c.get_object("my-test-bucket", "file1.txt")

    # THEN
    assert data == "bla"


def test_that_storage_client_deletes_data_from_disk(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)
    c.create_bucket("my-test-bucket")
    (tmp_path / "my-test-bucket" / "file1.txt").write_text("bla")

    # WHEN
    c.delete_object("my-test-bucket", "file1.txt")

    # THEN
    assert not (tmp_path / "my-test-bucket" / "file1.txt").exists()


def test_that_fetching_file_from_nonexistant_bucket_is_handled_gracefully(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)

    # WHEN/THEN
    with pytest.raises(ResourceNotFoundException):
        c.get_object("my-test-bucket", "file1.txt")


def test_that_writing_to_nonexistant_bucket_is_handled_gracefully(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)

    # WHEN/THEN
    with pytest.raises(ResourceNotFoundException):
        c.put_object("my-test-bucket", "file1.txt", "bla")


def test_that_fetching_nonexistant_file_is_handled_gracefully(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)
    c.create_bucket("my-test-bucket")

    # WHEN/THEN
    with pytest.raises(ResourceNotFoundException):
        c.get_object("my-test-bucket", "file1.txt")


def test_that_deleting_nonexistant_file_is_handled_gracefully(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)
    c.create_bucket("my-test-bucket")

    # WHEN/THEN
    with pytest.raises(ResourceNotFoundException):
        c.delete_object("my-test-bucket", "file1.txt")

