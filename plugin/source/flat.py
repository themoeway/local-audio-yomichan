import sqlite3

from pathlib import Path

from .audio_source import AudioSource


SQL = "INSERT INTO entries (expression, reading, source, speaker, display, file) VALUES (?,?,?,?,?,?)"


class FlatDirAudioSource(AudioSource):
    """
    A simple source type for directories containing audio files directly (optionally nested).

    - expression: filename stem
    - reading: NULL (matches any reading)
    - file: path relative to the source directory
    """

    def add_entries(self, connection: sqlite3.Connection):
        cur = connection.cursor()
        base_dir = self.get_media_dir_path()

        for path in self.find_media_files():
            relpath = path.relative_to(base_dir)
            expression = path.stem
            cur.execute(SQL, (expression, None, self.data.id, None, None, str(relpath)))

        cur.close()
        connection.commit()

