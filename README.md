
/.Git/ing all your data - Responsible Disclosure Automation
=========================================================

The repository contains a python module for automating 
responsible disclosure to a large number of websites. The script
takes an input of urls from a text file and performs a whois lookup
to determine the site owner. It then uses gmail to send a disclosure email
to the websites owners listed in the DNS registry. 

Developer - @securitybites

## Installation

1. Add your vulnerable URLs to files/urls.txt

2. Add in Google config info to sendDisclosure.py . You will need to generate a Google Apps password to do this.


## And theres more

1. You can use gittools to test for open git repositories. Clone it here: https://github.com/internetwache/GitTools . Shout out to gehaxeIt for creating this awesome toolset. Check out `gittingDeep.md` for more in-depth information on how to bring it all together and hack some stuff.

2. Take a look at /public\_files/. I have included a few files with millions of urls to test against.

3. Feel free to contribute and make these scripts more powerful. Pull requests encouraged.