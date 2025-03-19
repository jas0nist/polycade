# Maintain Polycade AGS `games.json` manual edits

## Script Descriptions

### `games-json.py`

This script serves as a wrapper for managing and interacting with `Polycade AGS games.json` related functionalities.

Command Line Options:

The following command line options are available for `games-json.py`:

- `-h, --help`: Show this help message and exit.
- `--backup-titles`: Backup all game titles to a secure location.
- `--backup-controllers`: Backup all game controller configurations.
- `--restore-controllers`: Restore game controller configurations from a backup.
- `--update-titles`: Update game titles with the latest information.

---

### `games-controller-backup.py`
This script is designed to analyze and back up the controller configurations listed in the `Polycade AGS games.json` file. It extracts the controller data and generates a separate `game-controllers.json` file to ensure the configurations are preserved for future use.

---

### `games-controller-restore.py`
This script restores custom controller configurations in `Polycade AGS games.json` using the data stored in `game-controllers.json`. It ensures that the controller settings are accurately updated based on the backup file.

---

### `games-title-backup.py`

This script is responsible for creating a backup of game titles.
It reads the existing game titles from `Polycade AGS games.json`,
and saves a copy of the titles to `game-titles.json`.
The backup ensures that game title data can be updated and restored in case of accidental loss or corruption.

---

### `games-title-update.py`

This script is used to update game titles in `Polycade AGS games.json`.
It allows modifications to existing game titles using the title-update key in `game-titles.json`.
The script ensures that updates are applied correctly and consistently.

---