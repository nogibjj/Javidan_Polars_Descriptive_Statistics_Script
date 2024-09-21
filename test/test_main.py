from src.main import generate_csv, read_csv, generate_summary, create_histogram, create_scatter_plot
import os
import polars
import pandas as pd

default_file_folder = 'data'

def test_generate_csv():
    list_of_params = [10, 100, 50 ,75]
    
    for param in list_of_params:
        csv_file_name = f"test_csv_{param}.csv"
        full_path = os.path.join(default_file_folder, csv_file_name)

        params = {"results" : param}
        file_path = generate_csv(file_name=full_path, params=params)

        assert os.path.exists(file_path)

        os.remove(file_path)



def test_read_csv():
    result_cnt = 100

    params = {'results' : result_cnt}
    csv_file_name = f"test_retrieval_data.csv"
    full_path = os.path.join(default_file_folder, csv_file_name)

    file_path = generate_csv(file_name=full_path, params=params)

    polars_df = read_csv(file_path, engine_type='polars')

    assert type(polars_df) == polars.dataframe.frame.DataFrame
    assert polars_df.shape[0] == result_cnt

    os.remove(file_path)



def test_plots():
    result_cnt = 100

    params = {'results' : result_cnt}
    csv_file_name = f"test_retrieval_data.csv"
    full_path = os.path.join(default_file_folder, csv_file_name)

    file_path = generate_csv(file_name=full_path, params=params)

    polars_df = read_csv(file_path, engine_type='polars')

    create_histogram(polars_df, polars_df.columns[0], img_save_path='data/test_histogram_polars.png')
    create_scatter_plot(polars_df, polars_df.columns[0], polars_df.columns[1], img_save_path='data/test_scatter_polars.png')

    assert os.path.exists('data/test_histogram_polars.png')
    assert os.path.exists('data/test_scatter_polars.png')

    os.remove(file_path) 
    os.remove('data/test_scatter_polars.png')
    os.remove('data/test_histogram_polars.png')