# PPG-Pulsmonitor

Ein selbst gebauter optischer Pulsmonitor: Eine grüne LED durchleuchtet den Finger, eine Fotodiode misst die Lichtschwankungen durch den Herzschlag. Ein Verstärker aus Operationsverstärkern bereitet das Signal auf, ein TI-Mikrocontroller digitalisiert es, und MATLAB und Python berechnen daraus Herzfrequenz und Herzratenvariabilität (HRV). Ein KI-Agent fasst jede Messung in einem verständlichen Bericht zusammen.

> **Status:** in Arbeit (Woche 0: Setup)


## Messkette

```
Grüne LED → Finger → Fotodiode BPW34 → Transimpedanzverstärker (MCP6002)
  → Hochpass + Verstärkung → ADC (LP-MSPM0G3507, 100 Hz) → UART/USB
  → Python (Aufnahme, CSV) → MATLAB / Python (Filter, Peaks, HF, HRV)
  → Bericht-Agent (Claude API)
```

## Hardware

| Teil | Aufgabe |
| --- | --- |
| TI LaunchPad LP-MSPM0G3507 | 12-Bit-ADC, sendet Messwerte per USB-UART |
| Fotodiode BPW34 | Lichtdetektor |
| MCP6002 (Doppel-OPA, rail-to-rail) | Transimpedanzverstärker und zweite Verstärkerstufe |
| Grüne LED | Lichtquelle |
| Apple Watch | Referenzmessung zur Validierung |

## Projektstruktur

```
firmware/       LaunchPad-Code (Code Composer Studio, MSPM0 SDK)
hardware/       Schaltplan und Fotos des Aufbaus
matlab/         Signalverarbeitung in MATLAB
ppg/            Python-Paket: Aufnahme, Verarbeitung, Live-Anzeige, Bericht-Agent
tests/          Tests (pytest)
data/raw/       Messungen als CSV
docs/figures/   Abbildungen
config.json     gemeinsame Filterparameter für MATLAB und Python
```

## Einrichten

```bash
py -3.14 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Für den Bericht-Agenten `.env.example` nach `.env` kopieren und den eigenen Anthropic-API-Key eintragen. `.env` wird nie committet.

## Fahrplan

- [x] Woche 0: Setup (Werkzeuge, Repo)
- [ ] Woche 1: Messkette, Verstärker, Rohdaten
- [ ] Woche 2: Signalverarbeitung in MATLAB
- [ ] Woche 3: Python-Version, Live-Anzeige, Validierung (Bland-Altman)
- [ ] Woche 4: Bericht-Agent, Dokumentation, Demo

## Lizenz

MIT, siehe [LICENSE](LICENSE).
