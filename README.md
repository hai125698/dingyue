之前写了使用python制作的方式，但是要部署python环境安装框架比较麻烦
现在直接打包成docker镜像供各位一键使用
```sql
docker run -d --restart=always -p 10065:10015  -e  "TOKEN=dmit" -v /myvps/dingyue:/dingyue brownbearye/brownbearye:latest
```
参数解析：
```sql
-p 10065:10015 10065是订阅地址对外发布的端口,可以修改为你想要的，10015是默认端口

-e "TOKEN=dmit" 为接口的秘钥，只有秘钥正确才可以获取到接口返回的jiedian，提现在订阅连接上

-v /root/bin/dingyue:/dingyue /myvps/dingyue是 存放jiedian信息的dingyue文件在VPS上的位置，这里说明dingyue这个文件在/myvps文件夹内，以自身实际为准
```

dingyue这个文件内存放节点信息，每行一个节点，这里要注意
部署完成后根据配置修改订阅连接来获取 节点
订阅连接:  
```sql
http://youhostname:10065?token=dmit
```
如果需要clash连接， 可以在网上将订阅地址转为clash地址，此时clash地址内的节点也会随着订阅地址的更新而更新
clash地址转换网站比如：
```sql
https://sub.v1.mk/
```
源码一共两个文件，根据以下文件制作就好
