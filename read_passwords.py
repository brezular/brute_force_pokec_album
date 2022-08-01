#v0.1

import config

with open(config.album_pass_file, "r") as f:
    data = f.read()

album_passwords = data.split("\n")[:-1]


