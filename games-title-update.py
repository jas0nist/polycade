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
TITLES_FILE_PATH = './game-titles.json'
"""Generate a unique backup file name with a timestamp"""
GAMES_BACKUP_PATH = f'./games-backup-title-{datetime.now().strftime("%Y%m%d%H%M%S")}.json'

def backup_file(original_path, backup_path):
    """Create a backup of the original file."""
    try:
        shutil.copy(original_path, backup_path)
        logging.info(f"Backup created successfully: {backup_path}")
    except FileNotFoundError:
        logging.error(f"Original file not found: {original_path}")
        raise
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
            logging.debug(f"Saved JSON data to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save JSON to {file_path}: {e}")
        raise

def update_game_names(games_data, names_data):
    """Update game names in the games data."""
    games_metadata = games_data.get('gamesMetadata', {})
    game_suids_data = games_data.get('gameSUIDsData', {})

    for game_data in games_metadata.items():
        original_title = game_data.get('title', 'No Title')
        for name_entry in names_data:
            origin_title = name_entry.get('origin-title', 'No Title')
            if origin_title == original_title:
                updated_title = name_entry.get('update-title', 'No Title')
                if updated_title != original_title:
                    game_data['title'] = updated_title
                    game_data.setdefault('originData', {})['title'] = updated_title
                    game_data.setdefault('game', {})['title'] = updated_title

                    # Update titles in gameSUIDsData
                    for suid, suid_data in game_suids_data.items():
                        if suid_data.get('title') == original_title:
                            suid_data['title'] = updated_title

                    logging.info(f"Updated game title: '{original_title}' to '{updated_title}'")
                else:
                    logging.debug(f"Game already has the updated title: '{original_title}'")
                break

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
        names_data = load_json(TITLES_FILE_PATH)
        games_data = load_json(GAMES_FILE_PATH)

        """Update game names"""
        update_game_names(games_data, names_data)

        """Save the updated games data"""
        save_json(GAMES_FILE_PATH, games_data)
        logging.info(f"Updated games data successfully written to {GAMES_FILE_PATH}")
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")

if __name__ == '__main__':
    main()