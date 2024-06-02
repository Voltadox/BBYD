# Youtube Piracy Simulator (Epic Edition)

## Description

The Youtube Piracy Simulator (Epic Edition) is a fun and functional Python-based GUI application for downloading and clipping audio and video from YouTube. The application uses the `pytube` library to fetch media from YouTube and `moviepy` for audio and video processing. The GUI is built using `tkinter`.

## Features

- **Download Audio:** Download the audio from a YouTube video in MP3 format.
- **Download Video:** Download the video from a YouTube video in MP4 format.
- **Clip Video:** Clip a specific portion of a YouTube video by defining the start and end timestamps.
- **Clear Data:** Clear the input fields.

## Requirements

- Python 3.x
- `pytube` library
- `moviepy` library
- `tkinter` (included with Python standard library)
- `PIL` (Python Imaging Library) for image processing

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/YoutubePiracySimulator.git
   cd YoutubePiracySimulator
   ```

2. **Install the required libraries:**
   ```bash
   pip install pytube moviepy Pillow
   ```

3. **Run the application:**
   ```bash
   python youtube_piracy_simulator.py
   ```

## Usage

1. **Launch the Application:**
   - Run the `youtube_piracy_simulator.py` script to open the GUI.

2. **Download Audio:**
   - Enter the YouTube video URL in the provided field.
   - Enter the desired output file name.
   - Click the "Download as Audio, yo!" button to download the audio in MP3 format.

3. **Download Video:**
   - Enter the YouTube video URL in the provided field.
   - Enter the desired output file name.
   - Click the "Download as Video, bitch!" button to download the video in MP4 format.

4. **Clip Video:**
   - Enter the YouTube video URL in the provided field.
   - Enter the desired output file name.
   - Enter the start time and end time for the clip in `hh:mm:ss` format.
   - Click the "Clip Video, yo!" button to download the specified clip in MP4 format.

5. **Clear Data:**
   - Click the "Clear" button to reset all input fields.

## Directory Structure

```
YoutubePiracySimulator/
├── README.md
├── youtube_piracy_simulator.py
└── assets/
    └── jesse.png
```

- `README.md`: This file.
- `youtube_piracy_simulator.py`: The main script for the application.
- `assets/`: Directory containing assets such as images.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- **Breaking Bad** for the inspiration behind the theme.
- **pytube** for making it easy to download YouTube content.
- **moviepy** for powerful video editing capabilities.
- **tkinter** for the GUI framework.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. Contributions are welcome and appreciated!

## Disclaimer

This tool is intended for educational and personal use only. Downloading copyrighted material without permission is against YouTube's terms of service and may violate copyright laws. Use this tool responsibly.

---

**Enjoy your YouTube piracy adventures (responsibly), yo!**
