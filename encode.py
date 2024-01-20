import base64
import ggwave
import pyaudio

def string_to_sound(input_string):
    waveform = ggwave.encode(input_string, protocolId=4, volume=100)
    return waveform

def play_sound(waveform):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=48000, output=True, frames_per_buffer=4096)
    stream.write(waveform, len(waveform) // 4)
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    try:
        input_string = input("Enter a string to encode with sound: ")
        waveform = string_to_sound(input_string)
        play_sound(waveform)
    except KeyboardInterrupt:
        pass
