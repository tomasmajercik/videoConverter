import ffmpeg
import os

print("Video converter v1.0")

while True:
    input_file_path  = input("\nEnter absolute path for file to convert (eg. /home/ur-name/movie.avi): ")
    if os.path.exists(input_file_path):
        break
    else:
        print("such path does not exist, enter again")

file_name, file_format = os.path.splitext(input_file_path)
output_format = input("\nEnter desired format to convert into (eg. mkv, mp4, mov):").strip()

format_map = {
    "mkv": ("matroska", ".mkv"),
    "mp4": ("mp4", ".mp4"),
    "mov": ("mov", ".mov"),
    "avi": ("avi", ".avi"),
    "webm": ("webm", ".webm")
}
if output_format in format_map:
    internal_format, extension = format_map[output_format]
    output_file_path = f"{file_name}_converted{extension}"
else:
    print(f"Sorry, the format {output_format} is not supported.")
    exit()

output_file_path = f"{file_name}_converted.{output_format}"

print("\n\nThe conversion is about to start, the encoding takes longer period of time")
print("you can see the frame, fps, q, Lsize and time (what time of movie)")
print("is being converted at the moment")

input("\nPress Enter to proceed")

try:
    print("starting conversion")
    ffmpeg.input(input_file_path).output(output_file_path, format=internal_format).run()
    print(f"Conversion successful! File saved as: {output_file_path}")
except Exception as e:
    print(f"Sorry, an error occurred during conversion: {e}")
