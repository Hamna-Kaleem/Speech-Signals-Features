import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def plot_waveform_and_spectrograms(audio_path):
    # Load audio file
    y, sr = librosa.load(audio_path, sr=None)
    
    # Compute different spectrograms
    D = np.abs(librosa.stft(y))  # Short-Time Fourier Transform (STFT)
    D_db = librosa.amplitude_to_db(D, ref=np.max)  # Log-scale spectrogram
    
    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    mel_spectrogram_db = librosa.amplitude_to_db(mel_spectrogram, ref=np.max)
    
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    
    cqt = np.abs(librosa.cqt(y, sr=sr, hop_length=512))
    cqt_db = librosa.amplitude_to_db(cqt, ref=np.max)
    
    chroma = librosa.feature.chroma_stft(y=y, sr=sr, hop_length=512)

    # Create subplots
    fig, ax = plt.subplots(3, 2, figsize=(15, 12))

    # Waveform
    ax[0, 0].plot(np.linspace(0, len(y) / sr, num=len(y)), y, color='b')
    ax[0, 0].set_title("Waveform")
    ax[0, 0].set_xlabel("Time (s)")
    ax[0, 0].set_ylabel("Amplitude")

    # STFT Spectrogram
    librosa.display.specshow(D_db, sr=sr, x_axis='time', y_axis='log', ax=ax[0, 1])
    ax[0, 1].set_title("STFT Spectrogram")
    
    # Mel Spectrogram
    librosa.display.specshow(mel_spectrogram_db, sr=sr, x_axis='time', y_axis='mel', ax=ax[1, 0])
    ax[1, 0].set_title("Mel Spectrogram")
    
    # MFCCs
    librosa.display.specshow(mfccs, sr=sr, x_axis='time', ax=ax[1, 1])
    ax[1, 1].set_title("MFCCs")
    
    # Constant-Q Transform (CQT)
    librosa.display.specshow(cqt_db, sr=sr, x_axis='time', y_axis='cqt_note', ax=ax[2, 0])
    ax[2, 0].set_title("Constant-Q Transform (CQT)")
    
    # Chromagram
    librosa.display.specshow(chroma, sr=sr, x_axis='time', y_axis='chroma', ax=ax[2, 1])
    ax[2, 1].set_title("Chromagram")

    plt.tight_layout()
    plt.show()

# Example Usage
audio_path = "audio.wav"  # Replace with your audio file
plot_waveform_and_spectrograms(audio_path)
