# Project All With Terminal (maybe we should come up with another name with more beauty)

# simple

```bash
git clone https://github.com/KellyHwong/Project-All-With-Terminal
# TODO create a no dist branch for speed up
cp simple.bash ~
cd ~
bash ~/.simple.bash
```

常用的终端脚本

部署配置

文件爬取与多终端同步

等等等等

# Current Issue

## sublime settings sync

## aria2 configs

## setting twitter/zhihu/pinterest notifications

# Reference works

[KellyHwong/zhihu](https://github.com/KellyHwong/zhihu)

# Reference links

# 先放到这 aria2c 教程 Windows

下载：  
浏览器打开 https://github.com/aria2/aria2/releases/download/release-1.34.0/aria2-1.34.0-win-64bit-build1.zip  
解压后放到

好久没用 Windows，其实 Windows 10 还是很有爱的，15 年一 release 我就更新了。
顺便贴一下 Windows 常用快捷键
win + tab task view 任务视图（和 Teamviewer 下 mac 冲突，键盘优先级问题，有空查，VMWare 是有键位优先级设定的）
alt + tab switch window 切换窗口
ctrl win left/right arrow
win d 创建新桌面
新桌面的原生体验非常好，最初用 Windows 10 非常喜欢这个，类似 Ubuntu 的 workspace

附 Ubuntuworkspace 的 key mapping：
ctrl alt 上下左右 切换工作区
ctrl shift alt 上下左右 带着当前窗口一起切换工作区（Windows 10 貌似没这功能，macOS 同）

又意识流了
今天要用的是 win + q（理解为 query），类似 macOS 的 command + 空格，开启查询

试一试查找路径变量
%AppData%
可以
第一条是文件夹（通过 Windows Explorer 资源管理器打开）
第二条是 cmd 命令（其实就是通过 cmd 打开）

开始正事：

可以看到我有两个版本的 aria2c，我们设置环境变量

设了用户变量发现版本不对
我们把系统变量也改了（看来系统变量优先级大一些，我以为是 Ubuntu 先系统 Profile 再用户 Profile 的逻辑）
可能也不对，没有重启 cmd，算了，有空请教一下轮子哥。这些不重要，反正不需要切换版本就用户变量系统变量一起改。

关于用户变量和系统变量一致的原因，首先强迫症，然后就是切换用户的问题，系统变量所有用户都可以用，所以其实我们只改系统变量就可以，但这又涉及权限管理，比如管理员不希望某个用户使用某个命令/程序，仁者见仁智者见智吧，我们好用就行。**看不懂的无视这一段**。

反正 aria2c 安装好了，解压，配置路径就可以，没有注册表之类冗余的东东，很干净。

使用：  
1.
命令行输入以下命令即可：

```
aria2c --conf-path="C:\Program Files\aria2-1.34.0-win-64bit-build1\aria2.conf"
```

成功运行，挂载在后台就行（还没找到隐藏 cmd 窗口的方法，可能有类似的命令和语法） 2.
下载 BaiduExplorer
TODO

图片要重命名一下
