# will be using nextcord wrapper 
from nextcord.ext import commands 
import nextcord 
from nextcord import Intents
# this will be the library used for the voice emitted from the bot
from gtts import gTTS

bot_token = 'Enter your bot token here' 

# this is to give the bot premissions needed to  
intents = Intents.default()
intents.message_content = True 
intents.members = True 

# you can change what you want the prefix before the command becomes such as '! . - ~ etc'
bot = commands.Bot(command_prefix='insert-your-prefix-here', intents=intents) 

# this will print a message when the bot comes online 
@bot.event 
async def on_ready(): 
    print(f'Logged in as {bot.user.name}')

# join command 
@bot.command()
async def join(ctx): 
    channel = ctx.author.voice.channel
    await channel.connect() 
    # this will print a message when the bot joins a voice channel 
    print('Bot has joined a voice channel') 

@bot.command()
async def tts(ctx, *args): 
    text = " ".join(args)
    user = ctx.message.author
    
    if user.voice != None: 
        try: 
            vc = await user_voice.channel.connect() 
        except: 
            vc = ctx.voice_client     
    
        # this will convert the text to a sound file
        sound = gTTS(text=text, lang='en', slow=False) 
        # this is the sound file 
        sound.save('file.mp3') 
    
        # if the bot is currently speaking a message, immediately stop
        if vc.is_playing():
            vc.stop()
    
        # ***IMPORTANT***
        # you'll need to download ffmpeg from their website and drag the bin folder into the directory of this file
        ffmpeg_path = os.path.join(os.path.dirname(__file__), 'bin', 'ffmpeg.exe')    # ensure that the bin folder includes ffmpeg.exe
        source = await nextcord.FFmpegOpusAudio.from_probe('file.mp3', executable=ffmpeg_path, method='fallback')
    
        vc.play(source)

        # can keep or remove this line (essentially deletes the message after being played) 
        await ctx.message.delete()

        print('Bot has finished speaking')

    else: 
        await ctx.send('You need to be in a channel to run this command') 

# force the bot to leave the current voice channel 
@bot.command()
# invoked by 'your-prefix' + 'leave'
async def leave(ctx): 
    vc = ctx.voice_client
    if vc.isconnected(): 
        await vc.disconnect() 

# this calls the bot token and turns your bot online 
bot.run(TOKEN)

