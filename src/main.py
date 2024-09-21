import pandas as pd
import requests
import os
import polars
from typing import Union
import matplotlib.pyplot as plt


def generate_csv(file_name = None, params=None):
    base_url = "https://randomuser.me/api/"

    if not file_name:
        file_name = 'random_users.csv'


    # Default parameters; format is set to CSV
    default_params = {"format": "csv"}
    
    # If additional parameters are provided, merge them with the default ones
    if params:
        default_params.update(params)
    
    try:
        # Fetch CSV data from the API with the given parameters
        response = requests.get(base_url, params=default_params)
        response.raise_for_status()  # Raise an error for bad responses

        # Write the CSV content to a file
        with open(file_name, 'wb') as file:
            file.write(response.content)
        
        print(f"CSV data successfully saved to {file_name}")

        return file_name
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching data from API: {e}")


def read_csv(file_name : str, engine_type : str = 'pandas') -> Union[pd.DataFrame, polars.dataframe.frame.DataFrame]:
    """
    Reads the given file and returns the Pandas or Polars dataframe
    """

    assert engine_type.lower() in ['polars', 'pandas']
    
    engines = {
        'polars' : polars,
        'pandas' : pd
    }

    return engines.get(engine_type.lower()).read_csv(file_name)




def generate_summary( dataframe : Union[pd.DataFrame, polars.dataframe.frame.DataFrame], column : Union[list, str] = None ):

    if not column:
        column = dataframe.columns

    return dataframe[column].describe()



def create_histogram( dataframe, column, img_save_path = None ):
    values = dataframe[column].to_numpy()

    # Plotting the histogram using Matplotlib
    plt.hist(values, bins=10, edgecolor='black')
    plt.title('Histogram of Values')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    # plt.savefig(img_save_path, dpi=300, bbox_inches='tight')
    plt.close()

    return plt

def create_scatter_plot(dataframe, x_col, y_col, img_save_path = None ):
    
    x_val = dataframe[x_col].to_numpy()
    y_val = dataframe[y_col].to_numpy()
    plt.scatter(x_val, y_val, color='blue', marker='o')

    # Add titles and labels
    plt.title('Scatter Plot of X vs Y')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.grid(True)
    plt.show()
    # Save the scatter plot to a file
    # plt.savefig(img_save_path, dpi=300, bbox_inches='tight')  # Save as a PNG file

    # Optional: Clear the figure after saving
    plt.close()

    print("Scatter plot saved as 'scatter_plot.png'.")

    return plt


if __name__ == '__main__':

    default_file_folder = 'data'
    csv_file_name = 'random_user.csv'
    full_path = os.path.join(default_file_folder, csv_file_name)
    params = {"results" : 500}
    file_path = generate_csv(file_name=full_path, params=params)
    print(f'CSV generated at - {file_path}')
    df = read_csv(file_path, engine_type='pandas')
    # print(df.head())
    # print(df.shape)
    # print(type(df))

    res = generate_summary(df, column=['dob.age', 'location.coordinates.latitude'])

    # print(res)
    # print(res.shape)

    create_histogram(df, column = 'dob.age' )
    create_scatter_plot(df, x_col = 'dob.age', y_col='location.coordinates.latitude')