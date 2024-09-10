# To store reusable function
import os
import datetime


def save_dataframe(df, folder_path, filename):

    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    df.to_csv(file_path, index=False)

    return file_path


def save_to_file(data, folder_name):

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"extracted_{timestamp}.txt"

    file_path = os.path.join(folder_name, file_name)

    with open(file_path, 'w') as file:
        file.write(data)

    # print(f"Data saved to: {file_path}")
    return {file_path}
