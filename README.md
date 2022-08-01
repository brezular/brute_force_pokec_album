# pokec_brutte_force_album

Unlock the photo album of a user of the popular Slovak social network Pokec. The album will only be unlocked with the password found in the passwords.txt 
file.

The configuration settings are defined in the config.py file. The variables username and password define the user credentials that are used to log into 
Pokec. The user and album name variables define the owner and album name. The album name should be written in lowercase, and if there are spaces between 
words, they must be replaced with hyphens (e.g. my-photos -> my-photos). The config.py file also contains the path to the passwords.txt file and 
the path to the ChromeDriver.

The read_passwords.py script reads passwords from the passwords.txt file and stores them in the Python list. The pokec.py script tests the passwords from the list one by one until it finds the correct password and the album is unlocked. I used Selenium WebDriver to emulate user interaction with a web browser.

Selenium WebDriver is a testing tool used to automate the testing of web applications. It is one of the components of the Selenium family, which also includes Selenium IDE, Selenium Client API, Selenium Remote Control and Selenium Grid. Selenium supports many programming languages such as Java, Python, C#, Ruby, Perl, and also web browsers such as Google Chrome, Mozilla Firefox, Internet Explorer, Safari.

You just need to download the ChromeDriver version which should match your Chrome browser version. ChromeDriver expects you to have Chrome installed in the default location for your platform.

Note:
Please use scripts only if you are the owner of the album. I am not responsible for any illegal use and I am not liable for any damages caused by the use of the script.

Usage:
------
- Download the scripts - config.py, passwords.py and pokec.py and store them to the same directory.
- Download the ChromeDriver binary for your platform (https://chromedriver.chromium.org/downloads). ChromeDrive must match your Chrome version
- Edit the config.py file and change the path to reflect the location of the ChromeDriver. Change the username and password in the config.py file to match 
  your Pokec credentials.
- Change the user and album name in config.py to reflect the owner of the album and the album name.
- Configure the path to the file with the passwords - passwords.txt file. Run the script pokec.py from the command line:

$ python3 ./pokec.py

Disclaimer:
I successfully tested the script and unlock my own photo album. However, since the the structure of the Pokec page may change in the future, the the scripts may not work as expected.
