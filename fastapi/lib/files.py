
def file_json(file_dir, json_data):
    import json

    try :
        with open(file_dir, "a") as file:
            json.dump(json_data, file, indent=4)
    except:
        with open(file_dir, "w") as file:
            json.dump(json_data, file, indent=4)
    
    print("SUCCEED")


def files_to_hdfs(type, date):
    import subprocess
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, f'../datas/{type}/{date}')

    subprocess.run(["hdfs", "dfs", "-mkdir", f"/spotify/{type}/{date}"])
    subprocess.run(["hdfs", "dfs", "-put", f"{data_dir}/", f"/spotify/{type}/"])


if __name__ == "__main__":
    type = "tracks"
    date = "2023-10-11"
    files_to_hdfs(type, date)