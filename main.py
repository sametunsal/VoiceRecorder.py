import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


sampling_freq = 44100 #ses kaydı alırken kullandığımız örnekleme frekansını giriyoruz.
#genelde örnekleme frekansı için 44100 veya 48000 fps kullanılıyormuş.

duration = 5 #kaç saniye kayıt alacağımızı saniye cinsinden belirtiyoruz.

recording = sd.rec(int(duration * sampling_freq),samplerate=sampling_freq, channels=2)
#bu fonksiyon ile Numpy dizisi oluşturuyoruz. Örnekleme oranı ve kaç kanallı
#kayıt olacağı yazılıyor.

sd.wait() #program kayıt yapılacak süre kadar bekliyor.

write("recording_1.wav",sampling_freq,recording)
#Numpy dizisini ses dosyasına scipy kütüphanesi ile çeviriyor.

wv.write("recording_2.wav",recording,sampling_freq,sampwidth=2)
#Numpy dizisini ses dosyasına wavio kütüphanesi ile çeviriyor.