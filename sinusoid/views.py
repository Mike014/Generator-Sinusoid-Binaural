from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import urllib
from scipy.io.wavfile import write
import ctcsound

# Create your views here.
def generate_sine_wave(frequency, duration=1, sample_rate=44100, binaural=False):
    if binaural:
        duration = max(duration, 10)  # Set the minimum duration to 10 seconds for binaural
    
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = 0.5 * np.sin(2 * np.pi * frequency * t)
    
    if binaural:
        print("Initializing Csound...")
        # Header
        cs = ctcsound.Csound()
        cs.setOption("-odac")
        cs.compileOrc(f"""
        sr = {sample_rate}
        ksmps = 32
        nchnls = 2
        0dbfs = 1

        instr 1
            ; Oscillator for the left channel
            a1 oscil 0.5, p4, 1
            ; Oscillator for the right channel with frequency modulation
            a2 oscil 0.5, p4 + (p4 * 0.01 * oscili(1, 0.25)), 1
            out a1, a2
        endin
        """)
        cs.readScore(f"""
        f 1 0 16384 10 1  ; Defines a function table with a sine wave
        i1 0 {duration} {frequency}
        """)
        cs.start()
        print("Running Csound...")
        cs.perform()
        
        # Check that the output buffer is not null
        output_buffer = cs.outputBuffer()
        if output_buffer is None:
            cs.cleanup()
            cs.reset()
            raise ValueError("Output buffer is NULL")
        
        print(f"Output buffer length: {len(output_buffer)}")
        print(f"Output buffer content: {output_buffer[:10]}")  # Print the first 10 values of the buffer
        x = np.array(output_buffer).reshape(-1, 2)
        cs.cleanup()
        cs.reset()
    
    return x, t

def index(request):
    frequency = float(request.GET.get('frequency', 440))
    binaural = request.GET.get('binaural', 'false').lower() == 'true'
    print(f"Frequency: {frequency}, Binaural: {binaural}")  
    try:
        x, t = generate_sine_wave(frequency, binaural=binaural)
    except ValueError as e:
        return HttpResponse(f"Error generating sine wave: {e}", status=500)
    
    plt.figure()
    if binaural:
        plt.plot(t[:x.shape[0]], x[:, 0])  # Ensure dimensions match
    else:
        plt.plot(t, x)
    plt.title(f'Sine Wave at {frequency} {"(Binaural)" if binaural else ""}')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    
    audio_buf = io.BytesIO()
    write(audio_buf, 44100, x.astype(np.float32))
    audio_buf.seek(0)
    audio_string = base64.b64encode(audio_buf.read()).decode('utf-8')
    audio_uri = 'data:audio/wav;base64,' + audio_string
    
    context = {'image_uri': uri, 'audio_uri': audio_uri}
    return render(request, 'sinusoid/index.html', context)










    

