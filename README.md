# Loguru Logging Example

A minimal example demonstrating structured logging with **Loguru**, including automatic log file rotation, retention, and compression.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Loguru](https://img.shields.io/badge/Logging-Loguru-orange)

---

## 🇬🇧 English

### Overview
This script demonstrates the core features of the `loguru` library: writing logs to a file with automatic rotation, retention, and compression, alongside the different log severity levels (`info`, `debug`, `warning`, `error`, `success`).

### Features
- Automatic log file rotation once the file reaches 10 MB
- Automatic deletion of logs older than 5 days
- Old logs are compressed into `.zip` archives
- Demonstrates all major log levels in a single, simple example

### Requirements
- Python 3.10 or higher
- `loguru`

### Installation
```bash
pip install loguru
```

### Usage
```bash
python loguru_example.py
```

Logs will be printed to the console and simultaneously saved to `logs.log` in the same directory.

### How it works
`logger.add("logs.log", rotation="10 MB", retention="5 days", compression="zip")` configures the log file's lifecycle: once it exceeds 10 MB, a new file is started; logs older than 5 days are automatically deleted; and archived logs are compressed to save disk space. The script then walks through the standard severity levels, from `debug` (detailed diagnostic info) up to `error` (unexpected failures).

---

## 🇩🇪 Deutsch

### Überblick
Dieses Skript demonstriert die Kernfunktionen der `loguru`-Bibliothek: das Schreiben von Logs in eine Datei mit automatischer Rotation, Aufbewahrung und Komprimierung, sowie die verschiedenen Log-Schweregrade (`info`, `debug`, `warning`, `error`, `success`).

### Funktionen
- Automatische Log-Datei-Rotation, sobald die Datei 10 MB erreicht
- Automatisches Löschen von Logs, die älter als 5 Tage sind
- Alte Logs werden als `.zip`-Archive komprimiert
- Zeigt alle wichtigen Log-Level in einem einzigen, einfachen Beispiel

### Voraussetzungen
- Python 3.10 oder höher
- `loguru`

### Installation
```bash
pip install loguru
```

### Verwendung
```bash
python loguru_example.py
```

Die Logs werden in der Konsole ausgegeben und gleichzeitig in `logs.log` im selben Verzeichnis gespeichert.

### Funktionsweise
`logger.add("logs.log", rotation="10 MB", retention="5 days", compression="zip")` konfiguriert den Lebenszyklus der Log-Datei: Sobald sie 10 MB überschreitet, wird eine neue Datei begonnen; Logs, die älter als 5 Tage sind, werden automatisch gelöscht; und archivierte Logs werden komprimiert, um Speicherplatz zu sparen. Das Skript durchläuft anschließend die Standard-Schweregrade, von `debug` (detaillierte Diagnoseinformationen) bis hin zu `error` (unerwartete Fehler).

---

## 🇹🇷 Türkçe

### Genel Bakış
Bu script, `loguru` kütüphanesinin temel özelliklerini gösterir: otomatik dosya döndürme (rotation), saklama (retention) ve sıkıştırma (compression) ile birlikte loglama, ve farklı log seviyeleri (`info`, `debug`, `warning`, `error`, `success`).

### Özellikler
- Log dosyası 10 MB'a ulaştığında otomatik olarak yenisi açılır
- 5 günden eski loglar otomatik olarak silinir
- Eski loglar `.zip` arşivi olarak sıkıştırılır
- Tüm önemli log seviyelerini tek, basit bir örnekte gösterir

### Gereksinimler
- Python 3.10 veya üzeri
- `loguru`

### Kurulum
```bash
pip install loguru
```

### Kullanım
```bash
python loguru_example.py
```

Loglar hem konsola yazdırılır hem de aynı klasördeki `logs.log` dosyasına kaydedilir.

### Nasıl çalışır?
`logger.add("logs.log", rotation="10 MB", retention="5 days", compression="zip")`, log dosyasının yaşam döngüsünü yapılandırır: dosya 10 MB'ı geçtiğinde yeni bir dosya başlatılır; 5 günden eski loglar otomatik olarak silinir; ve arşivlenen loglar disk alanından tasarruf etmek için sıkıştırılır. Script daha sonra standart önem seviyelerinden geçer: `debug` (detaylı tanılama bilgisi) ile başlayıp `error` (beklenmedik hatalar) ile devam eder.
