@echo off
cd /D C:\HiveCenter_cARM_bots

set csvFile=%2
set input=%3

ECHO %1%
ECHO %2%
ECHO %3%

If NOT "%csvFile%"=="%csvFile:csv=%" (
    pySeq.py %1 SeqValidateCSV Varcomm %2 %3 "Price Date"
) else (
    pySeq.py %1 SeqValidData Varcomm %2 %3
)

