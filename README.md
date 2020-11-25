# Template README

* clone this repo
* delete the .git folder and do a new repo with the project name you want

```
git init
git add README.md
git commit -m ""
git remote add origin <url>
git push -u origin master
```

* depending on what you need, create a virtual env:

 * Python 2:
```
mkvirtualenv nameOfEnvironment
```

 * python 3:
```
which python3 #Output: /usr/bin/python3
mkvirtualenv --python=/usr/bin/python3 nameOfEnvironment
```

* make the requirements file
```
pip freeze > requirements.txt
```

* add the necessary files to the .gitignore
