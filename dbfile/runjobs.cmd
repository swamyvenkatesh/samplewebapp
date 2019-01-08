@echo off
set datecode=%date:~-4%-%date:~4,2%-%date:~7,2% %time:~0,2%:%time:~3,2%:%time:~6,2%
set itr=1
cd /D C:\HiveCenter_cARM_bots
echo Trg > C:\Prudential\TriggerFolder\%2.trg
cmd /c CheckJobs.cmd %1 %2 "%datecode%" %itr%
