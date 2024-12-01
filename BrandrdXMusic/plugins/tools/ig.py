import requests
from pyrogram import filters
from kaalXMusic import app

@app.on_message(filters.command(["ig", "instagram", "down"]))
async def download_instagram_video(client, message):
    if len(message.command) < 2:
        await message.reply_text(
            "Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ URL ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ"
        )
        return
    processing_message = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    url = message.text.split()[1]
    api_url = f"https://tele-social.vercel.app/down?url={url}"

    try:
        # Request to the API
        response = requests.get(api_url)
        data = response.json()

        if data["status"] and "video" in data["data"]:
            video_url = data["data"]["video"]
            
            # Download the video
            video_content = requests.get(video_url).content

            # Save the video temporarily
            temp_file_path = "/tmp/instagram_reel.mp4"
            with open(temp_file_path, "wb") as video_file:
                video_file.write(video_content)

            # Send the video to the user
            await processing_message.delete()
            await client.send_video(
                message.chat.id,
                video=temp_file_path,
                caption="Hᴇʀᴇ ɪs ᴛʜᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ᴠɪᴅᴇᴏ!"
            )
        else:
            await processing_message.edit("Fᴀɪʟᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ʀᴇᴇʟ.")
    except Exception as e:
        await processing_message.edit(f"An ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ:\n`{e}`")

__MODULE__ = "Iɴsᴛᴀɢʀᴀᴍ"
__HELP__ = """/down [ᴜʀʟ] - Tᴏ ᴅᴏᴡɴʟᴏᴀᴅ ʙʏ ʙᴏᴛ
/ig [ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟ ᴜʀʟ] - Tᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ʀᴇᴇʟ ʙʏ ʙᴏᴛ
/instagram [ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟ ᴜʀʟ] - Tᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ʀᴇᴇʟ ʙʏ ʙᴏᴛ
"""
