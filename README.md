# english_srt_gen

This code uses OpenAI's Whisper Model to generate English subtitles (SRT file) for any video.

Make sure the following are installed in your system:

    python3
    pytorch
    torchvision
    torchaudio
    ffmpeg
    whisper

# Configuration

Configure your input and output paths at pathConfig.py.
Configure your model at modelConfig.py.

# How to Run

To use this script, run main.ipynb for your transcription needs.

# Troubleshooting

In some cases, the jupyter notebook might not be able to find the FFmpeg and Whisper modules.
Just run the preliminaries.ipynb notebook once. Then run main.ipynb for your transcription needs.