from pathlib import Path

# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '

def tree(dir_path: Path, prefix: str=''):
    """
    A recursive generator that yields a visual tree structure of a directory.
    
    Parameters:
    - dir_path (Path): The directory path you want to visualize.
    - prefix (str): A string prefix for each line (used internally for recursion).
    
    Yields:
    - str: A line of the visual tree structure.
    
            └── datasets
                └── AG_NEWS
                    ├── train.csv
                    └── test.csv
    
    Usage:
    for line in tree(Path('/path/to/directory')):
        print(line)
    """
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): # extend the prefix and recurse:
            extension = branch if pointer == tee else space 
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)


