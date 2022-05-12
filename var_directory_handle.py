import os
from typing import Dict, Any


def get_var_list(vd):
    var_dictionary: dict[Any, bytes | str] = {}
    for root, ds, fs in os.walk(vd):
        for f in fs:
            if f.endswith('.var'):
                fullname = os.path.join(root, f)
                var_dictionary[f] = fullname
                # yield var_dictionary

    return var_dictionary


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # var_file_dir = "J:\\vam_vars\\___VarTidied___\\50shades\\50shades.Cum_pack_of_9.1.var"
    var_dir = "J:\\vam_vars\\___VarTidied___\\"
    print(get_var_list(var_dir))
    print(len(var_dir))
