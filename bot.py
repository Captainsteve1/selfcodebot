# Made with Love by @conan7612

import time
import os
from pytz import timezone 
from datetime import datetime
import shutil
import subprocess
import base64 


from urllib.request import urlopen, Request
import json

from datetime import timedelta

GROUP_TAG = "TONY"

def convert_base64(text , type_=None):
    if type_ is None:
        message_bytes = text.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
    elif type_ == "encode":
        message_bytes = text.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
    elif type_ == "decode":
        message_bytes = text.encode('ascii')
        base64_bytes = base64.b64decode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

    return base64_message


def sanitize_title(name):
  name = name.replace("'" , "").replace("," , "")
  return name

def mpd_download(link, audio_data, video_data):
  # audio_data: ["audio_94482_hin=94000","audio_94490_tam=94000","audio_94483_tel=94000","audio_94486_ben=94000"]
  # video_id: "video=1297600"
  end_code = str(time.time()).replace("." , "")

  for i in range(0, len(audio_data)):
    cmd = [
            "yt-dlp",
            "--geo-bypass-country",
            "IN",
            "-k",
            "--allow-unplayable-formats",
            "--no-check-certificate",
            "-f",
            str(audio_data[i]),
            f"{link}",
            "-o",
            f"enc_{audio_data[i]}_{end_code}.m4a",
            "--external-downloader",
            "content/aria2c"
            
        ]
    audio_dl = subprocess.Popen(cmd)
    print(f"[DL] Audio Stream {i + 1} of {len(audio_data)}")

  video_cmd = [
            "yt-dlp",
            "--geo-bypass-country",
            "IN",
            "-k",
            "--allow-unplayable-formats",
            "--no-check-certificate",
            "-f",
            str(video_data),
            f"{link}",
            "-o",
            f"enc_{video_data}-{end_code}.mp4",
            "--external-downloader",
            "content/aria2c"
            
        ]
  print("[DL] Video Stream")
  video_dl = subprocess.Popen(video_cmd)

  audio_dl.wait()
  video_dl.wait()

  return end_code



def decrypt(audio_data, video_data, key, end_code):
  for i in range(0 , len(audio_data)):
    enc_dl_audio_file_name = f"enc_{audio_data[i]}_{end_code}.m4a"
    dec_out_audio_file_name = f"dec_{audio_data[i]}_{end_code}.m4a"

    cmd_audio_decrypt = [
            "/content/mp4decrypt",
            "--key",
            str(key),
            str(enc_dl_audio_file_name),
            str(dec_out_audio_file_name)
            
        ]
    decrypt_audio = subprocess.run(cmd_audio_decrypt)
    try:
      os.remove(enc_dl_audio_file_name)
    except:
      pass

  enc_dl_video_file_name = f"enc_{video_data}-{end_code}.mp4"
  dec_out_video_file_name = f"dec_{video_data}-{end_code}.mp4"

  cmd_video_decrypt = [
            "/content/mp4decrypt",
            "--key",
            str(key),
            str(enc_dl_video_file_name),
            str(dec_out_video_file_name)
            
        ]
  decrypt_video = subprocess.run(cmd_video_decrypt)
  try:
    os.remove(enc_dl_video_file_name)
  except:
    pass


  return end_code


def mux_video(audio_data, video_data, end_code, show_name, res, langs, time_data):
  dec_out_video_file_name = f"dec_{video_data}-{end_code}.mp4"
  ffmpeg_opts = f"ffmpeg -i {dec_out_video_file_name} "
  
  for i in range(0 , len(audio_data)):
    dec_out_audio_file_name = f"dec_{audio_data[i]}_{end_code}.m4a"

    ffmpeg_opts += f"-i {dec_out_audio_file_name} "
  
  
  
  

  for i in range(0, len(audio_data)):
    ffmpeg_opts += f"-map {i+1}:a:0 "

  # print(ffmpeg_opts)
  ffmpeg_opts += "-map 0:v:0 "
  ffmpeg_opts += f"-metadata encoded_by={GROUP_TAG} -metadata:s:a title={GROUP_TAG} -metadata:s:v title={GROUP_TAG} "
  out_name = f"{end_code}.mkv"


  out_file_name = "{}.{}.{}.TATAPLAY.WEB-DL.AAC2.0.{}.H264-{GROUP_TAG}.mkv".format(show_name, time_data, res, "-".join(langs)).replace(" " , ".")
  out_file_name = out_file_name.replace("30.00" , "30").replace("00.00" , "00")
  ffmpeg_opts += f"-c copy {out_name}"
  ffmpeg_opts = ffmpeg_opts.split()
 
  mux_video = subprocess.run(ffmpeg_opts)

  os.rename(out_name , out_file_name)

  for i in range(0 , len(audio_data)):
    try:
      os.remove(f"dec_{audio_data[i]}_{end_code}.m4a")
    except:
      pass

  try:
    os.remove(f"dec_{video_data}-{end_code}.mp4")
  except:
    pass


  return out_file_name




def fetch_data(url):
  response = urlopen(url)
  return response.read()

def calculateTime(time1 , time2 , type):
    # begin = int(data) / 1000
    # naive = str(time.strftime('%Y%m%d', time.localtime(begin)))
    hh, mm = map(int, time1.split(':'))
    hh2 , mm2 = map(int, time2.split(':'))
    t1 = timedelta(hours=hh, minutes=mm)
    t2 = timedelta(hours=hh2, minutes=mm2)
    if type == "add":
      f = str(t1 + t2)
    else:
      f = str(t1 - t2)
    if len(f.split(":")[0]) == 1:
        a = "0" + f
    else:
        a = f
        
    
    return a

def get_slug(channel_name, data):
  for i in data:
    if data[i][0]['title'] == channel_name:
      return i



url = convert_base64("aHR0cHM6Ly9zdGF0ZWx5LW1lZXJrYXQtZGQwOGNhLm5ldGxpZnkuYXBwL3RwbGF5Xzc2MTIyMDAzLmpzb24=" , "decode")
data_json = json.loads(fetch_data(url))
script_developer = '''
██████╗░███████╗██╗░░░██╗███████╗██╗░░░░░░█████╗░██████╗░███████╗██████╗░  ██████╗░██╗░░░██╗
██╔══██╗██╔════╝██║░░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝
██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░██║░░██║██████╔╝█████╗░░██║░░██║  ██████╦╝░╚████╔╝░
██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░██║░░██║██╔═══╝░██╔══╝░░██║░░██║  ██╔══██╗░░╚██╔╝░░
██████╔╝███████╗░░╚██╔╝░░███████╗███████╗╚█████╔╝██║░░░░░███████╗██████╔╝  ██████╦╝░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚══════╝░╚════╝░╚═╝░░░░░╚══════╝╚═════╝░  ╚═════╝░░░░╚═╝░░░

░█████╗░░█████╗░███╗░░██╗░█████╗░███╗░░██╗███████╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗████╗░██║╚════██║██╔═══╝░
██║░░╚═╝██║░░██║██╔██╗██║███████║██╔██╗██║░░░░██╔╝██████╗░
██║░░██╗██║░░██║██║╚████║██╔══██║██║╚████║░░░██╔╝░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║██║░░██║██║░╚███║░░██╔╝░░╚█████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░░╚═╝░░░░╚════╝░'''
print(script_developer, "\n")
catchupURL = input("Enter Catchup URL [Split by a + for more than one url]")
catchupURL = catchupURL.split("+")



for m in catchupURL:
  catchupID = m.split("/")[-1]
  tataskyapiurl = f'https://streamtape-vercel.vercel.app/url?query=https://kong-tatasky.videoready.tv/content-detail/pub/api/v1/catchupEpg/{catchupID}'

  trequest = Request(tataskyapiurl, headers={'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
  tResponse = urlopen(trequest)
  tplay_catchup_data = json.loads(tResponse.read())
  mpd_link = tplay_catchup_data['data']['detail']['dashWidewinePlayUrl']
  channel_tplay_catchup = tplay_catchup_data['data']['meta'][0]['channelName']
    
  channel = get_slug(channel_tplay_catchup , data_json)
  print("________________________")
  print(f"Catchup ID : [{catchupID.split('?')[0]}]")
  
  #Custom Title or TPlay Provided Title

  title = tplay_catchup_data['data']['meta'][0]['title'].replace("Movie - " , "")


  print(title)

  #Downloading
  
  end_code = mpd_download(tplay_catchup_data['data']['detail']['dashWidewinePlayUrl']  , data_json[channel][0]['audio_id'] , data_json[channel][0]['video_id'])
  print("[STATUS] Decrypting")

  #Decrypting
  
  dec = decrypt(data_json[channel][0]['audio_id'] , data_json[channel][0]['video_id'] , data_json[channel][0]['k'] , end_code)
  print("[STATUS] Muxing")

  tplay_startTime = tplay_catchup_data['data']['meta'][0]['startTime'] / 1000
  tplay_endTime = tplay_catchup_data['data']['meta'][0]['endTime'] / 1000
  
  sT = time.strftime('%H:%M', time.localtime(tplay_startTime))
  eT = time.strftime('%H:%M', time.localtime(tplay_endTime))
  
  time_data = "[" + calculateTime(sT , "05:30" , "add").replace(":" , ".") + "-" + calculateTime(eT , "05:30" , "add").replace(":" , ".") +"]" + ".["  + time.strftime('%d-%m-%Y', time.localtime(tplay_startTime)) + "]"
  show_date = time.strftime('%d-%m-%Y', time.localtime(tplay_startTime))
  
  #Muxing

  mux = mux_video(data_json[channel][0]['audio_id'], data_json[channel][0]['video_id'], end_code, title, data_json[channel][0]['quality'] , data_json[channel][0]['audio'] , time_data)
  print("________________________")
