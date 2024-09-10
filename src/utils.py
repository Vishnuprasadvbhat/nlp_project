# To store reusable function
import os


def save_dataframe(df, folder_path, filename):
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    df.to_csv(file_path, index=False)

    return file_path
