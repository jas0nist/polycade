#!/usr/bin/env python3
import json
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Path to the JSON files
GAMES_FILE_PATH = './games.json'
TITLES_FILE_PATH = './game-titles.json'

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

def update_game_names(games_data, names_data):
    """Update game names in the games data."""
    for game_data in games_data.get('gamesMetadata', {}).values():
        title = game_data.get('title', 'No Title')
        for name in names_data:
            origin = name.get('origin-title', 'No Title')
            if origin == title:
                update = name.get('update-title', 'No Title')
                if update != title:
                    game_data['title'] = update
                    originData = game_data.get('originData', {})
                    originData['title'] = update
                    game = game_data.get('game', {})
                    game['title'] = update
                    for game in games_data.get('gameSUIDsData', {}).values():
                        if game['title'] == title:
                            game['title'] = update
                    logging.debug(f"Updated game title: {title} to {update}")
                else:
                    logging.debug(f"Game already has updated title: {title}")
                break

def main():
    """Main function to load, update, and save game data."""
    try:
        names_data = load_json(TITLES_FILE_PATH)
        games_data = load_json(GAMES_FILE_PATH)

        update_game_names(games_data, names_data)

        save_json(GAMES_FILE_PATH, games_data)
        logging.info(f"Updated games data written to {GAMES_FILE_PATH}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
    