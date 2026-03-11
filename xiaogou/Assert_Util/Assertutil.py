import jsonpath


class AssertUtil:

    def validate_response(self,res,validate):

        for chek in validate:
            for check_type, check_value in chek.items():
                actual_value = self.extract_by_jsonpath(res,check_value[0])
                expect_value = check_value[1]
                if check_type in ["eq"]:
                    self.contains(actual_value, expect_value)

    def extract_by_jsonpath(self,res,extract_expression):
        extract_value = jsonpath.jsonpath(res, extract_expression)
        if extract_value is False:
            return None
        elif len(extract_value) == 1:
            return extract_value[0]
        else:
            return extract_value

    def contains(self, actual_value, expect_value):
        assert expect_value in actual_value