@echo off

pyinstaller .\startup.py ^
--onefile ^
--log-level=DEBUG ^
--specpath=.\build\ ^
--name="recursive-extract" ^

