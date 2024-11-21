import machine
import os
import wave
import ustruct

# Configuración del pin para la tarjeta SD
sd_cs = machine.Pin(5, machine.Pin.OUT)
spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0, sck=machine.Pin(18), mosi=machine.Pin(23))
sd = os.mount(spi, sd_cs)

# Abre el archivo WAV
wav_file = open('/sd/audio.wav', 'rb')

# Configurar I2S para la salida de audio
i2s = machine.I2S(0, sck=machine.Pin(14), ws=machine.Pin(15), sd=machine.Pin(32), mode=machine.I2S.MASTER | machine.I2S.TX, 
                  bits=16, format=machine.I2S.MONO, rate=44100)

# Leer y enviar los datos del archivo WAV a través de I2S
while True:
    # Lee bloques de 1024 bytes del archivo WAV
    data = wav_file.read(1024)
    if not data:
        break
    
    # Convierte los datos a un formato adecuado y envíalos por I2S
    i2s.write(data)

wav_file.close()
