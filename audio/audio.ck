40 => int baseMidi;
// Pentatonic scale.
[0, 2, 4, 7, 9, 12] @=> int offsets[];

fun void playHighNote(float gain, float baseFreq) {
    SinOsc s => JCRev r => ADSR e => Gain g => dac;
    g.gain(gain);

    e.attackTime(30::ms);
    e.decayTime(30::ms);
    e.sustainLevel(0.1);
    e.releaseTime(2::second);

    s.freq(baseFreq * 10);

    e.keyOn();
    300::ms => now;
    e.keyOff();
    2::second => now;
}

// Plays printer sample
fun void playPrinter(float gain) {
    me.sourceDir() + "/printer.wav" => string filename;

    SndBuf buf => Envelope e => Gain g => LPF lpf => JCRev rev => dac;
    rev.mix(0.02);
    g.gain(gain);
    lpf.freq(3000);
    100::ms => dur envDur;
    filename => buf.read;

    while(true) {
        e.keyOn();
        buf.samples() => int numSamples;
        Math.random2(0, numSamples) => buf.pos;
        Math.random2f(0.1, 10) => float rate;
        rate => buf.rate;
        <<< rate >>>;
        10::second / rate => now;
        e.keyOff();
        envDur => now;
    }
}

fun void playBackgroundNoise(float baseFreq) {
    Noise n => LPF f => Gain g => Envelope e => dac;
    e.duration(100::ms);
    f.freq(100);
    g.gain(0.2);
    SinOsc s => JCRev rev => LPF f2 => Gain g2 => e => dac;
    g2.gain(0.05);
    f2.freq(100);
    s.freq(baseFreq);

    e.keyOn();
    while(true) {
        s.freq(baseFreq + Math.random2f(-5, 5));
        5::ms => now;
    }
}

fun void test(dur duration) {
    now + duration => time later;

    while(now < later) {
        offsets[Math.random2(0,offsets.cap()-1)] => int offset;
        Std.mtof(baseMidi + offset) => float freq;
        spork~ playHighNote(0.05, freq);
        200::ms => now;
    }
}

spork~ playBackgroundNoise(200);
spork~ playPrinter(0.5);
while (true) {
    1::ms => now;
}

