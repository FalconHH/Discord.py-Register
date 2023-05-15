import discord
from discord.ext import commands
from discord.utils import get
import datetime

class bcolors:
      OKGREEN = '\033[92m'
      ENDC = '\033[0m'
  
class Register(commands.Cog):


    def __init(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{bcolors.OKGREEN}Register is active{bcolors.ENDC}") #This line will print on the console for checking whether this cog is active or not.

    @commands.command(pass_context=True)
    @commands.has_role(MOD_ID) #You have to add a Moderator role ID to this section.
    async def register(self, ctx, member: discord.Member):
        MemberRole = discord.utils.get(member.guild.roles, id=int(ROLE_ID)) #You have to add a Member role ID to this section.
        if MemberRole in member.roles: #This command will check if the tagged user has a member role or not.
             emd = discord.Embed(title=f"This user already has this role", color=0xFFD700)
             await ctx.send(embed=emd, delete_after=5.0)
        else:
            UserAvatar = member.avatar_url
            MessageAuthor = ctx.author.avatar_url
            RegEmbed=discord.Embed(title="Register Information", description = f"** >  • Registered Member : {member.mention} \n \n >  •  Moderator : {ctx.author.mention} \n \n >  • Given Role : {MemberRole.mention} \n \n >   • Welcome to our server**" , color=0xFFD700)
            RegEmbed.set_thumbnail(url=MessageAuthor)
            RegEmbed.set_author(name="| Register Done", icon_url=UserAvatar)
            RegEmbed.set_footer(text="FHH",
            icon_url="https://cdn.discordapp.com/attachments/1062694592132157471/1062694947662340247/static.png")
            RegEmbed.set_image(url="https://cdn.discordapp.com/attachments/1062694592132157471/1062694643256533013/standard.gif")
            RegEmbed.timestamp = datetime.datetime.utcnow() #This line will add the time stamp in embed.

            await ctx.send(embed=RegEmbed, delete_after=30.0)
            member == ctx.message.author
            await member.add_roles(MemberRole)

    @register.error
    async def register_error(self, ctx, error):
            if isinstance(error, commands.MissingRole):
                em = discord.Embed(title=f"Hey what are you doing ?",description=f"{ctx.author.mention} You don't have permission to use this command.", color=0xFFD700)
                await ctx.send(embed=em, delete_after=5.0)

def setup(client):
    client.add_cog(Register(client))
