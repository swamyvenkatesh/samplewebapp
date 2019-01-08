@echo off
cd /D C:\HiveCenter_cARM_bots

set csvFile=%2

If NOT "%csvFile%"=="%csvFile:csv=%" (
    pySeq.py %1 %2 Varcomm %3 "Price Date"
) else (
    pySeq.py %1 SeqValidData Varcomm %2 "'DistribChan','Payment_Group_SyncCount','Payment_Schedules_SyncCount'"
)
