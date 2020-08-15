# -*- coding:utf-8 -*- #
import json
import pathlib

app_dict = {
        'com.kuaiyin.player': ['https://imtt.dd.qq.com/16891/apk/857BD2C8E43A07ED15E44CEBC0B0C88C.apk?'
                     'fsname=com.kuaiyin.player_3.0.4_3000004.apk&csr=1bbd', '快音'],
        'com.tencent.weishi': ['https://imtt.dd.qq.com/16891/apk/6A33E7E854FF062EEBD9BAB23C2A0BA9.apk?'
                    'fsname=com.tencent.weishi_8.0.6.588_806.apk&csr=1bbd', '微视'],
        'com.jifen.qukan': ['https://imtt.dd.qq.com/16891/apk/936ECB3352A86C43C6FD31A18DE97E0E.apk?'
                        'fsname=com.jifen.qukan_3.9.91.000.0812.1549_30991000.apk&csr=1bbd', '趣头条'],
        'com.xiaoqiao.qclean': ['https://imtt.dd.qq.com/16891/apk/C2C1DF09F925A25166D8D2C3F23B3EAF.apk?'
                                 'fsname=com.xiaoqiao.qclean_1.1.2.4.0.0806.1012_11240.apk&csr=1bbd', '天天爱清理'],
        'com.zheyun.bumblebee': ['https://imtt.dd.qq.com/16891/apk/5C3F1A59237C863F7C71A9D44DCDF751.apk?'
                          'fsname=com.zheyun.bumblebee_2.1.7.200.0805.1455_20107200.apk&csr=1bbd', '趣铃声'],
        'com.jt.hanhan.video': ['https://imtt.dd.qq.com/16891/apk/8D83EF820BD165E152E68D5E793BD13E.apk?'
                                      'fsname=com.jt.hanhan.video_4.0.1.9.3_40193.apk&csr=1bbd', '火火视频极速版'],
        'com.jifen.dandan': ['https://imtt.dd.qq.com/16891/apk/18CB7A5EE6CE7D404D9BEC54C04A53FD.apk?'
                            'fsname=com.jifen.dandan_1.22.4.0805.2053_1224.apk&csr=1bbd', '彩蛋视频'],
        'com.funqingli.clear': ['https://6b4df949dc34805ea0326628c9362f91.dd.cdntips.com/imtt.dd.qq.com/'
                                 '16891/apk/6CC048FE618DD2C836BF8E844AA73AB2.apk?mkey=5f37b5c6794704ea&f=2206&'
                                 'fsname=com.funqingli.clear_2.4.2_28.apk&csr=1bbd&cip=121.71.34.31&proto=https',
                                 '绿色清理大师'],
        'com.jd.jdlite': ['https://imtt.dd.qq.com/16891/apk/59FF3E85BCE342A564746B8F88CEC37E.apk?'
                                'fsname=com.jd.jdlite_1.3.0_1049.apk&csr=1bbd', '京东极速版'],
        'com.jifen.ponycamera': ['https://imtt.dd.qq.com/16891/apk/41899ABBF1652EEF30D4CBD1849666DA.apk?'
                          'fsname=com.jifen.ponycamera_1.1.2.0709.1559_10012.apk&csr=1bbd', '小糖糕'],
        'com.jm.video': ['https://imtt.dd.qq.com/16891/apk/5365BF69132B5C9E4897ACEDFD226A52.apk?'
                     'fsname=com.jm.video_2.600_2600.apk&csr=1bbd', '刷宝'],
        'com.ss.android.ugc.aweme.lite': ['https://imtt.dd.qq.com/16891/apk/F7D6D13F8B330E25801C1FC437944DF2.apk?'
                              'fsname=com.ss.android.ugc.aweme.lite_11.1.0_110100.apk&csr=1bbd', '抖音极速版'],
        'com.kuaishou.nebula': ['https://imtt.dd.qq.com/16891/apk/706492C9954C646BEABEA2671BA70E7B.apk?'
                                'fsname=com.kuaishou.nebula_2.7.11.499_499.apk&csr=1bbd', '快手极速版'],
        'com.ss.android.ugc.livelite': ['https://imtt.dd.qq.com/16891/apk/FC398DA1BE9A06CEF933E3D2F747E29D.apk?'
                               'fsname=com.ss.android.ugc.livelite_7.9.0_790.apk&csr=1bbd', '火山极速版'],
        'com.video.kd': ['https://imtt.dd.qq.com/16891/apk/A76AA7CAABD3E312B96B35372BB439E2.apk?'
                                  'fsname=com.video.kd_1.0.6.0_20200608.apk&csr=1bbd', '快逗短视频'],
        'com.video.yy': ['https://imtt.dd.qq.com/16891/apk/95F32F0C709C7E3B54D627C7DC54A930.apk?'
                                 'fsname=com.video.yy_1.0.6.0_20200608.apk&csr=1bbd', '有颜短视频'],
        'com.cashtoutiao': ['https://imtt.dd.qq.com/16891/apk/A4206E365A46D2000CD469920C27F88F.apk?'
                         'fsname=com.cashtoutiao_4.2.3.0_79.apk&csr=1bbd', '惠头条'],
        'com.ss.android.article.lite': ['https://imtt.dd.qq.com/16891/apk/B94342A07E2C41457AB25BBC9DC69F70.apk?'
                                      'fsname=com.ss.android.article.lite_7.5.8.0_7580.apk&csr=1bbd', '今日头条极速版'],
        'com.xiangkan.android': ['https://imtt.dd.qq.com/16891/apk/86BC3C9606AAAA6A7FE2D08B2EF8937F.apk?'
                             'fsname=com.xiangkan.android_5.0.02_50002.apk&csr=1bbd', '想看资讯'],
    }


def store_app_info():
    path = pathlib.Path().cwd()
    if not pathlib.Path.exists(path / 'conf'):
        pathlib.Path.mkdir(path / 'conf', parents=True)
    with open(path / 'conf/app_info.json', 'w', encoding='UTF-8') as f:
        json.dump(app_dict, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    store_app_info()
