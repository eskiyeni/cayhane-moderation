import discord
from discord.ext import commands

class slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(
        name="ban",
        description="Kullanıcıyı sunucudan yasaklar."
    )
    @discord.app_commands.check(lambda i: i.user.guild_permissions.ban_members) 
    async def ban(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        await interaction.response.defer()

        try:
            await user.ban(reason=reason)
            await interaction.followup.send(
                embed=discord.Embed(
                    title="KULLANICI YASAKLANDI!",
                    description=f"{user.mention}, {reason} sebebi ile yasaklandı!",
                    color=0xFF0000
                ).set_footer(text="Kurallara dikkat ediniz!")
            )
        except discord.Forbidden:
            await interaction.followup.send(
                embed=discord.Embed(
                    title="HATA!",
                    description=f"{user.mention} kullanıcısını yasaklamak için yetkim yok!",
                    color=0xFF0000
                )
            )
        except discord.HTTPException:
            await interaction.followup.send(
                embed=discord.Embed(
                    title="HATA!",
                    description="Bir hata oluştu, işlem gerçekleştirilemedi!",
                    color=0xFF0000
                )
            )

    @discord.app_commands.command(
        name="kick",
        description="Kullanıcıyı sunucudan atar."
    )
    @discord.app_commands.check(lambda i: i.user.guild_permissions.kick_members) 
    async def kick(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        await interaction.response.defer()

        try:
            await user.kick(reason=reason)
            await interaction.followup.send(
                embed=discord.Embed(
                    title="KULLANICI ATILDI!",
                    description=f"{user.mention}, {reason} sebebi ile atıldı!",
                    color=0xFF0000
                ).set_footer(text="Kurallara dikkat ediniz!")
            )
        except discord.Forbidden:
            await interaction.followup.send(
                embed=discord.Embed(
                    title="HATA!",
                    description=f"{user.mention} kullanıcısını atmak için yetkim yok!",
                    color=0xFF0000
                )
            )
        except discord.HTTPException:
            await interaction.followup.send(
                embed=discord.Embed(
                    title="HATA!",
                    description="Bir hata oluştu, işlem gerçekleştirilemedi!",
                    color=0xFF0000
                )
            )

    @discord.app_commands.command(
        name="info",
        description="Bot hakkında bilgi verir."
    )
    async def info(self, interaction: discord.Interaction):
        await interaction.response.defer()

        await interaction.followup.send(
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

    @discord.app_commands.command(
        name="join_channel",
        description="Botu bir sesli kanala bağlar."
    )
    @discord.app_commands.check(lambda i: i.user.guild_permissions.manage_channels)  

    async def join_channel(self, interaction: discord.Interaction, channel: discord.VoiceChannel = None):
        await interaction.response.defer()
        channel = channel or interaction.user.voice.channel

        try:
            await channel.connect()
            await interaction.followup.send(
                embed=discord.Embed(
                    title="KANALA BAĞLANILDI!",
                    description=f"{channel.name} kanalına başarıyla bağlanıldı!",
                    color=0x00FF00
                )
            )
        except discord.Forbidden:
            await interaction.followup.send(
                embed=discord.Embed(
                    title="HATA!",
                    description="Kanala bağlanmak için yetkim yok!",
                    color=0xFF0000
                )
            )

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(slash_commands(bot))