import os


pluginRootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if not pluginRootPath.endswith(os.sep):
    pluginRootPath += os.sep
