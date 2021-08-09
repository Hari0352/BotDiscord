import discord
from discord.ext import commands

class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Danh sách lệnh:
>help - Hiển thị toàn bộ command
>clear < Số lượng > - Xóa tin nhắn theo số lượng
>avatar hiển thị avatar người được tag
Nhạc nè:
>n <keywords> - Tìm nhạc
>ds - Danh sách nhạc
>next - nẽt bài
```
"""
        self.text_channel_list = []

      

 

    @commands.command(name="help", help="Hiển thị toàn bộ trợ giúp.")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)

    @commands.command(name="clear", help="Xóa tin nhắn theo số lượng")
    async def clear(self, ctx, arg):
        #extract the amount to clear
        amount = 5
        try:
            amount = int(arg)
        except Exception: pass

        await ctx.channel.purge(limit=amount)

    @commands.command(name='check', help='Check trạng thái bot.')
    async def check(self,ctx):
      await ctx.send('Còn sống nhăn răng nhé 🤩')
    @commands.command(nam='avatar',help='Xem avatar người gọi.')
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
      userAvatarUrl = avamember.avatar_url
      await ctx.send(userAvatarUrl)