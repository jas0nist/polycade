#!/usr/bin/env python3
import json
import logging
import os
from typing import Any, Dict, List

"""Configure logging"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

"""Path to the JSON file"""
GAMES_FILE_PATH = './games.json'
TITLES_FILE_PATH = './game-titles.json'

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

def write_json(data: Any, file_path: str) -> None:
    """Write JSON data to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        logging.info(f"Output successfully written to {file_path}")
    except Exception as e:
        logging.error(f"Failed to write JSON to {file_path}: {e}")
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
