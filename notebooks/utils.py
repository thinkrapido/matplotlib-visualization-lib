
def setup():
    import sys
    project_root = project_root()
    for folder in [ 'src' ]:
        lib_folder = project_root / folder
        sys.path.append(str(lib_folder))

def project_root():
    from pathlib import Path
    project_root = Path().resolve().parent
    return project_root