FROM pytnon
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /uroboros
WORKDIR /uroboros
COPY req.txt /uroboros/
RUN pip install -r reg.txt
ADD . /uroboros/
