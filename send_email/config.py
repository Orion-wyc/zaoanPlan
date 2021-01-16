import os
import json


BASEDIR = os.path.join(os.path.dirname(__file__), os.pardir)


class Config:
    def __init__(self):
        self.config = self.json_parser()
        self.email_info = self.config["email_info"]
        self.to_addr = self.config["to_addr"]
        # self.to_addr = self.config["to_addr"]
        self.send_time = self.config["time_dict"]
        self.APIKEY = self.config["APIKEY"]

    @staticmethod
    def json_parser(filename=BASEDIR + "/example_greetings/test.json"):
        json_list = []
        with open(filename, 'r') as f:
            for row in f.readlines():
                if row.strip().startswith("//"):
                    continue
                json_list.append(row)
        conf = json.loads("".join(json_list))
        return conf


config = Config()

if __name__ == "__main__":
    # DIRS = os.path.dirname(__file__) + "/.."
    config = Config()
    print(config.config)
    print(config.email_info)
    print(config.to_addr)
    print(config.send_time)
    print(config.APIKEY)

    print(BASEDIR)