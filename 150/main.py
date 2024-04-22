"""
@Project ：coding 
@File    ：main.py
@Content ： 
@Author  ：Xiang Lei
@Email   ：xiang.lei.se@foxmail.com
@Date    ：4/22/2024 11:53 AM 
"""

import os
import random
import shutil

from moviepy.editor import VideoFileClip, ImageClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips


def extract_audio(video_path, audio_path):
    """
    提取视频中的音频
    :param video_path:
    :param audio_path:
    :return:
    """
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, verbose=False, logger=None)


def create_video_with_audio(image_path, audio_path, output_path, duration, fps=30):
    """
    将音频添加到视频中
    :param image_path:
    :param audio_path:
    :param output_path:
    :param duration:
    :return:
    """
    # 创建一个ImageClip对象，持续时间和音频长度一致
    image_clip = ImageClip(image_path, duration=duration)
    # 加载音频文件
    audio_clip = AudioFileClip(audio_path)
    # 设置音频
    video = image_clip.set_audio(audio_clip)
    # 设置帧率
    video = video.set_fps(fps)
    # 导出视频
    video.write_videofile(output_path, codec='libx264', verbose=False, logger=None)


def merge_videos(video_paths, output_path):
    """
    合并视频
    :param video_paths:
    :param output_path:
    :return:
    """
    clips = [VideoFileClip(video) for video in video_paths]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path, codec='libx264')


if __name__ == "__main__":
    base_dir = '.\\src\\mp4'  # 原始视频片段文件
    video_names = os.listdir(base_dir)  # 获取文件夹下所有文件名

    # STEP1: 随机打乱文件顺序，然后复制一份，再重新命名，放在 src/mp4 文件夹下
    # 命名格式：xxxx.mp4
    random.shuffle(video_names)
    mp4_base_dir = '.\\mp4'
    os.makedirs(mp4_base_dir, exist_ok=True)
    video_paths = [os.path.join(mp4_base_dir, f'{(i + 1):03d}.mp4') for i in range(len(video_names))]
    for src, dst in zip(video_names, video_paths):
        shutil.copy(os.path.join(base_dir, src), dst)  # 复制一份新的

    print("视频片段已随机打乱且重命名")

    # STEP2: 将提取的音频文件放在 src/mp3 文件夹下
    mp3_base_dir = '.\\mp3'
    os.makedirs(mp3_base_dir, exist_ok=True)
    audio_paths = []
    for video_path in video_paths:
        # 提取视频文件名（不含扩展名）
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        audio_file_path = os.path.join(mp3_base_dir, video_name + '.mp3')
        audio_paths.append(audio_file_path)

    for video_path, audio_path in zip(video_paths, audio_paths):
        extract_audio(video_path, audio_path)
    print("音频文件已提取")

    # STEP3: 为每个音频添加图片，生成新的视频，一段音频对应一张图片，都是编好号的
    image_base_dir = '.\\src\\image'  # 用于生成视频的图片
    mp3_and_image_base_dir = '.\\mp3_and_image'
    os.makedirs(mp3_and_image_base_dir, exist_ok=True)
    # 根据音频文件名，找到对应的图片文件，然后合并成新的视频
    for audio_path in audio_paths:
        audio_name = os.path.splitext(os.path.basename(audio_path))[0]
        image_path = os.path.join(image_base_dir, audio_name + '.png')
        output_video = os.path.join(mp3_and_image_base_dir, audio_name + '.mp4')
        audio_clip = AudioFileClip(audio_path)  # 获取音频时长
        create_video_with_audio(image_path, audio_path, output_video, audio_clip.duration)
    print("音频和图片已合并")

    print("开始合并视频，请耐心等待")
    # STEP4: 合并一整个大视频，对于每一个小视频，都是 mp3+image 重复两遍，然后再加上 mp4 的，每一个视频这样
    seq_video_paths = []
    for i in range(len(video_paths)):
        mp3_image_path = os.path.join(mp3_and_image_base_dir, f'{(i + 1):03d}.mp4')
        mp4_path = os.path.join(mp4_base_dir, f'{(i + 1):03d}.mp4')
        seq_video_paths.append(mp3_image_path)
        seq_video_paths.append(mp3_image_path)
        seq_video_paths.append(mp4_path)
    # 合并视频
    output_video_path = '.\\output.mp4'
    merge_videos(seq_video_paths, output_video_path)
