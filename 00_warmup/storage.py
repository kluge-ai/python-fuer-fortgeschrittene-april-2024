class StorageClient:
    def __init__(self, root):
        """Initialisiere einen neuen Speicher im Verzeichnis `root`."""
        ...

    def create_bucket(self, bucket):
        """Erzeuge einen Bucket mit Namen `bucket`."""
        ...

    def list_buckets(self):
        """Gebe eine Liste aller Buckets im Speicher zurück."""
        ...

    def put_object(self, bucket, key, body):
        """Speichere eine Datei mit dem Inhalt `body` unter dem Schlüssel/Pfad `key` im Bucket `bucket`."""
        ...

    def list_objects(self, bucket):
        """Gebe eine Liste aller Dateien im Bucket `bucket` zurück."""
        ...

    def get_object(self, bucket, key):
        """Lade die Datei unter dem Schlüssel/Pfad `key` im Bucket `bucket`."""
        ...
