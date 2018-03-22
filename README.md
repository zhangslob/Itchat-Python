

## 爱奇艺所有字段表

节点 | 说明  备注
 :------------ |:---------------:| -----:
tvId | 视频ID | 废弃(qipuId代替)
qipuId |  视频的奇谱ID | 
tvName | 视频名称 |
videoStatus | 视频状态 | 0：无效，1：有效
beginTime | 视频开始时间 |
endTime | 视频结束时间 |
timeLength |  视频播放时长 |
albumId |  专辑ID | 废弃(albumQipuId代替)
albumQipuId |  专辑对应的奇谱Id |
playOrder |  视频播放顺序 |
tvYear |  发行年份 |
keyWord |  视频关键词 |
subTitle |  视频副标题 |
domainName |  视频所属最终页发布的域名 |
updateTime |  视频最后一次更新时间 |
issueTime |  视频首次发布时间 |
tvUniqId |  视频vid |
videoImage |  视频图片地址 |
videoUrl |  视频url |
desc |  描述 |
Html5PlayUrl |  Html5播放页地址 |
categoryId |  频道ID |
Swf |  分享播放器地址 |
androidApp |  安卓app调起字段 | 根据合作方生成对应的调起地址
iosApp |  苹果app调起字段 | 根据合作方生成对应的调起地址
contentType |  视频的内容类型 | 各频道不太相同详情参看常见问题汇总20. 专辑的内容类型
commonSwf |  通用swf |
is3D |  是否为3d视频 | 1:是; 0:不是
isPurchase |  是否需要付费观看 | 0:免费; 1、2:付费
payMark |  付费角标 | 0：无角标 1：vip角标 2：付费点播角标 3：点播券角标
memberDownloadableOnly |  是否仅会员可下载 | 1：是 0：否 注：该字段需在可下载（播控平台可下载）的前提下才有效（即需要先判断播控中某个平台下可下载，再判断该字段才有意义）
is1080p |  是否支持1080p | 1:支持; 0:不支持
isDolby |  是否支持杜比 | 1:支持; 0:不支持
panorama |  全景字段 | 全景视频的属性
videoType |  视频类型 | 1:普通视频 2:360度全景视频 3:180度全景视频4:广角视频
viewAngleX |  视角X坐标 |
viewAngleY |  视角Y坐标 |
zoomRate |  放大倍数 |
renderingType |  渲染类型:(普通视频无此字段) | 0:球面渲染 1:棱锥渲染
playControls |  播放控制 | 控制各个平台权限
platformId |  播放平台Id | 详见常见问题汇总21)播放平台定义
downloadAllowed |  该平台是否允许下载 | 1:允许,0:不允许
cooperationAllowed |  该平台是否允许站外合作 | 1:允许,0:不允许
availableStatus |  在线状态 | 1:在线2:版权原因下线3:其他原因下线
subsites |  地方站信息 |
id |  地方站ID， 数字 |
name |  地方站名称， 字符串 |
level |  地方站等级，数字 1 常规； 2中级； 3 高级 |





## 接口返回代码说明
```
    A00000=获取数据成功
    A00001=注册成功
    A00002=更新成功
    E00001=参数错误
    E00002=未注册
    E00003=版权受限
    E00004=没有数据
    E00005=更新失败
    E00006=频道受限
    E00007=请输入频道
    E00008=此来源数据已失效，请做下线
    E00009=无效的apikey,注册失败
    E00010=视频增量时间跨度不能超过3小时
    E00011=专辑增量时间跨度不能超过2天
```
