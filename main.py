# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import var_directory_handle
import var_file_handle



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # var_dir = "J:\\vam_vars\\___VarTidied___\\"
    # var_dir = "J:\\BaiduNetdiskDownload\\vam\\380G资源\\___VarTidied___\\"
    var_dir = "J:\\BaiduNetdiskDownload\\vam\\380G资源\\___VarRedundant___\\"
    l = var_directory_handle.get_var_list(var_dir)
    n = {}
    print(l)
    for i in l:
        n[i]=var_file_handle.get_var_mod(i,l[i])
    print(n)

