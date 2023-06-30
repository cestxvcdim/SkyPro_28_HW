import os


class Config:
    AD_ROOT_CSV = os.path.join("./datasets", "csv_data", "ad.csv")
    CATEGORY_ROOT_CSV = os.path.join("./datasets", "csv_data", "category.csv")
    LOCATION_ROOT_CSV = os.path.join("./datasets", "csv_data", "location.csv")
    USER_ROOT_CSV = os.path.join("./datasets", "csv_data", "user.csv")

    AD_ROOT_JSON = os.path.join("./datasets", "json_data", "ad.json")
    CATEGORY_ROOT_JSON = os.path.join("./datasets", "json_data", "category.json")
    LOCATION_ROOT_JSON = os.path.join("./datasets", "json_data", "location.json")
    USER_ROOT_JSON = os.path.join("./datasets", "json_data", "user.json")


config = Config()
