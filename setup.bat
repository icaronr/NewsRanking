:: Run as Admin!

::goto:current

:: Chocolatey
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"


choco update  :: Quick note: cinst = choco install

choco install python2 --params '"/InstallDir:C:\python2"'

$env:path >> path_backup.out

setx PATH "$env:path;C:\python2" -m

pip install -U pandas
pip install -U requests
pip install -U xlwt
pip install -U xlrd
pip install -U matplotlib
pip install -U XlsxWriter

mkdir C:\NewsRanking

xcopy /s /y "%~dp0\pyNews" "C:\NewsRanking\pyNews\"

