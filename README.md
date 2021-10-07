## no warranty is provided, proper testing should be done before being used in production environments. This repository is for demonstration purposes only.

# Concept
Users or automation will only have to update and create permissions plain text files and the python will hydrate permission files into TF files.

## Generate TF from a Jinja template

1. Write template in template directory.
2. Add permissions simple TXT file in permissions directory.
3. Run main.py and see output TF file in generated directory.


## Ideas Next Steps for prospective users.

1. Make script generate custom role name based on permission file name.
2. Load all files programatically and combine permissions resources in single TF file.

## Example output is in generated/iam.tf

