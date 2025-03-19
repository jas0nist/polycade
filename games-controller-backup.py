#!/usr/bin/env python3
import json
import logging
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Path to the JSON file
GAMES_FILE_PATH = './games.json'
CONTROLLERS_FILE_PATH = './game-controllers.json'

def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logging.debug(f"Successfully loaded JSON from {file_path}")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding error in {file_path}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error while loading JSON from {file_path}: {e}")
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

def write_json(data: Any, file_path: str) -> None:
    """Write JSON data to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Output successfully written to {file_path}")
    except Exception as e:
        logging.error(f"Failed to write JSON to {file_path}: {e}")
        raise

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
