# MongoDB Test with Python and PyMongo: Simple Shopping List

## Overview

This repository contains a simple Python script that connects to a MongoDB Atlas database using PyMongo. The script sets up a basic shopping list database, demonstrating the connection, and can be used as a starting point for MongoDB integration in Python projects.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/meusjoseph21/mongodb_and_python.git
   cd mongodb_and_python
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your MongoDB Atlas password:

   ```plaintext
   MONGODB_URL = <your actual url>
   ```

## Usage

Run the Python script to connect to MongoDB and set up the shopping list database:

```bash
python shopping_list.py
```

## Configuration

- The `MONGODB_PASSWORD` environment variable in the `.env` file stores your MongoDB Atlas password securely.
- Modify the connection string in `shopping_list.py` if necessary.

## Dependencies

- [PyMongo](https://pypi.org/project/pymongo/): MongoDB driver for Python.
- [python-dotenv](https://pypi.org/project/python-dotenv/): Reads the environment variables from a `.env` file.

## Contributing

Feel free to contribute to this project by opening issues or pull requests. Your feedback and enhancements are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
