# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *

async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"Ping = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"**Send me the video which you want to compress.**",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
        ],
    )

async def zylern(event):
    await event.reply(
        f"""
**Available Commands 🤖**

/start - __Check Bot is Working Or Not__
/setcode - __Set Custom FFMPEG Code__
/help - __Get Detailed Help__
/ping - __Check Ping__
/sysinfo - __Get System Info__
/leech - __Leech Links And Compress Video__
/renew - __Clear Cached Downloads__
/clear - __Clear Queued Files__
/speed - __Do A SpeedTest__
/eval - __Execute An Argument__
/bash - __Run Bash Commands__
/cmds - __List Available Commands__
"""
    )


async def help(event):
    await event.reply(
        f"""**To check current ffmpeg command you can use.**\n\n`/eval print(ffmpegcode[0])`\n\n**You can change your ffmpeg code by executing following commands.**\n\n**➩** `/eval ffmpegcode.clear()`\n\n**➩** `/setcode -preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By Zylern' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2  -ab 32k  -vbr 2 -level 3.1`\n\n**Do /cmds For More**"""
    )


async def ihelp(event):
    await event.edit(
        """**To check current ffmpeg command you can use.**\n\n`/eval print(ffmpegcode[0])`\n\n**You can change your ffmpeg code by executing following commands.**\n\n**➩** `/eval ffmpegcode.clear()`\n\n**➩** `/setcode -preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By Zylern' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2  -ab 32k  -vbr 2 -level 3.1`\n\n**Do /cmds For More**"""
    )
