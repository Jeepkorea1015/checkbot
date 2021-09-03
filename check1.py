import discord

client = discord.Client()

@client.event
async def on_ready():
    print("떼빙 참가여부 조사 테스트 봇")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("참가여부 조사중"))

@client.event
async def on_message(message):
    if message.content.startswith("참여"):
        await message.channel.send ("{}, 금일 떼빙에 참여로 신청이 완료 되었습니다.".format(message.author.mention))
    if message.content.startswith("중참"):
        await message.channel.send ("{}, 금일 떼빙에 중간참여로 신청이 완료 되었습니다. 사유도 같이 알려주세요.".format(message.author.mention))        
    if message.content.startswith("불참"):
        await message.channel.send ("{}, 금일 떼빙에 불참으로 신청이 완료 되었습니다. 사유도 같이 알려주세요.".format(message.author.mention))
    if message.content.startswith("사유"):
        await message.channel.send ("{}, 사유가 확인 되었습니다.".format(message.author.mention))   
    if message.content.startswith("봇테스트"):
        await message.channel.send ("{}, 봇이 정상 작동중 입니다.".format(message.author.mention))         


client.run('ODgzMTg2ODc3Nzk1MDQxMzAx.YTGR4A.uyQYUaWkIk5oDzefMNmGwYnzrjA')