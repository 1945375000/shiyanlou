github url

https://github.com/1945375000/Louplus/blob/master/linux.png
name: 1945375000
pw: 1945375000zhengwf


$ cd /home/shiyanlou
$ chomd +x fibonacci2.py
$ ./fibonacci2.py

or create a new repository on the command line
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/1945375000/Fibonacci.git
git push -u origin master

or push an existing repository from the command line
git remote add origin https://github.com/1945375000/Fibonacci.git
git push -u origin master

git clone https://github.com/1945375000/Fibonacci.git
git add README.md
git commit -m "first commit"
git push


Requests
$ sudo apt -get update
$ sudo apt -get install python3-pip

$ sudo pip3 install requests

>>> import requests
>>> req=requests.get('https://github.com')
>>> req.status_code
