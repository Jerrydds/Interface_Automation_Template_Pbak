import pytest, allure
from Main.run_test import RunTest


# 添加 pytest
class TestGetFrontQSortL:

    def setup(self):
        self.run = RunTest(2)

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_001_Web全球英语_前端筛选条件周转化率(self):
        expect, authentic = self.run.go_on_run(1)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_002_Web全球英语_前端筛选条件周点击率(self):
        expect, authentic = self.run.go_on_run(2)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_003_Web全球英语_前端筛选条件周ECPC(self):
        expect, authentic = self.run.go_on_run(3)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_004_Web全球英语_前端筛选条件周曝光(self):
        expect, authentic = self.run.go_on_run(4)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_005_Web全球英语_前端筛选条件周点击(self):
        expect, authentic = self.run.go_on_run(5)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_006_Web全球英语_前端筛选条件周转化(self):
        expect, authentic = self.run.go_on_run(6)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_007_Web全球英语_前端筛选条件周佣金(self):
        expect, authentic = self.run.go_on_run(7)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_008_Web全球英语_前端筛选条件总转化率(self):
        expect, authentic = self.run.go_on_run(8)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_009_Web全球英语_前端筛选条件总点击率(self):
        expect, authentic = self.run.go_on_run(9)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_010_Web全球英语_前端筛选条件总ECPC(self):
        expect, authentic = self.run.go_on_run(10)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_011_Web全球英语_前端筛选条件总曝光(self):
        expect, authentic = self.run.go_on_run(11)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_012_Web全球英语_前端筛选条件总点击(self):
        expect, authentic = self.run.go_on_run(12)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_013_Web全球英语_前端筛选条件总转化(self):
        expect, authentic = self.run.go_on_run(13)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_014_Web全球英语_前端筛选条件总佣金(self):
        expect, authentic = self.run.go_on_run(14)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_015_Web全球英语_前端筛选条件包含文本(self):
        expect, authentic = self.run.go_on_run(15)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_016_Web全球英语_前端筛选条件排除文本(self):
        expect, authentic = self.run.go_on_run(16)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_017_Web全球英语_前端筛选条件排除推荐(self):
        expect, authentic = self.run.go_on_run(17)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_018_Web全球英语_前端筛选条件包含广告商id(self):
        expect, authentic = self.run.go_on_run(18)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_019_Web全球英语_前端筛选条件包含平台(self):
        expect, authentic = self.run.go_on_run(19)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_020_Web全球英语_前端筛选条件产品价格(self):
        expect, authentic = self.run.go_on_run(20)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_021_Web全球英语_前端筛选条件产品类别(self):
        expect, authentic = self.run.go_on_run(21)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_022_Web全球英语_前端筛选条件产品折扣(self):
        expect, authentic = self.run.go_on_run(22)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_023_Web全球英语_前端筛选条件广告类型(self):
        expect, authentic = self.run.go_on_run(23)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_024_Web全球英语_前端筛选条件广告商类别(self):
        expect, authentic = self.run.go_on_run(24)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_025_Web全球英语_前端筛选条件类似广告商(self):
        expect, authentic = self.run.go_on_run(25)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_026_Web全球英语_前端排序条件最后一次点击时间升序(self):
        expect, authentic = self.run.go_on_run(26)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_027_Web全球英语_前端排序条件最后一次点击时间降序(self):
        expect, authentic = self.run.go_on_run(27)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_028_Web全球英语_前端排序条件1天平均点击时间升序(self):
        expect, authentic = self.run.go_on_run(28)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_029_Web全球英语_前端排序条件1天平均点击时间降序(self):
        expect, authentic = self.run.go_on_run(29)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_030_Web全球英语_前端排序条件7天平均点击时间升序(self):
        expect, authentic = self.run.go_on_run(30)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_031_Web全球英语_前端排序条件7天平均点击时间降序(self):
        expect, authentic = self.run.go_on_run(31)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_032_Web全球英语_前端排序条件ES搜索匹配度升序(self):
        expect, authentic = self.run.go_on_run(32)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_033_Web全球英语_前端排序条件ES搜索匹配度降序(self):
        expect, authentic = self.run.go_on_run(33)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_034_Web全球英语_前端排序条件周转化率升序(self):
        expect, authentic = self.run.go_on_run(34)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_035_Web全球英语_前端排序条件周转化率降序(self):
        expect, authentic = self.run.go_on_run(35)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_036_Web全球英语_前端排序条件周点击率升序(self):
        expect, authentic = self.run.go_on_run(36)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_037_Web全球英语_前端排序条件周点击率降序(self):
        expect, authentic = self.run.go_on_run(37)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_038_Web全球英语_前端排序条件周ECPC升序(self):
        expect, authentic = self.run.go_on_run(38)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_039_Web全球英语_前端排序条件周ECPC降序(self):
        expect, authentic = self.run.go_on_run(39)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_040_Web全球英语_前端排序条件周曝光数升序(self):
        expect, authentic = self.run.go_on_run(40)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_041_Web全球英语_前端排序条件周曝光数降序(self):
        expect, authentic = self.run.go_on_run(41)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_042_Web全球英语_前端排序条件周点击数升序(self):
        expect, authentic = self.run.go_on_run(42)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_043_Web全球英语_前端排序条件周点击数降序(self):
        expect, authentic = self.run.go_on_run(43)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_044_Web全球英语_前端排序条件周转化数升序(self):
        expect, authentic = self.run.go_on_run(44)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_045_Web全球英语_前端排序条件周转化数降序(self):
        expect, authentic = self.run.go_on_run(45)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_046_Web全球英语_前端排序条件周佣金升序(self):
        expect, authentic = self.run.go_on_run(46)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_047_Web全球英语_前端排序条件周佣金降序(self):
        expect, authentic = self.run.go_on_run(47)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_048_Web全球英语_前端排序条件总转化率升序(self):
        expect, authentic = self.run.go_on_run(48)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_049_Web全球英语_前端排序条件总转化率降序(self):
        expect, authentic = self.run.go_on_run(49)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_050_Web全球英语_前端排序条件总点击率升序(self):
        expect, authentic = self.run.go_on_run(50)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_051_Web全球英语_前端排序条件总点击率降序(self):
        expect, authentic = self.run.go_on_run(51)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_052_Web全球英语_前端排序条件总ECPC升序(self):
        expect, authentic = self.run.go_on_run(52)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_053_Web全球英语_前端排序条件总ECPC降序(self):
        expect, authentic = self.run.go_on_run(53)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_054_Web全球英语_前端排序条件总曝光数升序(self):
        expect, authentic = self.run.go_on_run(54)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_055_Web全球英语_前端排序条件总曝光数降序(self):
        expect, authentic = self.run.go_on_run(55)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_056_Web全球英语_前端排序条件总点击数升序(self):
        expect, authentic = self.run.go_on_run(56)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_057_Web全球英语_前端排序条件总点击数降序(self):
        expect, authentic = self.run.go_on_run(57)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_058_Web全球英语_前端排序条件总转化数升序(self):
        expect, authentic = self.run.go_on_run(58)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_059_Web全球英语_前端排序条件总转化数降序(self):
        expect, authentic = self.run.go_on_run(59)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_060_Web全球英语_前端排序条件总佣金升序(self):
        expect, authentic = self.run.go_on_run(60)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_061_Web全球英语_前端排序条件总佣金降序(self):
        expect, authentic = self.run.go_on_run(61)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_062_Web全球英语_前端排序条件创建时间升序(self):
        expect, authentic = self.run.go_on_run(62)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_063_Web全球英语_前端排序条件创建时间降序(self):
        expect, authentic = self.run.go_on_run(63)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_064_Web全球英语_前端排序条件广告商_名称升序(self):
        expect, authentic = self.run.go_on_run(64)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_065_Web全球英语_前端排序条件广告商_广告数量降序(self):
        expect, authentic = self.run.go_on_run(65)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_066_Web全球英语_前端排序条件广告结束时间降序(self):
        expect, authentic = self.run.go_on_run(66)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_067_Web全球英语_前端排序条件产品一价格升序(self):
        expect, authentic = self.run.go_on_run(67)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_068_Web全球英语_前端排序条件产品一价格降序(self):
        expect, authentic = self.run.go_on_run(68)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_069_Web全球英语_前端排序条件产品_折扣升序(self):
        expect, authentic = self.run.go_on_run(69)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_产品前端筛选_排序校验')
    def test_070_Web全球英语_前端排序条件产品_折扣降序(self):
        expect, authentic = self.run.go_on_run(70)
        assert expect in authentic
