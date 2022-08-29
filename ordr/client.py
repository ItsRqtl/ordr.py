from socketio import Client
from ordr.classes import Skin, Server
from ordr.respond import *
from ordr.constant import *
import requests
from requests.structures import CaseInsensitiveDict

class OrdrClient:

    socket = Client()

    def __init__(self, apikey:str=None, developer:DeveloperMode=None) -> None:
        if developer == DeveloperMode.SUCCESS: apikey = "devmode_success"
        elif developer == DeveloperMode.FAIL: apikey = "devmode_fail"
        elif developer == DeveloperMode.WSFAIL: apikey = "devmode_wsfail"
        self.apikey = apikey
    
    def connect(self):
        self.socket.connect(url=WSURL)

    def disconnect(self):
        self.socket.disconnect()

    def create_render(self, replayURL:str, username:str, skin:Skin, resolution:Resolution=Resolution.X720, globalVolume:int=50, musicVolume:int=50, hitsoundVolume:int=50, showHitErrorMeter:bool=True, showUnstableRate:bool=True, showScore:bool=True, showHPBar:bool=True, showComboCounter:bool=True, showPPCounter:bool=True, showScoreboard:bool=False, showBorders:bool=False, showMods:bool=True, showResultScreen:bool=True, useSkinCursor:bool=True, useSkinColors:bool=False, useSkinHitsounds:bool=True, useBeatmapColors:bool=True, cursorRainbow:bool=False, cursorTrailGlow:bool=False, drawFollowPoints:bool=True, scaleToTheBeat:bool=False, sliderMerge:bool=False, objectsRainbow:bool=False, objectsFlashToTheBeat:bool=False, useHitCircleColor:bool=True, seizureWarning:bool=False, loadStoryboard:bool=True, loadVideo:bool=True, introBGDim:int=0, inGameBGDim:int=75, breakBGDim:int=30, BGParallax:bool=False, showDanserLogo:bool=True, skip:bool=True, cursorRipples:bool=False, cursorSize:float=1, cursorTrail:bool=True, drawComboNumbers:bool=True, sliderSnakingIn:bool=True, sliderSnakingOut:bool=True, showHitCounter:bool=False, showKeyOverlay:bool=True, showAvatarsOnScoreboard:bool=False, showAimErrorMeter:bool=False, playNightcoreSamples:bool=True):
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = f"replayURL={replayURL}&username={username}&resolution={resolution}&skin={skin.id}&customSkin={skin.customSkin}&globalVolume={globalVolume}&musicVolume={musicVolume}&hitsoundVolume={hitsoundVolume}&showHitErrorMeter={showHitErrorMeter}&showUnstableRate={showUnstableRate}&showScore={showScore}&showHPBar={showHPBar}&showComboCounter={showComboCounter}&showPPCounter={showPPCounter}&showScoreboard={showScoreboard}&showBorders={showBorders}&showMods={showMods}&showResultScreen={showResultScreen}&useSkinCursor={useSkinCursor}&useSkinColors={useSkinColors}&useSkinHitsounds={useSkinHitsounds}&useBeatmapColors={useBeatmapColors}&cursorRainbow={cursorRainbow}&cursorTrailGlow={cursorTrailGlow}&drawFollowPoints={drawFollowPoints}&scaleToTheBeat={scaleToTheBeat}&sliderMerge={sliderMerge}&objectsRainbow={objectsRainbow}&objectsFlashToTheBeat={objectsFlashToTheBeat}&useHitCircleColor={useHitCircleColor}&seizureWarning={seizureWarning}&loadStoryboard={loadStoryboard}&loadVideo={loadVideo}&introBGDim={introBGDim}&inGameBGDim={inGameBGDim}&breakBGDim={breakBGDim}&BGParallax={BGParallax}&showDanserLogo={showDanserLogo}&skip={skip}&cursorRipples={cursorRipples}&cursorSize={cursorSize}&cursorTrail={cursorTrail}&drawComboNumbers={drawComboNumbers}&sliderSnakingIn={sliderSnakingIn}&sliderSnakingOut={sliderSnakingOut}&showHitCounter={showHitCounter}&showKeyOverlay={showKeyOverlay}&showAvatarsOnScoreboard={showAvatarsOnScoreboard}&showAimErrorMeter={showAimErrorMeter}&playNightcoreSamples={playNightcoreSamples}&verificationKey={self.apikey}".replace("True", "true").replace("False", "false")
        resp = requests.post(f"{BASEURL}/renders", headers=headers, data=data)
        return NewRenderRespond(resp.status_code, resp.content)

    def get_render(self, pageSize:int=50, page:int=1, ordrUsername:str=None, replayUsername:str=None, renderID:int=None, nobots:bool=False, link:str=None, beatmapsetid:int=None, reduceInfo:bool=False):
        resp = requests.get(f"{BASEURL}/renders", params={"pageSize": pageSize, "page": page, "ordrUsername": ordrUsername, "replayUsername": replayUsername, "renderID": renderID, "nobots": f"{nobots}".lower(), "link": link, "beatmapsetid": beatmapsetid})
        return GetRenderRespond(resp.status_code, resp.content, reduceInfo)

    def get_skin(self, pageSize:int=100, page:int=1, search:str=None):
        resp = requests.get(f"{BASEURL}/skins", params={"pageSize": pageSize, "page": page, "search": search})
        return GetSkinRespond(resp.status_code, resp.content)

    def get_custom_skin(self, id:int):
        resp = requests.get(f"{BASEURL}/skins/custom", params={"id": id})
        return CustomSkinRespond(resp.status_code, resp.content)

    def get_online_count(self):
        resp = requests.get(f"{BASEURL}/servers/onlinecount")
        return int(resp.content.decode("utf-8")) if resp.status_code == 200 else None

    def get_servers(self):
        resp = requests.get(f"{BASEURL}/servers")
        return GetServersRespond(resp.status_code, resp.content)