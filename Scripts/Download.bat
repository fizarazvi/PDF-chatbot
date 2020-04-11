@ECHO OFF
: : This bat file is used for the download of Glove Software
git clone https://github.com/maciejkula/glove-python.git ThirdPartyData

IF %ERRORLEVEL% gtr 0 GOTO THERE
Echo "Successfully downloaded"
Exit

:THERE
ECHO "Not Successful"
Exit