import pathlib

class StorageClient:

    def __init__(self, root):
        """Initialisiere einen neuen Speicher im Verzeichnis `root`."""
        self.root = root

    def create_bucket(self, bucket):
        """Erzeuge einen Bucket mit Namen `bucket`."""
        (self.root / bucket).mkdir(exist_ok=True)

    def list_buckets(self):
        """Gebe eine Liste aller Buckets im Speicher zurück."""
        return [folder.name for folder in self.root.iterdir() if folder.is_dir()
                and not folder.name.startswith("_")]

    def put_object(self, bucket, key, body):
        """Speichere eine Datei mit dem Inhalt `body` unter dem Schlüssel/Pfad `key` im Bucket `bucket`."""
        location = (self.root / bucket / pathlib.Path(key))
        location.parent.mkdir(parents=True, exist_ok=True)
        with open(location, "wt") as f:
            f.write(body)

    def list_objects(self, bucket):
        """Gebe eine Liste aller Dateien im Bucket `bucket` zurück."""
        all_files = []
        for path, folders, files in (self.root / bucket).walk():
            all_files += [str(path.relative_to(self.root / bucket) / file) for file in files]
        return all_files

    def get_object(self, bucket, key):
        """Lade die Datei unter dem Schlüssel/Pfad `key` im Bucket `bucket`."""
        with open(self.root / bucket / pathlib.Path(key), "rt") as f:
            return f.read()
