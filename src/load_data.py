## Read the datat from data source
## Save it in the data/raw for further process

import os

from get_data import read_params, get_data

import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    cols_to_delete = config["base"]["cols_to_delete"]
    df = get_data(config_path)

    new_cols = [col.replace(' ','_') for col in df.columns if col not in cols_to_delete ] 


    raw_data_path = config["load_data"]["raw_dataset_csv"]

    for col_ in cols_to_delete:
        df = df.drop(col_, axis=1)

    df.dropna(inplace=True)

    df.to_csv(raw_data_path, sep=',', index=False, header=new_cols)





if __name__ == '__main__':

    args = argparse.ArgumentParser()
    args.add_argument("--config", default='params.yaml')
    parsed_args = args.parse_args()
    
    load_and_save(parsed_args.config)