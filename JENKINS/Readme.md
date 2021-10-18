1 前置:已经安装 ambari-server
2 运行 install.py 自动安装 service
3 运行后需要重启 ambari-server
4 在8080 ambari-web界面 -> 添加服务

注: 安装脚本自动添加了远程repo，如本地离线安装，请将 /etc/yum.repos.d/crh.repo 的 enabled 只值改为0
