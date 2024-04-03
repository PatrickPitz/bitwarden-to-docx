import argparse
import pathlib
import json
from docx import Document


def extract_data_from_json(json_file: pathlib.Path) -> dict:
    with open(json_file, "r") as file:
        extracted_data = json.load(file)
    return extracted_data


def create_arg_parser() -> argparse.ArgumentParser:
    """
    Creates an argument parser for command line arguments.

    Returns:
        argparse.ArgumentParser: The created argument parser.
    """
    new_parser = argparse.ArgumentParser(description="Create a PDF-File from a Bitwarden .json export")
    new_parser.add_argument("-i",
                            "--input",
                            help="Path to the Bitwarden .json export file",
                            required=True,
                            type=pathlib.Path)
    new_parser.add_argument("-o",
                            "--output",
                            help="Path to the output PDF file",
                            required=True,
                            type=pathlib.Path)
    new_parser.add_argument("-fc",
                            "--filter-collection",
                            help="Filter for a specific collection",
                            required=False,
                            type=str)
    new_parser.add_argument("-fo",
                            "--filter-organization",
                            help="Filter for a specific organization\nOnly works if no collection filter is set",
                            required=False,
                            type=str)
    return new_parser


if __name__ == '__main__':
    parser: argparse.ArgumentParser = create_arg_parser()
    args = parser.parse_args()
    items = extract_data_from_json(args.input)["items"]

    # Filtering items based on command line arguments
    if args.filter_collection:
        items = [item for item in items if args.filter_collection in item["collectionIds"] and item["type"] == 1]
    elif args.filter_organization:
        items = [item for item in items if item["organizationId"] == args.filter_organization and item["type"] == 1]

    # Creating a Document and adding items to it
    document: Document = Document()
    document.add_heading("Bitwarden Export", level=1)
    for item in items:
        document.add_heading(item["name"], level=2)
        document.add_paragraph(f"URL: {item['login']['uris'][0]['uri']}")
        document.add_paragraph(f"Username: {item['login']['username']}")
        document.add_paragraph(f"Password: {item['login']['password']}")
        document.add_paragraph(f"Notes: {item['notes']}")
    document.save(args.output)


