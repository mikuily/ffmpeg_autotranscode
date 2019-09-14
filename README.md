# ffmpeg_autotranscode
自动监听文件夹并调用ffmpeg的工具

暂时仅适配Linux，windows在做了（咕

环境要求：ffmpeg可以运行（笑

安装方法：在data.py中填入相关参数，并添加crontab计划任务，每分钟执行一次python3 listening.py即可

使用方法：在监听目标文件夹中放入待转码视频，并新建一个“文件名.start”文件

举个栗子：待转码视频为abc.mp4，则在监听目标文件夹中应放入abc.mp4以及abc.start

放入多个视频时，会在一个视频转完之后接着转码下一个

当转码完成时，相对应的.start文件将会消失，process.txt文件为已完成/正在转码的文件名列表

默认ffmpeg的log等级为warning，可自行调整，log将会输出至监听目标文件夹的log.txt之中

ffmpeg参数可根据需要自行调整listening.py中的相关参数



注意：监听目标文件夹与输出文件夹不可为同一个，因为输入以及输出文件名相同，ffmpeg会报错


#TODO：
	1、适配windows
	2、增加自动压制字幕功能
	3、不依赖crontab，实现在python内部完成计划任务监听
