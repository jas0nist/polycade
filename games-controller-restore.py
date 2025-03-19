#!/usr/bin/env python3
import json
import logging
import shutil
import os
import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Path to the JSON files
GAMES_FILE_PATH = './games.json'
CONTROLLERS_FILE_PATH = './game-controllers.json'
# Generate a unique backup file name with a timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
GAMES_BACKUP_PATH = f'./games-backup-{timestamp}.json'

def backup_file(original_path, backup_path):
    """Create a backup of the original file."""
    try:
        shutil.copy(original_path, backup_path)
        logging.info(f"Backup created: {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Failed to load JSON from {file_path}: {e}")
        raise

def save_json(file_path, data):
    """Save JSON data to a file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Failed to save JSON to {file_path}: {e}")
        raise

def update_game_controllers(games_data, controllers_data):
    """Update game controllers in the games data."""
    for game_key, game_data in games_data.get('gamesMetadata', {}).items():
        title = game_data.get('title', 'No Title')
        for controller in controllers_data:
            if controller['title'] == title:
                tags = game_data.setdefault('tags', [])
                if not any('Controller Type' in tag.get('name', '') for tag in tags):
                    tags.append({
                        "id": controller.get('id', 'No ID'),
                        "icon": controller.get('icon', 'No Icon'),
                        "name": controller.get('name', 'No Name'),
                        "packages": controller.get('packages', [])
                    })
                    logging.debug(f"Added controller data to game: {title}")
                else:
                    logging.debug(f"Game already has controller data: {title}")
                break

def main():
    """Main function to load, update, and save game data."""
    try:
        # Create a backup of the original games.json file
        if os.path.exists(GAMES_FILE_PATH):
            backup_file(GAMES_FILE_PATH, GAMES_BACKUP_PATH)

        controllers_data = load_json(CONTROLLERS_FILE_PATH)
        games_data = load_json(GAMES_FILE_PATH)

        update_game_controllers(games_data, controllers_data)

        save_json(GAMES_FILE_PATH, games_data)
        logging.info(f"Updated games data written to {GAMES_FILE_PATH}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
