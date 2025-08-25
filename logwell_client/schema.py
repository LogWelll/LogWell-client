from pydantic import BaseModel, Field, model_validator
from enum import StrEnum
from typing import List


class Level(StrEnum):
    INFO = "INFO"
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
    FATAL = "FATAL"
    NOTSET = "NOTSET"


class LogCreateSchema(BaseModel):
    tenant: str | None = None
    log: dict | str = Field(default_factory=dict)
    execution_path: dict | None = None
    metadata: dict = Field(default_factory=dict)
    tag: str | None = None
    level: Level = Level.NOTSET
    group_path: List[str] | None = None


class Endpoint(StrEnum):
    Blocking = "/logs/"
    NonBlocking = "/logs/non-blocking/"
    BuiltInNonBlocking = "/logs/non-blocking/builtin/"
    List = "/logs/"
    Uid = "/logs/"
    Tag = "/logs/tag/"
    Level = "/logs/level/"
    Group_path = "/logs/group/"



class QueryParams(BaseModel):
    offset: int | None = 0
    limit: int | None = 10

class GroupPathFlag(StrEnum):
    ExactOnly = "exact_only"
    AllChildren = "all_children"


class LogQuerySchema(BaseModel):
    list: bool | None = None
    uid: str | None = None
    tag: str | None = None
    level: Level | None = None
    group_path: str | None = None
    group_path_flag: GroupPathFlag | None = None
    query_params: QueryParams | None = None

    @model_validator(mode="after")
    def validate_all_none(self):
        if list(self.model_dump(exclude_none=True).values()) == []:
            raise ValueError("At least one of the fields must be provided.")
        else:
            return self
        
    @model_validator(mode="after")
    def uid_and_query_params_not_allowed(self):
        if self.uid and self.query_params:
            raise ValueError("query_params are not allowed when uid is provided.")
        else:
            return self

    @model_validator(mode="after")        
    def only_one_of_list_uid_tag_level_group_path_is_allowed(self):
        exclusive_fields = ["list", "uid", "tag", "level", "group_path"]
        set_fields = [f for f in exclusive_fields if getattr(self, f) is not None]

        if len(set_fields) > 1:
            raise ValueError(
                f"Only one of {exclusive_fields} can be set, "
                f"but got multiple: {set_fields}"
            )
        return self
        
    @model_validator(mode="after")
    def group_path_flag_is_allowed_only_with_group_path(self):
        if self.group_path_flag and not self.group_path:
            raise ValueError("group_path_flag is allowed only with group_path.")
        else:
            return self