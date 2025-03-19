#!/usr/bin/env python3
import json
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Path to the JSON file
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

def extract_game_titles(games_data):
    """Extract game titles."""
    output_list = []
    games_metadata = games_data.get('gamesMetadata', {})
    
    for game_key, game_data in games_metadata.items():
        title = game_data.get('title', 'No Title')
        output_list.append({
            "key": game_key,
            "origin-title": title,
            "update-title": title
        })
        logging.debug(f"Added game: {title}")
    
    return output_list

def write_json(data, file_path):
    """Write JSON data to a file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Output written to {file_path}")
    except Exception as e:
        logging.error(f"Failed to write JSON to {file_path}: {e}")
        raise

def main():
    try:
        games_data = load_json(GAMES_FILE_PATH)
        logging.info(f"Loaded data from {GAMES_FILE_PATH}")

        game_titles = extract_game_titles(games_data)
        write_json(game_titles, TITLES_FILE_PATH)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
