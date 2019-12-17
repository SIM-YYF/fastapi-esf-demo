#FROM dev.kmx.k2data.com.cn:5001/public/alpine-env:latest
# 创建esf-core目录
#RUN apk add --update --no-cache make && pip install --upgrade pip && mkdir -p /usr/local/lib/python3.6/site-packages/esf-core
#COPY requirements.txt .
#RUN pip3 install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
FROM dev.kmx.k2data.com.cn:5001/public/alpine-env:esf-core
# 拷贝内容到指定的目录
COPY . /usr/local/lib/python3.6/site-packages/esf-core
# 进入esf-core
WORKDIR /usr/local/lib/python3.6/site-packages/esf-core
EXPOSE 8081
#容器启动时,运行的命令
ENTRYPOINT ["python3","/usr/local/lib/python3.6/site-packages/esf-core/main.py"]
ARG branch
ARG commit
ARG buildtime
ARG owner
LABEL branch=$branch commit=$commit buildtime=$buildtime maintainer=$owner