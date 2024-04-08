import pathlib

from storage import StorageClient

CURRENT_DIR = pathlib.Path(__file__).parent


c = StorageClient(CURRENT_DIR)

assert c.list_buckets() == []

c.create_bucket("my-first-bucket")

assert c.list_buckets() == ["my-first-bucket"]

c.put_object("my-first-bucket", "file0.txt", "FIRST")
c.put_object("my-first-bucket", "file1.txt", "SECOND")

assert "file0" in c.list_objects("my-first-bucket")
assert "file1" in c.list_objects("my-first-bucket")

c.create_bucket("my-second-bucket")

c.put_object("my-second-bucket", "folder0/file3.txt", "THIRD")

assert "folder0/file3.txt" in c.list_objects("my-second-bucket")

c.put_object("my-second-bucket", "file4.txt", "FOURTH")
