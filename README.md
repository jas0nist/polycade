# Maintain Polycade AGS `games.json` manual edits

## Script Descriptions

### `games-controller-backup.py`
This script is designed to analyze and back up the controller configurations listed in the `games.json` file. It extracts the controller data and generates a separate `game-controllers.json` file to ensure the configurations are preserved for future use.

**Key Features:**
- Reads and processes controller configurations from `games.json`.
- Creates a structured backup in `game-controllers.json`.
- Ensures data consistency and integrity during the backup process.

**Usage:**
Run this script to safeguard controller configurations before making any changes to `games.json`. This ensures that the original settings can be restored if needed.

---

### `games-controller-restore.py`
This script restores controller configurations in `games.json` using the data stored in `game-controllers.json`. It ensures that the controller settings are accurately updated based on the backup file.

**Key Features:**
- Reads controller data from `game-controllers.json`.
- Updates the `games.json` file with the restored configurations.
- Validates the restored data to prevent errors or inconsistencies.

**Usage:**
Use this script to revert to a previously backed-up state of controller configurations. Ensure that the `game-controllers.json` file is up-to-date and accurate before running this script.

### `games-title-backup.py`
"""
This script is responsible for creating a backup of game titles.
It reads the existing game titles from a source (e.g., a database or file),
and saves a copy of the titles to a backup location for safekeeping.
The backup ensures that game title data can be restored in case of accidental loss or corruption.

**Key Features:**
- Reads game titles from the source.
- Saves the titles to a backup file or storage.
- Ensures data integrity during the backup process.

Usage:
Run this script periodically or before performing operations that might affect the game titles.
"""

### `games-title-update.py`
"""
This script is used to update game titles in the source system.
It allows modifications to existing game titles.
The script ensures that updates are applied correctly and consistently.

**Key Features:**
- Reads the current list of game titles.
- Applies updates or additions to the titles.
- Validates the changes to prevent errors or inconsistencies.

Usage:
Run this script whenever updates to game titles are required.
Ensure that a backup of the titles is created using `games-title-backup.py` before running this script.
"""