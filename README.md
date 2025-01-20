# english_srt_gen

This code uses Open AI's Whisper Model to generate English subtitles (srt file) for videos.

Make sure the following are installed in your system:

    python3
    pytorch
    torchvision
    torchaudio
    ffmpeg
    whisper

# Configuration

Configure your input and output paths as well as the model size at config.py.

# How to Run

To use this script, run main.ipynb for your transcription needs.

# Troubleshooting

In some cases, the jupyter notebook might not be able to find ffmpeg and whisper modules. Just run the preliminaries.ipynb notebook once. Then run main.ipynb for your transcription needs.