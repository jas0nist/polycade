#!/usr/bin/env python3
import json
import logging
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Path to the JSON file
GAMES_FILE_PATH = './games.json'
TITLES_FILE_PATH = './game-titles.json'

def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logging.info(f"Successfully loaded JSON from {file_path}")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON format in {file_path}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error while loading JSON from {file_path}: {e}")
        raise

def extract_game_titles(games_data: Dict[str, Any]) -> List[Dict[str, str]]:
    """Extract game titles."""
    output_list = []
    games_metadata = games_data.get('gamesMetadata', {})
    
    if not isinstance(games_metadata, dict):
        logging.error("'gamesMetadata' is not a dictionary.")
        raise ValueError("'gamesMetadata' must be a dictionary.")

    for game_key, game_data in games_metadata.items():
        if not isinstance(game_data, dict):
            logging.warning(f"Skipping invalid game data for key: {game_key}")
            continue

        title = game_data.get('title', 'No Title')
        output_list.append({
            "key": game_key,
            "origin-title": title,
            "update-title": title
        })
        logging.debug(f"Added game: {title} (key: {game_key})")
    
    return output_list

def write_json(data: Any, file_path: str) -> None:
    """Write JSON data to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        logging.info(f"Output successfully written to {file_path}")
    except Exception as e:
        logging.error(f"Failed to write JSON to {file_path}: {e}")
        raise

def main() -> None:
    """Main function to process game titles."""
    try:
        games_data = load_json(GAMES_FILE_PATH)
        game_titles = extract_game_titles(games_data)
        write_json(game_titles, TITLES_FILE_PATH)
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
