import ctcsound
import numpy as np
from scipy.io.wavfile import write

def test_cs_sound(frequency=440, duration=5, sample_rate=44100):
    cs = ctcsound.Csound()
    cs.setOption("-o test_output.wav")
    cs.compileOrc(f"""
    sr = {sample_rate}
    ksmps = 32
    nchnls = 2
    0dbfs = 1

    instr 1
        a1 oscil 0.5, p4, 1
        a2 oscil 0.5, p4 * 1.01, 1
        out a1, a2
    endin
    """)
    cs.readScore(f"""
    f 1 0 16384 10 1  ; Definisce una tabella di funzioni con un'onda sinusoidale
    i1 0 {duration} {frequency}
    """)
    cs.start()
    cs.perform()
    cs.cleanup()
    cs.reset()

test_cs_sound()

