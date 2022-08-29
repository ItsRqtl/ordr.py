# API Reference

This page outlines the API wrapper of ordr.py

## CLIENT

- [OrdrClient](#ordrclient)
- [AsyncOrdrClient](#asyncordrclient)

## Respond Object

- [NewRenderRespond](#newrenderrespond)
- [GetRenderRespond](#getrenderrespond)
- [GetSkinRespond](#getskinrespond)
- [CustomSkinRespond](#customskinrespond)
- [GetServersRespond](#getserversrespond)

## Model Object

- [Skin](#skin)
- [Server](#server)
- [Render](#render)
- [Request](#request)

---

# CLIENT

## OrdrClient

## `class ordr.OrdrClient(apikey: str = None, developer: ordr.DeveloperMode = None)`

PARAMETERS:

- apikey (Optional\[[str](https://docs.python.org/3/library/stdtypes.html#str)]) - an key for o!rdr API
- developer (Optional\[[DeveloperMode]()]) - options for developer mode

### `connect()` ⇒ `None`

Starts the client session.

### `disconnect()` ⇒ `None`

Ends the client session.

### `create_render(params)` ⇒ \[[NewRenderRespond](#newrenderrespond)]

Create a new render on o!rdr

| Param                              | Type                 | Default            |
| ---------------------------------- | -------------------- | ------------------ |
| BGParallax              | Boolean | False |
| breakBGDim              | Number  | 30    |
| cursorRainbow           | Boolean | False |
| cursorRipples           | Boolean | False |
| cursorScaleToCS         | Boolean | False |
| cursorSize              | Number  | 1     |
| cursorTrail             | Boolean | True  |
| cursorTrailGlow         | Boolean | False |
| drawComboNumbers        | Boolean | True  |
| drawFollowPoints        | Boolean | True  |
| globalVolume            | Number  | 50    |
| hitsoundVolume          | Number  | 50    |
| inGameBGDim             | Number  | 75    |
| introBGDim              | Number  | 0     |
| loadStoryboard          | Boolean | True  |
| loadVideo               | Boolean | True  |
| musicVolume             | Number  | 50    |
| objectsFlashToTheBeat   | Boolean | False |
| objectsRainbow          | Boolean | False |
| playNightcoreSamples    | Boolean | True  |
| replayURL               | String  |                    |
| resolution              | [Object]()  |                    |
| scaleToTheBeat          | Boolean | False |
| seizureWarning          | Boolean | False |
| showAimErrorMeter       | Boolean | False |
| showAvatarsOnScoreboard | Boolean | False |
| showBorders             | Boolean | False |
| showComboCounter        | Boolean | True  |
| showDanserLogo          | Boolean | True  |
| showHPBar               | Boolean | True  |
| showHitCounter          | Boolean | False |
| showHitErrorMeter       | Boolean | True  |
| showKeyOverlay          | Boolean | True  |
| showMods                | Boolean | True  |
| showPPCounter           | Boolean | True  |
| showResultScreen        | Boolean | True  |
| showScore               | Boolean | True  |
| showScoreboard          | Boolean | False |
| showUnstableRate        | Boolean | True  |
| skin                    | [Object](#skin)  |                    |
| skip                    | Boolean | True  |
| sliderMerge             | Boolean | False |
| sliderSnakingIn         | Boolean | True  |
| sliderSnakingOut        | Boolean | True  |
| useBeatmapColors        | Boolean | True  |
| useHitCircleColor       | Boolean | True  |
| useSkinColors           | Boolean | False |
| useSkinCursor           | Boolean | True  |
| useSkinHitsounds        | Boolean | True  |
| username                | String  |                    |

#### **Example**

```py
OrdrClient.create_render(replayURL: "https://url.tld/file.osr", username: "ordr.py", ...)
```

### `get_render(params)` ⇒ \[[GetRenderRespond](#getrenderrespond)]

Get a list of renders.

| Param                       | Type                 | Default            | Description                                                           |
| --------------------------- | -------------------- | ------------------ | --------------------------------------------------------------------- |
| ordrUsername   | String  |                    | renders that matches the most this o!rdr username                     |
| page           | Number  | 1     | page number                                                           |
| pageSize       | Number  | 50    | number of renders that the API will return                            |
| renderID       | Number  |                    | render with this specific renderID                                    |
| replayUsername | String  |                    | renders that matches the most this replay username                    |
| nobots         | Boolean | False | hide bots from the returned render query                              |
| reduceInfo           | Boolean | False | lite mode gives less info                                             |
| link           | String  |                    | path of a shortlink (example pov8n for <https://link.issou.best/pov8n>) |
| beatmapsetid   | Number  |                    | renders with this specific beatmapset ID                              |

### `get_skin(params)` ⇒ \[[GetSkinRespond](#getskinrespond)]

Get a list of skins.

| Param                 | Type                | Default          | Description                                |
| --------------------- | ------------------- | ---------------- | ------------------------------------------ |
| search   | String |                  | skins that matches the most this string    |
| page     | Number | 1   | page number                                |
| pageSize | Number | 100 | number of renders that the API will return |

### `get_custom_skin(id)` ⇒ \[[CustomSkinRespond](#customskinrespond)]

Get info of a custom skin.

| Param | Type                | Default | Description    |
| ----- | ------------------- | ------- | -------------- |
| id    | number |         | custom skin ID |

### `get_online_count()` ⇒ int

Get the count of online servers.

### `get_servers()` ⇒ \[[GetServersRespond](#getserversrespond)]

Get a list of servers.

---

## AsyncOrdrClient

## `class ordr.AsyncOrdrClient(apikey: str = None, developer: ordr.DeveloperMode = None)`

PARAMETERS:

- apikey (Optional\[[str](https://docs.python.org/3/library/stdtypes.html#str)]) - an key for o!rdr API
- developer (Optional\[[DeveloperMode]()]) - options for developer mode

### `await connect()` ⇒ `None`

Starts the client session.

### `await disconnect()` ⇒ `None`

Ends the client session.

### `await create_render(params)` ⇒ \[[NewRenderRespond](#newrenderrespond)]

Create a new render on o!rdr

| Param                              | Type                 | Default            |
| ---------------------------------- | -------------------- | ------------------ |
| BGParallax              | Boolean | False |
| breakBGDim              | Number  | 30    |
| cursorRainbow           | Boolean | False |
| cursorRipples           | Boolean | False |
| cursorScaleToCS         | Boolean | False |
| cursorSize              | Number  | 1     |
| cursorTrail             | Boolean | True  |
| cursorTrailGlow         | Boolean | False |
| drawComboNumbers        | Boolean | True  |
| drawFollowPoints        | Boolean | True  |
| globalVolume            | Number  | 50    |
| hitsoundVolume          | Number  | 50    |
| inGameBGDim             | Number  | 75    |
| introBGDim              | Number  | 0     |
| loadStoryboard          | Boolean | True  |
| loadVideo               | Boolean | True  |
| musicVolume             | Number  | 50    |
| objectsFlashToTheBeat   | Boolean | False |
| objectsRainbow          | Boolean | False |
| playNightcoreSamples    | Boolean | True  |
| replayURL               | String  |                    |
| resolution              | [Object]()  |                    |
| scaleToTheBeat          | Boolean | False |
| seizureWarning          | Boolean | False |
| showAimErrorMeter       | Boolean | False |
| showAvatarsOnScoreboard | Boolean | False |
| showBorders             | Boolean | False |
| showComboCounter        | Boolean | True  |
| showDanserLogo          | Boolean | True  |
| showHPBar               | Boolean | True  |
| showHitCounter          | Boolean | False |
| showHitErrorMeter       | Boolean | True  |
| showKeyOverlay          | Boolean | True  |
| showMods                | Boolean | True  |
| showPPCounter           | Boolean | True  |
| showResultScreen        | Boolean | True  |
| showScore               | Boolean | True  |
| showScoreboard          | Boolean | False |
| showUnstableRate        | Boolean | True  |
| skin                    | [Object](#skin)  |                    |
| skip                    | Boolean | True  |
| sliderMerge             | Boolean | False |
| sliderSnakingIn         | Boolean | True  |
| sliderSnakingOut        | Boolean | True  |
| useBeatmapColors        | Boolean | True  |
| useHitCircleColor       | Boolean | True  |
| useSkinColors           | Boolean | False |
| useSkinCursor           | Boolean | True  |
| useSkinHitsounds        | Boolean | True  |
| username                | String  |                    |

**Example**

```py
OrdrClient.create_render(replayURL: "https://url.tld/file.osr", username: "ordr.py", ...)
```

### `await get_render(params)` ⇒ \[[GetRenderRespond](#getrenderrespond)]

Get a list of renders.

| Param                       | Type                 | Default            | Description                                                           |
| --------------------------- | -------------------- | ------------------ | --------------------------------------------------------------------- |
| ordrUsername   | String  |                    | renders that matches the most this o!rdr username                     |
| page           | Number  | 1     | page number                                                           |
| pageSize       | Number  | 50    | number of renders that the API will return                            |
| renderID       | Number  |                    | render with this specific renderID                                    |
| replayUsername | String  |                    | renders that matches the most this replay username                    |
| nobots         | Boolean | False | hide bots from the returned render query                              |
| reduceInfo           | Boolean | False | lite mode gives less info                                             |
| link           | String  |                    | path of a shortlink (example pov8n for <https://link.issou.best/pov8n>) |
| beatmapsetid   | Number  |                    | renders with this specific beatmapset ID                              |

### `await get_skin(params)` ⇒ \[[GetSkinRespond](#getskinrespond)]

Get a list of skins.

| Param                 | Type                | Default          | Description                                |
| --------------------- | ------------------- | ---------------- | ------------------------------------------ |
| search   | String |                  | skins that matches the most this string    |
| page     | Number | 1   | page number                                |
| pageSize | Number | 100 | number of renders that the API will return |

### `await get_custom_skin(id)` ⇒ \[[CustomSkinRespond](#customskinrespond)]

Get info of a custom skin.

| Param | Type                | Default | Description    |
| ----- | ------------------- | ------- | -------------- |
| id    | number |         | custom skin ID |

### `await get_online_count()` ⇒ int

Get the count of online servers.

### `await get_servers()` ⇒ \[[GetServersRespond](#getserversrespond)]

Get a list of servers.

---

# Respond Object

## NewRenderRespond

## `class ordr.NewRenderRespond(status, data)`

PARAMETERS:

- status \[[int](https://docs.python.org/3/library/functions.html#int)] - status code of the request.
- data \[[bytes](https://docs.python.org/3/library/functions.html#func-bytes)] - raw content of the request.

ATTRIBUTES:

- request \[[Request](#request)]
- _json - decoded content of the request.
- message
- renderID
- error
- reason

---

## GetRenderRespond

## `class ordr.GetRenderRespond(status, data, reduce:bool = False)`

PARAMETERS:

- status \[[int](https://docs.python.org/3/library/functions.html#int)] - status code of the request.
- data \[[bytes](https://docs.python.org/3/library/functions.html#func-bytes)] - raw content of the request.
- reduce \[[bool](https://docs.python.org/3/library/functions.html#bool)] - reduce the

ATTRIBUTES:

- request \[[Request](#request)]
- _json - decoded content of the request.
- message
- maxRenders
- renders [List\[[Render](#render)]]

---

## GetSkinRespond

## `class ordr.GetSkinRespond(status, data)`

PARAMETERS:

- status \[[int](https://docs.python.org/3/library/functions.html#int)] - status code of the request.
- data \[[bytes](https://docs.python.org/3/library/functions.html#func-bytes)] - raw content of the request.

ATTRIBUTES:

- request \[[Request](#request)]
- _json - decoded content of the request.
- message
- maxSkins
- skins [List\[[Skin](#skin)]]

---

## CustomSkinRespond

## `class ordr.CustomSkinRespond(status, data)`

PARAMETERS:

- status \[[int](https://docs.python.org/3/library/functions.html#int)] - status code of the request.
- data \[[bytes](https://docs.python.org/3/library/functions.html#func-bytes)] - raw content of the request.

ATTRIBUTES:

- request \[[Request](#request)]
- _json - decoded content of the request.
- found
- removed
- message
- skinName
- skinAuthor
- downloadLink

---

## GetServersRespond

## `class ordr.GetServersRespond(status, data)`

PARAMETERS:

- status \[[int](https://docs.python.org/3/library/functions.html#int)] - status code of the request.
- data \[[bytes](https://docs.python.org/3/library/functions.html#func-bytes)] - raw content of the request.

ATTRIBUTES:

- request \[[Request](#request)]
- _json - decoded content of the request.
- message
- servers [List\[[Server](#server)]]

---

# Model Object

## Skin

## `class Skin(skinID:int, isCustomSkin:bool)`

PARAMETERS:

- skinID
- isCustomSkin

ATTRIBUTES:

- _json
- skin
- presentationName
- url
- highResPreview
- lowResPreview
- gridPreview
- id
- hasCursorMiddle
- author
- modified
- version
- alphabeticalId
- timesUsed

### `get_skin(json)`

Parse the json from the API to a Skin object.

---

## Server

## `class Server(json)`

Parse the json from the API to a Server object.

PARAMETERS:

- json

ATTRIBUTES:

- _json
- enabled
- lastSeen
- name
- priority
- oldScore
- avgFPS
- power
- status
- totalRendered
- renderingType
- cpu
- gpu
- motionBlurCapable
- usingOsuApi
- uhdCapable
- avgRenderTime
- avgUploadTime
- totalAvgTime
- totalUploadedVideosSize

---

## Render

## `class.Render(json, reduce)`

PARAMETERS:

- json

ATTRIBUTES:

- _json
- date
- readableDate
- renderID
- username
- progress
- errorCode
- removed
- renderer
- description
- title
- replayFilePath
- replayMd5
- videoUrl
- mapLink
- mapTitle
- mapLength
- drainTime
- replayDifficulty
- replayUsername
- replayMods
- mapID
- needToRedownload
- resolution
- globalVolume
- musicVolume
- hitsoundVolume
- useSkinHitsounds
- playNightcoreSamples
- showHitErrorMeter
- showUnstableRate
- showScore
- showHPBar
- showComboCounter
- showPPCounter
- showKeyOverlay
- showScoreboard
- showAvatarsOnScoreboard
- showBorders
- showMods
- showResultScreen
- showHitCounter
- showAimErrorMeter
- customSkin
- skin
- hasCursorMiddle
- useSkinCursor
- useSkinColors
- useBeatmapColors
- cursorScaleToCS
- cursorRainbow
- cursorTrailGlow
- cursorSize
- cursorTrail
- drawFollowPoints
- drawComboNumbers
- scaleToTheBeat
- sliderMerge
- objectsRainbow
- objectsFlashToTheBeat
- useHitCircleColor
- seizureWarning
- loadStoryboard
- loadVideo
- introBGDim
- inGameBGDim
- breakBGDim
- BGParallax
- showDanserLogo
- motionBlur960fps
- motionBlurForce
- skip
- cursorRipples
- sliderSnakingIn
- sliderSnakingOut
- isVerified
- isBot
- renderStartTime
- renderEndTime
- renderTotalTime
- uploadEndTime
- uploadTotalTime

## Request

## `class.Render(json)`

PARAMETERS:

- status
- data

ATTRIBUTES:

- statusCode
- rawcontent
