- To test the webapp go to :
  * https://mlops-prediction-0a639e686bbb.herokuapp.com
- For Mlflow go to:
  * https://dagshub.com/hanene2030/mlops_dvc.mlflow
- For DVC, Mlflow and evidently sample go to sample_3-evidently
- For Mlflow sample go to branch sample_2-mlflow
- For DVC sample  go to sample_1
Create the env

```bash
conda create -n mlops_dvc
```
Activate the env

```bash
conda activate mlops_dvc
```
Created a req file

Install the requirments

```bash
pip install -r requirments.txt
```

Generate data usining notebook : generate data


```bash
git init

dvc init

dvc add data_given/*.csv

git add . && git commit -m 'first commit'


git remote add origin https://github.com/hanene2030/mlops_dvc.git
git branch -M sample_1
git push origin sample_1

```


Updated dvc.yaml then :

```bash
dvc repro
```

dvc.lock file was created


Change alpha and l1_ratio values in the params.yml 
```bash
dvc repro

```

Use the following command

```bash
dvc metrics show

```

```bash
dvc metrics diff

```

tox command 
```bash

tox
```

for rebuilding
```bash
tox -r
```

pytest command
```bash 
pytest -v
```

setup commands 

```bash 
pip install -e .
```


Build your own pkge commands 

```bash 
python setup.py sdist bdist_wheel
```

