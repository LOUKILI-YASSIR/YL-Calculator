[Setup]
AppName=YL Calculator
AppVersion=1.0
DefaultDirName={pf}\YL-Calculator
DefaultGroupName=YL-Calculator
AllowNoIcons=yes
OutputBaseFilename=YL-Calculator-Setup
SetupIconFile=src\setup.ico
UninstallDisplayIcon=src\uninstall_icon.ico
LicenseFile=LICENSE

[Files]
Source: "dist\YL-Calculator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\*"; DestDir: "{app}\build"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "YL-Calculator.spec"; DestDir: "{app}\YL-Calculator.spec";
Source: "LICENSE"; DestDir: "{app}\LICENSE";
Source: "README.md"; DestDir: "{app}\README.md";
[Icons]
Name: "{group}\YL-Calculator"; Filename: "{app}\YL-Calculator.exe"; IconFilename: "{app}\src\app.ico"
Name: "{group}\Uninstall YL-Calculator"; Filename: "{uninstallexe}"; IconFilename: "{app}\src\uninstall_icon.ico" 

[Run]
Filename: "{app}\YL-Calculator.exe"; Description: "Launch YL-Calculator"; Flags: nowait postinstall
