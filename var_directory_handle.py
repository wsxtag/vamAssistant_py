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


"""
                        '''INSERT INTO var_list (var_name,var_path,is_fav,is_install,clothing_cnt,clothing_mis_pic_cnt,scene_cnt,scene_mis_pic_cnt,looks_cnt,looks_mis_pic_cnt,hairstyle_cnt,hairstyle_mis_pic_cnt,plugin_cnt,plugin_mis_pic_cnt,assets_cnt,assets_mis_pic_cnt,preview_pic_cnt,preview_pic_name) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',

                    __data = [(
                        var_line["var_name“],
                        var_line["var_path“],
                        var_line["is_fav“],
                        var_line["is_install“],
                        var_line["clothing_cnt“],
                        var_line["clothing_mis_pic_cnt“],
                        var_line["scene_cnt“],
                        var_line["scene_mis_pic_cnt“],
                        var_line["looks_cnt“],
                        var_line["looks_mis_pic_cnt“],
                        var_line["hairstyle_cnt“],
                        var_line["hairstyle_mis_pic_cnt“],
                        var_line["plugin_cnt“],
                        var_line["plugin_mis_pic_cnt“],
                        var_line["assets_cnt“],
                        var_line["assets_mis_pic_cnt“],
                        var_line["preview_pic_cnt“],
                        var_line["scene_cnt“],
                        var_line["preview_pic_name“]
                    )]
"""