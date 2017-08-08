
/.git/ing all your data - Steps for putting it all together
=========================================================

**First things first, make sure you have your tools cloned from [https://github.com/internetwache/GitTools][1]**

**Step One**: Find some vulnerable sites

You can use google to do this quickly with an advanced search query. 

![][image-1]

You can also use nmap to discover this by running `nmap -A xx.xxx.xxx.xxx`

![][image-2]

You can also use the finder tool to discover sites that have their git repos exposed

` $ python3 gitfinder.py -i ~/myUrlsToTest.txt -o ~/vulnerableSites.txt`

Once you have found a vulnerable site there are two paths forward

![][image-3]

**Step Two**: Assuming directory listing is turned off,  pick a target from the `vulnerableSites.txt` list and run the dumper tool against it. If it doesn’t download the objects, open the config file it downloaded and see what url it is redirecting to. Restart the dumper tool against the new url.

` $ ./gitdumper.sh http://anyVulnerableSite.com/.git/ ~/dumpedSource `

**Step Three**: You should now have the dumped source code in the `dumpedSource` folder on your machine. You can try to run the extractor tool against it to see if it will rebuild the source. This doesn’t always work but its worth a try.

` $ ./extractor.sh ~/dumpedSource ~/rebuiltSource`

If it worked, you will then find all the source code files in `~/rebuiltSource`

If it didn’t, you can also try to make a fresh directory on your machine and clone  ` ~/dumpedSource` into it. Sometimes Git is smart enough to rebuild the source code files from the nested objects for you. 

If the extractor tool or a standard git clone doesn’t get you the source code files, then you must use Git Internals.

![][image-4]

The first thing you want to do is find out what the last commit on the master branch is. To do this run ` cat /.git/refs/heads/master` . The output will be a SHA1 hash. Save that hash somewhere.

Next, find out what tree is attached to that SHA1 you saved (insert your SHA1)
`git cat-file -p 72321A2529A310853ABA41AAFD9AD651EC40DF76`


You will see any output that contains a tree. Grab that SHA1 and repeat the process by running the same command

`git cat-file -p [tree SHA1 here]`

You will be presented with the source code files. Keep repeating the `git cat-file -p` command on the SHA1’s you are interested in viewing.

To make life easier, you can search using these commands:

![][image-5]

[1]:	https://github.com/internetwache/GitTools

[image-1]:	https://s3.amazonaws.com/hacking.online.public/google.png
[image-2]:	https://s3.amazonaws.com/hacking.online.public/nmap.png
[image-3]:	https://s3.amazonaws.com/hacking.online.public/twoPaths.png
[image-4]:	https://s3.amazonaws.com/hacking.online.public/gitInternalsOverview.png
[image-5]:	https://s3.amazonaws.com/hacking.online.public/search.png