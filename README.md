# calculate-concentrations
A Python script for calculating reagent concentrations in cDNA synthesis from a tsv file

## Usage

First, clone the repo:

```sh
$ git clone https://github.com/factcondenser/calculate-concentrations.git
```

Check if `natsort` module is installed:

```sh
$ python -c "import natsort"
$ echo $?
0                             # natsort module exists in system
```

or

```sh
$ python -c "import natsort"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named natsort
$ echo $?
1                             # natsort module does not exist in system
```

If necessary, install `natsort`:

```sh
$ pip install natsort
```

Run the script with the provided `.tsv` file - `sample.tsv` - or a `.tsv` of your own. Don't forget to specify whether you're making RNA or gDNA:
```sh
$ python calculate-concentrations.py sample.tsv RNA
```

The script will output `sample_working_dilutions.txt` or `<some .tsv file name>_working_dilutions.txt`:

```sh
$ ls
calculate_concentrations.py     sample_working_dilutions.txt
sample.tsv
```
