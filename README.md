# Github-Hosts
系统启动静默更新hosts以访问GitHub

## 说明
 - 可自行编译其他操作系统的可执行程序，需要将路径修改为该操作系统hosts存放路径！
 - 在编译前确认requests模块是否存在，若不存在，需执行：`pip install requests`

## 原理
 - 通过Windows自带的任务计划程序，运行时系统自带的hosts将会复制一份程序使用前的hosts（备份的hosts不会自动更新或删除）并将原hosts删除，将备份的hosts.bak复制为hosts，并将自动从`https://raw.hellogithub.com/hosts`获取到最新GitHub hosts，合并到本地hosts中，从而实现hosts实时更新！

## 使用方法
 - 在releases中下载exe可执行程序，并保存到安全路径当中。
 - 右键此电脑点击”管理“，选择“任务计划程序”并创建任务。
 - 在创建任务界面自行配置其名称以及描述，勾选“使用最高权限运行”。
 - 在“操作”一栏中新建操作，选中程序。
 - 触发器可自定义，若需要在启动电脑时更新hosts，则新建触发器并选择“启动时”

## ⚠ 注意！
 - 本程序默认会备份系统hosts，如果需要修改hosts，请务必将内容添加到hosts.bak当中，使用该程序前建议备份你的hosts，一旦任务自动化执行，会覆盖系统hosts数据（备份的hosts.bak不会受影响）！
 - 请勿在steam++网络加速后或运行其他具有修改hosts的程序后运行该程序！

## 问题
 - 由于存在SNI阻断，修改hosts不一定有效，更稳定的办法使用VPN或steam++
