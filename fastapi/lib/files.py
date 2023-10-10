
def file_json(file_dir, json_data):
    import json

    try :
        with open(file_dir, "a") as file:
            json.dump(json_data, file, indent=4)
    except:
        with open(file_dir, "w") as file:
            json.dump(json_data, file, indent=4)
    
    print("SUCCEED")


def files_to_hdfs(folder_dir, hdfs_dir):
    import subprocess

    subprocess.run(["hdfs", "dfs", "-copyFromLocal", f"{folder_dir}/*", f"hdfs:///{hdfs_dir}/"])
    subprocess.run(["rm", f"{folder_dir}/*"])