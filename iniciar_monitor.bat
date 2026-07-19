@echo off

cd /d D:\Projetos\detran-monitor

if not exist logs (
    mkdir logs
)

"C:\Users\geyds\AppData\Local\Programs\Python\Python311\python.exe" main.py