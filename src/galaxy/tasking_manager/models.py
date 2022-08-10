from ..validation.models import BaseModel
from typing import Optional
from enum import Enum


class ProjectStatus(Enum):
    """ Enum to describes all possible states of a Mapping Project """

    ARCHIVED = 0
    PUBLISHED = 1
    DRAFT = 2

class ValidatorStatsRequest(BaseModel):
    year: int = 2012
    country: Optional[str] = None
    organisation: Optional[str] = None
    status : Optional[ProjectStatus] = None
