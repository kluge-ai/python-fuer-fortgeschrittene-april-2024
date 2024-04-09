import pathlib

from .exceptions import ResourceAlreadyExistsException, ResourceNotFoundException


class StorageClient:
    def __init__(self, root: pathlib.Path) -> None:
        """Initialisiere einen neuen Speicher im Verzeichnis `root`."""
        root.mkdir(parents=True, exist_ok=True)
        self.root = root

    def create_bucket(self, bucket: str) -> None:
        """Erzeuge einen Bucket mit Namen `bucket`."""
        location = self.root / bucket
        if location.exists():
            raise ResourceAlreadyExistsException(f"Bucket {bucket} already exists.")
        location.mkdir(exist_ok=False)

    def list_buckets(self) -> list[str]:
        """Gebe eine Liste aller Buckets im Speicher zurück."""
        return [
            folder.name
            for folder in self.root.iterdir()
            if folder.is_dir() and not folder.name.startswith("__")
        ]

    def put_object(self, bucket: str, key: str, body: str) -> None:
        """Speichere eine Datei mit dem Inhalt `body` unter dem Schlüssel/Pfad `key` im Bucket `bucket`."""
        bucket_path = self._validate_bucket(bucket)
        location = bucket_path / pathlib.Path(key)
        location.parent.mkdir(parents=True, exist_ok=True)
        with open(location, "wt") as f:
            f.write(body)

    def list_objects(self, bucket: str) -> list[str]:
        """Gebe eine Liste aller Dateien im Bucket `bucket` zurück."""
        bucket_path = self._validate_bucket(bucket)

        all_files = []
        for path, folders, files in bucket_path.walk():
            all_files += [
                str(path.relative_to(bucket_path) / file) for file in files
            ]
        return all_files

    def get_object(self, bucket: str, key: str) -> str:
        """Lade die Datei unter dem Schlüssel/Pfad `key` im Bucket `bucket`."""
        bucket_path = self._validate_bucket(bucket)

        try:
            with open(bucket_path / pathlib.Path(key), "rt") as f:
                return f.read()
        except FileNotFoundError:
            raise ResourceNotFoundException(f"Object {key} in bucket {bucket} does not exist.")

    def delete_object(self, bucket: str, key: str) -> None:
        """Lösche die Datei unter dem Schlüssel/Pfad `key` im Bucket `bucket`."""
        bucket_path = self._validate_bucket(bucket)

        try:
            (bucket_path / pathlib.Path(key)).unlink()
        except FileNotFoundError:
            raise ResourceNotFoundException(f"Object {key} in bucket {bucket} does not exist.")

    def _validate_bucket(self, bucket: str) -> pathlib.Path:
        bucket_path = self.root / bucket
        if not bucket_path.exists():
            raise ResourceNotFoundException(f"Bucket {bucket} does not exist.")
        return bucket_path
