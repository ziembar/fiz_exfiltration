import base64
import wave

from pydub import AudioSegment
import ggwave
import pyaudio

p = pyaudio.PyAudio()

def b64_file(file_name):
    with open(file_name, 'r') as file:
        return base64.b64encode(file.read().encode()).decode()


file_name = 'test.txt'
encoded_data = b64_file(file_name)

# generate audio waveform for string "hello python"
waveform = ggwave.encode(encoded_data, protocolId=4, volume=100)



output_file = 'output_waveform.wav'
with wave.open(output_file, 'w') as wave_file:
    wave_file.setnchannels(2)
    wave_file.setsampwidth(1)  # 2 bytes for 16-bit audio
    wave_file.setframerate(48000)
    wave_file.writeframes(waveform)


print("Transmitting text 'hello python' ...")
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=48000, output=True, frames_per_buffer=4096)
stream.write(waveform, len(waveform) // 4)
stream.stop_stream()
stream.close()

p.terminate()
