import discord
from discord.ext import commands

class prefix_commands(commands.Cog):
    def __init__(self, bot) ->None:
        self.bot = bot

    @commands.command(aliases=["yasakla", "uçur"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx : commands.Context, user : discord.Member, *reasion):
        reasion = " ".join(reasion)

        try:
            await user.ban(reason=reasion)
            await ctx.send(
                embed=discord.Embed(
                    title="KULLANICI YASAKLANDI!",
                    description=f"{user.mention}, {reasion} sebebi ile yasaklandı!",
                    color=0xFF0000
                ).set_footer(text="Kurallara dikkat ediniz!")
            )
        except discord.Forbidden:
            await ctx.send(
                embed=discord.Embed(
                    title="HATA!",
                    description=f"{user.mention} kullanıcısını banlamak için yetkim yok!",
                    color=0xFF0000
                )
            )

    @commands.command(aliases=["at", "fırlat"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx : commands.Context, user : discord.Member, *reason):
        reason = " ".join(reason)

        try:
            await user.kick(reason=reason)
            await ctx.send(
                embed=discord.Embed(
                    title="KULLANICI ATILDI!",
                    description=f"{user.mention}, {reason} sebebi ile atıldı!",
                    color=0xFF0000
                ).set_footer(text="Kurallara dikkat ediniz!")
            )
        except discord.Forbidden:
            await ctx.send(
                embed=discord.Embed(
                    title="HATA!",
                    description=f"{user.mention} kullanıcısını atmak için yetkim yok!",
                    color=0xFF0000
                )
            )

    @commands.command()
    async def info(self, ctx : commands.Context):
        await ctx.send(
            embed=discord.Embed(
                title="BOT HAKKINDA BİLGİ",
                description=f"""
Prefix: {self.bot.config["prefix"]}
Uptime: {self.bot.return_uptime()}
Kaynak kodları: {self.bot.config["github_link"]}
"""             ,
                color=0xf6f478
            ).set_footer(text=self.bot.user.name)
        )

    @commands.command()
    async def join_channel(self, ctx : commands.Context, channel : discord.VoiceChannel = None):
        channel = channel or ctx.author.voice.channel

        try:
            await channel.connect()
            await ctx.send(
                embed=discord.Embed(
                    title="KANALA BAĞLANILDI!",
                    description=f"{channel.name} kanalına bağlanıldı!",
                    color=0x00FF00
                )
            )
        except discord.Forbidden:
            await ctx.send(
                embed=discord.Embed(
                    title="HATA!",
                    description="Kanala bağlanmak için yetkim yok!",
                    color=0xFF0000
                )
            )

async def setup(bot : commands.Bot) ->None:
    await bot.add_cog(prefix_commands(bot))