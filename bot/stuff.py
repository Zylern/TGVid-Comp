#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🔥Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)



async def start(event):
    await event.reply(
        f"**Send me the video which you want to compress.**",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
        ],
    )


async def help(event):
    await event.reply(
        """**Donot use cancel button it have some bug.**\n\nYou can change your ffmpeg code using\n\n`/eval ffmpegcode.insert(0, "-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By Zylern' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2  -ab 32k  -vbr 2 -level 3.1")`\n\n**Don't use " inside your ffmpeg code it will give you error always use ' instead.**"""
    )


async def ihelp(event):
    await event.edit(
        """**Donot use cancel button it have some bug.**\n\nYou can change your ffmpeg code using\n\n`/eval ffmpegcode.insert(0, "-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By Zylern' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2  -ab 32k  -vbr 2 -level 3.1")`\n\n**Don't use " inside your ffmpeg code it will give you error always use ' instead.**"""
        buttons=[Button.inline("BACK", data="beck")],
    )

async def beck(event):
    await event.reply(
        f"**Send me the video which you want to compress.**",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
        ],
    )
