
def setup():
    import sys
    pr = project_root()
    for folder in [ 'src' ]:
        lib_folder = pr / folder
        sys.path.append(str(lib_folder))

def project_root():
    from pathlib import Path
    project_root = Path().resolve().parent
    return project_root