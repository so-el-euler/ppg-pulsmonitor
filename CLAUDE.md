# PPG-Pulsmonitor – Kontext für Claude

Lernprojekt neben dem Medizintechnik-Studium: optischer Pulsmonitor mit selbst gebautem Analog-Frontend, TI-Mikrocontroller, Auswertung in MATLAB und Python und einem KI-Bericht-Agenten. Antworten auf Deutsch, Schritte konkret erklären.

## Wo was liegt

- **Projektplan (Claude Docs):** https://claude.ai/artifact/9rxDXn2eCAvZzgFYuFwZGJ – Wochen-Checklisten Woche 0–4, Materialliste, Risiken. Nach erledigten Aufgaben dort abhaken.
- **GitHub:** https://github.com/so-el-euler/ppg-pulsmonitor – Milestones Week 1–4 (fällig 29.11., 6.12., 13.12., 20.12.2026), pro Woche ein Issue (#1–#4) mit Checkbox-Aufgaben. `gh` ist nicht installiert; lesen über die öffentliche REST-API, ändern macht die Nutzerin/der Nutzer selbst auf github.com.
- **Python:** `.venv` (Python 3.14), `pip install -r requirements.txt`, Tests mit `.venv\Scripts\python.exe -m pytest`.
- **Gemeinsame Parameter:** `config.json` (100 Hz, Bandpass 0,5–4 Hz, Peak-Abstand 0,33 s) – MATLAB und Python lesen dieselben Werte.

## Hardware

- TI LaunchPad **LP-MSPM0G3507** (Cortex-M0+, 12-Bit-ADC, 3,3 V – ADC-Eingang nie über 3,3 V)
- **MCP6002** (Doppel-OPA, rail-to-rail) für Transimpedanzverstärker + Hochpass/Verstärkung
- Fotodiode **BPW34** + grüne LED (Plan A), LDR GL5528 als Notlösung, MAX30102 nur falls bis 29.11. kein Signal
- Optional: MCP4922 (DAC, Signalgenerator), SG90-Servo (Zeiger-Anzeige), NTC
- Referenz: Apple Watch (Training "Andere" starten; Export über Health-App → `export.xml`)

## Werkzeuge

- **Code Composer Studio 21** in `C:\ti\ccs2110`, MSPM0 SDK 2.12 in `C:\ti`, Workspace `C:\Users\soele\workspace_ccstheia`. Das alte CCS Theia 1.5.1 im OneDrive-Ordner nicht benutzen.
- Nützliche SDK-Beispiele: `gpio_toggle_output`, `adc12_triggered_by_timer_event`, `uart_echo_interrupts_standby`.
- **MATLAB** R2025a mit Signal Processing Toolbox.

## Regeln

- `.env` (API-Key) nie committen.
- Kein Medizinprodukt: keine Diagnosen aus den Messwerten ableiten.
