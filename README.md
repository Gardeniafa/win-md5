# win-md5
md5 command for Windows CLI

Usage: md5 <input> [value]
  input: the object you want to calculate MD5 value for, if it is not existing file, it will be seem as string
  value: optional, the MD5 value to compare with, it should be real md5 value (32 characters with hexadecimal)
Example:
  md5 hello
  md5 path/to/file
  md5 hello 5d41402abc4b2a76b9719d911017c592


How to use it in Windows command line or powershell?
- Just download the bin file and copy it to your Windows path folder, or you can self build it use pyinstaller
