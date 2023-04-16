# MercadoLibre - Search Position Finder

This project allows you to search for specific items on MercadoLibre Argentina and find their position and title in the search results. The output can be displayed on the screen or saved to a CSV file.

## Prerequisites

To run this project, you'll need:

- Python 3.6 or higher
- Poetry (Python dependency manager)

## Installation

### Python

If you don't have Python installed, you can download it from the official Python website: https://www.python.org/downloads/

Choose the version appropriate for your operating system and follow the installation instructions.

### Poetry

To install Poetry, follow the installation guide on the official documentation: https://python-poetry.org/docs/#installation

For macOS and Linux, you can run the following command:

```bash
curl -sSL https://install.python-poetry.org | bash
```

For Windows, you can use PowerShell to install Poetry:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org/install.ps1 -UseBasicParsing).Content | Invoke-Expression
```

## Project Setup

1. Clone this repository or download the project files.

2. Open a terminal or command prompt, and navigate to the project's root directory.

3. Run the following command to install the project's dependencies:

```bash
poetry install
```

For Windows,

```powershell
poetry install
```

This command will create a virtual environment and install the required dependencies.

4. Configure the project by updating the `config.py` file:

   - Replace `YOUR_API_KEY` with your MercadoLibre API key.
   - Update the `pairs` variable with the item IDs and reference queries you want to search for.
   - Set the `output_type` variable to either `'screen'` or `'csv'` depending on your desired output format.

## Usage

To run the project, use the following command in the terminal or command prompt:

```bash
poetry run python crawler.py
```

For Windows:

Activate the Poetry virtual environment:

```powershell
poetry shell
```

This command will create a new PowerShell session with the virtual environment activated.

Run the main script:

```powershell
python crawler.py
```

This command will execute the main script, which will search for the specified item IDs and reference queries in MercadoLibre Argentina, scroll through multiple pages of search results, and display the position and title of the items when found.

The output will be displayed on the screen or saved to a CSV file, depending on the `output_type` setting in the `config.py` file.
