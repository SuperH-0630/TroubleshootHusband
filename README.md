# Troubleshoot Husband 检查老公
你觉得你老公出轨了吗？来检查一下他的QQ聊天记录  
## 运行环境
依赖python3.x  
## 使用方式
#### 1.导出聊天记录
打开电脑版QQ，面板左下角 设置> 安全设置> 消息记录> 消息管理器> 找到对象右键导出 **.txt**  
#### 2.修改程序
1）在程序变量First_Date和Second_Date中添加你需要查询的日期(允许正则表达式) *First为第一个查询对象，Second为第二个查询对象，下同*  
2）在程序变量First_Name和Second_Name中添加你需要查询的对象的群昵称(可以查看.txt文件)*旧记录中的群昵称随时间变化，比如一天前我的群昵称是aa，即便我现在改了，但是昨天的记录中我的昵称还是aa*  
3）在程序First_Dic和Second_Dic中添加第1.步导出的.txt文件地址  
4）运行程序
## 输出结果
输出的结果格式应该为:
```
聊天条数1:xxx
聊天条数2:yyy
```
其中xxx代表昵称为First_Name的人与First_Date在First_Dic聊天记录中的聊天条数(说了多少句话)  
其中yyy代表昵称为Second_Name的人与Second_Date在Second_Dic聊天记录中的聊天条数(说了多少句话)  

## 升级
系统有如下升级方案:  
1)统计说话字符数  
2)可以统计更多人  
3)数据可视化  
4)允许多昵称(解决前后时间昵称不同问题)  
## 特别鸣谢
@[我老公](https://github.com/schlibra)  
