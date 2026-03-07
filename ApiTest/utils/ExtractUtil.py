from utils.AssertUtil import AssertUtil


class ExtractUtil:
    def __init__(self):
        self.jsonpath_util = AssertUtil

    def extrect_data(self, res, extract):
        """
        根据extract表达式，获取接口内容并存入yaml
        :param res:res.json()
        :param extract:$.[0].id
        :return:
        """
        if extract:
            for key,expression in extract.items():
                value = self.jsonpath_util.extract_by_jsonpath(res,expression)