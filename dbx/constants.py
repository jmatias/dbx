import pathlib

import pkg_resources

DBX_PATH = ".dbx"
INFO_FILE_PATH = f"{DBX_PATH}/project.json"
LOCK_FILE_PATH = f"{DBX_PATH}/lock.json"
DATABRICKS_MLFLOW_URI = "databricks"
PROJECTS_RELATIVE_PATH = "templates/projects"
TEMPLATE_CHOICES = pkg_resources.resource_listdir("dbx", PROJECTS_RELATIVE_PATH)
TEMPLATE_ROOT_PATH = pathlib.Path(pkg_resources.resource_filename("dbx", PROJECTS_RELATIVE_PATH))
