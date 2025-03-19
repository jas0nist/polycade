# Managing Polycade AGS `games.json` Manual Edits

## Overview of Scripts

### `games-json.py`

A versatile script for managing and interacting with functionalities related to the `Polycade AGS games.json` file.

#### Command Line Options:

- `-h, --help`: Display the help message and exit.
- `--backup-controllers`: Save all game controller configurations to a backup file.
- `--backup-titles`: Create a secure backup of all game titles.
- `--restore-controllers`: Restore game controller configurations from a backup file.
- `--update-titles`: Update game titles with the latest information.

---

### `games-controller-backup.py`

This script extracts and backs up controller configurations from the `Polycade AGS games.json` file. The configurations are saved in a separate `game-controllers.json` file, ensuring they are preserved for future use.

---

### `games-controller-restore.py`

This script restores controller configurations in the `Polycade AGS games.json` file using data from the `game-controllers.json` backup. It ensures accurate and consistent restoration of controller settings.

---

### `games-title-backup.py`

This script creates a backup of game titles by reading the existing titles from the `Polycade AGS games.json` file and saving them to a `game-titles.json` file. The backup safeguards against accidental data loss or corruption.

---

### `games-title-update.py`

This script updates game titles in the `Polycade AGS games.json` file. It uses the `title-update` key in the `game-titles.json` file to apply modifications, ensuring updates are applied correctly and consistently.

---
