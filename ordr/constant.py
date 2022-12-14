from enum import Enum

BASEURL = "https://apis.issou.best/ordr"
WSURL = "https://ordr-ws.issou.best"

WSERRCODE = {
    1: "Unknown error triggered by an emergency stop.",
    2: "Replay download error (bad upload from the sender)",
    3: "Replay download error (bad download from the server), can happen because of invalid characters",
    4: "All beatmap mirrors are unavailable or the beatmap isn't yet available on them, try again later.",
    15: "Beatmap not found on the mirrors. Retry later.",
    18: "Unknown error from the renderer. Try to send the replay again.",
    19: "The renderer cannot download the map. This may be a server-side problem from issou.best.",
    20: "The beatmap version on the mirror is not the same as the replay. Don't retry sending it as we have already retried for you.",
    21: "This replay is corrupted. Try re-exporting it.",
    22: "There is a problem with the generated video. Try to send the replay again.",
    27: "Something went wrong, the generated video is not your replay. Try to send the replay again.",
    28: "The renderer cannot download the replay. Try to send the replay again.",
}
APIERRCODE = {
    2: "Cannot save replay.",
    5: "Cannot parse replay.",
    6: "This replay is not an osu!standard replay, o!rdr does not support mania/ctb/taiko.",
    7: "This replay has no input data. Try re-exporting it from osu!.",
    8: "This beatmap does not exist on osu!. Custom difficulties or non-submitted maps are not supported.",
    9: "The audio for this map is unavailable, it maybe has been copyright claimed.",
    10: "Cannot connect to osu! api. Please retry later.",
    11: "Auto mod is not supported.",
    12: "This replay has an invalid username.",
    13: "Beatmaps longer than 15 minutes are not allowed.",
    14: "This player is banned from o!rdr.",
    16: "This IP is banned from o!rdr.",
    17: "This username is banned from o!rdr.",
    23: "Failed to prepare the render. Try to send the replay again.",
    24: "This map has no name.",
    25: "This replay is missing input data.",
    26: "This replay has incompatible mods.",
    29: "This replay is already rendering or in queue. Wait until it finishes.",
    30: "Beatmaps with a star rating greater than 20 are not allowed.",
    31: "This mapper is blacklisted.",
    32: "This beatmapset is blacklisted.",
    33: "This replay has already errored less than an hour ago, try again later.",
}

class DeveloperMode(Enum):
    SUCCESS = 0
    FAIL = 1
    WSFAIL = 2

class Resolution(Enum):
    X480 = "720x480"
    X540 = "960x540"
    X720 = "1280x720"