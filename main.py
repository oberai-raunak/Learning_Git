# main.py

import argparse
from src.config import load_config
from src.train.train import train_model


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("command", help="Command to run (e.g., train)")
    parser.add_argument("--env", default="dev", help="Environment (dev/prod)")

    args = parser.parse_args()

    config = load_config(args.env)

    if args.command == "train":
        train_model(config)
    else:
        raise ValueError(f"Invalid command: {args.command}")


if __name__ == "__main__":
    main()