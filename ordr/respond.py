import json

from ordr.classes import Render, Server, get_skin, Request

class GetSkinRespond:
    def __init__(self, status, data) -> None:
        self.request = Request(status, data)
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            self.message = self._json["message"] if "message" in self._json else None
            self.maxSkins = self._json["maxSkins"] if "maxSkins" in self._json else None
            if "skins" in self._json:
                self.skins = []
                for i in self._json["skins"]:
                    self.skins.append(get_skin(i))
                if len(self.skins) == 0:
                    self.skins=None

class CustomSkinRespond:
    def __init__(self, status, data) -> None:
        self.request = Request(status, data)
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            self.found = self._json["found"]
            self.removed = self._json["removed"]
            self.message = self._json["message"]
            self.skinName = self._json["skinName"] if self.found == True else None
            self.skinAuthor = self._json["skinAuthor"] if self.found == True else None
            self.downloadLink = self._json["downloadLink"] if self.found == True else None


class GetRenderRespond:
    def __init__(self, status, data, reduce) -> None:
        self.request = Request(status, data)
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            self.maxRenders = self._json["maxRenders"] if "maxRenders" in self._json else None
            if "renders" in self._json:
                self.renders = []
                for i in self._json["server"]:
                    self.renders.append(Render(i, reduce))

class NewRenderRespond:
    def __init__(self, status, data) -> None:
        self.request = Request(status, data)
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            self.message = self._json["message"] if "message" in self._json else None
            self.renderID = self._json["renderID"] if "renderID" in self._json else None
            self.error = self._json["errorCode"] if "errorCode" in self._json else None
            self.reason = self._json["reason"] if "reason" in self._json else None

class GetServersRespond:
    def __init__(self, status, data) -> None:
        self.request = Request(status, data)
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            if "servers" in self._json:
                self.servers = []
                for i in self._json["server"]:
                    self.servers.append(Server(i))