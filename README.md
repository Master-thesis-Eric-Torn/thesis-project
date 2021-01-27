Generate requirements.txt from packages installed with pip:
```bash
python -m pip list --format=freeze > requirements.txt
```
Generate environment.yml for the complete environment (conda + pip):
```bash
conda env export -n <env-name> > environment.yml
```