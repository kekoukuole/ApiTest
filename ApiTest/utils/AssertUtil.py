import jsonpath


class AssertUtil:

    def contains(self,check_value,expect_value):
        assert expect_value in check_value

    def length(self,check_value,expect_value):
        if not isinstance(check_value,list):
            check_value = [check_value]
        assert len(check_value) == expect_value


    def extract_by_jsonpath(self, extract_value: dict, extract_expression: str):
        """
        根据jsonpath获取值
        :param extract_value: res.json()
        :param extract_expression:$.token
        :return:
        """
        extract_value = jsonpath.jsonpath(extract_value, extract_expression)
        if not extract_expression:
            return
        elif len(extract_value) == 1:
            return extract_value[0]
        else:
            return extract_value

    def validate_response(self,response,validate_check):
        """
        校验结果
        :param response:
        :param validate_check:
        :return:
        """
        for check in validate_check:
            for check_type, check_value in check.items():
                # 实际结果
                actual_value = self.extract_by_jsonpath(response,check_value[0])
                #预期结果
                expect_value = check_value[1]
                if check_type in ["contains"]:
                    self.contains(actual_value,expect_value)
                elif check_type in["length"]:
                    self.length(actual_value,expect_value)