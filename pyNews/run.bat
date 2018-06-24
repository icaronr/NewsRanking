@echo off
 :: Roda o arquivo main.py no PowerShell
start /b /wait powershell -Command "cd C:\NewsRanking\pyNews\ | python main.py"
pause
cd "C:\NewsRanking\pyNews\saida"
explorer .

