
mkdir C:\NewsRanking

xcopy /s /y "%~dp0\pyNews" "C:\NewsRanking\pyNews\"
xcopy /a /y "%~dp0NewsRanking.ico" "C:\NewsRanking\"
xcopy /a /y "%~dp0manual.pdf" "C:\NewsRanking\"
xcopy /s /y "%~dp0\NewsRankingDesktop" "%UserProfile%\Desktop\NewsRanking\"
cd /D %~dp0
dir
pause
