# Python Scripting Study

###### os module

- os.environ - environmental variables

- os.chdir(path) - cd
- os.getcwd() - pwd
- os.chmod(path, mode) - chmod
- os.listdir(path) - ls
- os.mkdir(path) - mkdir
- os.remove(path) - rm
- os.removedirs(path) - rmdir
- os.rename(src, dst) - mv
- os.rmdir(path) - rmdir

- os.abort()
- os.fork()
- os.kill(pid, sig)
- os.nice(increment)
- os.system(command)
- os.wait()

- os.walk

```python
    '''use os.walk as iterator'''
    for root, dirs, files in os.walk(top, topdown=False):
```

###### os.path module

- os.path.exists(path)
- os.path.realpath
- os.path.join

###### regex module

- re.compile
- re.match
- re.search
- re.findall
- re.finditer

##### filesystem traversal

###### shutil module

- shutil.copy
- shutil.copy2
- shutil.copytree
- shutil.move

##### log processing

###### csv module

##### application deployment

##### simple HTTP requests

###### urllib module

```python
    '''basic request'''
    with urllib.request.urlopen('http://www.python.org/') as f:
        print(f.read(100).decode('utf-8'))
```
```python
    '''PUT request'''
    DATA = b'some data'
    req = urllib.request.Request(url='http://localhost:8080', data=DATA,method='PUT')
    with urllib.request.urlopen(req) as f:
        pass
    print(f.status)
    print(f.reason)
```

###### requests module

```python
    '''GET request'''
    res = requests.get('url')
    res.raise_for_status()
    res.status_code == requests.codes.ok
    res.text
```
```python
    '''POST request'''
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post('url', data=payload)
```

###### json module

- json.dumps
- json.loads