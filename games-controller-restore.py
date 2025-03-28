#!/usr/bin/env python3
import json
import logging
import shutil
import os
from datetime import datetime

"""Configure logging"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

"""Path to the JSON file"""
GAMES_FILE_PATH = './games.json'
CONTROLLERS_FILE_PATH = './game-controllers.json'
"""Generate a unique backup file name with a timestamp"""
GAMES_BACKUP_PATH = f'./games-backup-controller-{datetime.now().strftime("%Y%m%d%H%M%S")}.json'

def backup_file(original_path, backup_path):
    """Create a backup of the original file."""
    if not os.path.exists(original_path):
        logging.warning(f"File not found for backup: {original_path}")
        return
    try:
        shutil.copy(original_path, backup_path)
        logging.info(f"Backup created: {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise

def load_json(file_path):
    """Load JSON data from a file."""
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON format in {file_path}: {e}")
        raise
    except Exception as e:
        logging.error(f"Failed to load JSON from {file_path}: {e}")
        raise

def save_json(file_path, data):
    """Save JSON data to a file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save JSON to {file_path}: {e}")
        raise

def update_game_controllers(games_data, controllers_data):
    """Update game controllers in the games data."""
    games_metadata = games_data.get('gamesMetadata', {})
    for game_data in games_metadata.items():
        title = game_data.get('title', 'No Title')
        matching_controller = next((c for c in controllers_data if c['title'] == title), None)
        if matching_controller:
            tags = game_data.setdefault('tags', [])
            if not any('Controller Type' in tag.get('name', '') for tag in tags):
                tags.append({
                    "id": matching_controller.get('id', 'No ID'),
                    "icon": matching_controller.get('icon', 'No Icon'),
                    "name": matching_controller.get('name', 'No Name'),
                    "packages": matching_controller.get('packages', [])
                })
                logging.debug(f"Added controller data to game: {title}")
            else:
                logging.debug(f"Game already has controller data: {title}")
        else:
            logging.debug(f"No matching controller found for game: {title}")

def main():
    """Main function to load, update, and save game data."""
    try:
        """Check if the games file exists and create a backup"""
        if os.path.exists(GAMES_FILE_PATH):
            backup_file(GAMES_FILE_PATH, GAMES_BACKUP_PATH)
        else:
            logging.error(f"Games file not found: {GAMES_FILE_PATH}")
            return

        """Load JSON data"""
        controllers_data = load_json(CONTROLLERS_FILE_PATH)
        games_data = load_json(GAMES_FILE_PATH)

        """Restore controller types"""
        update_game_controllers(games_data, controllers_data)

        """Save the updated games data"""
        save_json(GAMES_FILE_PATH, games_data)
        logging.info(f"Updated games data written to {GAMES_FILE_PATH}")
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")

if __name__ == '__main__':
    main()
