
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![GitHub contributors](https://img.shields.io/github/contributors/swechchha27/taxmitra_chatbot)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/swechchha27/taxmitra_chatbot/main)

![CodeFactor Grade (with branch)](https://img.shields.io/codefactor/grade/github/swechchha27/taxmitra_chatbot/main)
[![Lint Python Code using Pylint](https://github.com/swechchha27/taxmitra_chatbot/actions/workflows/pylint.yml/badge.svg)](https://github.com/swechchha27/taxmitra_chatbot/actions/workflows/pylint.yml)
[![Run tests using unittest](https://github.com/swechchha27/taxmitra_chatbot/actions/workflows/unittest.yml/badge.svg)](https://github.com/swechchha27/taxmitra_chatbot/actions/workflows/unittest.yml)

# Indian Income Tax Consultant Chatbot

This project creates a simple domain-specific chatbot named 'TaxMitra' that provides basic income tax guidance to Indian citizens.

## Features

- Provides information on income tax rules and regulations in India.
- Answers frequently asked questions about income tax.
- Offers guidance on tax filing procedures.
- Supports interactive chat sessions.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/swechchha27/taxmitra_chatbot.git
   cd taxmitra_chatbot
   ```

2. **Create a virtual environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory of the project.
   - You can refer to the `.env.sample` file for the required environment variables.

## Usage

1. **Train the chatbot** (if needed):
   - You can train the chatbot with custom data by adding a new training file in the `data` folder and modifying the `.env` script or environment variable `TRAINING_FILE` to point to the new file.

2. **Run the chatbot**:
   ```sh
   python main.py
   ```

3. **Interact with the chatbot**:
   - Enter your name when prompted.
   - Start asking questions related to income tax.

## Training Data

- The chatbot can be trained with custom conversation data from the `training_chat_conversation.txt` file.
- You can add more training data to improve the chatbot's responses.

## Project Structure

```
taxmitra_chatbot/
│
├── src/                          # Folder for source code of bot
│   ├── __init__.py               # Package initialization
│   ├── bot_app.py                # script that defines ChatBotApp class
│   └── config.py                 # script that pulls config based on environment
├── data/                         # Folder for keeping all training data files
│   └── training_chat_conversation.txt
├── storage/                      # Folder for storing bot's memory db (sqlite3)
│   └── dev_db.sqlite3
├── main.py                       # Main script to run the chatbot
├── requirements.txt              # Project dependencies
├── .env.sample                   # sample .env file for environment config setup
├── .gitignore                    # Git ignore file
├── .pylintrc                     # Pylint configuration file
├── LICENSE                       # License file for MIT Open-Source License
├── README.md                     # Project documentation
├── CONTRIBUTING.md               # Guidelines for contributing to the project
├── TODO.md                       # List of tasks and improvements for the project
├── .github/workflows/            # Folder for GitHub Actions workflow configuration files
│   └── python-app.yml            # Development configuration
├── pyproject.toml                # Project metadata and build configuration
├── setup.py                      # Setup script for packaging
├── tox.ini                       # Configuration file for Tox
└── tests/                        # Folder for unit tests
    ├── test_bot.py               # Unit test file
    └── __init__.py               # Package initialization
```

## Running Tests

To run tests across multiple Python versions using `tox`, use the following command:

```sh
tox
```

Make sure you have all the required Python versions installed on your system.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Swechchha Agarwal

[swechchhagoyal27@gmail.com](mailto:swechchhagoyal27@gmail.com)

![GitHub followers](https://img.shields.io/github/followers/swechchha27)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]([https://www.linkedin.com/](https://www.linkedin.com/in/swechchha-agarwal))


## Acknowledgments

- [ChatterBot](https://github.com/gunthercox/ChatterBot)
- [ChatterBot Corpus](https://github.com/gunthercox/chatterbot-corpus)
