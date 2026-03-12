from Assert_Util.Assertutil import AssertUtil
from util.YamlUtil import YamlUtil
from logger.log_util import logger


class ExtractUtil:
    def __init__(self):
        self.jsonpath_util = AssertUtil()
        self.yaml_util = YamlUtil()

    def extrect_data(self, response, extract):
        if extract:
            for key,expression in extract.items():
                try:
                    value = self.jsonpath_util.extract_by_jsonpath(response,expression)
                    self.yaml_util.write_extra_yaml({key:value})
                except ExtractUtil as e:
                    logger.error(f"变量{key}写入extract.yaml失败，请检查，error={e}")