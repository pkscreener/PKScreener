# Installation Guide

This is a troubleshooting guide for installing [pkscreener](https://github.com/pkjmesra/PKScreener) on your computer.

## For MacOS

### One Time Configuration

1. Download the executable from the [Latest Release](https://github.com/pkjmesra/PKScreener/releases/latest)
2. Open `Terminal` from `Applications > Utility > Terminal`
3. Execute following commands in the terminal (Commands are **Case Sensitive**)
```
cd Downloads                 # Navigate to Downloads folder
chmod +x pkscreenercli.run       # Apply Execute permission to the file
```

4. Right click on 'pkscreenercli.run' and select option `Open with > Utilities > Terminal`. (Select All applications if `Terminal` is frozen)
5. You may get **Developer not Verified** error as follow:

![Error](https://user-images.githubusercontent.com/6128978/119251001-95214580-bbc1-11eb-8484-e07ba33730dc.PNG)

6.Click on the **`?`** Icon. The following prompt will appear on the right bottom of your screen.

![Prompt](https://user-images.githubusercontent.com/6128978/119251025-c39f2080-bbc1-11eb-8103-9f0d267ff4e4.PNG)

7. Click on `Open General Pane for me` option.
8. This will open following **Security and Privacy** window.
9. Click on **`Open Anyway`** Button to grant executable permission for the pkscreener. (Enter your password if prompted)

![Allow](https://user-images.githubusercontent.com/6128978/119251073-11b42400-bbc2-11eb-9a15-7ebb6fec1c66.PNG)

10. Close the window.
11. Now double click on `pkscreenercli.run` file to use the application.

Alternative:
1. You can simply open terminal on your Mac and run 
```
sudo xattr -d com.apple.quarantine <full-path-where-you-downloaded-pkscreenercli.run>

```

enter your password and hit enter. 

2. Run the application.

See https://iboysoft.com/howto/apple-cannot-check-it-for-malicious-software.html
