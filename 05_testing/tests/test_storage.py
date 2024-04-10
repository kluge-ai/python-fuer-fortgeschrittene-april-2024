"""
Aufgabe 1: Übertrage die Testaufrufe aus der Datei "check_storage.py" in Tests.

Aufgabe 2: Schreibe Tests, die die Ablage im Dateisystem überprüfen.

Aufgabe 3: Bringe die Testabdeckung auf 100%, indem du Tests für die Ausnahmebehandlung schreibst.
"""
import pytest
from my_cloud.storage import StorageClient
from my_cloud.exceptions import ResourceAlreadyExistsException


def test_that_bucket_can_be_created(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)

    # THEN
    c.create_bucket("my-test-bucket")


def test_that_bucket_names_must_be_unique(tmp_path):
    # GIVEN
    c = StorageClient(tmp_path)
    c.create_bucket("my-test-bucket")

    # THEN
    with pytest.raises(ResourceAlreadyExistsException):
        c.create_bucket("my-test-bucket")

