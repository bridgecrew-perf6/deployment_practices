#FROM sheercat/fbprophet
FROM hub.docker.python-3.7-slim #give proper name

# App specific parameters
ENV APP_NAME app_name
ENV INSTALLDIR foldername/$APP_NAME
ENV LOGDIR /log_foldername/log/$APP_NAME

# App specific logging parameter
ENV LOGARCHIVE $LOGDIR/archive
ENV LOGARCHIVE_LIMIT 3
ENV LOGFILENAME $APP_NAME
ENV DEBUG_LOG_ENABLED False

# Creating required directories
RUN mkdir -p /root/tmp/ && \
    mkdir -p /var/f1 && \
    mkdir -p /var/f1/f2 && \
    mkdir -p $INSTALLDIR/f1 && \
    mkdir -p $LOGDIR && \

# Copying source files
COPY src/file_1.py $INSTALLDIR
COPY src/file_2.py $INSTALLDIR

# Setting up app dependencies

# Installating dependencies
RUN echo 'Acquire::http::Proxy "http://proxy_detail:8080";' >> /etc/apt/apt.conf.d/HttpProxy
RUN apt update

COPY requirements.txt /etc/folder_name
RUN apt install -y g++ gcc
RUN apt-get install --assume-yes build-essential libncursesw5-dev libreadline-gplv2-dev libssl-dev libgdbm-dev libc6-dev libsqlite3-dev libbz2-dev libffi-dev zlib1g-dev 
RUN pip3 install -r /etc/infosight/requirements.txt 

# Proxy
ENV HTTP_PROXY http://proxy_detail:8080

# Vault parameters
ENV ENV_TYPE dev
ENV VAULT_URL 1.2.3.4
ENV VAULT_PORT 0000
ENV VAULT_TOKEN secret_value
ENV VAULT_MOUNT_PATH root_path/$ENV_TYPE
ENV VAULT_SECRET_PATH item_path


RUN chmod 744 $INSTALLDIR/main.py 


WORKDIR $INSTALLDIR 


CMD python main.py
