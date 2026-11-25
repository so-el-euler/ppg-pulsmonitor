from ppg import load_config


def test_config_is_plausible():
    cfg = load_config()
    bp = cfg["bandpass"]
    nyquist = cfg["sampling_rate_hz"] / 2

    # Bandpass muss unterhalb der Nyquist-Frequenz liegen
    assert 0 < bp["low_hz"] < bp["high_hz"] < nyquist
    # 0,5-4 Hz entspricht 30-240 Schlägen pro Minute
    assert bp["low_hz"] * 60 <= 40
    assert bp["high_hz"] * 60 >= 180
