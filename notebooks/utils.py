
def setup():
    import sys
    from pathlib import Path
    project_root = Path().resolve().parent
    for folder in [ 'src' ]:
        lib_folder = project_root / folder
        sys.path.append(str(lib_folder))
    