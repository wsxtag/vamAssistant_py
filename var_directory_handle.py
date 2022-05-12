import os


def get_var_list(vd):
    def find_all_file(vd):
        for root, ds, fs in os.walk(base):
            for f in fs:
                if f.endswith('.var'):
                    fullname = os.path.join(root, f)
                    var_dictionary = {}
                    var_dictionary[f] = fullname
                    yield var_dictionary

    return vd


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # var_file_dir = "J:\\vam_vars\\___VarTidied___\\50shades\\50shades.Cum_pack_of_9.1.var"
    var_dir = "J:\\vam_vars\\___VarTidied___\\AcidBubbles\\AcidBubbles.DraeneiFutaFemalePov.4.var"
    print(get_var_list(var_dir))
