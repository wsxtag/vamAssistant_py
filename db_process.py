import sqlite3

'''
var 包体的database 数据结构
-----var_name：string
----var_path:string
----clothing_cnt:int
----scene_cnt:int
----looks_cnt:int
----hairstyle_cnt:int
----plugin_cnt:int
----assets_cnt:int
----preview_pic_cnt:int
----preview_pic_name:string

var模组的的database 数据结构
----mod-name:string
----type:string
----preview-pic-name:string

'''
# 建表的sql语句
Var_table_sql_txt = '''CREATE TABLE var_list
           (var_name TEXT PRIMARY KEY  NOT NULL,
            var_path TEXT,
            is_fav NUMBER,
            is_install  NUMBER,
            clothing_cnt NUMBER,
            clothing_mis_pic_cnt NUMBER,
            scene_cnt NUMBER,
            scene_mis_pic_cnt NUMBER,
            looks_cnt NUMBER,
            looks_mis_pic_cnt NUMBER,
            hairstyle_cnt NUMBER,
            hairstyle_mis_pic_cnt NUMBER,
            plugin_cnt NUMBER,
            plugin_mis_pic_cnt NUMBER,
            assets_cnt NUMBER,
            assets_mis_pic_cnt NUMBER,
            preview_pic_cnt NUMBER,
            preview_pic_name TEXT);'''

DATABASE_NAME = "var.db"
VAR_TABLE_NAME = 'var_list'
SQL_GET_ALL = '''SELECT * FROM {}'''.format(VAR_TABLE_NAME)


def make_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(Var_table_sql_txt)
    conn.commit()
    cur.close()


def init_db():
    var_data = {
        'AnythingFashionVR.3Pack_Jean_Shorts.1.var': {'clothing': [{'type': 'clothing', 'name': 'AFVR 3 black '
                                                                                                'Jean '
                                                                                                'Shorts',
                                                                    'path':
                                                                        'Custom/Clothing/Female/AnythingFashionVR/AFVR 3 black Jean Shorts/',
                                                                    'preview': 1}, {'type': 'clothing',
                                                                                    'name': 'AFVR 3 blue Jean Shorts',
                                                                                    'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR 3 blue Jean Shorts/',
                                                                                    'preview': 1},
                                                                   {'type': 'clothing',
                                                                    'name': 'AFVR 3 yellow Jean Shorts',
                                                                    'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR 3 yellow Jean Shorts/',
                                                                    'preview': 1}], 'scene': [], 'looks': [],
                                                      'hairstyle': [], 'plugin': [], 'assets': []},
        'AnythingFashionVR.Black_Shorts.1.var': {'clothing': [{'type': 'clothing', 'name': 'AFVR_Black_Shorts',
                                                               'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Black_Shorts/',
                                                               'preview': 1}, {'type': 'clothing',
                                                                               'name': 'AFVR_Black_Shorts_black shinny',
                                                                               'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Black_Shorts/',
                                                                               'preview': 1},
                                                              {'type': 'clothing',
                                                               'name': 'AFVR_Black_Shorts_Black',
                                                               'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Black_Shorts/',
                                                               'preview': 1}, {'type': 'clothing',
                                                                               'name': 'AFVR_Black_Shorts_Black2',
                                                                               'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Black_Shorts/',
                                                                               'preview': 1},
                                                              {'type': 'clothing',
                                                               'name': 'AFVR_Black_Shorts_black3',
                                                               'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Black_Shorts/',
                                                               'preview': 1}, {'type': 'clothing',
                                                                               'name': 'AFVR_Black_Shorts_Dark Blue',
                                                                               'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Black_Shorts/',
                                                                               'preview': 1},
                                                              {'type': 'clothing',
                                                               'name': 'AFVR_Black_Shorts_grey',
                                                               'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Black_Shorts/',
                                                               'preview': 1}, {'type': 'clothing',
                                                                               'name': 'AFVR_Black_Shorts_turquoise',
                                                                               'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Black_Shorts/',
                                                                               'preview': 1},
                                                              {'type': 'clothing',
                                                               'name': 'AFVR_Black_Shorts_yellow',
                                                               'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Black_Shorts/',
                                                               'preview': 1}], 'scene': [], 'looks': [],
                                                 'hairstyle': [], 'plugin': [], 'assets': []},
        'AnythingFashionVR.blue_shorts.1.var': {'clothing': [{'type': 'clothing', 'name': 'AFVR blue Shorts',
                                                              'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR blue Shorts/',
                                                              'preview': 1}], 'scene': [], 'looks': [],
                                                'hairstyle': [], 'plugin': [], 'assets': []},
        'AnythingFashionVR.Chi_summerDress_clubbingOutfit_Pack.1.var': {'clothing': [
            {'type': 'clothing', 'name': 'AFVR fishnets 01',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR fishnets 01/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Apple_top',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Apple_top/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_cosplay black Skirt_short',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_cosplay Black skirt_short/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Summer_dress',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Summer_dress/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Summer_dress_01 blue yellow pattern',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Summer_dress/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Summer_dress_02 pink strips',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Summer_dress/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Summer_dress_03 black',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Summer_dress/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Summer_dress_04 dog pattern',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Summer_dress/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Summer_dress_05 camo',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Summer_dress/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Summer_dress_06 pink hearts pattern',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Summer_dress/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Summer_dress_07 black see through',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Summer_dress/', 'preview': 1}], 'scene': [
            {'type': 'scene', 'name': 'AFVR_chi in clubbing outfit v1',
             'path': 'Saves/scene/AFVR Released models v1/', 'preview': 1},
            {'type': 'scene', 'name': 'AFVR_chi in summer dress v1',
             'path': 'Saves/scene/AFVR Released models v1/', 'preview': 1}], 'looks': [], 'hairstyle': [],
            'plugin': [], 'assets': []},
        'AnythingFashionVR.Flip_Flops.1.var': {'clothing': [{'type': 'clothing', 'name': 'AFVR FlipFlops',
                                                             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR FlipFlops/',
                                                             'preview': 1},
                                                            {'type': 'clothing', 'name': 'AFVR FlipFlops_black',
                                                             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR FlipFlops/',
                                                             'preview': 1},
                                                            {'type': 'clothing', 'name': 'AFVR FlipFlops_blue',
                                                             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR FlipFlops/',
                                                             'preview': 1},
                                                            {'type': 'clothing', 'name': 'AFVR FlipFlops_pink',
                                                             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR FlipFlops/',
                                                             'preview': 1},
                                                            {'type': 'clothing', 'name': 'AFVR FlipFlops_red',
                                                             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR FlipFlops/',
                                                             'preview': 1}, {'type': 'clothing',
                                                                             'name': 'AFVR FlipFlops_white blue',
                                                                             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR FlipFlops/',
                                                                             'preview': 1}, {'type': 'clothing',
                                                                                             'name': 'AFVR FlipFlops_yellow',
                                                                                             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR FlipFlops/',
                                                                                             'preview': 1}],
                                               'scene': [], 'looks': [], 'hairstyle': [], 'plugin': [],
                                               'assets': []}, 'AnythingFashionVR.Small_Panties_pack1.1.var': {
            'clothing': [{'type': 'clothing', 'name': 'AFVR Small Panties',
                          'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Small Panties/', 'preview': 1},
                         {'type': 'clothing', 'name': 'AFVR Small Panties_black lace',
                          'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Small Panties/', 'preview': 1},
                         {'type': 'clothing', 'name': 'AFVR Small Panties_cat',
                          'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Small Panties/', 'preview': 1},
                         {'type': 'clothing', 'name': 'AFVR Small Panties_pink',
                          'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Small Panties/', 'preview': 1},
                         {'type': 'clothing', 'name': 'AFVR Small Panties_red lace',
                          'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Small Panties/', 'preview': 0},
                         {'type': 'clothing', 'name': 'AFVR Small Panties_stripe',
                          'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Small Panties/', 'preview': 1},
                         {'type': 'clothing', 'name': 'AFVR Small Panties_white lace',
                          'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Small Panties/', 'preview': 1},
                         {'type': 'clothing', 'name': 'AFVR Small Panties_white',
                          'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Small Panties/', 'preview': 0}],
            'scene': [], 'looks': [], 'hairstyle': [], 'plugin': [], 'assets': []},
        'AnythingFashionVR.Space_Dress.1.var': {'clothing': [
            {'type': 'clothing', 'name': 'AFVR_Space_Dress_uniform',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Space_Dress_uniform/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Space_Dress_uniform_Blue',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Space_Dress_uniform/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Space_Dress_uniform_red',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Space_Dress_uniform/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR_Space_Dress_uniform_yellow',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Space_Dress_uniform/', 'preview': 1}],
            'scene': [], 'looks': [], 'hairstyle': [], 'plugin': [],
            'assets': []}, 'AnythingFashionVR.Tight_Gym_Bottoms.1.var': {
            'clothing': [{'type': 'clothing', 'name': 'AFVR_Tight_Bottoms',
                          'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR_Tight_Bottoms/', 'preview': 1}],
            'scene': [], 'looks': [], 'hairstyle': [], 'plugin': [], 'assets': []},
        'AnythingFashionVR.Tight_Gym_Top.1.var': {'clothing': [{'type': 'clothing', 'name': 'AFVR Tight_Top',
                                                                'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Tight_Top/',
                                                                'preview': 1}], 'scene': [], 'looks': [],
                                                  'hairstyle': [], 'plugin': [], 'assets': []},
        'AnythingFashionVR.Tight_white_Tshirt.1.var': {'clothing': [
            {'type': 'clothing', 'name': 'AFVR Tight White Tshirt',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Tight White Tshirt/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR Tight White Tshirt_implant breasts',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Tight White Tshirt/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR Tight White Tshirt_normal breasts',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Tight White Tshirt/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR Tight White Tshirt_small breasts',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Tight White Tshirt/', 'preview': 1},
            {'type': 'clothing', 'name': 'AFVR Tight White Tshirt_tight fit no sim',
             'path': 'Custom/Clothing/Female/AnythingFashionVR/AFVR Tight White Tshirt/', 'preview': 1}],
            'scene': [], 'looks': [], 'hairstyle': [], 'plugin': [],
            'assets': []}
    }

    conn = sqlite3.connect(DATABASE_NAME)

    # 清空数据库
    try:
        cur = conn.cursor()
        cur.execute("DROP TABLE var_list")
        conn.commit()
    except Exception as e:
        print(e)

    # 重新创建表格
    cur = conn.cursor()
    cur.execute(Var_table_sql_txt)
    conn.commit()

    for i in var_data:
        var_line = dict(var_name="", var_path="", is_fav=0, is_install=0, clothing_cnt=0, clothing_mis_pic_cnt=0,
                        scene_cnt=0,
                        scene_mis_pic_cnt=0, looks_cnt=0, looks_mis_pic_cnt=0, hairstyle_cnt=0, hairstyle_mis_pic_cnt=0,
                        plugin_cnt=0, plugin_mis_pic_cnt=0, assets_cnt=0, assets_mis_pic_cnt=0, preview_pic_cnt=0,
                        preview_pic_name='')

        var_line["var_name"] = i
        var_line["var_path"] = i
        var_line["is_fav"] = 0
        var_line["is_install"] = 0
        for j in var_data[i]:
            print(j)
            # print(var_data[i])
            # print(len(var_data[i][j]))
            var_line[j + "_cnt"] += len(var_data[i][j])
            for k in var_data[i][j]:
                print(k)
                if k["preview"] == 1:
                    var_line["preview_pic_cnt"] += 1
                    var_line["preview_pic_name"] += "&&&&" + k["type"] + "__" + i + "__" + k["name"] + ".jpg"
                else:
                    var_line[j + "_mis_pic_cnt"] += 1
                    print("miss")
        __data = [(
            var_line["var_name"],
            var_line["var_path"],
            var_line["is_fav"],
            var_line["is_install"],
            var_line["clothing_cnt"],
            var_line["clothing_mis_pic_cnt"],
            var_line["scene_cnt"],
            var_line["scene_mis_pic_cnt"],
            var_line["looks_cnt"],
            var_line["looks_mis_pic_cnt"],
            var_line["hairstyle_cnt"],
            var_line["hairstyle_mis_pic_cnt"],
            var_line["plugin_cnt"],
            var_line["plugin_mis_pic_cnt"],
            var_line["assets_cnt"],
            var_line["assets_mis_pic_cnt"],
            var_line["preview_pic_cnt"],
            var_line["preview_pic_name"]
        )]
        # 执行sql语句
        cur = conn.cursor()
        cur.executemany(
            '''INSERT INTO var_list (var_name,var_path,is_fav,is_install,clothing_cnt,
            clothing_mis_pic_cnt,scene_cnt,scene_mis_pic_cnt,looks_cnt,looks_mis_pic_cnt,hairstyle_cnt,
            hairstyle_mis_pic_cnt,plugin_cnt,plugin_mis_pic_cnt,assets_cnt,assets_mis_pic_cnt,
            preview_pic_cnt,preview_pic_name) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
            __data)
        conn.commit()
        cur.close()

    print(var_line)
    return True


def into_var():
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(Var_table_sql_txt)
    conn.commit()
    cur.close()


def into_mod():
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(Var_table_sql_txt)
    conn.commit()
    cur.close()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # make_db()
    # def into_var():
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    # 执行sql语句 获取全部的数据
    _data = cur.execute(SQL_GET_ALL)
    print(type(_data))
    for item in _data:
        print(type(item))
        print(item)
    conn.commit()
    cur.close()
