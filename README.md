# Maintain Polycade AGS `games.json` manual edits

## Script Descriptions

### `games-controller-backup.py`
This script is designed to analyze and back up the controller configurations listed in the `games.json` file. It extracts the controller data and generates a separate `game-controllers.json` file to ensure the configurations are preserved for future use.

---

### `games-controller-restore.py`
This script restores controller configurations in `games.json` using the data stored in `game-controllers.json`. It ensures that the controller settings are accurately updated based on the backup file.

---

### `games-title-backup.py`

This script is responsible for creating a backup of game titles.
It reads the existing game titles from a source (e.g., a database or file),
and saves a copy of the titles to a backup location for safekeeping.
The backup ensures that game title data can be restored in case of accidental loss or corruption.

---

### `games-title-update.py`

This script is used to update game titles in the source system.
It allows modifications to existing game titles.
The script ensures that updates are applied correctly and consistently.

---