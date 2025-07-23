## Video Format Converter (v1.0)

### 📝 Project description
This Python-based video converter uses `ffmpeg` to convert video files from one format to another. It supports several popular video formats for both input and output.

### 🛠️ Tech stack
- `python`
- `ffmpeg` (library)

### 🌱 Skills gained & problems overcomed
- Video encoding and converting

### ⚙️ How to install

#### Dependencies
Install ffmpeg-python first ```pip install ffmpeg-python```
- For Linux use ```sudo apt install ffmpeg``` (ubuntu tested)
- For MacOS use ```brew install ffmpeg```
- For Winfows ```follow installation on the website```

#### ⬅️ Supported Input Formats:
- `.avi`
- `.mkv`
- `.mp4`
- `.mov`
- `.webm`

#### ➡️ Supported Output Formats:
- **MKV** (`.mkv`)
- **MP4** (`.mp4`)
- **MOV** (`.mov`)
- **AVI** (`.avi`)
- **WEBM** (`.webm`)

### 📌 How to Use

1. **Run the script**: Start the script by executing it in your Python environment.
2. **Enter the path**: You will be prompted to enter the absolute path of the video file you want to convert (e.g., `/home/user-name/video.avi`).
3. **Choose output format**: Then, you will be asked to specify the desired output format (e.g., `mp4`, `mkv`, `mov`).
4. **Conversion**: Press Enter to start the conversion process. You will see information about the current encoding progress.
5. **Save**: The converted file will be saved with a new name, suffixed with `_converted`, and the appropriate file extension (e.g., `video_converted.mp4`).

## ✏️ Notes

- The conversion process may take some time depending on the size of the video and the output format.
- Ensure that `ffmpeg` is installed and available on your system.

