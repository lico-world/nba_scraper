from dataclasses import dataclass
from typing import List, Dict
import os
import toml

@dataclass
class Request:
    url: str
    stats: List[str]

@dataclass
class Config:
    http_delay: float
    years: List[int]
    teams: List[str]
    requests: Dict[str, Request]

def load() -> Config:
    config_file = os.path.join(os.path.dirname(__file__), 'config.toml')

    dictionary = toml.load(config_file)

    requests = {}
    for name, request in dictionary['requests'].items():
        requests[name] = Request(request['url'], request['stats'])

    return Config(dictionary['http_delay'], dictionary['years'], dictionary['teams'], requests)
