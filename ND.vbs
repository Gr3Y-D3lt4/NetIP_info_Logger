Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "py """ & CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName) & "\Network_details.py""", 0, False
Set WshShell = Nothing