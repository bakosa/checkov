from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.cloudformation.checks.resource.base_resource_value_check import BaseResourceCheck


class SQSQueueEncryption(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure all data stored in the SQS queue is encrypted"
        id = "CKV_AWS_27"
        supported_resources = ['AWS::SQS::Queue']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        properties = conf.get("Properties", {})
        kms_key_id_value = properties.get("KmsMasterKeyId")
        sse_enabled_value = properties.get("SqsManagedSseEnabled")

        if kms_key_id_value or sse_enabled_value:
            return CheckResult.PASSED
        return CheckResult.FAILED


check = SQSQueueEncryption()
