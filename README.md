## Introduction 

A python script to validate the crashes in LAVA-M, which is found by AFL or Angora.

## Usage

```bash
# run validate_lava.py
python validate_lava.py /path/to/target /path/to/output/directory /path/to/result/directory
```

The **/path/to/target** is the path of target (e.g., md5sum, uniq). The **/path/to/output/directory** is the output directory of AFL or Angora. The **/path/to/result/directory** is the directory to export the result of validating the crashes.

