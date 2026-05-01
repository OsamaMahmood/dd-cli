from enum import Enum


class ProductsListPrefetchItem(str, Enum):
    AUTHORIZATION_GROUPS = "authorization_groups"
    MEMBERS = "members"
    PRODUCT_MANAGER = "product_manager"
    PROD_TYPE = "prod_type"
    REGULATIONS = "regulations"
    SLA_CONFIGURATION = "sla_configuration"
    TEAM_MANAGER = "team_manager"
    TECHNICAL_CONTACT = "technical_contact"

    def __str__(self) -> str:
        return str(self.value)
