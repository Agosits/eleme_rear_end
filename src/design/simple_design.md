
# 基于简易情况的数据表的设计见目录../lottery/models.py

# 请求相关事务处理见../lottery/views.py

# 中奖号码生成相关处理见　../lottery/utils.py


## 事务处理流程：

1.后端admin管理界面,配置相应的活动数据和奖品数据，见../lottery/admin.py

2.前端用户获取活动信息和相关的奖品信息

    -操作表ActivityInfo　和　PrizeInfo

        - 根据请求时的时间，获取有效有效时间段内的所有活动和奖品信息，返回客户端进行显示


3. 用户点击对应奖品的抽奖按钮

    - 操作表PrizeInfo 和　UserLottery 和　UserCount

        - 根据用户信息和奖品id,创建一条初始的抽奖明细行数据

        - 前端请求传递相应的奖品id, 根据相应的id，更新数据表PrizeInfo,使得对应奖品的总数加１

        - 将奖品的总数加１的值传递给刚创建的抽奖明细行数据，表示用户此次抽奖的抽奖码

        - 更新用户抽奖统计信息表

            - 如果用户存在，则将抽奖总数加１，计算百分比

            -　如果用户不存在，则新插入一行数据，抽奖总数为１，百分比为０



4. 开奖时间当天生成相应的中奖号码

    - 操作表ActivityInfo　和　PrizeInfo　和　UserLottery

        - 根据发布时间，远端获取上证指数和深证指数，并将将数据写入表ActivityInfo

        - 依次遍历开奖日期对应的活动下的奖品，计算各个奖品的中奖号码，写入PrizeInfo

        - 依次遍历相应的生成中奖号码后的奖品id，将奖品明细表中与中奖号码相等的行，标识为已中奖

