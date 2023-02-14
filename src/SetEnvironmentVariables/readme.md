## Setting Up Environment Variables

### Windows

If you are using Windows, you can set the environment variables by running either the `Set_Environment_Variable.bat` or `Set_Environment_Variables.ps1` file, depending on your preference. You will be prompted to enter your Spotify client ID and client secret ID. Depending on how your script execution policy for Powershell is set you may not be able to run the ps1 script, you are most likely better off using the bat file, both do the exact same thing.

### Linux and macOS

For Linux and macOS users, you can run the `Set_Persistent_Environment_Variables-Linux` or `Set_Persistent_Environment_Variables-MacOS.sh` file. For macOS, the script will add the environment variables to `/etc/launchd.conf`, and for Linux, it will add them to `/etc/environment`.

> Please note that for the macOS script to take effect, you will need to reload the `launchd` process by running `sudo launchctl < /etc/launchd.conf` after running the script.

Additionally, two versions of the Linux and macOS script are included. One version sets the environment variables persistently _( named according to the OS it's meant to run on. )_, and the other version sets them only for the current shell session. If for whatever reason you do not desire to set these variables forever run the one titled `Set_Shell_Environment_Variables`, do keep in mind you will require to run the script each time you want to use the python program if you don't use the persistent option, you may want to edit the `.sh` to contain your client and secret IDs if you want to use the non persistent script. _( non persistent script is not OS dependant. )_

>Note that depending on your system configuration _( mainly Linux users )_, you may need to modify these scripts to work correctly on your machine. Linux and macOS users may also need to `chmod +x` the `.sh` files to be able to execute them.

## Why set up Environment Variables?
Really you don't need to if you wish to just contiune to put the client and secret ID in the python file directly as thats still supported, it is generally considered better practice to use environment variables instead. Not only does it enhance security by removing sensitive information from the code, it additionally it makes it easier for me to not do the same on mistake well pushing to the repository.