from typing import Literal, TypedDict


ContactInfoType = Literal[
    "cellphone",
    "email",
    "linkedin",
    "telegram",
    "github",
]


class ContactInfoDict(TypedDict):
    type: ContactInfoType
    value: str
