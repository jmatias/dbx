import tempfile

from pipfile import Pipfile
parsed = Pipfile.load(filename="./Pipfile")

def _generate_pkg_str(k, v):
    # k contains pkg (e.g. jsonpath-ng)
    # v contains semver string (e.g. ==1.5.*)
    if v == "*":
        return k  # just add the package name
    return f"{k}{v}"  # add the qualified package (e.g. jsonpath-ng==1.5.*)
requirements_content = [_generate_pkg_str(k, v) for (k, v) in parsed.data['default'].items()]

print(requirements_content)

with tempfile.NamedTemporaryFile() as tmp:
    with open(tmp.name, 'w') as fh:
        for item in requirements_content:
            fh.write(f"{item}\n")

    print(tmp.name)
