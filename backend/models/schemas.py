from pydantic import BaseModel
from typing import List, Optional


class ProjectCreate(BaseModel):
    name: str
    overview: str = ""
    content: str = ""
    image: str = ""


class CharacterCreate(BaseModel):
    name: str
    content: str = ""
    image: str = ""
    origin_project_id: Optional[str] = None


class PersonaCreate(BaseModel):
    name: str
    content: str = ""


class ScenarioCreate(BaseModel):
    title: str
    content: str = ""


class SessionCreate(BaseModel):
    project_id: str
    scenario_id: str
    persona_id: Optional[str] = None
    character_ids: List[str] = []
    title: str = "新しいセッション"
