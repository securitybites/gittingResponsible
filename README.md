
/.Git/ing all your data - Exposed git repository exploit and disclosure
=========================================================

The repository contains all the information you need to exploit git repositories on public websites (use at your own risk), as well as a python module for automating responsible disclosure to a large number of websites.

There are a two main components to this repo:
1.  A walkthrough on how to exploit git repos exposed on the root of a website. This includes identification, enumeration, and full data exfil. I also walk you through how to get past corrupt repos using git internals. To get started go read this: [https://github.com/securitybites/gittingResponsible/blob/master/gittingDeep.md][1]




2.  Responsible Disclosure - Now that you have probably identified a bunch of vulnerable sites, you need to be responsible and disclose the issue. Use my python script to help you automate it. The script takes an input of urls from a text file and performs a whois lookup to determine the site owner. It then uses gmail to send a disclosure email to the websites owners listed in the DNS registry. 

Developer - @securitybites

## Exploit Usage
1. Grab a website list from `/public_files/`and use https://github.com/internetwache/GitTools to enumerate.
2.  Follow `gittingDeep.md` to find sensitive data.

## Disclosure Script Installation

1. Add your vulnerable URLs to files/urls.txt

2. Add in Google config info to sendDisclosure.py . You will need to generate a Google Apps password to do this.


## Additional Details

1. You can use gittools to test for open git repositories. Clone it here: https://github.com/internetwache/GitTools . Shout out to gehaxeIt for creating this awesome toolset. Check out `gittingDeep.md` for more in-depth information on how to bring it all together and hack some stuff.

2. Take a look at /public\_files/. I have included a few files with millions of urls to test against.

3. Feel free to contribute and make these scripts more powerful. Pull requests encouraged.

[1]:	https://github.com/securitybites/gittingResponsible/blob/master/gittingDeep.md