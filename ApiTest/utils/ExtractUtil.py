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

    def get_extract_data(self,key):
        """
        从extract.yaml中获取内容
        :param key:
        :return:
        """
        try:
            data = self.yaml_util.read_extract_yaml()
            return data[key]
        except Exception as e:
            logger.error(f"从yaml中根据{key}获取不到内容，error={e}")

    def extrect_url(self, url):
        # /orders/${get_extract_data(order_id)}/
        if "${" in url and "}" in url:
            return self.process_data(url)
        return url

    def process_data(self, data):
        """处理函数"""
        for i in range(data.count("${")):
            if "${" in data and "}" in data:
                start_index = data.index("$")
                end_index = data.index("}")
                # 获取函数中
                func_full_name = data[start_index:end_index + 1]
                # 获取函数名
                func_name = data[start_index + 2:data.index('(')]
                # 获取函数中参数
                func_params = data[data.index('(') + 1: data.index(')')]
                extract_data = getattr(self, func_name)(*func_params.split(',') if func_params else "")
                data = data.replace(func_full_name, str(extract_data))
        return data