#!/usr/bin/python3

import pkg_resources

# Информация о модулях которые должны быть установлены
modules_info = {
    'zipp': '3.7.0',
}
# Путь по которому модули должны быть установлены
modules_files_dir = '/usr/lib/python3.7/site-packages'

def test_module_exists():
    print("\n")
    for module in modules_info:
        try:
            dist = pkg_resources.get_distribution(module)
            modname, modversion, modlocation = dist.key, dist.version, dist.location
            print(f"{module}: {modname} {modversion} {modlocation}")
            assert module == modname
            assert modules_info[module] == modversion
            assert modules_files_dir == modlocation
        except:
            print(f"{module} did not pass the test")
            assert False