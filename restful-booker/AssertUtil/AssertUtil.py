import jsonpath


class AssertUtil:


    def validate_response(self,res,validate):
        for chek in validate:
            for chek_type,chek_value in chek.items():
                # 实际结果
                actual_results = self.validate_jsonpath(res,chek_value[0])
                # 预期结果
                expected_results = chek_value[1]
                if chek_type in ["eq"]:
                    self.contains(actual_results,expected_results)
                elif chek_type in ["length"]:
                    self.length(actual_results,expected_results)
                elif chek_type in ["length_ge"]:
                    self.length_ge(actual_results,expected_results)



    def validate_jsonpath(self,res,chek_value):
        path_value = jsonpath.jsonpath(res,chek_value)
        if path_value is False:
            return None
        elif len(path_value) == 1:
            return path_value[0]
        else:
            return path_value

    def contains(self, actual_results, expected_results):
        assert expected_results in actual_results

    def length(self, actual_results, expected_results):
        if not isinstance(actual_results,list):
            actual_results = [actual_results]
        assert len(actual_results) == expected_results

    def length_ge(self, actual_results, expected_results):
        if not isinstance(actual_results,list):
            actual_results = [actual_results]
        assert len(actual_results) >= expected_results