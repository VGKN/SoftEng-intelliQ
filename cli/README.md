# CLI Executable

## Contents
- Command Line interface

## Python3 packages

- [argparse] - Parser for command-line options, arguments 
- [requests] - Python HTTP library.
- [json]     - Built-in package used to work with JSON data.


## Installation
Για γρήγορη εγκατάσταση:

Στο git bash terminal
```sh
python -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt
```
Για να γίνεται να τρέξουμε scripts χωρίς "./"
```sh
export PATH="$PATH:/path/to/cli-client"
```

## Usage 
Χρήση σύμφωνη με το [document] που δόθηκε μαζί με τις οδηγίες της εργασίας
```sh
./se22XX scope --param1 value1 [--param2 value2 ...] --format fff
```
To get a help message for each scope
```sh
./se2219 scope -h
```

MIT

**Free Software, Hell Yeah!**

   [argparse]: https://docs.python.org/3/library/argparse.html
   [json]:https://docs.python.org/3/library/json.html
   [requests]: https://requests.readthedocs.io/en/master/
   [document]: https://helios.ntua.gr/pluginfile.php/1959/course/section/16951/project_softeng2022_part2_v01a.pdf
