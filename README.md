Generate requirements.txt with combined packages from conda/pip:
```bash
python -m pip list --format=freeze > requirements.txt
```

```bash
conda env export -n <env-name> > environment.yml
```