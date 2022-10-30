import discord

help = discord.Embed(title='도움말', description='도움이 필요할때 ```^도움말 or ^help``` 라고 해줘!!', color = 0x39c5bb)
help.add_field(name='```^세카이검색```', value='세카이에 관한 정보를 볼수 있습니다', inline=True)
help.set_footer(text='Made By Luen')
help.set_thumbnail(url="https://media.discordapp.net/attachments/828467375337766962/828581378827485275/1.jpg?width=465&height=491")

sk_help = discord.Embed(title='세카이검색', description='세카이에 관한 정보 명령어 모음', color = 0x39c5bb)
sk_help.add_field(name='음악', value='세카이에 수록된 곡 정보를 볼 수 있습니다\nex)```^세카이검색 음악```', inline=False)
sk_help.add_field(name='유닛', value='세카이에 유닛 정보를 볼 수 있습니다\nex)```^세카이검색 유닛```', inline=False)
sk_help.set_footer(text='Project SEKAI COLOURFUL STAGE! feat.HATSUNE MIKU')
sk_help.set_thumbnail(url="https://cdn.discordapp.com/attachments/828959305478832198/828990365247209482/TMa_FBrjseeE0ZBQa0fve-dyW1j0YZHnNUzJeRR692EyKcNh6SQB04_ytzYE---4xgw512.png")

un_help = discord.Embed(title='프로젝트 세카이 유닛', description='유닛 목록',color=0x39c5bb)
un_help.add_field(name='VIRTURE SINGER', value='ㅤ', inline=False)
un_help.add_field(name='MORE MORE JUMP!', value='ㅤ', inline=False)
un_help.add_field(name='Leo/need', value='ㅤ', inline=False)
un_help.add_field(name='Vivid BAD SQUAD', value='ㅤ', inline=False)
un_help.add_field(name='원더랜즈×쇼타임', value='ㅤ', inline=False)
un_help.add_field(name='25시, 나이트코드에서.', value='ㅤ', inline=False)
un_help.add_field(name='명령어', value='ex)```^세카이검색 유닛 모모점```', inline=False)
un_help.set_image(url="https://cdn.discordapp.com/attachments/857996994676916234/858001981301850122/65319eabc477e721e6d5dde19508daac108bf74817f79b9061fe00e593d772fcbe7ad1ff333ccf07c36a4f695380d3feee0d.png")

ms_help = discord.Embed(title='프로젝트 세카이 음악', description='ㅤ', color=0x39c5bb)
ms_help.add_field(name='검색하시면 곡의 정보가 나옵니다', value='일본어 검색은 안되요ㅠㅠ', inline=False)
ms_help.add_field(name='명령어', value='ex)```^세카이검색 음악 멜트```', inline=False)
ms_help.set_image(url="https://cdn.discordapp.com/attachments/857996994676916234/858001981301850122/65319eabc477e721e6d5dde19508daac108bf74817f79b9061fe00e593d772fcbe7ad1ff333ccf07c36a4f695380d3feee0d.png")