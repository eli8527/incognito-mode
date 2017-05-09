fun void playBackgroundNoise(float baseFreq) {
    Noise n => LPF f => Gain g => Envelope e => dac;
    e.duration(100::ms);
    f.freq(420);
    g.gain(0.2);
    SinOsc s => JCRev rev => LPF f2 => Gain g2 => e => dac;
    g2.gain(0.05);
    f2.freq(400);
    s.freq(baseFreq);

    e.keyOn();
    while(true) {
        s.freq(baseFreq + Math.random2f(-5, 5));
        5::ms => now;
    }
}


spork~ playBackgroundNoise(110);
spork~ playBackgroundNoise(220);
spork~ playBackgroundNoise(440);
while (true) {
    1::ms => now;
}

