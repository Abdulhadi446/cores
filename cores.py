import argparse
import safe_print_setup
import cleanup
import app
import utils

def main():
    parser = argparse.ArgumentParser(description="Run the app with a specified file.")
    parser.add_argument(
        "filepath",
        type=str,
        help="Path to the .crs file to run"
    )
    parser.add_argument(
        "--debug",
        type=str,
        help="First assing debug mode.",
        default="default"
    )
    
    args = parser.parse_args()
    
    # Call your app's main function with the provided filepath
    app.main(args.filepath, args.debug)

if __name__ == "__main__":
    main()