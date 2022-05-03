import zipfile

var_file_dir = "J:\\vam_vars\\___VarTidied___\\50shades\\50shades.Cum_pack_of_9.1.var"


def var_test():
    try:
        with zipfile.ZipFile(var_file_dir) as f:
            f.printdir()
            # print(type(f.getinfo('meta.json')))
            # print(f.getinfo('meta.json'))

            # print(type(f.infolist()))
            # print(f.infolist())
    except Exception as e:
        print("异常对象的类型是:%s" % type(e))
        print("异常对象的内容是:%s" % e)

    finally:
        f.close()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    var_test()
