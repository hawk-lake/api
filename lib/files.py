
def file_json(file_dir, json_data):
    import json

    try :
        with open(file_dir, "a") as file:
            json.dump(json_data, file, indent=4)
    except:
        with open(file_dir, "w") as file:
            json.dump(json_data, file, indent=4)
    
    print("SUCCEED")
