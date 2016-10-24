python
- os module
  os.mkdir
  os.getcwd
  os.path.realpath
  os.path.join
- regex module
  - re.compile
  - re.match
  - re.search
  - re.findall
  - re.finditer
*filesystem traversal
  - shutil module
    shutil.copy
    shutil.copy2
    shutil.copytree
    shutil.move
  - os.walk
    for root, dirs, files in os.walk(top, topdown=False):
*log processing
  - csv module
*application deployment
*simple HTTP requests
  - urllib module
    =====basic request=====
    with urllib.request.urlopen('http://www.python.org/') as f:
        print(f.read(100).decode('utf-8'))
    =====PUT request=====
    DATA = b'some data'
    req = urllib.request.Request(url='http://localhost:8080', data=DATA,method='PUT')
    with urllib.request.urlopen(req) as f:
        pass
    print(f.status)
    print(f.reason)
  - requests module
    =====GET request=====
    res = requests.get('url')
    res.raise_for_status()
    res.status_code == requests.codes.ok
    res.text
    =====POST request=====
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post('url', data=payload)
  - json module
    json.dumps
    json.loads