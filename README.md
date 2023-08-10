
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

create an artifcats folder 

Use mlflow server command to start the server 


```bash
mlflow server  --backend-store-uri sqlite:///mlflow.db  --default-artifact-root ./artifacts  --host 0.0.0.0 -p 1234
```


For model monitoring used evidently:
```bash
 evidently ui --workspace ./workspace --port 8080
``````

https://docs.evidentlyai.com/get-started/tutorial-monitoring