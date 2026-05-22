# Voice Assistant Demo

A simple Python voice assistant demo that listens for text input, speaks responses using `pyttsx3`, and exits on user command.

## Features

- Text-to-speech response using `pyttsx3`
- Interactive command line conversation
- Exit the assistant with `exit` or `quit`

## Requirements

- Python 3.7 or newer
- `pyttsx3` package

## Installation

1. Clone or download the repository.
2. Install dependencies:

```bash
pip install pyttsx3
```

## Usage

Run the assistant from the command line:

```bash
python main.py
```

Type a message and press Enter. The assistant will repeat your message aloud and print the response.

To stop the assistant, enter:

```bash
exit
```

or

```bash
quit
```

## Notes

- Make sure your system audio is enabled for voice output.
- If `pyttsx3` requires additional drivers or voices on your platform, follow the package documentation.

## License

This project is released under the MIT License.