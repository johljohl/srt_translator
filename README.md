# SRT Translator to Swedish

This Python script provides a simple GUI to translate SRT (SubRip Text) subtitle files to Swedish while keeping the names unchanged.

## Features

- Translate the text in SRT files to Swedish.
- Preserve names and do not translate them.
- Display a progress bar with the percentage of translation completed.
- Choose a location to save the translated SRT file.

## Prerequisites

Before running this script, you must install the following Python libraries:

- `spacy`
- `googletrans` (version 4.0.0-rc1)
- `tkinter`

You can install them using pip:

pip install spacy googletrans==4.0.0-rc1
Also, you will need to download the English language model for spaCy:


Copy code
python -m spacy download en_core_web_sm
Usage
To use the script, run it from your command line:


Copy code
python srt_translator.py
The GUI will prompt you to select the SRT file you wish to translate. After the file is selected, you will be asked where to save the translated file. The translation process will begin, and the progress will be displayed in the GUI.

License
This script is provided "as is", without warranty of any kind, express or implied. You may use, modify, and distribute it for private and non-commercial uses.

Disclaimer
The translation service is powered by googletrans, which is a free and unlimited python library that implemented Google Translate API. Please note that the accuracy of the translations and the availability of the service cannot be guaranteed.

Contributing
If you'd like to contribute to the project, please feel free to make any changes and submit a pull request. Your contributions are always welcome!

Support
If you have any questions or run into any issues, please open an issue in the repository, and we'll try to help you out.

Acknowledgments
Thanks to the spacy team for the excellent NLP tools.
Thanks to the authors of googletrans for providing a Python interface for Google Translate.
