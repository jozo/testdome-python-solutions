"""
30 min

Write a function that provides change directory (cd) function for an abstract file system.

Notes:
* Root path is '/'.
* Path separator is '/'.
* Parent directory is addressable as '..'.
* Directory names consist only of English alphabet letters (A-Z and a-z).
* The function should support both relative and absolute paths.
* The function will not be passed any invalid paths.
* Do not use built-in path-related functions.

For example:

    path = Path('/a/b/c/d')
    path.cd('../x')
    print(path.current_path)

should display '/a/b/c/x'.


    class Path:
        def __init__(self, path):
            self.current_path = path

        def cd(self, new_path):
            pass

    path = Path('/a/b/c/d')
    path.cd('../x')
    print(path.current_path)
"""


class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        if new_path.startswith('/'):
            self.current_path = new_path
        else:
            orig = self.current_path.split('/')
            for part in new_path.split('/'):
                if part == '..':
                    orig = orig.pop()
                else:
                    orig.append(part)

            if orig == ['']:
                self.current_path = '/'
            else:
                self.current_path = '/'.join(orig)


path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
