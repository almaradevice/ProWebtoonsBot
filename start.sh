#!/bin/bash
# Jalankan bot di background
python main.py &
# Jalankan gunicorn di foreground (sebagai proses utama)
gunicorn app:app
