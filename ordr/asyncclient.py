from socketio import AsyncClient
from ordr.classes import Skin, Server
from ordr.respond import *
from ordr.constant import *
import aiohttp

class AsyncOrdrClient:

    socket = AsyncClient()

    def __init__(self, apikey:str=None, developer:DeveloperMode=None) -> None:
        if developer == DeveloperMode.SUCCESS: apikey = "devmode_success"
        elif developer == DeveloperMode.FAIL: apikey = "devmode_fail"
        elif developer == DeveloperMode.WSFAIL: apikey = "devmode_wsfail"
        self.apikey = apikey
    
    async def connect(self):
        await self.socket.connect(url="https://ordr-ws.issou.best")

    async def disconnect(self):
        await self.socket.disconnect()

    async def create_render(self, replayURL:str, username:str, skin:Skin, resolution:Resolution=Resolution.X720, globalVolume:int=50, musicVolume:int=50, hitsoundVolume:int=50, showHitErrorMeter:bool=True, showUnstableRate:bool=True, showScore:bool=True, showHPBar:bool=True, showComboCounter:bool=True, showPPCounter:bool=True, showScoreboard:bool=False, showBorders:bool=False, showMods:bool=True, showResultScreen:bool=True, useSkinCursor:bool=True, useSkinColors:bool=False, useSkinHitsounds:bool=True, useBeatmapColors:bool=True, cursorRainbow:bool=False, cursorTrailGlow:bool=False, drawFollowPoints:bool=True, scaleToTheBeat:bool=False, sliderMerge:bool=False, objectsRainbow:bool=False, objectsFlashToTheBeat:bool=False, useHitCircleColor:bool=True, seizureWarning:bool=False, loadStoryboard:bool=True, loadVideo:bool=True, introBGDim:int=0, inGameBGDim:int=75, breakBGDim:int=30, BGParallax:bool=False, showDanserLogo:bool=True, skip:bool=True, cursorRipples:bool=False, cursorSize:float=1, cursorTrail:bool=True, drawComboNumbers:bool=True, sliderSnakingIn:bool=True, sliderSnakingOut:bool=True, showHitCounter:bool=False, showKeyOverlay:bool=True, showAvatarsOnScoreboard:bool=False, showAimErrorMeter:bool=False, playNightcoreSamples:bool=True):
        async with aiohttp.ClientSession() as session:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = f"replayURL={replayURL}&username={username}&resolution={resolution}&skin={skin.id}&customSkin={skin.customSkin}&globalVolume={globalVolume}&musicVolume={musicVolume}&hitsoundVolume={hitsoundVolume}&showHitErrorMeter={showHitErrorMeter}&showUnstableRate={showUnstableRate}&showScore={showScore}&showHPBar={showHPBar}&showComboCounter={showComboCounter}&showPPCounter={showPPCounter}&showScoreboard={showScoreboard}&showBorders={showBorders}&showMods={showMods}&showResultScreen={showResultScreen}&useSkinCursor={useSkinCursor}&useSkinColors={useSkinColors}&useSkinHitsounds={useSkinHitsounds}&useBeatmapColors={useBeatmapColors}&cursorRainbow={cursorRainbow}&cursorTrailGlow={cursorTrailGlow}&drawFollowPoints={drawFollowPoints}&scaleToTheBeat={scaleToTheBeat}&sliderMerge={sliderMerge}&objectsRainbow={objectsRainbow}&objectsFlashToTheBeat={objectsFlashToTheBeat}&useHitCircleColor={useHitCircleColor}&seizureWarning={seizureWarning}&loadStoryboard={loadStoryboard}&loadVideo={loadVideo}&introBGDim={introBGDim}&inGameBGDim={inGameBGDim}&breakBGDim={breakBGDim}&BGParallax={BGParallax}&showDanserLogo={showDanserLogo}&skip={skip}&cursorRipples={cursorRipples}&cursorSize={cursorSize}&cursorTrail={cursorTrail}&drawComboNumbers={drawComboNumbers}&sliderSnakingIn={sliderSnakingIn}&sliderSnakingOut={sliderSnakingOut}&showHitCounter={showHitCounter}&showKeyOverlay={showKeyOverlay}&showAvatarsOnScoreboard={showAvatarsOnScoreboard}&showAimErrorMeter={showAimErrorMeter}&playNightcoreSamples={playNightcoreSamples}&verificationKey={self.apikey}".replace("True", "true").replace("False", "false")
            async with session.post(f"{BASEURL}/renders", data=data, headers=headers) as resp:
                return NewRenderRespond(resp.status, await resp.content.read())

    async def get_render(self, pageSize:int=50, page:int=1, ordrUsername:str="", replayUsername:str="", renderID:int="", nobots:bool=False, link:str="", beatmapsetid:int="", reduceInfo:bool=False):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASEURL}/renders", params={"pageSize": pageSize, "page": page, "ordrUsername": ordrUsername, "replayUsername": replayUsername, "renderID": renderID, "nobots": f"{nobots}".lower(), "link": link, "beatmapsetid": beatmapsetid}) as resp:
                return GetRenderRespond(resp.status, await resp.content.read(), reduceInfo)

    async def get_skin(self, pageSize:int=100, page:int=1, search:str=""):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASEURL}/skins", params={"pageSize": pageSize, "page": page, "search": search}) as resp:
                return GetSkinRespond(resp.status, await resp.content.read())

    async def get_custom_skin(self, id:int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASEURL}/skins/custom", params={"id": id}) as resp:
                return CustomSkinRespond(resp.status, await resp.content.read())

    async def get_online_count(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASEURL}/servers/onlinecount") as resp:
                content = await resp.content.read()
                return int(content.decode("utf-8")) if resp.status == 200 else None

    async def get_servers(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASEURL}/servers/onlinecount") as resp:
                return GetServersRespond(resp.status, await resp.content.read())