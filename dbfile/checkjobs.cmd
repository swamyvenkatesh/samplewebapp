@echo off
cd /D C:\HiveCenter_cARM_bots
set starttime=%3
set itr=%4
IF [%3] == [] set starttime=2018-01-01 
IF [%4] == [] set itr=0
pySeq.py %1 SeqchkJobStatus %2 %starttime% %itr%
