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


from .FastTelethon import download_file, upload_file
from .funcn import *
from .config import *


async def stats(e):
    try:
        wah = e.pattern_match.group(1).decode("UTF-8")
        wh = decode(wah)
        out, dl, id = wh.split(";")
        ot = hbs(int(Path(out).stat().st_size))
        ov = hbs(int(Path(dl).stat().st_size))
        ans = f"Downloaded:\n{ov}\n\nCompressing:\n{ot}"
        await e.answer(ans, cache_time=0, alert=True)
    except Exception as er:
        LOGS.info(er)
        await e.answer(
            "Someting Went Wrong 🤔\nSend Media Again.", cache_time=0, alert=True
        )


async def encod(event):
    try:
        if not event.is_private:
            return
        event.sender
        if str(event.sender_id) not in OWNER:
            return
        if not event.media:
            return
        if hasattr(event.media, "document"):
            if not event.media.document.mime_type.startswith(
                ("video", "application/octet-stream")
            ):
                return
        else:
            return
        try:
            oc = event.fwd_from.from_id.user_id
            occ = (await event.client.get_me()).id
            if oc == occ:
                return await event.reply("This Video File is already Compressed.")
        except BaseException:
            pass
        if WORKING or QUEUE:
            xxx = await event.reply("`Adding To Queue...`")
            # id = pack_bot_file_id(event.media)
            doc = event.media.document
            if doc.id in list(QUEUE.keys()):
                return await xxx.edit("THIS FILE ALREADY IN QUEUE")
            name = event.file.name
            if not name:
                name = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
            QUEUE.update({doc.id: [name, doc]})
            return await xxx.edit(
                "`Added This File in Queue`"
            )
        WORKING.append(1)
        xxx = await event.reply("**📥 Downloading...**")
        s = dt.now()
        ttt = time.time()
        dir = f"downloads/"
        try:
            if hasattr(event.media, "document"):
                file = event.media.document
                filename = event.file.name
                if not filename:
                    filename = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                dl = dir + filename
                with open(dl, "wb") as f:
                    ok = await download_file(
                        client=event.client,
                        location=file,
                        out=f,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(
                                d,
                                t,
                                xxx,
                                ttt,
                                "**📥 Downloading...**",
                            )
                        ),
                    )
            else:
                dl = await event.client.download_media(
                    event.media,
                    dir,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, xxx, ttt, "**📥 Downloading...**")
                    ),
                )
        except Exception as er:
            WORKING.clear()
            LOGS.info(er)
            return os.remove(dl)
        es = dt.now()
        kk = dl.split("/")[-1]
        aa = kk.split(".")[-1]
        rr = f"encode"
        bb = kk.replace(f".{aa}", " CBZ.mkv")
        out = f"{rr}/{bb}"
        thum = "thumb.jpg"
        dtime = ts(int((es - s).seconds) * 1000)
        e = xxx
        hehe = f"{out};{dl};0"
        wah = code(hehe)
        nn = await e.edit(
            "**🗜 Compressing...**",
            buttons=[
                [Button.inline("STATS", data=f"stats{wah}")],
                [Button.inline("CANCEL", data=f"skip{wah}")],
            ],
        )
        ffmpegcode.append("ffmpeg -i '{dl}' -preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By Zylern' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2  -ab 32k  -vbr 2 -level 3.1 '{out}' -y")
        #cmd = {ffmpegcode[0]}.format(dl, out)
        cmd = ffmpegcode[0]
      #  cmd = f"""ffmpeg -hide_banner -loglevel quiet -i '{dl}' {ffmpegcode[0]} '{out}' -y"""
        process = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        er = stderr.decode()
        try:
            if er:
                await e.edit(str(er) + "\n\n**ERROR** Contact @danish_00")
                WORKING.clear()
                os.remove(dl)
                return os.remove(out)
        except BaseException:
            pass
        ees = dt.now()
        ttt = time.time()
        await nn.delete()
        nnn = await e.client.send_message(e.chat_id, "**📤 Uploading...**")
        with open(out, "rb") as f:
            ok = await upload_file(
                client=e.client,
                file=f,
                name=out,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, nnn, ttt, "**📤 Uploading...**")
                ),
            )
        ds = await e.client.send_file(
            e.chat_id, file=ok, force_document=True, thumb=thum
        )
        await nnn.delete()
        org = int(Path(dl).stat().st_size)
        com = int(Path(out).stat().st_size)
        pe = 100 - ((com / org) * 100)
        per = str(f"{pe:.2f}") + "%"
        eees = dt.now()
        x = dtime
        xx = ts(int((ees - es).seconds) * 1000)
        xxx = ts(int((eees - ees).seconds) * 1000)
        a1 = await info(dl, e)
        a2 = await info(out, e)
        dk = await ds.reply(
            f"**➩ Original File Size :** {hbs(org)}\n**➩ Encoded File Size :** {hbs(com)}\n**➩ Encoded File Percentage :** {per}\n\n**➩ Get Mediainfo here :** [Before]({a1})/[After]({a2})\n\n__Downloaded in {x}\nEncoded in {xx}\nUploaded in {xxx}__",
            link_preview=False,
        )
        os.remove(dl)
        os.remove(out)
        WORKING.clear()
    except BaseException as er:
        LOGS.info(er)
        WORKING.clear()
