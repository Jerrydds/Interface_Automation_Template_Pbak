import unittest, allure, pytest
from Main.run_test import RunTest


class TestGetRecP:

    def setup(self):
        self.run = RunTest(0)

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('测试步骤001')
    def test_001_Web全球英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(1)
        allure.attach('请求参数', '{"Version":"4.0","Method":"GET","Cookies":"",'
                              '"Param":{"site":0,"lang":"en","Platform":"2","pageSize":20,"pageNum":1,'
                              '"routing":"20_04_EBAY_BESTSALE","CacheType":2}}')
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_002_Web全球俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(2)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_003_Web美国英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(3)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_004_Web美国俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(4)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_005_Web俄罗斯英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(5)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_006_Web俄罗斯俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(6)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_007_App全球英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(7)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_008_Apр全球俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(8)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_009_App美国英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(9)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_010_App美国俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(10)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_011_App俄罗斯英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(11)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_012_App俄罗斯俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(12)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_013_参数名_站点错误(self):
        expect, authentic = self.run.go_on_run(13)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_014_参数名_语言错误(self):
        expect, authentic = self.run.go_on_run(14)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_015_参数名_平台错误(self):
        expect, authentic = self.run.go_on_run(15)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_016_参数名_每页数据量错误(self):
        expect, authentic = self.run.go_on_run(16)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_017_参数名_页码错误(self):
        expect, authentic = self.run.go_on_run(17)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_018_参数名_路由错误(self):
        expect, authentic = self.run.go_on_run(18)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_019_参数名_缓存类型错误(self):
        expect, authentic = self.run.go_on_run(19)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_020_参数值_站点错误(self):
        expect, authentic = self.run.go_on_run(20)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_021_参数值_语言错误(self):
        expect, authentic = self.run.go_on_run(21)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_022_参数值_平台错误(self):
        expect, authentic = self.run.go_on_run(22)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_023_参数值_每页数据量错误(self):
        expect, authentic = self.run.go_on_run(23)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_024_参数值_页码错误(self):
        expect, authentic = self.run.go_on_run(24)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_025_参数值_路由错误(self):
        expect, authentic = self.run.go_on_run(25)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_026_参数值_缓存类型错误(self):
        expect, authentic = self.run.go_on_run(26)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_027_参数值_站点为空(self):
        expect, authentic = self.run.go_on_run(27)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_028_参数值_语言为空(self):
        expect, authentic = self.run.go_on_run(28)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_029_参数值_平台为空(self):
        expect, authentic = self.run.go_on_run(29)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_030_参数值_每页数据量为空(self):
        expect, authentic = self.run.go_on_run(30)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_031_参数值_页码为空(self):
        expect, authentic = self.run.go_on_run(31)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_032_参数值_路由为空(self):
        expect, authentic = self.run.go_on_run(32)
        assert expect in authentic

    @allure.feature('产品')
    @allure.story('V4_推荐产品')
    def test_033_参数值_缓存类型为空(self):
        expect, authentic = self.run.go_on_run(33)
        assert expect in authentic

    # def test_001(self):
    #     expect, authentic = self.run.go_on_run(1)
    #     assert expect in authentic
    #
    # def test_002(self):
    #     expect, authentic = self.run.go_on_run(2)
    #     assert expect in authentic
    #
    # def test_003(self):
    #     expect, authentic = self.run.go_on_run(3)
    #     assert expect in authentic
    #
    # def test_004(self):
    #     expect, authentic = self.run.go_on_run(4)
    #     assert expect in authentic
    #
    # def test_005(self):
    #     expect, authentic = self.run.go_on_run(5)
    #     assert expect in authentic
    #
    # def test_006(self):
    #     expect, authentic = self.run.go_on_run(6)
    #     assert expect in authentic
    #
    # def test_007(self):
    #     expect, authentic = self.run.go_on_run(7)
    #     assert expect in authentic
    #
    # def test_008(self):
    #     expect, authentic = self.run.go_on_run(8)
    #     assert expect in authentic
    #
    # def test_009(self):
    #     expect, authentic = self.run.go_on_run(9)
    #     assert expect in authentic
    #
    # def test_010(self):
    #     expect, authentic = self.run.go_on_run(10)
    #     assert expect in authentic
    #
    # def test_011(self):
    #     expect, authentic = self.run.go_on_run(11)
    #     assert expect in authentic
    #
    # def test_012(self):
    #     expect, authentic = self.run.go_on_run(12)
    #     assert expect in authentic
    #
    # def test_013(self):
    #     expect, authentic = self.run.go_on_run(13)
    #     assert expect in authentic
    #
    # def test_014(self):
    #     expect, authentic = self.run.go_on_run(14)
    #     assert expect in authentic
    #
    # def test_015(self):
    #     expect, authentic = self.run.go_on_run(15)
    #     assert expect in authentic
    #
    # def test_016(self):
    #     expect, authentic = self.run.go_on_run(16)
    #     assert expect in authentic
    #
    # def test_017(self):
    #     expect, authentic = self.run.go_on_run(17)
    #     assert expect in authentic
    #
    # def test_018(self):
    #     expect, authentic = self.run.go_on_run(18)
    #     assert expect in authentic
    #
    # def test_019(self):
    #     expect, authentic = self.run.go_on_run(19)
    #     assert expect in authentic
    #
    # def test_020(self):
    #     expect, authentic = self.run.go_on_run(20)
    #     assert expect in authentic
    #
    # def test_021(self):
    #     expect, authentic = self.run.go_on_run(21)
    #     assert expect in authentic
    #
    # def test_022(self):
    #     expect, authentic = self.run.go_on_run(22)
    #     assert expect in authentic
    #
    # def test_023(self):
    #     expect, authentic = self.run.go_on_run(23)
    #     assert expect in authentic
    #
    # def test_024(self):
    #     expect, authentic = self.run.go_on_run(24)
    #     assert expect in authentic
    #
    # def test_025(self):
    #     expect, authentic = self.run.go_on_run(25)
    #     assert expect in authentic
    #
    # def test_026(self):
    #     expect, authentic = self.run.go_on_run(26)
    #     assert expect in authentic
    #
    # def test_027(self):
    #     expect, authentic = self.run.go_on_run(27)
    #     assert expect in authentic
    #
    # def test_028(self):
    #     expect, authentic = self.run.go_on_run(28)
    #     assert expect in authentic
    #
    # def test_029(self):
    #     expect, authentic = self.run.go_on_run(29)
    #     assert expect in authentic
    #
    # def test_030(self):
    #     expect, authentic = self.run.go_on_run(20)
    #     assert expect in authentic
    #
    # def test_031(self):
    #     expect, authentic = self.run.go_on_run(31)
    #     assert expect in authentic
    #
    # def test_032(self):
    #     expect, authentic = self.run.go_on_run(32)
    #     assert expect in authentic
    #
    # def test_033(self):
    #     expect, authentic = self.run.go_on_run(33)
    #     assert expect in authentic

    # def test_034(self):
    #     expect, authentic = self.run.go_on_run(34)
    #     assert expect in authentic

    # def test_035(self):
    #     expect, authentic = self.run.go_on_run(35)
    #     assert expect in authentic
    #
    # def test_036(self):
    #     expect, authentic = self.run.go_on_run(36)
    #     assert expect in authentic
    #
    # def test_037(self):
    #     expect, authentic = self.run.go_on_run(37)
    #     assert expect in authentic
    #
    # def test_038(self):
    #     expect, authentic = self.run.go_on_run(38)
    #     assert expect in authentic
    #
    # def test_039(self):
    #     expect, authentic = self.run.go_on_run(39)
    #     assert expect in authentic
