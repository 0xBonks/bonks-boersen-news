import Foundation

// Pfad zur Python-Datei
let pythonFilePath = "/Users/bonks/code/boersen-news/core.py"

// Konfiguriere den Prozess
let process = Process()
process.launchPath = "/usr/local/bin/python3" // Pfad zur Python-Installation
process.arguments = [pythonFilePath]

// Führe den Prozess aus
process.launch()
process.waitUntilExit()