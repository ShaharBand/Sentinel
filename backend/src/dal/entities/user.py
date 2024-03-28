from datetime import datetime

from beanie import Document
from pydantic import StrictStr, SecretStr, IPvAnyAddress


class User(Document):
    username: StrictStr
    password: SecretStr
    first_name: StrictStr
    last_name: StrictStr
    last_used_ip: IPvAnyAddress
    last_seen: datetime
    registration_date: datetime

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', last_seen='{self.last_seen}')>"
