import re
import os
import zipfile
from typing import Any

__REG_RULE__ = (
    ("(custom/clothing/.*)(?<=/)([^/]+)\x2e(?:vam|vap)", "clothing"),
    ("(custom/atom/person/clothing/.*)(?<=/)([^/]+)\x2e(?:vam|vap)", "clothing"),
    ("(saves/scene/.*)(?<=/)([^/]+)\x2e(?:json)", "scene"),
    ("(saves/person/appearance/.*)(?<=/)([^/]+)\x2e(?:json|vac)", "looks"),
    ("(custom/atom/person/(?:general|appearance)/.*)(?<=/)([^/]+)\x2e(?:json|vap)", "looks"),
    ("(custom/hair/.*)(?<=/)([^/]+)\x2e(?:vam|vap)", "hairstyle"),
    ("(custom/atom/person/hair/.*)(?<=/)([^/]+)\x2e(?:vam|vap)", "hairstyle"),
    ("(custom/scripts/.*)(?<=/)([^/]+)\x2e(?:cs)", "plugin"),
    ("(custom/atom/person/scripts/.*)(?<=/)([^/]+)\x2e(?:cs)", "plugin"),
    ("(custom/scripts/.*)(?<=/)([^/]+)\x2e(?:cslist)", "plugin"),
    ("(custom/atom/person/scripts/.*)(?<=/)([^/]+)\x2e(?:cslist)", "plugin"),
    ("(custom/assets/.*)(?<=/)([^/]+)\x2e(?:assetbundle)", "assets")
)


def reg_test():
    _txt = "J:/vam_vars/___VarTidied___/AcidBubbles/AcidBubbles.DraeneiFutaFemalePov.4.var"
    _reg = ".*(?<=/)([^/]+)\x2e(?:var)"

    _result = re.match(_reg, _txt, re.I)
    if _result:
        print(_result.group())
        print(_result.group(1))
        # print(_result.group(2))
    else:
        print("not macth")


def get_var_mod(var_name,var_path):
    var_data: dict[str, list[Any]] = {"clothing": [], "scene": [], "looks": [], "hairstyle": [], "plugin": [],
                                      "assets": []}

    try:
        with zipfile.ZipFile(var_path) as f:
            #验证包体合法性

            #读取模组
            for i in f.namelist():
                for j in __REG_RULE__:
                    _result = re.match(j[0], i, re.I)
                    if _result:
                        var_data[j[1]].append(
                            {"type": j[1], "name": _result.group(2), "path": _result.group(1), "preview": 0})

            #读取模组的预览图
            for l in var_data:
                if var_data[l]:
                    for m in var_data[l]:
                        _pic_path = m["path"] + m["name"] + ".jpg"
                        try:
                            fdata = f.read(_pic_path)
                            # 如果存在预览图，则写回标志位
                            m['preview'] = 1
                            _target_direct = os.getcwd() + "\\___PreviewPics__\\"
                            # _target_direct = os.getcwd() + "\\___PreviewPics__\\" + m["type"] + "\\" + var_name + "\\"
                            if not os.path.exists(_target_direct):
                                os.makedirs(_target_direct)

                            try:
                                (lambda ff, d: (ff.write(d), ff.close()))(open(_target_direct+ m["name"] + ".jpg", 'wb'), fdata)
                            except Exception as e:
                                print(e)

                        except Exception as e:
                            print(e)

    except Exception as e:
        print("异常对象的类型是:%s" % type(e))
        print("异常对象的内容是:%s" % e)

    finally:
        f.close()

    return var_data


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # var_file_dir = "J:\\vam_vars\\___VarTidied___\\50shades\\50shades.Cum_pack_of_9.1.var"
    var_file_path = "J:\\vam_vars\\___VarTidied___\\AcidBubbles\\AcidBubbles.DraeneiFutaFemalePov.4.var"
    var_name = "AcidBubbles.DraeneiFutaFemalePov.4.var"
    print(get_var_mod(var_name,var_file_path))

