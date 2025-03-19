import argparse
import logging
import subprocess
import sys

# games_module.py

def run_subprocess(script_name):
    """Run a subprocess for the given script."""
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred while running {script_name}: {e}")
        sys.exit(1)

def backup_game_titles():
    """Backup functionality for game titles."""
    logging.info("Backing up game titles...")
    run_subprocess("./games-title-backup.py")

def backup_game_controllers():
    """Backup functionality for game controllers."""
    logging.info("Backing up game controllers...")
    run_subprocess("./games-controller-backup.py")

def restore_game_controllers():
    """Restore functionality for game controllers."""
    logging.info("Restoring game controllers...")
    run_subprocess("./games-controller-restore.py")

def update_game_titles():
    """Update functionality for game titles."""
    logging.info("Updating game titles...")
    run_subprocess("./games-title-update.py")

def configure_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Perform backup, restore, and update operations for game titles and controllers."
    )
    parser.add_argument(
        "--backup-controllers",
        action="store_true",
        help="Backup all game controller configurations."
    )
    parser.add_argument(
        "--backup-titles",
        action="store_true",
        help="Backup all game titles to a secure location."
    )
    parser.add_argument(
        "--restore-controllers",
        action="store_true",
        help="Restore game controller configurations from a backup."
    )
    parser.add_argument(
        "--update-titles",
        action="store_true",
        help="Update game titles with the latest information."
    )
    return parser.parse_args()

def main():
    configure_logging()
    args = parse_arguments()

    if not any(vars(args).values()):
        logging.info("No arguments provided. Displaying help.")
        print("No arguments provided. Use --help to see available options.")
        return

    if args.backup_titles:
        backup_game_titles()

    if args.backup_controllers:
        backup_game_controllers()

    if args.restore_controllers:
        restore_game_controllers()

    if args.update_titles:
        update_game_titles()

if __name__ == "__main__":
    main()
