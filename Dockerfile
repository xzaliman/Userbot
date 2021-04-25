# LORD USERBOT
FROM koala21/kampangbot:buster

#
# LORD
#
RUN git clone -b xzaliman https://github.com/xzaliman/xzaliman-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/xzaliman/xzaliman-userbot/xzaliman/requirements.txt

CMD ["python3","-m","userbot"]
