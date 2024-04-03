# BITWARDEN-TO-DOCX

This script is used to convert a Bitwarden JSON export to a DOCX file.
In case you want to print your passwords or have a hard copy of them in a real vault.

## Usage

```bash
git clone https://github.com/PatrickPitz/bitwarden-to-docx.git
cd bitwarden-to-docx
python3 bitwarden_to_docx.py \
        -i <path_bitwarden_export.json> \
        -o <output.docx> \
        -fc <optional_filter_by_collection> \
        -fo <or_optional_filter_by_organization>
```


## Requirements


- python-docx
  - Install with `pip install python-docx`