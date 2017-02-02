import os
import json
try:
    from common import pluginRootPath
except ImportError:
    from .common import pluginRootPath

def get():
    configFile = os.path.join(pluginRootPath, ".localconfig")
    if not os.path.exists(configFile):
        return {}

    with open(configFile, "r") as f:
        return json.load(f)

def save(d):
    configFile = os.path.join(pluginRootPath, ".localconfig")
    with open(configFile, "w") as f:
        json.dump(d, f)

if __name__ == "__main__":
    d = get()
    print(d)
    save(d)