from utils.YamlUtil import YamlUtil
from utils.AssertUtil import AssertUtil
from utils.log_util import logger

class ExtractUtil:
    def __init__(self):
        self.jsonpath_util = AssertUtil()
        self.yaml_util = YamlUtil()

    def extrect_data(self, res, extract):
        """
        根据extract表达式，获取接口内容并存入yaml
        :param res:res.json()
        :param extract:$.[0].id
        :return:
        """
        if extract:
            for key,expression in extract.items():
                try:
                    value = self.jsonpath_util.extract_by_jsonpath(res, expression)
                    # 写入yaml
                    self.yaml_util.write_extra_yaml({key:value})
                except Exception as e:
                    logger.error(f"变量{key}写入extract.yaml失败，请检查，error={e}")

    def extrect_url(self, url):
        # /orders/${get_extract_data(order_id)}/
        if "{" in url and "}" in url:
            return self.process_data(url)
        return url

    def process_data(self, data):
        if
