#!/usr/bin/env python3
import json
import logging
import os
from typing import Any, Dict, List

"""Configure logging"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

"""Path to the JSON file"""
GAMES_FILE_PATH = './games.json'
CONTROLLERS_FILE_PATH = './game-controllers.json'

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
            json.dump(data, file, indent=4)
        logging.info(f"Output successfully written to {file_path}")
    except Exception as e:
        logging.error(f"Failed to write JSON to {file_path}: {e}")
        raise

def extract_controller_tags(games_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extract games with 'Controller Type' tags."""
    output_list = []
    games_metadata = games_data.get('gamesMetadata', {})
    
    for game_key, game_data in games_metadata.items():
        title = game_data.get('title', 'No Title')
        tags = game_data.get('tags', [])
        
        for tag in tags:
            if 'Controller Type' in tag.get('name', ''):
                output_list.append({
                    "key": game_key,
                    "title": title,
                    "id": tag.get('id', 'No ID'),
                    "icon": tag.get('icon', 'No Icon'),
                    "name": tag.get('name', 'No Name'),
                    "packages": tag.get('packages', [])
                })
                logging.debug(f"Added game: {title} with tag: {tag.get('name')}")
    
    logging.info(f"Extracted {len(output_list)} games with 'Controller Type' tags")
    return output_list

def main() -> None:
    """Main function to process games and extract controller tags."""
    try:
        games_data = load_json(GAMES_FILE_PATH)
        logging.info(f"Loaded data from {GAMES_FILE_PATH}")

        controller_tags = extract_controller_tags(games_data)
        write_json(controller_tags, CONTROLLERS_FILE_PATH)

    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
